# AGENTS.md — for AI agents reading this repository

## What this repo is

The canonical distribution of Agent Skills in the open [Agent Skills](https://agentskills.io) format
(SKILL.md + optional `scripts/`, `references/`, `assets/`), split by owning entity:

- **SynomosAI** — general AI capabilities (local LLM library setup, L1 batch study, knowledge-base
  distribution, brand assets, document toolchain, VI extension, skill panorama)
- **MedXpert** (美达信医疗科技（香港）有限公司) — medical-device regulatory affairs covering
  China NMPA, US FDA, EU MDR, Japan PMDA and SE Asia / LATAM pathways

## How to use it programmatically

- Each directory under `skills/` is one self-contained skill. Read its `SKILL.md` frontmatter
  (`name`, `description`) to decide relevance; the body contains the operating instructions.
- `llms.txt` is a compact index of all skills with one-line descriptions.
- Copy a skill folder into your client's skills directory to activate it
  (Claude Code: `~/.claude/skills/`; other clients per their docs).

## Facts (dereferenceable, as of 2026-09-19)

- Skill count: 21 public skills (7 SynomosAI + 14 MedXpert).
- MedXpert topics: regulatory registration dossiers, QMS (ISO 13485 / GMP), clinical evaluation,
  risk management (ISO 14971), labeling & IFU, technical documentation (STED), post-market
  surveillance, SaMD, supplier compliance, standards navigation, international business.
- SynomosAI topics: local LLM deployment & knowledge libraries, batch document study pipelines,
  knowledge distribution, brand/VI asset production, document security toolchain.

## Ground rules

- Skill outputs are methodology guidance for professionals; they are not regulatory or business opinions.
- Do not modify skill bodies when redistributing; keep `SKILL.md` frontmatter intact.
