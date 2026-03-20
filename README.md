# MemoX - 结构化记忆系统

**MemoX** = **Memo**ry E**x**ploration（记忆探索）

混合架构的记忆管理系统，结合 YAML 结构化数据（快速检索）和 Markdown 完整记录（保留上下文）。

## 目录结构

```
memory/
├── MemoX/                    # 结构化记忆（YAML）
│   ├── decisions.yaml        # 关键决策记录
│   ├── errors.yaml           # 错误和解决方案
│   ├── learnings.yaml        # 学习记录
│   ├── context.yaml          # 当前上下文/状态
│   └── index.yaml            # 统计索引
├── snippets/                 # 关键对话片段
│   └── YYYY-MM-DD/
└── YYYY-MM-DD.md            # 完整对话记录（Markdown）
```

## 压缩效果

| 内容类型 | 原始对话 | MemoX | 压缩率 |
|---------|---------|-------|--------|
| 简单决策 | 500 tokens | 50 tokens | 90% |
| 错误解决 | 1000 tokens | 100 tokens | 90% |
| 复杂学习 | 2000 tokens | 150 tokens | 92% |

平均压缩率：**~90%**

## 使用方式

### 添加决策
```bash
python scripts/update_structured_memory.py add-decision \
  "2026-03-20" \
  "话题" \
  "决策内容" \
  "决策理由"
```

### 添加错误
```bash
python scripts/update_structured_memory.py add-error \
  "2026-03-20" \
  "错误描述" \
  "症状" \
  "解决方案"
```

### 添加学习
```bash
python scripts/update_structured_memory.py add-learning \
  "2026-03-20" \
  "类别" \
  "学习内容"
```

### 更新索引
```bash
python scripts/update_structured_memory.py update-index
```

## 维护计划

- **每日**: 自动更新索引
- **每周**: 完整检查和优化
- **每月**: 归档旧数据

## 数据格式

所有 YAML 文件遵循统一格式，包含：
- `id`: 唯一标识（如 D20260320001）
- `date`: 日期
- `tags`: 标签列表
- `source`: 指向原始 Markdown 的链接

---
*Created: 2026-03-20*
*Version: 1.0*
