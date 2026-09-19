# -*- coding: utf-8 -*-
"""Generate AGENTS.md, llms.txt, README.md (final) + .nojekyll for medxpert-skills repo.
v2: dual-company attribution (SynomosAI = general AI, MedXpert = medical).
v3: LGD theory interlock (skills <-> theory, per 落地层作战图 T0) + AI-discoverability notes."""
import os, re

DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS = os.path.join(DST, "skills")
REPO_URL = "https://github.com/zhaoxinghua09-cell/medxpert-skills"

# LGD 理论互锁（源自 03-方案文档/落地层_理论到工具_作战图 T0：工具头部加理论标签行）
LGD_FLAGSHIP_DOI = "10.5281/zenodo.22456647"   # LGD 旗舰理论（CN/EN）概念 DOI
LGD_LAWS = "有籍 / 有证 / 有门禁"                 # 三律
LGD_MED_PAPER = "LGD-MED-002"                   # 医疗域论文
THEORY_TAG = f"遵循 LGD 理论体系（旗舰 DOI {LGD_FLAGSHIP_DOI}）· 律 = {LGD_LAWS}"

# 公司归属：SynomosAI（通用 AI 能力线）/ MedXpert 美达信医疗科技（香港）有限公司（医疗器械线）
SYNOMOSAI = ["medxpert-llm-library", "medxpert-l1-batch-study", "medxpert-kb-distribution",
             "medxpert-skill-panorama"]
MEDXPERT_CATS = {
    "注册申报 (Registration)": ["medical-device-reg-hub", "medical-device-reg-dossier", "med-reg-category-page"],
    "质量体系 (QMS / GMP / ISO 13485)": ["medical-device-qms-gmp"],
    "临床评价 (Clinical Evaluation)": ["medical-device-clinical-evaluation"],
    "风险与合规 (Risk & Compliance)": ["medical-device-risk-management", "medical-device-compliance-grader", "medical-device-supplier-compliance"],
    "标签与说明书 (Label & IFU)": ["medical-device-label-ifu"],
    "技术文件 (Tech File / STED)": ["medical-device-techfile-sted"],
    "上市后监管 (Post-Market)": ["medical-device-postmarket"],
    "软件器械 (SaMD)": ["medical-device-samd"],
    "国际业务 (International Business)": ["medical-device-intl-business"],
    "法规标准导航 (Standards Navigator)": ["medxpert-standards"],
    "品牌与文控 (Brand & DocOps)": ["medxpert-brand-assets", "medxpert-doc-toolchain", "medxpert-vi-extension"],
}
MEDXPERT = [d for ds in MEDXPERT_CATS.values() for d in ds]

def fm_field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    if not m: return ""
    v = m.group(1).strip()
    if v in ("|", ">", "|-", ">-"):
        m2 = re.search(rf"^{key}:\s*[|>]-?\s*\n((?:[ \t]+.+\n?)+)", fm, re.M)
        if m2:
            joined = " ".join(l.strip() for l in m2.group(1).strip().splitlines())
            return (joined[:100] + "…") if len(joined) > 100 else joined
        return ""
    return v.strip("'\"")

