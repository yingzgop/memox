#!/usr/bin/env python3
"""
MemoX Record Script - Quick entry point for recording memories
Called by the memox skill or used directly
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path to import memox module
sys.path.insert(0, str(Path.home() / ".openclaw/workspace/memory/MemoX/src"))

try:
    from memox import MemoXUpdater
except ImportError:
    print("Error: Could not import MemoX module")
    print("Make sure memox.py is in ~/.openclaw/workspace/memory/MemoX/src/")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Record memories to MemoX")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Decision subcommand
    decision_parser = subparsers.add_parser("decision", help="Record a decision")
    decision_parser.add_argument("--date", required=True, help="Date (YYYY-MM-DD)")
    decision_parser.add_argument("--topic", required=True, help="Decision topic")
    decision_parser.add_argument("--decision", required=True, help="The decision made")
    decision_parser.add_argument("--reasoning", help="Reasoning behind the decision")
    decision_parser.add_argument("--alternatives", help="Comma-separated alternatives considered")
    decision_parser.add_argument("--status", default="implemented", help="Status: implemented/pending/rejected")
    decision_parser.add_argument("--tags", help="Comma-separated tags")
    
    # Error subcommand
    error_parser = subparsers.add_parser("error", help="Record an error")
    error_parser.add_argument("--date", required=True, help="Date (YYYY-MM-DD)")
    error_parser.add_argument("--error", required=True, help="Error description")
    error_parser.add_argument("--symptom", required=True, help="Error symptoms")
    error_parser.add_argument("--solution", required=True, help="Solution applied")
    error_parser.add_argument("--status", default="resolved", help="Status: open/workaround/resolved")
    error_parser.add_argument("--workaround", action="store_true", help="Is this a workaround?")
    error_parser.add_argument("--tags", help="Comma-separated tags")
    
    # Learning subcommand
    learning_parser = subparsers.add_parser("learning", help="Record a learning")
    learning_parser.add_argument("--date", required=True, help="Date (YYYY-MM-DD)")
    learning_parser.add_argument("--category", required=True, help="Learning category")
    learning_parser.add_argument("--learning", required=True, help="What was learned")
    learning_parser.add_argument("--source", help="Source of learning")
    learning_parser.add_argument("--importance", default="medium", help="Importance: high/medium/low")
    learning_parser.add_argument("--tags", help="Comma-separated tags")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Initialize updater
    updater = MemoXUpdater()
    
    # Parse tags
    tags = [t.strip() for t in args.tags.split(",")] if args.tags else []
    
    if args.command == "decision":
        alternatives = [a.strip() for a in args.alternatives.split(",")] if args.alternatives else None
        decision_id = updater.add_decision(
            date=args.date,
            topic=args.topic,
            decision=args.decision,
            reasoning=args.reasoning or "",
            alternatives=alternatives,
            status=args.status,
            tags=tags
        )
        print(f"[OK] Recorded decision: {decision_id}")
        
    elif args.command == "error":
        error_id = updater.add_error(
            date=args.date,
            error=args.error,
            symptom=args.symptom,
            solution=args.solution,
            status=args.status,
            workaround=args.workaround,
            tags=tags
        )
        print(f"[OK] Recorded error: {error_id}")
        
    elif args.command == "learning":
        learning_id = updater.add_learning(
            date=args.date,
            category=args.category,
            learning=args.learning,
            source=args.source or "",
            importance=args.importance,
            tags=tags
        )
        print(f"[OK] Recorded learning: {learning_id}")
    
    # Update index
    updater.update_index()
    print("[OK] Index updated")


if __name__ == "__main__":
    main()
