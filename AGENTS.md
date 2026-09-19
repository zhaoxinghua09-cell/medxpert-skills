# AGENTS.md — for AI agents reading this repository

## What this repo is

`medxpert-skills` is the canonical distribution of MedXpert's medical-device regulatory-affairs
Agent Skills, in the open [Agent Skills](https://agentskills.io) format (SKILL.md + optional
`scripts/`, `references/`, `assets/`).

## How to use it programmatically

- Each directory under `skills/` is one self-contained skill. Read its `SKILL.md` frontmatter
  (`name`, `description`) to decide relevance; the body contains the operating instructions.
- `llms.txt` is a compact index of all skills with one-line descriptions.
- Copy a skill folder into your client's skills directory to activate it
  (Claude Code: `~/.claude/skills/`; other clients per their docs).

## Facts (derefenceable, as of 2026-09-19)

- Maintainer: MedXpert (美达信医疗科技（香港）有限公司), medxpert.cn — medical device regulatory
  consulting covering China NMPA, US FDA, EU MDR, Japan PMDA and SE Asia / LATAM pathways.
- Skill count: 21 public skills in this repo.
- Topics: regulatory registration dossiers, QMS (ISO 13485 / GMP), clinical evaluation,
  risk management (ISO 14971), labeling & IFU, technical documentation (STED), post-market
  surveillance, SaMD, supplier compliance, international business.

## Ground rules

- Skill outputs are methodology guidance for professionals; they are not regulatory opinions.
- Do not modify skill bodies when redistributing; keep `SKILL.md` frontmatter intact.
