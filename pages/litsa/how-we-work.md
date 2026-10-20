---
title: "How LITSA's Build work is organized"
owner: "Build committee"
last_reviewed: 2026-10-20
---

# How LITSA's Build work is organized

## Committees

LITSA has six committees: **Build**, **Events**, **Research & Writing**, **Skills**, **Network** and **Comms**. Each has a topic in the LITSA GroupMe. Build owns the code; Research & Writing owns accuracy; Skills runs workshops and owns the how-to guides; the others own their parts of each project. Anyone can work on any issue.

## Repos

The [org profile](https://github.com/suffolklitsa) lists every repo with a one-line description. Each repo's README explains what it is and how to run it, and its `AGENTS.md` lists its rules.

## Issues and labels

| Label | Means |
|---|---|
| `good first issue` | Small and well-defined; a good first real task |
| `no code needed` | Writing, research, review or design; no programming |
| `needs R&W review` | A second Research & Writing member checks it against the source before it merges |
| `committee: ...` | Which committee owns it |
| `size: small / medium / large` | About an afternoon / a few sessions / several sessions |

Every issue has **Background**, **What to do**, **Done when**, **Start here** and **Size**. Comment to claim one so it can be assigned to you.

## The board

[LITSA Build](https://github.com/orgs/suffolklitsa/projects/1) shows every issue across every repo, by status. Org members can see it.

## Reviews

`main` is protected in every public repo: changes reach it only through a pull request with one approving review and passing checks. Every pull request is reviewed by someone else before it merges. Reviewers check the "Done when" list, the checks, and the rules. Be kind and specific; the point is a better change.
