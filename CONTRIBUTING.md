# Contributing to the handbook

The org-wide guide is at [suffolklitsa/.github](https://github.com/suffolklitsa/.github/blob/main/CONTRIBUTING.md).

## Writing pages

- Every page starts with front matter: `title`, `owner` (a committee, or your name), `last_reviewed` (YYYY-MM-DD).
- Write for someone who has never used GitHub. One action per step; say what they should see when it worked.
- Use the screen's exact words for buttons and menus. Check them yourself; they change.
- Link to good outside material instead of rewriting it, and say why it's worth the reader's time.
- Plain words, short sentences, no hype.
- Anything about a tool's price or plan is likely to go stale. Say "check the tool's site" rather than quoting a number.

## Checks

```
python3 scripts/check_pages.py
python3 -m unittest discover -s tests
```
