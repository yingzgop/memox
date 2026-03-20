#!/usr/bin/env python3
"""
MemoX Update Script
Updates MemoX (structured memory) YAML files from daily markdown memories
"""

import re
import yaml
from datetime import datetime
from pathlib import Path

class MemoXUpdater:
    def __init__(self, base_path: Path = None):
        # Load configuration
        self.config = self._load_config()
        
        # Use configured path or default
        if base_path is None:
            base_path_str = self.config.get("base_path", "~/.openclaw/workspace/memory")
            self.base_path = Path(base_path_str).expanduser()
        else:
            self.base_path = base_path
            
        self.memox_path = self.base_path / "MemoX"
        
    def _load_config(self) -> dict:
        """Load configuration from memox.yaml"""
        # Try multiple config locations
        config_paths = [
            Path(__file__).parent.parent / "memox.yaml",  # Project directory
            Path.home() / ".openclaw/workspace/memory/MemoX/memox.yaml",  # User directory
            Path("memox.yaml"),  # Current directory
        ]
        
        for config_path in config_paths:
            if config_path.exists():
                try:
                    with open(config_path, 'r', encoding='utf-8') as f:
                        return yaml.safe_load(f) or {}
                except Exception as e:
                    print(f"Warning: Could not load config from {config_path}: {e}")
                    
        return {}  # Return empty config if none found
        
    def load_yaml(self, filename: str) -> dict:
        """Load a YAML file or return empty structure"""
        filepath = self.memox_path / filename
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        return {}
    
    def save_yaml(self, filename: str, data: dict):
        """Save data to YAML file"""
        filepath = self.memox_path / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    def generate_id(self, prefix: str, date_str: str, seq: int) -> str:
        """Generate unique ID like D20260320001"""
        date_num = date_str.replace("-", "")
        return f"{prefix}{date_num}{seq:03d}"
    
    def update_index(self):
        """Update index.yaml with statistics"""
        decisions = self.load_yaml("decisions.yaml").get("decisions", [])
        errors = self.load_yaml("errors.yaml").get("errors", [])
        learnings = self.load_yaml("learnings.yaml").get("learnings", [])
        
        # Build tag cloud
        tags = {}
        by_topic = {}
        by_date = {}
        
        for item in decisions + errors + learnings:
            date = item.get("date", "unknown")
            item_tags = item.get("tags", [])
            topic = item.get("topic", item.get("error", item.get("learning", "unknown")))[:30]
            
            # Count tags
            for tag in item_tags:
                tags[tag] = tags.get(tag, 0) + 1
            
            # Group by date
            if date not in by_date:
                by_date[date] = {"decisions": [], "errors": [], "learnings": []}
            
            item_type = "decisions" if item in decisions else ("errors" if item in errors else "learnings")
            by_date[date][item_type].append(item.get("id", "unknown"))
        
        index = {
            "metadata": {
                "schema_version": "1.0",
                "last_update": datetime.now().strftime("%Y-%m-%d"),
                "total_entries": {
                    "decisions": len(decisions),
                    "errors": len(errors),
                    "learnings": len(learnings)
                }
            },
            "tags": tags,
            "by_topic": by_topic,
            "by_date": by_date
        }
        
        self.save_yaml("index.yaml", index)
        print(f"Index updated: {len(decisions)} decisions, {len(errors)} errors, {len(learnings)} learnings")
    
    def add_decision(self, date: str, topic: str, decision: str, reasoning: str,
                     alternatives: list = None, status: str = "implemented",
                     tags: list = None, source: str = "", key_quotes: list = None):
        """Add a new decision"""
        data = self.load_yaml("decisions.yaml")
        decisions = data.get("decisions", [])
        
        # Generate ID
        seq = len([d for d in decisions if d.get("date") == date]) + 1
        decision_id = self.generate_id("D", date, seq)
        
        new_decision = {
            "id": decision_id,
            "date": date,
            "topic": topic,
            "decision": decision,
            "reasoning": reasoning,
            "status": status,
            "tags": tags or []
        }
        
        if alternatives:
            new_decision["alternatives"] = alternatives
        if source:
            new_decision["source"] = source
        if key_quotes:
            new_decision["key_quotes"] = key_quotes
            
        decisions.append(new_decision)
        data["decisions"] = decisions
        self.save_yaml("decisions.yaml", data)
        
        # Update context
        self._update_recent("recent_decisions", decision_id)
        
        return decision_id
    
    def add_error(self, date: str, error: str, symptom: str, solution: str,
                  status: str = "open", workaround: bool = False,
                  tags: list = None, source: str = ""):
        """Add a new error record"""
        data = self.load_yaml("errors.yaml")
        errors = data.get("errors", [])
        
        seq = len([e for e in errors if e.get("date") == date]) + 1
        error_id = self.generate_id("E", date, seq)
        
        new_error = {
            "id": error_id,
            "date": date,
            "error": error,
            "symptom": symptom,
            "solution": solution,
            "status": status,
            "workaround": workaround,
            "tags": tags or []
        }
        
        if source:
            new_error["source"] = source
            
        errors.append(new_error)
        data["errors"] = errors
        self.save_yaml("errors.yaml", data)
        
        self._update_recent("recent_errors", error_id)
        
        return error_id
    
    def add_learning(self, date: str, category: str, learning: str,
                     source: str = "", importance: str = "medium",
                     tags: list = None, related_decisions: list = None):
        """Add a new learning"""
        data = self.load_yaml("learnings.yaml")
        learnings = data.get("learnings", [])
        
        seq = len([l for l in learnings if l.get("date") == date]) + 1
        learning_id = self.generate_id("L", date, seq)
        
        new_learning = {
            "id": learning_id,
            "date": date,
            "category": category,
            "learning": learning,
            "source": source,
            "importance": importance,
            "tags": tags or []
        }
        
        if related_decisions:
            new_learning["related_decisions"] = related_decisions
            
        learnings.append(new_learning)
        data["learnings"] = learnings
        self.save_yaml("learnings.yaml", data)
        
        self._update_recent("recent_learnings", learning_id)
        
        return learning_id
    
    def _update_recent(self, field: str, item_id: str, max_items: int = 3):
        """Update recent items in context.yaml"""
        context = self.load_yaml("context.yaml")
        recent = context.get(field, [])
        
        # Add to front, remove duplicates, keep max
        recent = [item_id] + [r for r in recent if r != item_id]
        recent = recent[:max_items]
        
        context[field] = recent
        self.save_yaml("context.yaml", context)


