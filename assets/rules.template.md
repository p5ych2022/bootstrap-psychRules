# 项目规则

## 语言规则

- `.psychRules/` 内文件名保持英文。
- `.psychRules/` 内文件内容以中文为主。
- 中文优先，英文仅作补充。
- `.psychRules/` 可能包含敏感信息，默认不纳入版本控制。
- git commit 标题默认使用英文 conventional commit 风格。

## 常用命令

- 启动命令：
- 测试命令：
- 静态检查命令：
- 构建或打包命令：

## 环境依赖

- 相关服务依赖文档链接：
- 外部服务：

## 质量规则

- 在进行实质性工作前先阅读 `.psychRules/basic.md` 和本文件。
- 发现稳定的环境、架构、命令、风险信息后，及时回写到 `.psychRules/`。
- 每次有意义的 `debug`、`fix`、`feat`、`refactor` 或 `note` 会话，都要创建一条 memory。

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
