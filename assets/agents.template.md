# Agent Notes

This project uses `.psychRules/` as durable agent context.
这个项目使用 `.psychRules/` 作为长期可维护的 agent 上下文。

## Start Of Thread

- Read `.psychRules/basic.md`.
- 先阅读 `.psychRules/basic.md`。

- Read `.psychRules/rules.md`.
- 再阅读 `.psychRules/rules.md`。

- If the target is a child project inside a larger workspace, prefer the nearest relevant project root instead of updating unrelated areas.
- 如果目标是大工作区中的某个子项目，优先使用离任务最近的项目根目录，不要误改无关区域。

## During Work

- Keep the project goal central to decisions.
- 所有决策都应围绕项目目标展开。

- Add stable environment, architecture, command, and risk discoveries back into `.psychRules/basic.md` or `.psychRules/rules.md`.
- 发现稳定的环境、架构、命令、风险信息后，回写到 `.psychRules/basic.md` 或 `.psychRules/rules.md`。

- Create one markdown note under `.psychRules/memory/` for each meaningful `debug`, `fix`, `feat`, `refactor`, or `note` session.
- 每次有意义的 `debug`、`fix`、`feat`、`refactor` 或 `note` 会话，都在 `.psychRules/memory/` 下创建一条 markdown 记录。

## Git Safety

- If a git repo already exists at the chosen root, keep the memory file aligned with related commits when practical.
- 如果目标根目录已有 git 仓库，尽量让 memory 文件和相关 commit 同步。

- Do not run `git init` automatically for a workspace with nested projects unless the user explicitly asks.
- 对于包含多个子项目的工作区，除非用户明确要求，否则不要自动执行 `git init`。
