# OpenClaw Skill

MemoX 的 OpenClaw 技能，支持通过自然语言触发记录记忆。

## 安装

```bash
# 复制技能到 OpenClaw 技能目录
cp -r skills/memox ~/.agents/skills/
```

## 触发关键词

### 直接请求
- "记录这个"、"记住"、"记下来"
- "记一下"、"保存这个"、"别忘了"
- "标记一下"、"写进备忘录"

### 决策记录
- "我决定..."、"我们决定..."
- "选用..."、"采用...方案"
- "最终选择..."、"确定用..."

### 错误与解决
- "问题是..."、"错误是..."
- "解决了..."、"修复了..."
- "原因是..."、"根因是..."

### 学习记录
- "我学到..."、"我发现..."
- "原来..."、"才知道..."
- "意识到..."、"明白了..."

### 重要信息
- "这个很重要..."
- "注意..."、"切记..."
- "值得记住..."

## 使用示例

用户说："**记录一下**，我们决定用 Docker"

系统自动执行：
```bash
python ~/.agents/skills/memox/scripts/record.py decision \
  --date "2026-03-23" \
  --topic "部署方案" \
  --decision "使用 Docker" \
  --reasoning "便于环境一致性管理"
```

## 文件结构

```
skills/memox/
├── SKILL.md          # 技能定义文档
└── record.py         # 快速记录脚本
```

## 依赖

需要 MemoX 核心脚本已安装：
```bash
# 确保 memox.py 在正确位置
~/.openclaw/workspace/memory/MemoX/src/memox.py
```
