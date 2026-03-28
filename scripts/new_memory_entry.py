from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


VALID_KINDS = ["debug", "fix", "feat", "refactor", "note"]


def suggest_commit_type(kind: str) -> str:
    mapping = {
        "debug": "fix",
        "fix": "fix",
        "feat": "feat",
        "refactor": "refactor",
        "note": "docs",
    }
    return mapping[kind]


def slugify(title: str) -> str:
    lowered = title.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    return slug or "untitled"


def next_sequence(memory_dir: Path) -> int:
    pattern = re.compile(r"^[a-z]+(\d+)_")
    values: list[int] = []
    for item in memory_dir.glob("*.md"):
        match = pattern.match(item.name)
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def load_template(skill_root: Path) -> str:
    return load_named_template(skill_root, "memory.template.md")


def load_named_template(skill_root: Path, name: str) -> str:
    return (skill_root / "assets" / name).read_text(encoding="utf-8")


def render(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def safe_print(message: str) -> None:
    encoding = sys.stdout.encoding or "utf-8"
    sys.stdout.buffer.write((message + "\n").encode(encoding, errors="backslashreplace"))


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def ensure_context_files(root: Path, generated_at: str, skill_root: Path) -> None:
    psych_dir = root / ".psychRules"
    memory_dir = psych_dir / "memory"
    replacements = {
        "PROJECT_NAME": root.name,
        "ROOT_KIND": "project",
        "ROOT_PATH": str(root),
        "GENERATED_AT": generated_at,
        "TITLE": "Psych Rules Memory Entry",
        "KIND": "note",
        "SEQUENCE": "00",
    }

    write_if_missing(
        psych_dir / "session.md",
        render(load_named_template(skill_root, "session.template.md"), replacements),
    )
    write_if_missing(
        memory_dir / "index.md",
        render(load_named_template(skill_root, "memory-index.template.md"), replacements),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a .psychRules memory entry")
    parser.add_argument("--root", required=True, help="Target project or workspace root")
    parser.add_argument("--kind", required=True, choices=VALID_KINDS)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--scope",
        default="psych-rules",
        help="Commit scope suggestion, for example p-pop or psych-rules",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    psych_dir = root / ".psychRules"
    memory_dir = psych_dir / "memory"
    if not memory_dir.exists():
        raise FileNotFoundError(f"memory directory not found: {memory_dir}")

    seq = next_sequence(memory_dir)
    filename = f"{args.kind}{seq:02d}_{slugify(args.title)}.md"
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    skill_root = Path(__file__).resolve().parents[1]
    ensure_context_files(root, generated_at, skill_root)

    content = render(
        load_template(skill_root),
        {
            "TITLE": args.title,
            "KIND": args.kind,
            "SEQUENCE": f"{seq:02d}",
            "GENERATED_AT": generated_at,
            "ROOT_PATH": str(root),
        },
    )

    target = memory_dir / filename
    target.write_text(content, encoding="utf-8")
    safe_print(str(target))
    commit_type = suggest_commit_type(args.kind)
    commit_subject = slugify(args.title).replace("-", " ")
    safe_print(f"suggested_commit={commit_type}({args.scope}): {commit_subject}")
    safe_print("reminder=sync session.md for active work and promote durable takeaways into memory/index.md")


if __name__ == "__main__":
    main()
