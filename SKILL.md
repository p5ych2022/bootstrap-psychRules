---
name: bootstrap-psychRules
description: Use when the user wants to initialize or maintain a project-level .psychRules folder, create AI-readable context and rules files, scaffold AGENTS.md guidance, or record structured memory notes. 适用于初始化或维护项目级 .psychRules、规则文档与变更记忆。
---

# Bootstrap Psych Rules

Use this skill when a project needs a durable context system that agents can keep up to date.
当项目需要一套可持续维护的上下文系统，并希望后续线程能持续复用这些信息时，使用这个 skill。


Generated `.psychRules` files should use Chinese as the primary language, while filenames stay in English.
生成出来的 `.psychRules` 文件内容应以中文为主，但文件名保持英文。

Treat `.psychRules/` as private project memory by default. It may contain sensitive context, so it should be ignored by git unless the user explicitly wants to track it.
默认把 `.psychRules/` 当成私有项目记忆。它可能包含敏感上下文，所以除非用户明确希望跟踪，否则应当被 git 忽略。

## Workflow

1. Determine the target root.
1. 先判断目标根目录。

Prefer the git root when one exists.
如果存在 git 根目录，优先以 git 根目录作为目标。

If the current directory is a multi-project workspace without a single `.git`, treat it as a workspace-level setup unless the user points to a child project.
如果当前目录是一个没有单一 `.git` 的多项目工作区，就把它当作工作区级别来处理，除非用户明确指定某个子项目。

2. Initialize the scaffold.
2. 初始化骨架。

Run `scripts/init_psych_rules.py --root <path>`.
执行 `scripts/init_psych_rules.py --root <path>`。

Add `--workspace` when the target contains multiple child projects.
如果目标目录包含多个子项目，则追加 `--workspace` 参数。

Ensure the target root has a `.gitignore` entry for `.psychRules/`; 
确保目标根目录的 `.gitignore` 中包含 `.psychRules/`；

3. Fill or refine the generated files.
3. 填充或完善生成的文件。

Update `.psychRules/basic.md` with project goal, environment facts, first-principles business logic, architecture, and key boundaries.
把项目目标、环境事实、第一性原理层面的业务逻辑、架构设计和关键边界写进 `.psychRules/basic.md`。

Update `.psychRules/rules.md` with startup commands, dependencies, warnings, review hotspots, commit-memory policy, language rules, and the rule that `.psychRules/` stays out of version control by default.
把启动命令、依赖、警告事项、审查重点、commit-memory 同步规则、语言规则，以及 “`.psychRules/` 默认不进版本控制” 这条规则写进 `.psychRules/rules.md`。

4. Keep a change memory.
4. 持续维护变更记忆。

For each meaningful debug, fix, feature, refactor, or investigation session, run:
每次有意义的 debug、fix、feature、refactor 或调查记录时，都执行：

`scripts/new_memory_entry.py --root <path> --kind <debug|fix|feat|refactor|note> --title "<short title>"`
`scripts/new_memory_entry.py --root <path> --kind <debug|fix|feat|refactor|note> --title "<short title>"`

5. Sync memory notes with git commits when git exists.
5. 当目标目录已经有 git 时，让 memory 与 git commit 保持同步。

If the user asks for a git commit, first create or update the corresponding memory note, then include that note in the same commit when practical.
如果用户要求执行 git commit，先创建或更新对应的 memory 文件，再尽量把这个 memory 文件和代码一起放进同一个 commit。

If the user asks to create a new memory note for a code change but has not asked for a commit yet, ask a concise follow-up question about whether to create a git commit as well.
如果用户要求为某次代码改动创建 memory，但还没要求 commit，则补一句简短确认：是否要顺便创建对应的 git commit。

Commit messages should follow a consistent English conventional-commit style such as `feat(scope): short summary`, `fix(scope): short summary`, or `refactor(scope): short summary`.
commit message 应遵循统一的英文 conventional commit 风格，例如 `feat(scope): short summary`、`fix(scope): short summary`、`refactor(scope): short summary`。

Keep the subject lowercase, concise, and under 72 characters. A Chinese body is acceptable when extra explanation is helpful.
commit 标题保持小写、简洁、最好不超过 72 个字符；如果需要补充背景，正文可以使用中文。

6. Keep git behavior safe.
6. 保持 git 操作安全。

Do not run `git init` automatically in a multi-project workspace or nested-repo structure unless the user explicitly asks.
不要在多项目工作区或嵌套仓库结构里自动执行 `git init`，除非用户明确要求。

Do not assume `.psychRules/` should be committed. Ignoring it is the default safe path.
不要默认假设 `.psychRules/` 应该被提交。忽略它才是默认安全路径。

## Output Expectations

`.psychRules/basic.md` should be stable context, not a scratchpad.
`.psychRules/basic.md` 应该沉淀稳定上下文，而不是临时草稿。

`.psychRules/rules.md` should contain actionable rules and commands.
`.psychRules/rules.md` 应该保存可执行的规则和命令。

`.psychRules/memory/` should contain one markdown file per meaningful change session with summary, touched files, validation, and follow-up notes.
`.psychRules/memory/` 中每个有意义的变更会话都应对应一个 markdown 文件，记录摘要、涉及文件、验证方式和后续事项。

`AGENTS.md` should instruct future threads to read and maintain `.psychRules`.
`AGENTS.md` 应该明确要求后续线程先读取并维护 `.psychRules`。



## Files

- `scripts/init_psych_rules.py`
- `scripts/new_memory_entry.py`
- `assets/*.template.md`
