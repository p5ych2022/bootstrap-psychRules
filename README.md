# bootstrap-psychRules

`bootstrap-psychRules` 是一个用于初始化和维护项目级 `.psychRules/` 的个人 Codex skill。
它的目标不是做“全量常驻记忆”，而是建立一套低 token 成本的分层上下文系统，让后续线程更快进入状态，也更少误读历史。

## 它会生成什么

初始化后，目标目录会得到如下结构：

```text
project-root/
├─ AGENTS.md
└─ .psychRules/
   ├─ basic.md
   ├─ rules.md
   ├─ session.md
   └─ memory/
      ├─ index.md
      └─ init00_psych-rules-bootstrap.md
```

其中：

- `basic.md`：稳定事实，保存项目目标、环境、第一性原理、架构和边界。
- `rules.md`：工作规则，保存命令、风险、启动读取协议、memory/commit 同步策略。
- `session.md`：当前任务热上下文，只记录活跃工作、阻塞点、下一步和在改的文件。
- `memory/index.md`：长期记忆索引，只记录真正值得反复复用的高价值结论。
- `memory/*.md`：详细会话记录，每次重要 debug/fix/feat/refactor/note 一条。

这套结构的核心原则是：

- 稳定信息常驻：`basic.md` + `rules.md`
- 当前任务热信息短驻：`session.md`
- 历史信息按需检索：先看 `memory/index.md`，再看具体 `memory/*.md`

## 启动协议

`AGENTS.md` 会要求后续线程：

- 启动时必读 `basic.md` 和 `rules.md`
- 如果存在，再读取 `session.md`
- 不默认通读整个 `memory/`
- 只有需要历史决策、旧 bug、接续上次工作时，才先查 `memory/index.md`，再按需打开具体记录

这比“每轮 heartbeat 都扫记忆”更省 token，也更符合代码开发场景。

## 脚本

`scripts/init_psych_rules.py`

- 初始化 `.psychRules/` 骨架和 `AGENTS.md`
- 如果目标根目录已经有 `.gitignore`，会补上 `.psychRules/`

`scripts/new_memory_entry.py`

- 创建新的详细 memory 记录
- 输出建议的 conventional commit subject
- 确保 `session.md` 和 `memory/index.md` 存在
- 提醒把活跃上下文同步到 `session.md`，把长期结论同步到 `memory/index.md`

## 使用方式

自然语言是主要入口。常见说法例如：

```text
用 bootstrap-psychRules 为这个项目初始化 .psychRules
读取这个仓库的 README、.psychRules/basic.md、.psychRules/rules.md 和 session.md
为这次修复创建一条 memory，并把值得保留的结论同步到 memory/index.md
```

如果你想手动跑脚本，也可以：

```powershell
py -3 scripts/init_psych_rules.py --root "/your-project"
py -3 scripts/init_psych_rules.py --root "/your-workspace" --workspace
py -3 scripts/new_memory_entry.py --root "/your-project" --kind fix --title "repair cache merge bug" --scope p-pop
```

## Commit 与 Memory

如果目标目录已存在 git：

- 用户要求 commit 时，先创建或更新对应 memory，再尽量与代码一起提交
- 用户只要求写 memory、还没要求 commit 时，应该补问是否顺手创建 commit
- commit 标题建议用英文 conventional commit，例如 `fix(scope): short summary`

## 默认安全策略

- 不在多项目工作区或嵌套仓库里自动执行 `git init`
- 默认把 `.psychRules/` 当作私有上下文，不跟踪进版本库
- 最稳妥的做法，是把 `.psychRules/` 放在真正拥有代码和 git 历史的项目根目录
