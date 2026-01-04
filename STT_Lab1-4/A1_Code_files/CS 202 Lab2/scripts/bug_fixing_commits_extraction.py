# scripts/identify_bugfix_commits.py
import re
import csv
from pathlib import Path
from pydriller import Repository

# Paths
WORKSPACE_ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = WORKSPACE_ROOT / "data" / "bugfix_commits.csv"

# Target remote repository (PyDriller will handle access internally)
REPO_URL = "https://github.com/agno-agi/agno.git"

# Bug-fix keyword list (from lecture + extended)
KEYWORDS = [
    "fix", "fixes", "fixed", "bug", "bugfix", "patch", "resolve", "resolves", "resolved",
    "close", "closes", "closed", "issue", "issues", "regression", "fallback", "assert",
    "assertion", "fail", "fails", "failed", "failure", "crash", "crashes",
    "error", "errors", "exception", "hang", "timeout", "leak", "memory leak",
    "overflow", "underflow", "incorrect", "wrong", "broken", "segfault",
    "npe", "nullpointer", "panic", "deadlock", "race", "workaround", "stop",
    "avoid", "fixme", "hotfix"
]
pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in KEYWORDS) + r')\b', re.IGNORECASE)

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

def main():
    header = ["Hash", "Message", "Hashes of parents", "Is a merge commit?", "List of modified files"]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)

        for commit in Repository(REPO_URL).traverse_commits():
            msg = commit.msg or ""

            # Heuristic: check if commit message contains bug-fix keywords
            if not pattern.search(msg):
                continue

            parents = ";".join(commit.parents) if commit.parents else ""
            is_merge = "Yes" if len(commit.parents) > 1 else "No"
            modified_files = ";".join([m.new_path or m.old_path or "" for m in commit.modified_files])

            writer.writerow([
                commit.hash,
                msg.replace("\n", " ").strip(),
                parents,
                is_merge,
                modified_files
            ])

    print(f"✅ Bug-fix commit metadata written to {OUT_CSV}")

if __name__ == "__main__":
    main()
