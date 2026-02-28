# Simple Notes App with File Storage

一个简单的Python笔记应用，支持文件存储和基本CRUD操作。

## 功能特性

- ✅ 创建、读取、更新、删除笔记
- ✅ 文件存储（JSON格式）
- ✅ 笔记搜索功能
- ✅ 标签支持
- ✅ 归档功能
- ✅ 导出功能（JSON/TXT格式）
- ✅ 命令行界面

## 安装

```bash
# 克隆项目
git clone [项目地址]

# 进入目录
cd simple_notes_project

# 运行应用
python3 notes_app.py
```

## 使用方法

### 基本使用

```python
from notes_app import NotesApp

# 创建应用实例
app = NotesApp()

# 创建笔记
note = app.create_note(
    title="我的笔记",
    content="这是笔记内容",
    tags=["重要", "工作"]
)

# 获取所有笔记
notes = app.get_all_notes()

# 搜索笔记
results = app.search_notes("工作")

# 更新笔记
app.update_note(note_id=1, content="更新后的内容")

# 删除笔记
app.delete_note(note_id=1)
```

### 命令行界面

```bash
# 运行演示
python3 notes_app.py

# 运行测试
python3 test_notes_app.py
```

## 项目结构

```
simple_notes_project/
├── notes_app.py          # 核心应用代码
├── test_notes_app.py     # 单元测试
├── requirements.txt      # 依赖包
├── README.md            # 说明文档
└── examples/            # 使用示例
    ├── basic_usage.py
    └── advanced_features.py
```

## 技术栈

- Python 3.8+
- 标准库：json, os, datetime, pathlib
- 无外部依赖

## 贡献指南

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 推送到分支
5. 创建Pull Request

## 许可证

MIT License

## 作者

[你的名字] - GitHub赏金猎人