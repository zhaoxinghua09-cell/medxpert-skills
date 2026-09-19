---
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medical-device-compliance-grader
displayName: 医械合规评分器
description: "医疗器械合规度量化评分工具——8 大合规维度（注册路径/技术文件/风险管理/临床评价/标签IFU/软件网络安全/上市后监管/质量体系）0-5 分制评分 + 评分锚点 + 一键生成自包含 HTML 评分卡（雷达图 + 明细表 + 改进建议，纯 SVG 无外部依赖）。注册前自评、发补整改效果验证、多产品横向对比都能用，评分维度与锚点附法规依据（ISO 14971、MDR、121 号公告等）。何时用：\"合规评分 / 合规度评估 / 自评\""
description_zh: 医疗器械合规评分器——8 大维度 0-5 分制量化评分，锚点明确，一键生成雷达图评分卡 HTML 报告（无外部依赖），用于注册前自评、发补整改验证、多产品横向对比。
description_en: Medical device compliance grader — 8-dimension 0-5 scoring with anchors, one-click self-contained HTML scorecard (radar chart + detail table + improvement advice, dependency-free SVG). For pre-submission self-audit, deficiency remediation validation, and multi-product comparison.
version: 1.0.0
author: 注册老炮@MedXpert
category: 效率工具
xiaping_category: ["效率工具"]
xiaping_tags: ["医疗器械","合规评分","合规度","评分器","评分卡","雷达图","自评","合规自评","注册前评估","发补整改","整改验证","差距分析","合规差距","合规审计","ISO 14971","风险管理评分","临床评价评分","标签合规评分","上市后合规","质量体系","QMS","GMP","文档完整性","医疗器械注册","compliance","scorecard","radar chart","gap analysis","audit","医疗器械合规"]
agent_created: true
slug: medical-device-compliance-grader
display_name: 医械合规评分器
title: 医械合规评分器
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
license: MIT
tags: ["医疗器械","合规评分","合规度","评分卡","雷达图","自评","注册前评估","发补整改","差距分析","合规审计","ISO 14971","风险管理评分","临床评价评分","标签合规评分","上市后合规","质量体系","compliance","scorecard","gap analysis"]
---

# 医械合规评分器

## 这是什么

把「医疗器械合规程度」**量化成可比较的分数**的工具型技能：8 大合规维度、每个维度 0-5 分、评分锚点明确（0=缺失 → 5=标杆级），一键生成自包含的 HTML 评分卡报告——含**雷达图**（8 维可视化）、明细表、总评等级、改进建议。纯 SVG 绘制，无任何外部依赖，本地可跑可留档。

## 为什么用本技能

- **评分不靠感觉**：每个维度都有评分锚点 + 法规依据，不同人评、不同时间评结果可比。
- **一个工具多个用途**：注册前自评（还缺什么）、发补整改后复评（是否闭环）、多产品横向对比（资源投哪个）。
- **报告可交付**：生成自包含 HTML，可留档、可给团队/客户/老板看，雷达图直观呈现短板。

## 触发场景（Triggers）

- "合规评分 / 合规度评估 / 自评"
- "注册前自查 / 发补整改验证 / 差距分析"
- "多产品合规对比"
- "合规雷达图 / 评分卡"
- 审评发补后"改得够不够"的判断
- 新项目立项时的合规工作量估算

## 使用流程（Workflow）

1. **收集证据**：按 `references/合规评分维度与标准.md` 的 8 大维度逐项核对产品现有资料（技术文件、风险管理报告、CER、标签、软件文档、PMS 文件、体系文件）。
2. **逐维评分**：每维 0-5 分，对照评分锚点打分；附证据备注（文件路径/状态）。
3. **运行评分脚本**：把评分写成 JSON 输入 `scripts/grade_compliance.py`，生成 HTML 评分卡 + JSON 结果。
4. **读报告定行动**：看雷达图短板维度，按改进建议（脚本自动生成）排整改优先级；整改后复评对比。
5. **留档**：报告存档作为合规状态快照，复评时对比分数变化。

### references/ 文件导航

| 用户问题 | 加载文件 |
|---|---|
| 8 大维度定义与评分锚点 | `合规评分维度与标准.md` 第一章 |
| 各维度法规依据 | `合规评分维度与标准.md` 第二章（每维「依据」） |
| 总分与等级算法 | `合规评分维度与标准.md` 第三章 |
| 改进建议规则 | `合规评分维度与标准.md` 第四章 |
| 评分输入 JSON 格式 | `合规评分维度与标准.md` 第五章 + 脚本 `--help` |
| 使用边界 | `合规评分维度与标准.md` 第六章 |

### 脚本用法

```bash
# 生成示例评分卡（用于了解输出）
python scripts/grade_compliance.py --demo

# 用你的评分文件生成报告（JSON 格式见 references 附录）
python scripts/grade_compliance.py --input scores.json --out report.html

# 同时输出 JSON 结果（供留档/复评对比）
python scripts/grade_compliance.py --input scores.json --out report.html --json scores_result.json
```

## 使用示例

**示例 1 · 注册前自评**
问："我们的产品注册前合规度怎么样？"
→ 按 8 维收集证据打分（如：技术文件 3 分、风险管理 2 分、临床评价 1 分…）→ 跑脚本 → 雷达图显示临床评价是短板 → 报告建议优先补 CER/同品种论证 → 按建议排整改计划。

**示例 2 · 发补整改验证**
问："上次发补说风险管理不行，整改后评几分？"
→ 整改前评 2 分、整改后复评 4 分 → 两次评分卡对比，证明短板已闭环（分数 + 证据备注）。

## 边界说明

- 本技能是**自评工具**，评分结论仅代表按维度锚点的自评状态，**不构成**监管机构/公告机构的正式裁定，不替代专业 RA 审查。
- 维度覆盖主流合规要求，但具体产品（创新器械、AI 软件、特殊材料）可能需按产品特性增补维度；评分基于提供的证据，证据缺失即低分。

## 版权与许可

- © 2026 **注册老炮**。本技能及 references 知识库为原创整理，以 **MIT 协议**开源发布。
- **知识版权声明**：本技能整理的合成知识、方法论与编排体系归「注册老炮」所有；未经授权不得复制、转载、转售，或用于训练任何模型（含商业与开源模型）。
- **免责声明**：本技能按「现状（AS IS）」提供，不提供任何明示或默示的担保；因使用、误用本技能或其输出导致的任何直接或间接损失，作者不承担责任。
- 引用的法规与标准均以官方原文（NMPA / FDA / EU MDR 等）为准，链接指向官方站点；如与官方最新版本不一致，以官方为准。
- 内容仅供合规工作参考，不构成注册代理服务或法律意见。