def main():
    """Main entry point"""
    import sys
    
    # Initialize updater (will auto-load config)
    updater = MemoXUpdater()
    
    # Print config info
    config_path = updater.config.get("_config_path", "default settings")
    
    if len(sys.argv) < 2:
        print("MemoX - Structured Memory System")
        print(f"Base path: {updater.base_path}")
        print(f"Config: {config_path}")
        print("")
        print("Usage: python memox.py <command> [args...]")
        print("")
        print("Commands:")
        print("  update-index              Update index.yaml statistics")
        print("  add-decision <date> <topic> <decision> <reasoning>")
        print("  add-error <date> <error> <symptom> <solution>")
        print("  add-learning <date> <category> <learning>")
        print("")
        print("Examples:")
        print('  python memox.py add-decision 2026-03-20 "Topic" "Decision" "Reason"')
        sys.exit(1)
        print("Commands:")
        print("  update-index              Update index.yaml statistics")
        print("  add-decision <date> <topic> <decision> <reasoning>")
        print("  add-error <date> <error> <symptom> <solution>")
        print("  add-learning <date> <category> <learning>")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "update-index":
        updater.update_index()
    elif command == "add-decision" and len(sys.argv) >= 6:
        date, topic, decision, reasoning = sys.argv[2:6]
        decision_id = updater.add_decision(date, topic, decision, reasoning)
        print(f"Added decision: {decision_id}")
        updater.update_index()
    elif command == "add-error" and len(sys.argv) >= 6:
        date, error, symptom, solution = sys.argv[2:6]
        error_id = updater.add_error(date, error, symptom, solution)
        print(f"Added error: {error_id}")
        updater.update_index()
    elif command == "add-learning" and len(sys.argv) >= 5:
        date, category, learning = sys.argv[2:5]
        learning_id = updater.add_learning(date, category, learning)
        print(f"Added learning: {learning_id}")
        updater.update_index()
    else:
        print("Invalid command or missing arguments")
        sys.exit(1)


if __name__ == "__main__":
    main()
