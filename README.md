# MemoX

**MemoX** = **Memo**ry E**x**ploration

A hybrid structured memory system for AI agents, combining YAML (fast retrieval) with Markdown (full context) for ~90% token compression.

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

### Features

- 🎯 **90% Token Compression**: Drastically reduce context window usage
- 🔍 **Fast Query**: YAML structure enables instant filtering
- 📝 **Full Context**: Markdown preserves complete conversation details
- 🗂️ **3 Entity Types**: Decisions, Errors, Learnings
- 🏷️ **Tag System**: Flexible categorization and search
- 🔗 **Pointer Pattern**: Link structured data to full text
- ⚙️ **Configurable**: YAML-based configuration
- 💰 **Zero Cost**: No external APIs or services required
- 📊 **Git-Friendly**: Text-based, version-controllable
- 🔄 **Heartbeat Integration**: Auto-inject to agent context

### Quick Start

#### Installation

```bash
# Clone the repository
git clone https://github.com/yingzgop/memox.git

# Copy to your memory directory
cp -r memox ~/.openclaw/workspace/memory/

# Install Python dependency
pip install pyyaml
```

#### Configuration

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

#### Basic Usage

```bash
cd ~/.openclaw/workspace/memory

# Add a decision
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

# Query structured memory
python MemoX/src/memox_query.py recent
python MemoX/src/memox_query.py search "memory"

# Inject to agent context (heartbeat)
python MemoX/src/memox_inject.py
```

### Directory Structure

```
memory/
├── MemoX/                    # Structured memory
│   ├── src/
│   │   ├── memox.py         # Core update script
│   │   ├── memox_query.py   # Query tool
│   │   └── memox_inject.py  # Context injection
│   ├── docs/
│   │   └── ARCHITECTURE.md
│   ├── examples/
│   │   └── data-examples.yaml
│   ├── memox.yaml           # Configuration
│   ├── decisions.yaml       # Decision records
│   ├── errors.yaml          # Error records
│   ├── learnings.yaml       # Learning records
│   ├── context.yaml         # Current context
│   └── index.yaml           # Statistics
├── snippets/                # Key conversation snippets
└── YYYY-MM-DD.md           # Full conversations
```

### Tools

| Script | Purpose |
|--------|---------|
| `memox.py` | Add/update structured memory entries |
| `memox_query.py` | Query and search memory |
| `memox_inject.py` | Inject memory to agent context |

### Data Format

See [examples/data-examples.yaml](examples/data-examples.yaml)

### Architecture

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

### Comparison

| System | Compression | Cost | Complexity |
|--------|-------------|------|------------|
| Built-in compaction | ~50% | Free | Low |
| graph-memory | 75% | API $ | High |
| Vector DB | ~80% | Service $ | High |
| **MemoX** | **~90%** | **Free** | **Medium** |

---

<a name="中文"></a>
## 中文

### 特性

- 🎯 **90% Token 压缩率**：大幅降低上下文窗口占用
- 🔍 **快速查询**：YAML 结构支持即时过滤
- 📝 **完整上下文**：Markdown 保留完整对话细节
- 🗂️ **3 种实体类型**：决策、错误、学习
- 🏷️ **标签系统**：灵活分类和搜索
- 🔗 **指针模式**：结构化数据链接到完整文本
- ⚙️ **可配置**：基于 YAML 的配置
- 💰 **零成本**：无需外部 API 或服务
- 📊 **Git 友好**：纯文本，可版本控制
- 🔄 **心跳集成**：自动注入到代理上下文

### 快速开始

#### 安装

```bash
# 克隆仓库
git clone https://github.com/yingzgop/memox.git

# 复制到记忆目录
cp -r memox ~/.openclaw/workspace/memory/

# 安装 Python 依赖
pip install pyyaml
```

#### 配置

编辑 `memox.yaml`：

```yaml
base_path: "~/.openclaw/workspace/memory"

memox:
  auto_update_index: true
  archive_after_days: 30
  max_recent_items: 5
```

#### 基本用法

```bash
cd ~/.openclaw/workspace/memory

# 添加决策
python MemoX/src/memox.py add-decision \
  "2026-03-20" \
  "架构选择" \
  "使用 MemoX 管理记忆" \
  "零 API 成本，90% 压缩率"

# 添加错误记录
python MemoX/src/memox.py add-error \
  "2026-03-20" \
  "误报率高" \
  "检测到 36 个问题，32 个误报" \
  "优化正则表达式"

# 添加学习
python MemoX/src/memox.py add-learning \
  "2026-03-20" \
  "配置" \
  "必须设置 contextEngine 才能启用插件"

# 更新索引
python MemoX/src/memox.py update-index

# 查询记忆
python MemoX/src/memox_query.py recent
python MemoX/src/memox_query.py search "memory"

# 注入到代理上下文（心跳）
python MemoX/src/memox_inject.py
```

### 工具脚本

| 脚本 | 用途 |
|------|------|
| `memox.py` | 添加/更新结构化记忆条目 |
| `memox_query.py` | 查询和搜索记忆 |
| `memox_inject.py` | 注入记忆到代理上下文 |

---

## License

MIT

## Acknowledgments

Created for OpenClaw agent system.

---

*"Structure your memory, explore your knowledge."*  
*"结构化你的记忆，探索你的知识。"*
