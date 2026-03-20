#!/usr/bin/env python3
"""
MemoX to MEMORY.md Injector
将结构化记忆注入到长期记忆中
"""

import yaml
import re
from datetime import datetime
from pathlib import Path

class MemoXInjector:
    def __init__(self):
        self.memory_path = Path.home() / ".openclaw/workspace/memory"
        self.memox_path = self.memory_path / "MemoX"
        self.memory_md = Path.home() / ".openclaw/workspace/MEMORY.md"
        
    def load_yaml(self, filepath):
        """Load YAML file"""
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        return {}
    
    def format_decision(self, d):
        """Format decision entry"""
        lines = [
            f"- **{d['id']}**: {d['topic']}",
            f"  - Decision: {d['decision']}",
            f"  - Reason: {d.get('reasoning', 'N/A')[:100]}..." if len(d.get('reasoning', '')) > 100 else f"  - Reason: {d.get('reasoning', 'N/A')}",
        ]
        if d.get('tags'):
            lines.append(f"  - Tags: {', '.join(d['tags'])}")
        return '\n'.join(lines)
    
    def format_error(self, e):
        """Format error entry"""
        lines = [
            f"- **{e['id']}**: {e['error']}",
            f"  - Solution: {e.get('solution', 'N/A')[:100]}..." if len(e.get('solution', '')) > 100 else f"  - Solution: {e.get('solution', 'N/A')}",
        ]
        if e.get('tags'):
            lines.append(f"  - Tags: {', '.join(e['tags'])}")
        return '\n'.join(lines)
    
    def format_learning(self, l):
        """Format learning entry"""
        lines = [
            f"- **{l['id']}**: {l.get('category', 'General')}",
            f"  - {l['learning'][:150]}..." if len(l['learning']) > 150 else f"  - {l['learning']}",
        ]
        if l.get('tags'):
            lines.append(f"  - Tags: {', '.join(l['tags'])}")
        return '\n'.join(lines)
    
    def generate_memox_section(self):
        """Generate MemoX summary section"""
        # Load data
        decisions = self.load_yaml(self.memox_path / "decisions.yaml").get("decisions", [])
        errors = self.load_yaml(self.memox_path / "errors.yaml").get("errors", [])
        learnings = self.load_yaml(self.memox_path / "learnings.yaml").get("learnings", [])
        
        if not decisions and not errors and not learnings:
            return None
        
        # Get recent entries (last 5 of each)
        recent_decisions = decisions[-5:] if decisions else []
        recent_errors = [e for e in errors if e.get('status') != 'resolved'][-3:] if errors else []
        recent_learnings = learnings[-5:] if learnings else []
        
        lines = [
            "## 📊 MemoX 结构化记忆摘要",
            "",
            f"*自动更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
            "",
        ]
        
        # Decisions
        if recent_decisions:
            lines.extend([
                "### 关键决策",
                "",
            ])
            for d in recent_decisions:
                lines.append(self.format_decision(d))
            lines.append("")
        
        # Active Errors
        if recent_errors:
            lines.extend([
                "### 待解决问题",
                "",
            ])
            for e in recent_errors:
                lines.append(self.format_error(e))
            lines.append("")
        
        # Learnings
        if recent_learnings:
            lines.extend([
                "### 重要学习",
                "",
            ])
            for l in recent_learnings:
                lines.append(self.format_learning(l))
            lines.append("")
        
        lines.append("---")
        lines.append("")
        
        return '\n'.join(lines)
    
    def inject_to_memory(self):
        """Inject MemoX section into MEMORY.md"""
        memox_section = self.generate_memox_section()
        if not memox_section:
            print("No MemoX data to inject")
            return False
        
        # Read current MEMORY.md
        if self.memory_md.exists():
            with open(self.memory_md, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = "# MEMORY.md - 长期记忆\n\n"
        
        # Check if MemoX section already exists
        memox_pattern = r'## 📊 MemoX 结构化记忆摘要.*?---\n\n'
        
        if re.search(memox_pattern, content, re.DOTALL):
            # Replace existing section
            new_content = re.sub(memox_pattern, memox_section, content, flags=re.DOTALL)
            action = "Updated"
        else:
            # Insert after header or at specific position
            # Try to insert after "## 核心身份" or at the beginning
            if "## 核心身份" in content:
                # Insert after first section
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('## ') and insert_pos == 0:
                        insert_pos = i + 1
                        # Find end of section
                        for j in range(i+1, len(lines)):
                            if lines[j].startswith('## '):
                                insert_pos = j
                                break
                            insert_pos = j + 1
                        break
                lines.insert(insert_pos, '\n' + memox_section)
                new_content = '\n'.join(lines)
            else:
                # Insert at beginning after title
                new_content = content.replace(
                    "# MEMORY.md - 长期记忆\n\n",
                    "# MEMORY.md - 长期记忆\n\n" + memox_section + "\n"
                )
            action = "Inserted"
        
        # Write back
        with open(self.memory_md, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"{action} MemoX section in MEMORY.md")
        return True


def main():
    injector = MemoXInjector()
    success = injector.inject_to_memory()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