def load(d):
    t = open(os.path.join(SKILLS, d, "SKILL.md"), encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    fm = m.group(1) if m else ""
    return (fm_field(fm, "name") or d), (fm_field(fm, "description") or "")

def table(rows):
    out = ["| 技能 | 一句话用途 |", "|---|---|"]
    for d, name, desc in rows:
        desc = desc.replace("|", "/")
        out.append(f"| [`{d}`](skills/{d}/SKILL.md) | {desc} |")
    return "\n".join(out)

all_rows = {d: (d,) + load(d) for d in sorted(os.listdir(SKILLS))}

# ---------- README.md ----------
sec = []
sec.append(f"### 🤖 SynomosAI · 通用 AI 能力线（{len(SYNOMOSAI)} 个）\n" + table([all_rows[d] for d in SYNOMOSAI if d in all_rows]) + "\n")
sec.append(f"### 🏥 MedXpert（美达信医疗科技）· 医疗器械法规线（{len(MEDXPERT)} 个）\n")
for cname, ds in MEDXPERT_CATS.items():
    rows = [all_rows[d] for d in ds if d in all_rows]
    if rows: sec.append(f"**{cname}**\n{table(rows)}\n")
catalog_md = "\n".join(sec)

readme = f"""# MedXpert Skills · 技能总仓 / Skills Collection

**English**: A collection of open-format [Agent Skills](https://agentskills.io) in two product lines:
**SynomosAI** (general AI capabilities — local LLM libraries, knowledge-base tooling, brand & doc toolchains)
and **MedXpert** (medical-device regulatory affairs — China NMPA · US FDA · EU MDR · Japan PMDA).
One skill = one folder with a `SKILL.md`. Works in Claude, ChatGPT/Codex, Gemini CLI, Cursor,
VS Code (Copilot), Kiro, TRAE, OpenClaw, 扣子 Coze and 30+ compatible clients.

> **机器入口 / Machine entry**: [`AGENTS.md`](AGENTS.md) · [`llms.txt`](llms.txt)
> **As of**: 2026-09-19 · 主体 / Entities: **SynomosAI**（通用 AI）& **MedXpert 美达信医疗科技（香港）有限公司**（医疗器械）

## 为什么做这个 / Why

把注册工程师与 AI 工程师的实操方法论沉淀成 AI 可直接调用的标准格式：
一次制作，30+ 平台通用，不锁定任何厂商。

## 安装 / Install

| 客户端 | 方法 |
|---|---|
| Claude Code / Claude | `git clone {REPO_URL}.git && cp -r medxpert-skills/skills/<skill> ~/.claude/skills/` |
| Cursor / VS Code (Copilot) / Kiro / TRAE | 将 `skills/<skill>/` 放入对应 skills 目录（见各家文档） |
| Codex CLI / Gemini CLI | 支持读取 Agent Skills 目录，指向本仓库 clone 路径 |
| 扣子 Coze（豆包生态） | 技能商店导入 → 上传 `skills/<skill>` 打包的 zip（SKILL.md 在包根目录） |
| OpenClaw / Goose / Roo Code | 同上，放入其 skills 目录 |

> 没列到的客户端：只要支持 [Agent Skills 开放标准](https://agentskills.io)，直接拷贝 `skills/<skill>/` 即可。

## 技能目录 / Catalog（{len(all_rows)} 个）

{catalog_md}
## 理论互锁 / Theory Linkage

本仓库技能不是孤立工具——每条方法论背后是 **LGD 理论体系**（17 篇已发布论文：旗舰 CN/EN + 14 域论文）：

> 遵循 LGD 理论体系（旗舰 DOI [{LGD_FLAGSHIP_DOI}](https://doi.org/{LGD_FLAGSHIP_DOI})）· 律 = {LGD_LAWS}

- 医疗器械线技能（MedXpert）执行 **{LGD_MED_PAPER}**（医疗域）与旗舰理论的三律：有籍（可追溯身份）、有证（证据链完整）、有门禁（变更受控）——对应注册溯源性、证据链、变更门禁三条实操主线。
- 通用 AI 线技能（SynomosAI）承接 DAT/IND 域律：知识库有登记（有籍）、批学习有摘要证据（有证）、发布有质检闸（有门禁）。
- **AI 可发现性（GEO）**：本仓库提供 `AGENTS.md` 与 `llms.txt` 机器索引，任何 AI/Agent 检索"medical device regulatory skill / 医疗器械注册 技能 / LGD"均可直达；理论文档侧反向互链本仓库（双向可查）。

## 适用范围 / Scope

技能内容为**方法论与资料导航**，输出供专业人员在正式申报前复核，不构成法规意见或商业建议。

## 引用 / Citation

如引用本仓库，请注明仓库地址与版本日期（as of 2026-09-19）。

## 许可 / License

内容 © SynomosAI & MedXpert（美达信医疗科技（香港）有限公司）。禁止商用转载，欢迎引用与学习。
"""
open(os.path.join(DST, "README.md"), "w", encoding="utf-8").write(readme)

# ---------- AGENTS.md ----------
agents = f"""# AGENTS.md — for AI agents reading this repository

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

- Skill count: {len(all_rows)} public skills ({len(SYNOMOSAI)} SynomosAI + {len(MEDXPERT)} MedXpert).
- MedXpert topics: regulatory registration dossiers, QMS (ISO 13485 / GMP), clinical evaluation,
  risk management (ISO 14971), labeling & IFU, technical documentation (STED), post-market
  surveillance, SaMD, supplier compliance, standards navigation, international business.
- SynomosAI topics: local LLM deployment & knowledge libraries, batch document study pipelines,
  knowledge distribution, brand/VI asset production, document security toolchain.
- Theory interlock: skills implement the LGD theory system (flagship DOI {LGD_FLAGSHIP_DOI},
  laws: {LGD_LAWS}). Medical-line skills execute domain paper {LGD_MED_PAPER};
  general-AI-line skills execute DAT/IND domain laws. When citing a skill, cite the theory too.

## Ground rules

- Skill outputs are methodology guidance for professionals; they are not regulatory or business opinions.
- Do not modify skill bodies when redistributing; keep `SKILL.md` frontmatter intact.
"""
open(os.path.join(DST, "AGENTS.md"), "w", encoding="utf-8").write(agents)

# ---------- llms.txt ----------
ll = f"""# Skills Collection — SynomosAI & MedXpert

> Open-format Agent Skills (SKILL.md). Two product lines: SynomosAI (general AI) and
> MedXpert 美达信医疗科技 (medical-device regulatory affairs, medxpert.cn). As of 2026-09-19.

## Docs

- [AGENTS.md]({REPO_URL}/blob/main/AGENTS.md): programmatic usage & dereferenceable facts
- [README]({REPO_URL}/blob/main/README.md): install guide for 30+ clients (CN/EN) + theory linkage

## Theory

- Skills implement the LGD theory system: flagship DOI https://doi.org/{LGD_FLAGSHIP_DOI} (CN/EN),
  laws = {LGD_LAWS}; medical-line skills execute {LGD_MED_PAPER}. See README "Theory Linkage".

## SynomosAI — General AI Skills

"""
for d in SYNOMOSAI:
    if d in all_rows:
        _, name, desc = all_rows[d]
        ll += f"- [{d}]({REPO_URL}/blob/main/skills/{d}/SKILL.md): {desc}\n"
ll += "\n## MedXpert — Medical Device Regulatory Skills\n\n"
for d in MEDXPERT:
    if d in all_rows:
        _, name, desc = all_rows[d]
        ll += f"- [{d}]({REPO_URL}/blob/main/skills/{d}/SKILL.md): {desc}\n"
open(os.path.join(DST, "llms.txt"), "w", encoding="utf-8").write(ll)

open(os.path.join(DST, ".nojekyll"), "w").close()
print(f"README/AGENTS.md/llms.txt/.nojekyll written | SynomosAI={len(SYNOMOSAI)} MedXpert={len(MEDXPERT)} total={len(all_rows)}")
