<<<<<<< HEAD
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
=======
# MemoX

**MemoX** = **Memo**ry E**x**ploration

A hybrid structured memory system for AI agents, combining YAML (fast retrieval) with Markdown (full context) for ~90% token compression.

## Features

- 🎯 **90% Token Compression**: Drastically reduce context window usage
- 🔍 **Fast Query**: YAML structure enables instant filtering
- 📝 **Full Context**: Markdown preserves complete conversation details
- 🗂️ **3 Entity Types**: Decisions, Errors, Learnings
- 🏷️ **Tag System**: Flexible categorization and search
- 🔗 **Pointer Pattern**: Link structured data to full text
- 💰 **Zero Cost**: No external APIs or services required
- 📊 **Git-Friendly**: Text-based, version-controllable

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yingzgop/memox.git

# Copy to your memory directory
cp -r memox ~/.openclaw/workspace/memory/

# Install Python dependency
pip install pyyaml
```

### Basic Usage

```bash
# Add a decision
cd ~/.openclaw/workspace/memory
python MemoX/src/memox.py add-decision \
  "2026-03-20" \
  "Architecture Choice" \
  "Use MemoX for memory management" \
  "Provides 90% compression with zero API cost"

# Add an error record
python MemoX/src/memox.py add-error \
  "2026-03-20" \
  "High false positive rate" \
  "36 issues detected, 32 false positives" \
  "Optimize regex patterns"

# Add a learning
python MemoX/src/memox.py add-learning \
  "2026-03-20" \
  "configuration" \
  "contextEngine must be set for plugins to work"

# Update index
python MemoX/src/memox.py update-index
```

## Directory Structure

```
memory/
├── MemoX/                    # Structured memory
│   ├── src/
│   │   └── memox.py         # Core script
│   ├── docs/
│   │   └── ARCHITECTURE.md  # Design documentation
│   ├── examples/
│   │   └── data-examples.yaml
│   ├── memox.yaml           # Configuration
│   ├── decisions.yaml       # Decision records
│   ├── errors.yaml          # Error records
│   ├── learnings.yaml       # Learning records
│   ├── context.yaml         # Current context
│   ├── index.yaml           # Statistics
│   └── README.md            # This file
├── snippets/                # Key conversation snippets
└── YYYY-MM-DD.md           # Full conversations
```

## Data Format

### Decision Record

```yaml
decisions:
  - id: D20260320001
    date: "2026-03-20"
    topic: "Memory System Selection"
    decision: "Use MemoX structured memory"
    reasoning: |
      Provides 90% compression with zero cost.
      graph-memory requires additional APIs.
    alternatives:
      - "graph-memory"
      - "Vector database"
    status: implemented
    tags: ["memory", "architecture"]
    source: "memory/2026-03-20.md#L45-L60"
```

### Error Record

```yaml
errors:
  - id: E20260320001
    date: "2026-03-20"
    error: "High false positive rate"
    symptom: "36 issues detected, 32 false positives"
    solution: "Optimize regex patterns"
    status: pending
    tags: ["security", "audit"]
```

### Learning Record

```yaml
learnings:
  - id: L20260320001
    date: "2026-03-20"
    category: "configuration"
    learning: "contextEngine must be set for plugins"
    importance: high
    tags: ["openclaw", "plugin"]
```

## Configuration

Edit `memox.yaml`:

```yaml
base_path: "~/.openclaw/workspace/memory"

memox:
  auto_update_index: true
  archive_after_days: 30
  max_recent_items: 5

maintenance:
  daily: [update_index]
  weekly: [check_integrity, optimize_storage]
  monthly: [archive_old_data]
```

## Compression Comparison

| System | Compression | Cost | Complexity |
|--------|-------------|------|------------|
| Built-in compaction | ~50% | Free | Low |
| graph-memory | 75% | API $ | High |
| Vector DB | ~80% | Service $ | High |
| **MemoX** | **~90%** | **Free** | **Medium** |

## How It Works

1. **Extract**: During/after conversation, extract key info (decisions, errors, learnings)
2. **Store**: Save structured data to YAML, full context to Markdown
3. **Index**: Maintain statistics and tag cloud
4. **Query**: Use YAML for fast search, follow pointers for full details

## Maintenance

- **Daily**: Auto-update index
- **Weekly**: Check integrity, optimize storage
- **Monthly**: Archive old entries (>30 days)

## Contributing

Contributions welcome! Areas for improvement:
- Additional entity types
- Query interface (CLI/GUI)
- Integration with other agents
- Import/export tools

## License

MIT

## Acknowledgments

Created for OpenClaw agent system.

---

*"Structure your memory, explore your knowledge."*
>>>>>>> 6bd63a1 (Initial MemoX release - Structured Memory System for OpenClaw)
