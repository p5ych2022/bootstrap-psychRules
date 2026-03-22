# bootstrap-psychRules

`bootstrap-psychRules` is a personal Codex skill for initializing and maintaining a project-level `.psychRules/` context system.
`bootstrap-psychRules` 是一个个人 Codex skill，用来初始化并维护项目级 `.psychRules/` 上下文系统。

It helps create durable project context, working rules, and structured change memory so future threads can onboard faster and work more safely.
它的目标是为项目建立长期可维护的基础信息、工作规则和结构化变更记忆，让后续线程更快完成 onboarding，也更安全地开展工作。

## What It Creates

The skill scaffolds an `AGENTS.md` file and a `.psychRules/` folder at the target root.
这个 skill 会在目标根目录生成一个 `AGENTS.md` 文件和一个 `.psychRules/` 文件夹。

The generated structure looks like this:
生成后的结构大致如下：

```text
project-root/
├─ AGENTS.md
└─ .psychRules/
   ├─ basic.md
   ├─ rules.md
   └─ memory/
      └─ init00_*.md
```

`basic.md` stores stable project facts such as goals, environment, business logic, and architecture.
`basic.md` 用来记录稳定的项目事实，例如目标、环境、业务逻辑和架构设计。

`rules.md` stores working rules such as commands, dependencies, quality rules, and commit-memory policy.
`rules.md` 用来记录工作规则，例如常用命令、依赖、质量规则，以及 commit-memory 同步策略。

`memory/` stores one markdown file per meaningful debug, fix, feature, refactor, or investigation session.
`memory/` 用来按会话记录变更，每次有意义的 debug、fix、feature、refactor 或调查，都应落一个 markdown 文件。

## Language Rules

The skill itself is written in bilingual format, where each English paragraph is followed by its Chinese translation.
这个 skill 本体采用中英双语对照格式，每段英文后面紧跟对应中文翻译。

Generated `.psychRules` files use Chinese as the primary language, while filenames remain in English.
生成的 `.psychRules` 文件内容以中文为主，但文件名保持英文。

Git commit subjects should use a concise English conventional-commit style.
git commit 标题应使用简洁的英文 conventional commit 风格。

## Scripts

`scripts/init_psych_rules.py` initializes the scaffold for a project or workspace.
`scripts/init_psych_rules.py` 用来为项目或工作区初始化骨架。

`scripts/new_memory_entry.py` creates a new memory note and prints a suggested conventional commit subject.
`scripts/new_memory_entry.py` 用来创建新的 memory 记录，并输出建议使用的 conventional commit 标题。

## Usage

Initialize a single project:
初始化单一项目：

```powershell
py -3 scripts/init_psych_rules.py --root "D:\your-project"
```

Initialize a multi-project workspace:
初始化多项目工作区：

```powershell
py -3 scripts/init_psych_rules.py --root "D:\your-workspace" --workspace
```

Create a new memory entry:
创建一条新的 memory 记录：

```powershell
py -3 scripts/new_memory_entry.py --root "D:\your-project" --kind fix --title "repair cache merge bug" --scope p-pop
```

## Commit And Memory Sync

When a git repository already exists, memory notes should stay aligned with related commits whenever practical.
当目标目录已经存在 git 仓库时，memory 文件应尽量与相关 commit 保持同步。

If the user asks for a commit, the expected workflow is to create or update the matching memory note first, then commit both together.
如果用户要求执行 commit，推荐流程是先创建或更新对应的 memory，再把 memory 和代码一起提交。

If the user asks to create a memory note for a code change but has not asked for a commit yet, the agent should ask whether to create a commit as well.
如果用户要求为某次代码改动创建 memory，但还没有要求 commit，agent 应补一句确认：是否要顺便创建一次 commit。

## Notes

This skill does not automatically run `git init` in nested or multi-project workspaces unless the user explicitly asks.
这个 skill 不会在嵌套仓库或多项目工作区中自动执行 `git init`，除非用户明确要求。

The safest pattern is to keep `.psychRules/` close to the project root that actually owns the code and git history.
最稳妥的使用方式，是让 `.psychRules/` 尽量贴近真正拥有代码和 git 历史的项目根目录。
