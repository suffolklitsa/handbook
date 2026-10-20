---
title: "What coding agents are"
owner: "Build committee"
last_reviewed: 2026-10-20
---

# What coding agents are, and which ones you can use

A coding agent is an AI tool that can read a repo, propose changes across several files, run commands like the tests, and explain what it did. You describe the task; it does a draft; you check it. It's closer to working with a fast, eager junior colleague than to autocomplete.

## The ones members use

| Tool | Where it runs | How to get it |
|---|---|---|
| **GitHub Copilot** | In Codespaces and VS Code, plus an agent mode that works across files and can open pull requests | Included with the GitHub Student Developer Pack |
| **Claude Code** | In a terminal, including a Codespace's | Needs a Claude subscription or API account |
| **Codex** | In a terminal, an editor, or on the web | Comes with ChatGPT plans |

Plans and prices change, so check each tool's site before paying for anything. Copilot through the student pack costs nothing, so start there.

## They read the repo's rules

Every LITSA repo has an `AGENTS.md` file at the top level with that repo's commands and rules (Claude Code reads it through `CLAUDE.md`). Agents pick it up when they start. You should read it too: it's the shortest summary of how each repo works.

## What they're good and bad at

**Good at:** following a clear spec, writing tests, explaining unfamiliar code, repetitive edits, first drafts of docs.

**Bad at:** knowing what Suffolk actually requires, knowing whether a case says what they claim, noticing that the task itself is wrong, and admitting when they're unsure. They will invent a citation, a button name or an office's email if you let them.

That's why the rules put a person in charge of every fact. See [the rules](rules.md).

## Course policies

Some courses restrict AI use. Building LITSA tools isn't coursework, but never use LITSA work, or an agent, for anything graded where your course's policy says no.
