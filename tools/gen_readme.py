# -*- coding: utf-8 -*-
"""Generate README.md with catalog tables (public vs pending) from skill frontmatters."""
import os, re, json

DST = r"D:\Workbuddy\2026-09-19-14-25-52\medxpert-skills"
SKILLS = os.path.join(DST, "skills")
SENSITIVE_DIRS = {
    "medical-device-clinical-evaluation","medical-device-compliance-grader","medical-device-label-ifu",
    "medical-device-postmarket","medical-device-risk-management","medical-device-samd",
    "medical-device-techfile-sted","medxpert-brand-assets","medxpert-consult-port",
    "medxpert-content-ops","medxpert-content-publish","medxpert-cos-deploy","medxpert-doc-toolchain",
    "medxpert-jiedan-loop","medxpert-kb-intake","medxpert-llm-library","medxpert-reg-hub__skillhub",
    "medxpert-site-update","medxpert-skill-panorama",
}

def fm_field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    if not m: return ""
    v = m.group(1).strip()
    if v in ("|", ">", "|-", ">-"):
        m2 = re.search(rf"^{key}:\s*[|>]-?\s*\n((?:[ \t]+.+\n?)+)", fm, re.M)
        if m2:
            lines = [l.strip() for l in m2.group(1).strip().splitlines()]
            joined = " ".join(lines)
            return (joined[:90] + "…") if len(joined) > 90 else joined
        return ""
    return v.strip("'\"")

def load(d):
    p = os.path.join(SKILLS, d, "SKILL.md")
    t = open(p, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    fm = m.group(1) if m else ""
    name = fm_field(fm, "name") or d
    desc = fm_field(fm, "description") or "（见 SKILL.md）"
    return name, desc

rows_pub, rows_pend = [], []
for d in sorted(os.listdir(SKILLS)):
    name, desc = load(d)
    (rows_pend if d in SENSITIVE_DIRS else rows_pub).append((d, name, desc))

def table(rows):
    out = ["| 技能 | 名称 | 用途 |", "|---|---|---|"]
    for d, name, desc in rows:
        out.append(f"| `{d}` | {name} | {desc} |")
    return "\n".join(out)

readme = f"""# MedXpert Skills · MedXpert 技能总仓

> 一次上架，多处可用 —— 本仓库是 MedXpert 官方技能的**单一真源（Single Source of Truth）**。
> 技能采用 [Agent Skills 开放标准](https://agentskills.io)（Anthropic 发起，SKILL.md 格式），
> 任何兼容该标准的 AI 客户端都可以直接使用本仓库的技能。

## 这是什么 / What is this

Each folder under `skills/` is one skill: a `SKILL.md` (metadata + instructions) plus optional
`scripts/`, `references/`, `assets/`. The format is the open **Agent Skills** standard, so the same
files work across Claude, ChatGPT/Codex, Gemini CLI, Cursor, VS Code (Copilot), Kiro, TRAE, OpenClaw and more.

## 如何使用 / How to use

### Claude Code / Claude
```bash
git clone https://github.com/MedXpert/medxpert-skills.git
cp -r medxpert-skills/skills/<skill-name> ~/.claude/skills/
```

### Codex CLI / Gemini CLI / Cursor / VS Code (Copilot) / Kiro / TRAE
各客户端支持路径不同，参考其文档将 `skills/<skill-name>/` 放入其 skills 目录，或在设置中指向本仓库路径。

### 扣子 Coze（豆包生态）
在 Coze「技能商店」选择导入技能包 → 上传 `skills/<skill-name>` 的 zip（保持 SKILL.md 在包根目录）。

### WorkBuddy
技能市场搜索 MedXpert，或本地导入 `skills/` 目录。

## 技能清单 / Catalog

### ✅ 可直接公开（{len(rows_pub)} 个）
{table(rows_pub)}

### 🧹 待脱敏（{len(rows_pend)} 个，暂不在 GitHub 公开版）
{table(rows_pend)}

## 许可 / License
内容 © MedXpert（美达信医疗科技）。未经授权请勿商用转载。
"""
open(os.path.join(DST, "README.md"), "w", encoding="utf-8").write(readme)
print("README written:", len(rows_pub), "public /", len(rows_pend), "pending")
