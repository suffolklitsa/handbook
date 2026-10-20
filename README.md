# handbook

How LITSA's Build work happens, written for law students: getting set up on GitHub, working in the browser, your first pull request, working with AI coding agents, and the background each project relies on. **Start with [pages/index.md](pages/index.md).**

**Status:** first edition. The start-here path and the agent pages are written; legal tech primers are next (see the issues). The handbook will also appear at suffolklitsa.org/handbook.

## Who it's for

Any LITSA member, with or without coding experience. If you've never used GitHub, follow the start-here pages in order; you'll end with your name on the contributors page. If you have, skip to [working with AI agents](pages/agents/the-loop.md) and the [rules](pages/agents/rules.md).

## What's in it

| Section | Pages |
|---|---|
| Start here | GitHub account and joining the org, Codespaces, your first pull request |
| Working with AI agents | What coding agents are, the issue-to-PR loop, reviewing an agent's work, the rules |
| Background | How Build is organized, legal tech primers, glossary, outside resources |

## Why a repo and not a wiki

GitHub's built-in wikis skip pull requests and checks. The handbook gets the same review as everything else: anyone can propose a change, someone reviews it, and `scripts/check_pages.py` catches broken links and missing details.

## Branches

Pull requests go to `staging`, the default branch. `main` is the released version: maintainers promote `staging` to `main` with a pull request when a batch of changes is ready. Both branches are protected and need a review and passing checks.

## Contributing

The handbook gets better each time someone new uses it. If a step confused you, fix it in a pull request, or open an issue saying where you got stuck. Every page has an `owner` and `last_reviewed` date in its front matter; update the date when you've checked a page is still right. See [CONTRIBUTING.md](CONTRIBUTING.md).

```
python3 scripts/check_pages.py
python3 -m unittest discover -s tests
```

## License

The handbook's pages are CC BY 4.0 ([LICENSE-docs.md](LICENSE-docs.md)); other student groups are welcome to adapt them with credit. Scripts are MIT ([LICENSE](LICENSE)).
