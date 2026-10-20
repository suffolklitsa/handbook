---
title: "Your first pull request"
owner: "Build committee"
last_reviewed: 2026-10-20
---

# Your first pull request

A pull request ("PR") is how a change gets into a LITSA repo: you make the change on your own branch, open a pull request, someone reviews it, and it's merged. This walkthrough uses a change that can't break anything: adding your name to the [contributors page](../contributors.md).

**Time:** about 20 minutes.

## 1. Open a Codespace on this repo

Go to github.com/suffolklitsa/handbook → **Code** → **Codespaces** → **Create codespace on staging**.

## 2. Make a branch

In the terminal at the bottom:

```
git checkout -b add-your-name
```

A branch is your own copy of the files to change without affecting anyone else.

## 3. Make the change

Open `pages/contributors.md`, and add a line in alphabetical order by first name:

```
- Jane D. (@janedoe), Research & Writing
```

Use only what you're comfortable having public. A first name and last initial is fine.

## 4. Check it

```
python3 scripts/check_pages.py
```

It should end with `ok`.

## 5. Commit and push

```
git add pages/contributors.md
git commit -m "Add Jane D. to contributors"
git push -u origin add-your-name
```

A commit is a saved snapshot of your change with a short message saying what it does. If you aren't an org member yet, the push will offer to create a fork (your own copy of the repo); accept it.

## 6. Open the pull request

GitHub shows a banner on the repo page: **Compare & pull request**. Click it, check that it says `base: staging`, fill in the template (one sentence is enough), and click **Create pull request**.

## 7. After review

A reviewer may ask for a change. Make it in the Codespace, commit and push again; the pull request updates by itself. Once it's merged, you're on the page.

## What's next

Pick a real issue. Every repo has issues labeled `good first issue` and `no code needed`, and each says what done looks like and where to start. Comment "I'll take this" so it can be assigned to you. Then read [the loop](../agents/the-loop.md) to see how to work on it with an AI agent.
