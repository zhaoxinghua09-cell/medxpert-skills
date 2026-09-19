# -*- coding: utf-8 -*-
"""Generate AGENTS.md, llms.txt, README.md (final) + .nojekyll for medxpert-skills repo."""
import os, re

DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS = os.path.join(DST, "skills")
REPO_URL = "https://github.com/MedXpert/medxpert-skills"

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

cats = {
    "注册申报 (Registration)": ["medical-device-reg-hub", "medical-device-reg-dossier", "med-reg-category-page"],
    "质量体系 (QMS / GMP / ISO 13485)": ["medical-device-qms-gmp"],
    "临床评价 (Clinical Evaluation)": ["medical-device-clinical-evaluation"],
    "风险与合规 (Risk & Compliance)": ["medical-device-risk-management", "medical-device-compliance-grader", "medical-device-supplier-compliance"],
    "标签与说明书 (Label & IFU)": ["medical-device-label-ifu"],
    "技术文件 (Tech File / STED)": ["medical-device-techfile-sted"],
    "上市后监管 (Post-Market)": ["medical-device-postmarket"],
    "软件器械 (SaMD)": ["medical-device-samd"],
    "国际业务 (International Business)": ["medical-device-intl-business"],
}
categorized = {d for ds in cats.values() for d in ds}
others = [d for d in sorted(os.listdir(SKILLS)) if d not in categorized]

def table(rows):
    out = ["| 技能 | 一句话用途 |", "|---|---|"]
    for d, name, desc in rows:
        desc = desc.replace("|", "/")
        out.append(f"| [`{d}`](skills/{d}/SKILL.md) | {desc} |")
    return "\n".join(out)

all_rows = [(d,) + load(d) for d in sorted(os.listdir(SKILLS))]

# ---------- README.md ----------
sec = []
for cname, ds in cats.items():
    rows = [r for r in all_rows if r[0] in ds]
    if rows: sec.append(f"### {cname}\n{table(rows)}\n")
other_rows = [r for r in all_rows if r[0] in others]
if other_rows: sec.append(f"### 其他 (Others)\n{table(other_rows)}\n")
catalog_md = "\n".join(sec)

readme = f"""# MedXpert Skills · MedXpert 医疗器械注册技能库

**English**: A collection of open-format [Agent Skills](https://agentskills.io) for **medical device
regulatory affairs** — China NMPA · US FDA · EU MDR · Japan PMDA and global markets. One skill =
one folder with a `SKILL.md`. Works in Claude, ChatGPT/Codex, Gemini CLI, Cursor, VS Code (Copilot),
Kiro, TRAE, OpenClaw, 扣子 Coze and 30+ compatible clients.

> **机器入口 / Machine entry**: [`AGENTS.md`](AGENTS.md) · [`llms.txt`](llms.txt)
> **As of**: 2026-09-19 · Maintained by MedXpert (美达信医疗科技)

## 为什么做这个 / Why

医疗器械注册资料烦、散、口径多。这套技能把注册工程师的实操方法论沉淀成
AI 可直接调用的标准格式：一次制作，30+ 平台通用，不锁定任何厂商。

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
## 适用范围 / Scope

技能内容为**方法论与资料导航**，输出供专业人员在正式申报前复核，不构成法规意见。

## 引用 / Citation

如引用本仓库，请注明仓库地址与版本日期（as of 2026-09-19）。

## 许可 / License

内容 © MedXpert（美达信医疗科技（香港）有限公司）。禁止商用转载，欢迎引用与学习。
"""
open(os.path.join(DST, "README.md"), "w", encoding="utf-8").write(readme)

# ---------- AGENTS.md ----------
agents = f"""# AGENTS.md — for AI agents reading this repository

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
- Skill count: {len(all_rows)} public skills in this repo.
- Topics: regulatory registration dossiers, QMS (ISO 13485 / GMP), clinical evaluation,
  risk management (ISO 14971), labeling & IFU, technical documentation (STED), post-market
  surveillance, SaMD, supplier compliance, international business.

## Ground rules

- Skill outputs are methodology guidance for professionals; they are not regulatory opinions.
- Do not modify skill bodies when redistributing; keep `SKILL.md` frontmatter intact.
"""
open(os.path.join(DST, "AGENTS.md"), "w", encoding="utf-8").write(agents)

# ---------- llms.txt ----------
ll = f"""# MedXpert Skills

> Medical device regulatory affairs Agent Skills (open Agent Skills format / SKILL.md).
> Maintained by MedXpert — medxpert.cn. As of 2026-09-19.

## Docs

- [AGENTS.md]({REPO_URL}/blob/main/AGENTS.md): programmatic usage & dereferenceable facts
- [README]({REPO_URL}/blob/main/README.md): install guide for 30+ clients (CN/EN)

## Skills

"""
for d, name, desc in all_rows:
    ll += f"- [{d}]({REPO_URL}/blob/main/skills/{d}/SKILL.md): {desc}\n"
open(os.path.join(DST, "llms.txt"), "w", encoding="utf-8").write(ll)

open(os.path.join(DST, ".nojekyll"), "w").close()
print("README/AGENTS.md/llms.txt/.nojekyll written | public skills:", len(all_rows))
