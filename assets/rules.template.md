# 项目规则

## 语言规则

- `.psychRules/` 内文件名保持英文。
- `.psychRules/` 内文件内容以中文为主。
- 中文优先，英文仅作补充。
- `.psychRules/` 可能包含敏感信息，默认不纳入版本控制。
- git commit 标题默认使用英文 conventional commit 风格。

## 启动读取协议

- 开始实质性工作前，先阅读 `.psychRules/basic.md` 和 `.psychRules/rules.md`。
- 如果存在 `.psychRules/session.md`，再读取它作为当前任务的热上下文。
- 默认不要通读 `.psychRules/memory/` 下的所有文件。
- 当任务涉及历史决策、旧问题复现、接续上次工作时，先看 `.psychRules/memory/index.md`，再按需打开相关 memory 记录。

## 常用命令

- 启动命令：
- 测试命令：
- 静态检查命令：
- 构建或打包命令：

## 环境依赖

- 相关服务依赖文档链接：
- 外部服务：

## 质量规则

- 发现稳定的环境、架构、命令、风险信息后，及时回写到 `.psychRules/basic.md` 或 `.psychRules/rules.md`。
- `session.md` 只保留活跃工作上下文，不要把长期稳定事实写进去。
- `memory/index.md` 只记录高价值、可复用、长期有效的结论，不要堆砌流水账。
- 每次有意义的 `debug`、`fix`、`feat`、`refactor` 或 `note` 会话，都要创建一条详细 memory。
- 写完详细 memory 后，把真正值得长期保留的 1 到 3 条结论同步到 `memory/index.md`。

## Session 与 Memory 规则

- `session.md` 记录当前目标、阻塞点、下一步、正在处理的文件和最近决策。
- 一个任务结束、切换或失效后，及时刷新 `session.md`，避免把过期信息留在热上下文里。
- `memory/*.md` 记录每次会话的完整背景、改动、验证和后续事项。
- 如果某次会话仍在继续，把当前阶段性结论同步到 `session.md`。

## Memory 与 Commit 同步规则

- 如果用户要求执行 git commit，先创建或更新对应的 memory 文件，再执行 commit。
- 如果用户要求创建一条与代码变更相关的 memory，但尚未要求 commit，则应追问是否要同步创建 git commit。
- memory 文件尽量与相关代码处于同一个 commit 中。
- commit message 使用英文 conventional commit，例如：
- `feat(scope): short summary`
- `fix(scope): short summary`
- `refactor(scope): short summary`
- `docs(psych-rules): update project memory`

## 风险提示

- 已知 bug / 漏洞：
- 容易误操作的点：
- 代码审查需要重点关注的区域：

## Git 策略

- 如果目标目录已有 git，优先沿用现有仓库。
- 不要在多项目工作区或嵌套仓库结构中自动执行 `git init`，除非用户明确要求。
- 确保 `.gitignore` 中包含：`.psychRules/`；如果没有 `.gitignore`，就先创建。
- 执行 git 时优先使用：`git -c safe.directory=path_of_workflow -c core.sshCommand=C:/Windows/System32/OpenSSH/ssh.exe xxx`
