# AGENTS.md

Instructions for AI coding agents working in this repo, and for the people using them. Read README.md and CONTRIBUTING.md too.

## What this repo is

LITSA's handbook for members: Markdown pages in `pages/`, checked by `scripts/check_pages.py`.

## Commands

```
python3 scripts/check_pages.py
python3 -m unittest discover -s tests
```

## Rules for this repo

- **Readers are new.** Write for someone who has never used GitHub. Don't skip steps or assume terms; link the glossary.
- **Only describe what's real.** Button names, menus and steps must match what GitHub and the tools show today. If you can't confirm a step, say so in the pull request instead of guessing.
- **No prices or plan details** beyond "check the tool's site."
- **Keep front matter** on every page and update `last_reviewed` only when a person has checked the page.
- **`pages/contributors.md`** is for people adding themselves; don't add anyone else.

## Rules for every LITSA repo

- **No secrets.** Never write API keys, tokens or passwords into a file, a commit, an issue or a test.
- **No personal data** beyond what a person chooses to add about themselves.
- **No invented facts or law.** Link a source or say you couldn't find one.
- **Small changes,** one issue per pull request.
- **Run the checks** and report what they printed.
- **Plain writing.**
- **Disclose AI use** in the pull request description.
