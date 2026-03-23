---
name: memox
description: 记录结构化记忆（决策、错误、学习）到 MemoX YAML 文件。当用户想要记住重要信息、记录决策、记录错误和解决方案、或记录学习内容时使用。触发词包括"记录这个"、"记住"、"记下来"、"别忘了"、"我决定"、"问题是"、"解决了"、"我学到"、"发现"、"重要"、"关键点"等。
---

# MemoX 技能

将重要信息记录到结构化记忆（YAML）中，以便后续检索。

## 何时使用

当用户有以下表达时触发此技能：

### 直接请求（记录）
- "记录这个"、"记住"、"记下来"
- "记一下"、"保存这个"、"别忘了"
- "标记一下"、"写进备忘录"
- "帮忙记着"、"提醒一下"

### 决策记录
- "我决定..."、"我们决定..."
- "选用..."、"采用...方案"
- "最终选择..."、"确定用..."
- "定了，就用..."、"敲定..."

### 错误与解决
- "问题是..."、"错误是..."
- "解决了..."、"修复了..."
- "原因是..."、"根因是..."
- "临时方案是..."、"解决办法是..."

### 学习记录
- "我学到..."、"我发现..."
- "原来..."、"才知道..."
- "意识到..."、"明白了..."
- "关键是..."、"重点是..."
- "经验是..."、"教训是..."

### 重要信息
- "这个很重要..."
- "注意..."、"切记..."
- "值得记住..."、"务必..."
- "参考..."、"备忘..."

## 触发模式

在对话中寻找以下模式：

| 模式 | 示例 | 操作 |
|------|------|------|
| `[记录/记住]这个` | "记录这个配置" | 记录当前主题 |
| `我[决定/选定]...` | "我决定用Docker" | 记录决策 |
| `问题是...[解决/修复]...` | "问题是超时，解决了" | 记录错误 |
| `我[学到/发现]...` | "我学到异步更快" | 记录学习 |
| `原来...[这样/如此]` | "原来YAML需要引号" | 记录学习 |
| `[关键/重点]是...` | "关键是缓存" | 记录学习 |
| `别忘了...[做/设置]...` | "别忘了设置环境变量" | 记录备忘 |

## 如何使用

### 方式1：直接调用（推荐）

使用提供的脚本记录记忆：

```bash
# 记录决策
python ~/.agents/skills/memox/scripts/record.py decision \
  --date "2026-03-20" \
  --topic "系统架构" \
  --decision "使用PostgreSQL而不是MySQL" \
  --reasoning "更好的JSON支持和扩展性"

# 记录错误
python ~/.agents/skills/memox/scripts/record.py error \
  --date "2026-03-20" \
  --error "连接超时" \
  --symptom "API调用30秒后失败" \
  --solution "增加超时到60秒并添加重试逻辑"

# 记录学习
python ~/.agents/skills/memox/scripts/record.py learning \
  --date "2026-03-20" \
  --category "Python" \
  --learning "asyncio.gather()是并发执行而非顺序执行"
```

### 方式2：自然语言

与用户确认细节后记录：

用户："记住我们决定用Docker部署"
→ 确认："记录决策：用Docker部署。有什么具体理由吗？"
→ 执行：record.py decision ...

## 数据格式

记录保存到：
- `~/.openclaw/workspace/memory/MemoX/decisions.yaml`
- `~/.openclaw/workspace/memory/MemoX/errors.yaml`
- `~/.openclaw/workspace/memory/MemoX/learnings.yaml`

## 示例

### 示例1：记录决策

用户："**我们决定**用React做前端**而不是**Vue"

操作：
```python
python ~/.agents/skills/memox/scripts/record.py decision \
  --date "2026-03-20" \
  --topic "前端框架选择" \
  --decision "使用React而不是Vue" \
  --reasoning "更大的生态系统，更多可用开发者，更好的TypeScript支持" \
  --alternatives "Vue,Svelte" \
  --status "implemented"
```

### 示例2：记录错误

用户："**解决了**那个bug - **问题是**API key没放在header里"

操作：
```python
python ~/.agents/skills/memox/scripts/record.py error \
  --date "2026-03-20" \
  --error "API认证失败" \
  --symptom "所有API调用返回401未授权" \
  --solution "将API key从查询参数移到Authorization header" \
  --status "resolved"
```

### 示例3：记录学习

用户："**我学到**Python的defaultdict可以接受工厂函数"

操作：
```python
python ~/.agents/skills/memox/scripts/record.py learning \
  --date "2026-03-20" \
  --category "Python" \
  --learning "defaultdict接受一个生成默认值的工厂函数" \
  --importance "medium"
```

## 更多触发示例

| 用户说的话 | 识别为 | 操作 |
|-----------|--------|------|
| "**记录一下**，我们用Docker" | 决策 | 记录技术选型 |
| "**别忘了**，生产环境不一样" | 备忘 | 记录环境差异 |
| "**问题是**超时，**解决方式**是加缓存" | 错误 | 记录问题与解决 |
| "**我发现**Python字典是有序的" | 学习 | 记录知识点 |
| "**原来**YAML字符串需要引号" | 学习 | 记录语法细节 |
| "**关键是**缓存能减少90%负载" | 学习 | 记录性能优化 |
| "**经验教训**：要测真实数据" | 学习 | 记录最佳实践 |
| "**经验法则**：>100ms就要考虑缓存" | 学习 | 记录经验规则 |
| "**注意**，API限制是1000/小时" | 备忘 | 记录限制 |
| "**值得记住**，小团队更快" | 学习 | 记录团队洞察 |

## 最佳实践

1. **记录前确认** - 确保理解正确
2. **提取关键信息** - 不要全记，只记重点
3. **建议标签** - 帮助分类以便后续检索
4. **更新索引** - 记录后运行 `memox.py update-index`

## 集成

记录后，记忆将：
1. 保存到YAML文件
2. 建立索引供搜索
3. 可通过 `memox_query.py` 查询
4. 通过心跳注入MEMORY.md（如已配置）
