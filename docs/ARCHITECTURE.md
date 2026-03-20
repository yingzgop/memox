# MemoX Architecture

## Overview

MemoX is a hybrid memory system combining:
- **YAML** for structured, queryable data
- **Markdown** for full context preservation
- **~90% token compression** vs raw conversation

## Directory Structure

```
memory/
├── MemoX/                    # Structured memory (YAML)
│   ├── memox.yaml           # Configuration
│   ├── decisions.yaml       # Decision records
│   ├── errors.yaml          # Error & solution records
│   ├── learnings.yaml       # Learning records
│   ├── context.yaml         # Current session context
│   ├── index.yaml           # Statistics & index
│   └── README.md            # Documentation
├── snippets/                # Key conversation snippets
│   └── YYYY-MM-DD/
│       ├── key-quote-1.txt
│       └── key-quote-2.txt
└── YYYY-MM-DD.md           # Full conversation (Markdown)
```

## Data Flow

```
Conversation
    ↓
[Extract Key Info] → YAML (MemoX/)
    ↓
[Store Full Context] → Markdown (YYYY-MM-DD.md)
    ↓
[Update Index] → index.yaml
    ↓
[Query] ← YAML (fast) or Markdown (detailed)
```

## Entity Types

### Decision (D{date}{seq})
- What: Choice made
- Why: Reasoning
- Alternatives: Options considered
- Status: implemented/pending/rejected

### Error (E{date}{seq})
- What: Error description
- Symptom: How it manifested
- Solution: How it was fixed
- Status: open/workaround/resolved

### Learning (L{date}{seq})
- What: Knowledge gained
- Category: Domain
- Importance: high/medium/low
- Source: Where learned

## Compression Strategy

| Type | Raw Tokens | MemoX | Rate |
|------|-----------|-------|------|
| Decision | 500 | 50 | 90% |
| Error | 1000 | 100 | 90% |
| Learning | 2000 | 150 | 92% |

**Key insight**: Store pointers to full context, not full text.

## Query Patterns

### Fast Query (YAML)
```python
# Find all decisions about memory
[ d for d in decisions if "memory" in d.tags ]

# Find high-priority learnings
[ l for l in learnings if l.importance == "high" ]
```

### Detailed Query (Follow pointer)
```python
# Get full context
decision = find_decision("D20260320001")
full_text = load_markdown(decision.source)  # "memory/2026-03-20.md#L45-L60"
```

## Maintenance

### Daily
- Update index on new entries

### Weekly
- Check data integrity
- Optimize storage

### Monthly
- Archive old entries (>30 days)
- Remove duplicates
- Compress historical data

## Comparison with Alternatives

| System | Compression | Complexity | Cost | Cross-Session |
|--------|-------------|------------|------|---------------|
| Built-in compaction | ~50% | Low | Free | Partial |
| graph-memory | 75% | High | API $ | Strong |
| Vector DB | ~80% | High | Service $ | Strong |
| **MemoX** | **~90%** | **Medium** | **Free** | **Medium** |

## Design Principles

1. **Human-readable**: YAML is easy to read and edit
2. **Git-friendly**: Text-based, diffable
3. **Zero dependencies**: No external services
4. **Extensible**: Easy to add new entity types
5. **Transparent**: Full audit trail in Markdown
