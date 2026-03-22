from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def load_template(skill_root: Path, name: str) -> str:
    return (skill_root / "assets" / name).read_text(encoding="utf-8")


def render(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def write_if_missing(path: Path, content: str) -> str:
    if path.exists():
        return f"skip {path}"
    path.write_text(content, encoding="utf-8")
    return f"create {path}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize .psychRules and AGENTS.md")
    parser.add_argument("--root", required=True, help="Target project or workspace root")
    parser.add_argument("--name", default=None, help="Override project name")
    parser.add_argument("--workspace", action="store_true", help="Mark target as a workspace")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise FileNotFoundError(f"root does not exist: {root}")

    project_name = args.name or root.name
    root_kind = "workspace" if args.workspace else "project"
    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    skill_root = Path(__file__).resolve().parents[1]

    psych_dir = root / ".psychRules"
    memory_dir = psych_dir / "memory"
    psych_dir.mkdir(parents=True, exist_ok=True)
    memory_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        "PROJECT_NAME": project_name,
        "ROOT_KIND": root_kind,
        "ROOT_PATH": str(root),
        "GENERATED_AT": generated_at,
        "TITLE": "Psych Rules Bootstrap",
        "KIND": "init",
        "SEQUENCE": "00",
    }

    actions = []
    actions.append(
        write_if_missing(
            psych_dir / "basic.md",
            render(load_template(skill_root, "basic.template.md"), replacements),
        )
    )
    actions.append(
        write_if_missing(
            psych_dir / "rules.md",
            render(load_template(skill_root, "rules.template.md"), replacements),
        )
    )
    actions.append(
        write_if_missing(
            root / "AGENTS.md",
            render(load_template(skill_root, "agents.template.md"), replacements),
        )
    )
    actions.append(
        write_if_missing(
            memory_dir / "init00_psych-rules-bootstrap.md",
            render(load_template(skill_root, "memory.template.md"), replacements),
        )
    )

    for action in actions:
        print(action)


if __name__ == "__main__":
    main()
