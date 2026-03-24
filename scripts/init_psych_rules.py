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


def _line_ignores_psychrules(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return False
    content = stripped.split("#", 1)[0].strip()
    return ".psychRules" in content


def ensure_psychrules_in_gitignore_if_present(gitignore_path: Path) -> str:
    if not gitignore_path.exists():
        return "skip .gitignore (missing, not created)"

    existing = gitignore_path.read_text(encoding="utf-8")
    if any(_line_ignores_psychrules(line) for line in existing.splitlines()):
        return f"skip {gitignore_path}"

    entry = ".psychRules/"
    new_content = existing
    if new_content and not new_content.endswith(("\n", "\r")):
        new_content += "\n"
    new_content += f"{entry}\n"
    gitignore_path.write_text(new_content, encoding="utf-8")
    return f"update {gitignore_path}"


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
    actions.append(ensure_psychrules_in_gitignore_if_present(root / ".gitignore"))

    for action in actions:
        print(action)


if __name__ == "__main__":
    main()
