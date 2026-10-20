---
title: "The loop"
owner: "Build committee"
last_reviewed: 2026-10-20
---

# The loop: from an issue to a pull request with an agent

Every LITSA issue is written so it can serve as an agent's instructions: **Background**, **What to do**, **Done when**, **Start here**. The loop:

## 1. Read the issue yourself first

Make sure you understand what done looks like. If something's unclear, ask on the issue before starting. An agent will cheerfully build the wrong thing.

## 2. Open a Codespace and a branch

```
git checkout -b 12-week-view
```

Name the branch with the issue number.

## 3. Give the agent the issue

Paste the issue into the agent and add:

```
Work on this issue in this repo. Read AGENTS.md and the files under "Start here" first.
Before changing anything, tell me your plan in a few steps and wait for me to agree.
Then make the change, add or update tests, and run the checks from AGENTS.md.
Tell me exactly what the checks printed. Don't claim something works unless a check shows it.
```

Asking for a plan first catches misunderstandings while they're cheap.

## 4. Check the plan

Does it match "Done when"? Is it touching files the issue didn't mention? Push back now.

## 5. Let it work, then review the diff

Read every changed line in the Source Control panel. [Reviewing what an agent wrote](reviewing-ai-work.md) has a checklist.

## 6. Run the checks yourself

Run the commands from the repo's `AGENTS.md` in the terminal. Look at the page or the output if anything visible changed.

## 7. Open the pull request

Fill in the template. Say which AI tools helped. Go through the "Done when" list and tick what's actually done; say plainly what isn't.

## When not to use an agent

- When the task is writing down something only a person can know: a guide's steps on the real system, what a professor said, whether a summary is fair to a bill.
- When you're trying to learn the thing itself. Do it by hand once.
- When you can't check the answer. If you can't tell whether it's right, don't merge it.
