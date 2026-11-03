"""Rewrite the README's "Recently shipped" list from public merged pull requests.

Needs the GitHub CLI, authenticated (GH_TOKEN in CI).
"""

import json
import re
import subprocess
import sys
from pathlib import Path

LOGIN = "giaphutran12"
LIMIT = 6
README = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- recently_shipped starts -->"
END = "<!-- recently_shipped ends -->"


def merged_pull_requests():
    query = f"author:{LOGIN} is:pr is:merged is:public -repo:{LOGIN}/{LOGIN}"
    result = subprocess.run(
        ["gh", "api", "-X", "GET", "search/issues",
         "-f", f"q={query}", "-f", "sort=updated", "-f", "per_page=30"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"[recently-shipped] search failed: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    items = json.loads(result.stdout)["items"]
    # Search cannot sort by merge time; a merged pull request closes when it merges.
    return sorted(items, key=lambda item: item["closed_at"], reverse=True)


def repository_of(item):
    return item["repository_url"].removeprefix("https://api.github.com/repos/")


def latest_per_repository(items):
    seen = set()
    latest = []
    for item in items:
        if repository_of(item) not in seen:
            seen.add(repository_of(item))
            latest.append(item)
    return latest


def as_line(item):
    repository = repository_of(item)
    title = item["title"].replace("[", "(").replace("]", ")")
    return f"- [{title}]({item['html_url']}) in `{repository}`, {item['closed_at'][:10]}"


def main():
    items = merged_pull_requests()
    print(f"[recently-shipped] search returned {len(items)} merged pull requests")
    if not items:
        print("[recently-shipped] nothing found; leaving the README as it is")
        return
    chosen = latest_per_repository(items)[:LIMIT]
    lines = "\n".join(as_line(item) for item in chosen)
    readme = README.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        print("[recently-shipped] README has no recently_shipped markers", file=sys.stderr)
        sys.exit(1)
    updated = pattern.sub(lambda _: f"{START}\n{lines}\n{END}", readme)
    if updated == readme:
        print("[recently-shipped] list unchanged")
        return
    README.write_text(updated)
    print(f"[recently-shipped] wrote {len(chosen)} pull requests from {len(chosen)} repositories to the README")


if __name__ == "__main__":
    main()
