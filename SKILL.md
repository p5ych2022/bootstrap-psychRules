---
name: bootstrap-psychRules
description: Use when the user wants to initialize or maintain a project-level .psychRules folder, create layered AI-readable context and rules files, scaffold AGENTS.md guidance, or record structured memory notes without reading the entire history every time. 适用于初始化或维护项目级 .psychRules、分层上下文规则与变更记忆。
---

# Bootstrap Psych Rules

当项目需要一套可持续维护、又不想靠全量长记忆硬撑的上下文系统时，使用这个 skill。

生成出来的 `.psychRules` 文件内容应以中文为主，但文件名保持英文。
默认把 `.psychRules/` 当成私有项目记忆；除非用户明确要求，否则不要纳入 git 追踪。

## 核心设计

这套方案采用分层记忆，而不是“每轮都读全部记忆”：

- `basic.md`：稳定事实，启动必读
- `rules.md`：工作规则，启动必读
- `session.md`：当前任务热上下文，若存在则启动时读取
- `memory/index.md`：长期高价值记忆索引，历史检索时优先读取
- `memory/*.md`：详细会话记录，只在需要时按需打开

目标是减少 token 浪费，同时保留历史延续能力。

## Workflow

1. Determine the target root.
优先使用 git 根目录；如果当前目录是多项目工作区且没有单一 `.git`，除非用户明确指向某个子项目，否则按工作区级别处理。

2. Initialize or refine the scaffold.
运行 `scripts/init_psych_rules.py --root <path>`。
如果目标包含多个子项目，则加上 `--workspace`。
如果目标根目录已有 `.gitignore`，确保其中包含 `.psychRules/`。

3. Fill the layered context files.
- 把长期稳定的项目目标、环境、业务逻辑、架构、边界写入 `.psychRules/basic.md`
- 把命令、依赖、风险、读取协议、memory/commit 策略写入 `.psychRules/rules.md`
- 把当前任务的目标、阻塞点、下一步、正在处理的文件写入 `.psychRules/session.md`
- 把长期有效的决策、坑点、经验写入 `.psychRules/memory/index.md`

4. Keep detailed change memory.
每次有意义的 `debug`、`fix`、`feat`、`refactor` 或调查记录，都执行：
`scripts/new_memory_entry.py --root <path> --kind <debug|fix|feat|refactor|note> --title "<short title>"`

5. Promote only high-value memory.
详细 memory 写完后，不要把整篇内容复制到索引。
只把真正长期有价值的 1 到 3 条结论同步到 `.psychRules/memory/index.md`。
如果任务仍在继续，把当前热信息同步到 `.psychRules/session.md`。

6. Sync memory notes with git commits when git exists.
如果用户要求 git commit，先创建或更新对应 memory，再尽量与代码一起提交。
如果用户要求创建与代码变更相关的 memory，但尚未要求 commit，补一句简短确认：是否也要顺手创建 git commit。
commit message 使用统一的英文 conventional commit 风格，例如 `feat(scope): short summary`、`fix(scope): short summary`、`refactor(scope): short summary`。
标题保持小写、简洁、尽量不超过 72 个字符；需要补充背景时，正文可以使用中文。

7. Keep git behavior safe.
除非用户明确要求，不要在多项目工作区或嵌套仓库结构里自动执行 `git init`。
不要默认假设 `.psychRules/` 应该被提交；忽略它才是默认安全路径。

## Output Expectations

- `.psychRules/basic.md`：稳定上下文，不是草稿区
- `.psychRules/rules.md`：可执行规则与命令
- `.psychRules/session.md`：当前任务热上下文，保持短小且及时刷新
- `.psychRules/memory/index.md`：高价值索引，不写流水账
- `.psychRules/memory/*.md`：按会话记录详细背景、改动、验证和后续事项
- `AGENTS.md`：明确要求未来线程按“basic/rules/session 常驻，memory 按需检索”的协议工作

## Files

- `scripts/init_psych_rules.py`
- `scripts/new_memory_entry.py`
- `assets/*.template.md`
