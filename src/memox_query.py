#!/usr/bin/env python3
"""
MemoX Query Tool
查询结构化记忆并输出到控制台
"""

import yaml
import sys
from pathlib import Path

def load_yaml(filepath):
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    return {}

def search_by_tag(memox_path, tag):
    """Search all entities by tag"""
    results = []
    
    for filename in ['decisions.yaml', 'errors.yaml', 'learnings.yaml']:
        data = load_yaml(memox_path / filename)
        items = data.get(filename.replace('.yaml', 's'), [])
        
        for item in items:
            if tag in item.get('tags', []):
                results.append({
                    'type': filename.replace('.yaml', ''),
                    'id': item.get('id'),
                    'content': item.get('topic', item.get('error', item.get('learning', '')))
                })
    
    return results

def get_recent(memox_path, count=3):
    """Get recent entries from context"""
    context = load_yaml(memox_path / 'context.yaml')
    
    return {
        'decisions': context.get('recent_decisions', [])[:count],
        'errors': context.get('recent_errors', [])[:count],
        'learnings': context.get('recent_learnings', [])[:count]
    }

def main():
    memox_path = Path.home() / '.openclaw/workspace/memory/MemoX'
    
    if len(sys.argv) < 2:
        print("MemoX Query Tool")
        print("")
        print("Usage: python memox_query.py <command>")
        print("")
        print("Commands:")
        print("  recent              Show recent entries")
        print("  search <tag>        Search by tag")
        print("  stats               Show statistics")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'recent':
        recent = get_recent(memox_path)
        print("Recent MemoX Entries:")
        print("-" * 40)
        for category, items in recent.items():
            print(f"\n{category.upper()}:")
            for item_id in items:
                print(f"  - {item_id}")
                
    elif command == 'search' and len(sys.argv) >= 3:
        tag = sys.argv[2]
        results = search_by_tag(memox_path, tag)
        print(f"Results for tag '{tag}':")
        print("-" * 40)
        for r in results:
            print(f"[{r['type']}] {r['id']}: {r['content'][:50]}")
            
    elif command == 'stats':
        index = load_yaml(memox_path / 'index.yaml')
        stats = index.get('metadata', {}).get('total_entries', {})
        print("MemoX Statistics:")
        print("-" * 40)
        for key, value in stats.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
