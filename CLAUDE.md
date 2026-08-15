# Warpforge 解包项目 — 行为准则

## 🔒 安全红线（必须遵守）

1. **`~/.claude.json` 和 `~/.cc-switch/` 绝不同步网盘、不上传、不提交 git**——里面包含 API key 等敏感配置。任何备份/迁移/分享操作都不得包含这两个位置的文件。
2. **API key（MINIMAX_API_KEY 等）不写入任何项目文件、代码、文档、日志**——只从环境变量读取；不打印 key 值；配置里只用 `${MINIMAX_API_KEY}` 占位。
3. 对话中出现的 key 属于敏感信息，不引用、不重复、不写入任何持久化内容。

## 项目结构速览

- `解包整理/` — 解包资源（12 大类，44.9 万文件），入口文档 `解包整理/README.md`
- `Warhammer 40k Warpforge/` — 游戏本体（只读，不修改）
- `Warpforge_code/` — 反编译 C# 代码（查逻辑/枚举/字段用）
- `Warpforge_tools/` — Python 工具集（py312 环境 + 脚本），README 见 `Warpforge_tools/README.md`

## 常用约定

- 运行脚本用 `d:/2/Warpforge_tools/py312/python.exe`（勿用系统 Python 3.14）
- 卡图/资源路径相对 `d:/2/解包整理/`；卡牌索引 `解包整理/card_index.json`
- 视觉识别：用户要求看图时，走 vision skill（MCP 调用副模型），主模型无法直接看图
- 大文件/资源不动则不动；改动前先备份（用户要求：备份 → 测试 → 通过后删备份）
