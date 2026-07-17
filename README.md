# Visual UI Production

一个面向非专业设计师、前端初学者和独立游戏开发者的 Codex Skill。

它把 UI 工作拆成一条可见、可确认、可落地的流程：

1. 读取真实项目与现有界面；
2. 使用 Creative Production 和 ImageGen 生成可见方案；
3. 等待用户明确选择；
4. 将选定方案拆成可维护的素材、文字和语义控件；
5. 导入 Ren'Py、网页、桌面或移动应用；
6. 运行真实项目并进行视觉与交互验证。

The skill is designed for visual-first, approval-driven UI production. It shows
the design before implementation, preserves approved layouts, and keeps final
text and interactive controls deterministic in project code.

> 当前发布线：`v1.0.1`。仓库中的演示全部使用合成内容，不包含真实项目、
> 私人截图、人物照片或第三方商业素材。

## 适用场景

- 游戏主菜单、对话框、选项、存档、设置和档案界面；
- 网页、桌面应用和移动应用的 UI 新建或重设计；
- 现有界面过于模板化、AI 感明显、排版错位或可读性不足；
- 根据截图或已确认的视觉稿忠实实现真实界面；
- 使用生成式视觉工具制作纹理、边框、背景和装饰素材。

## 核心原则

- 先给用户看图，再开始写界面代码；
- 每个关键阶段都需要明确确认；
- 已确认的构图只做局部、可控修改；
- 正文、按钮文字、数字和交互控件由项目代码渲染；
- 生成图片主要负责纹理、氛围、边框和其他图像原生元素；
- 草稿与测试数据不进入正式项目素材目录；
- 同一时间最多运行一个游戏、服务器、浏览器或测试进程。

## 仓库结构

```text
visual-ui-production/
|-- .github/workflows/
|   |-- ci.yml
|   `-- release.yml
|-- examples/
|   |-- web-dashboard/
|   |-- desktop-settings/
|   `-- game-save-menu/
|-- tests/
|-- tools/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- .gitignore
`-- skills/
    `-- visual-ui-production/
        |-- SKILL.md
        |-- agents/
        |   `-- openai.yaml
        |-- references/
        |   |-- adapters-*.md
        |   |-- asset-manifest.md
        |   |-- design-lock.md
        |   |-- framework-routing.md
        |   `-- ...
        `-- scripts/
            |-- build_asset_manifest.py
            |-- compare_ui_screenshots.py
            |-- create_design_lock.py
            `-- inspect_ui_assets.py
```

## 前置条件

- 支持 Skills 的 Codex 环境；
- ImageGen，可用于生成或编辑位图视觉稿和 UI 素材；
- Creative Production 为推荐能力，但不是安装本 Skill 的硬性依赖；
- Python 3.10 或更高版本；
- Pillow，用于图片素材审计和截图对比脚本。

安装脚本依赖：

```bash
python -m pip install -r requirements.txt
```

## 安装

### 使用 Skill Installer

在 Codex 中调用 `$skill-installer`，要求它安装以下目录：

```text
https://github.com/Hypergg4631/visual-ui-production/tree/main/skills/visual-ui-production
```

安装完成后，新建一个 Codex 任务或重新启动 Codex，使 Skill 被重新发现。

### 手动安装

将 `skills/visual-ui-production` 整个目录复制到：

Windows：

```text
%USERPROFILE%\.codex\skills\visual-ui-production
```

macOS 或 Linux：

```text
~/.codex/skills/visual-ui-production
```

不要只复制 `SKILL.md`。`agents`、`references` 和 `scripts` 都属于 Skill 的
正式组成部分。

安装后可以运行：

```bash
python skills/visual-ui-production/scripts/create_design_lock.py --help
python skills/visual-ui-production/scripts/build_asset_manifest.py --help
python skills/visual-ui-production/scripts/compare_ui_screenshots.py --help
python skills/visual-ui-production/scripts/inspect_ui_assets.py --help
```

## 快速使用

可以在 Codex 中直接使用下面的提示词：

```text
使用 $visual-ui-production 重新设计这个 Ren'Py 主菜单。
先生成 3 个我能直接看见的完整方案，等我选定后再修改项目文件。
```

```text
使用 $visual-ui-production 忠实实现我选中的 UI 截图。
保留现有功能、存档兼容性和文字内容，先列出需要拆分的素材。
```

```text
使用 $visual-ui-production 检查当前设置页面的字体、对齐、悬停反馈和长文本排版。
一次只启动一个测试进程。
```

## 匿名演示

[`examples/`](examples/) 提供三个完全合成的演示：

- Web 数据看板；
- 桌面软件设置页；
- 游戏存档菜单。

每个演示都记录“原界面 → 可见方向 → 设计锁 → 素材清单 → 代码实现 →
截图对比”的交付链。示意图只表达工作流和组件边界，不冒充真实客户项目或
ImageGen 输出。

## 附带工具

创建并验证设计锁：

```bash
python skills/visual-ui-production/scripts/create_design_lock.py validate path/to/design-lock.json --require-approved
```

创建并验证素材清单：

```bash
python skills/visual-ui-production/scripts/build_asset_manifest.py validate path/to/asset-manifest.json
```

对比参考截图与运行截图：

```bash
python skills/visual-ui-production/scripts/compare_ui_screenshots.py reference.png actual.png --output-dir comparison
```

图片素材审计：

Skill 附带一个只读脚本，用来检查图片尺寸、格式、透明通道、SHA-256 和重复内容：

```bash
python skills/visual-ui-production/scripts/inspect_ui_assets.py path/to/assets
```

生成 JSON 报告：

```bash
python skills/visual-ui-production/scripts/inspect_ui_assets.py path/to/assets --json report.json
```

脚本不会修改被检查的图片。

## 本地验证

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/package_skill.py
```

CI 会检查 Python 3.10 和 3.12、frontmatter、相对资源链接、匿名示例、
四个脚本的端到端冒烟测试，以及禁止发布的缓存和本机信息。

## 隐私与素材

本仓库不应包含：

- API Key、Token、密码或 `.env`；
- 本机绝对路径、用户名或测试进程数据；
- 聊天记录、朋友照片或其他个人身份素材；
- 未获得授权的字体、图片、音效、游戏截图或商业素材；
- ImageGen 草稿、Creative Production 工作区内容或具体项目的生成结果。

Creative Production、ImageGen、Ren'Py 和其他外部工具不包含在本仓库中。
本项目仅提供工作流说明、参考文档和辅助脚本。

## 发布检查

公开新版本前：

1. 验证 `skills/visual-ui-production/SKILL.md` 的 frontmatter；
2. 检查相对链接和 `agents/openai.yaml`；
3. 搜索密钥、本机路径和个人信息；
4. 确认没有 `__pycache__`、`.pyc`、日志或生成草稿；
5. 从仓库副本执行一次全新安装；
6. 运行三个匿名示例和四个脚本的端到端测试；
7. 执行 `python tools/package_skill.py` 并检查压缩包；
8. 使用语义化版本标签；当前稳定版本为 `v1.0.1`。

## 贡献与安全

提交改动前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。敏感信息或授权问题请按
[SECURITY.md](SECURITY.md) 中的私下报告方式处理，不要在公开 Issue 中粘贴密钥
或私人素材。

## 许可

本项目使用 [MIT License](LICENSE)。

仓库许可证只覆盖本仓库原创内容，不自动授予任何第三方字体、图片、插件、
模型输出或项目素材的使用权。
