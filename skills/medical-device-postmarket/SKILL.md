---
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medical-device-postmarket
displayName: 医械上市后监管专家
description: "医疗器械上市后监管（Post-Market Surveillance, PMS）专题技能——中美欧日四市场上市后义务对照（不良事件报告、PSUR、FSCA/召回、PMCF）+ 各市场报告时限与流程清单 + PMS 计划/PSUR 撰写框架。拿证后的持续合规动作（监测—报告—纠正闭环）一站理清，附 FDA MDR、MDCG 2022-21、中国 2018 年 1 号令官方直达。何时用：\"上市后 / PMS / 上市后监管\" / \"不良事件\" / \"MDR 报告\" / \"MAUDE\""
description_zh: 医疗器械上市后监管专题——中美欧日 PMS 义务对照、不良事件/PSUR/FSCA/召回流程与时限清单、PMS 计划与 PSUR 撰写框架，附官方依据直达。
description_en: Medical device post-market surveillance skill — US/EU/CN/JP PMS obligations comparison, adverse event reporting, PSUR, FSCA/recall timelines & process checklists, PMS plan & PSUR writing framework with official references.
version: 1.0.0
author: 注册老炮@MedXpert
category: 文档处理
xiaping_category: ["效率工具"]
xiaping_tags: ["医疗器械","上市后监管","PMS","不良事件","不良事件报告","MDR","MAUDE","21 CFR 803","召回","FSCA","现场安全纠正","PSUR","MDCG 2022-21","PMCF","MDCG 2020-7","MDCG 2020-8","上市后临床跟踪","再评价","医疗器械再评价","2018年1号令","监测信息系统","警戒","EUDAMED","趋势报告","定期风险评价","SSCP","上市后安全","post-market surveillance","field safety corrective action","medical device reporting"]
agent_created: true
slug: medical-device-postmarket
display_name: 医械上市后监管专家
title: 医械上市后监管专家
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
license: MIT
tags: ["医疗器械","上市后监管","PMS","不良事件","召回","FSCA","PSUR","MDCG 2022-21","PMCF","上市后临床跟踪","再评价","警戒","EUDAMED","post-market surveillance","field safety corrective action"]
---

# 医械上市后监管专家

## 这是什么

聚焦「拿证之后」的**持续合规技能**：不良事件监测与报告、定期安全报告（PSUR）、纠正措施（FSCA/召回）、上市后临床跟踪（PMCF）——四大动作在中美欧日怎么落地、时限多少、文件怎么写，一站理清。核心逻辑是「监测—报告—纠正」闭环，闭环做不好，注册证都可能被收回。

## 为什么用本技能

- **义务不漏项**：四市场上市后义务对照表，跨国产品逐国建流程，不靠记忆。
- **时限不踩雷**：美国 MDR 报告时限、欧盟 FSCA 触发条件、中国报告时限，一条条给清楚。
- **文件有框架**：PMS 计划、PSUR、PMCF 计划/报告都给出撰写结构，与临床评价、风险管理文件互相呼应。

## 触发场景（Triggers）

- "上市后 / PMS / 上市后监管" / "不良事件" / "MDR 报告" / "MAUDE"
- "召回" / "FSCA" / "现场安全纠正" / "趋势报告"
- "PSUR" / "定期安全报告" / "MDCG 2022-21"
- "PMCF" / "上市后临床跟踪" / "MDCG 2020-7 / 2020-8"
- "再评价" / "定期风险评价" / "监测系统"
- 拿证后的持续合规动作安排

## 使用流程（Workflow）

1. **对市场建义务清单**：用 `references/上市后监管知识库.md` 的对照表，确认产品在哪些市场上市、各自触发哪些 PMS 义务。
2. **建监测—报告闭环**：不良事件接收渠道（内部 + 监管系统）、评估流程、报告时限（各国不同）。
3. **写定期文件**：PMS 计划 → 上市后数据收集 → PSUR（IIb/III 及植入类）/ PMS 报告（I 类/IIa）→ 结论回流技术文档。
4. **处理纠正措施**：FSCA/召回分级、通知义务、完成报告；与变更管理、风险管理（生产后活动）联动。
5. **标注时效**：报告时限以各国官方最新要求为准，跨国产品分别确认。

### references/ 文件导航

| 用户问题 | 加载文件 |
|---|---|
| 四市场 PMS 义务对照 | `上市后监管知识库.md` 第一章 |
| 美国不良事件报告（21 CFR 803） | `上市后监管知识库.md` 第二章 |
| 欧盟警戒 / FSCA / PSUR | `上市后监管知识库.md` 第三章 |
| PMCF 计划与报告 | `上市后监管知识库.md` 第四章 |
| 中国监测与再评价 | `上市后监管知识库.md` 第五章 |
| 日本 PMDA 报告 | `上市后监管知识库.md` 第六章 |
| PMS 计划 / PSUR 撰写框架 | `上市后监管知识库.md` 第七章 |

## 使用示例

**示例 1 · 报告义务**
问："我们在美国收到一起严重伤害不良事件，要报告吗？多久？"
→ 要。依据 21 CFR 803，制造商对致死事件 30 日历日内报告 FDA；严重伤害/故障 90 日历日。通过 eMDR 系统提交，并进入 MAUDE 数据库。

**示例 2 · PSUR 撰写**
问："出口欧盟的 IIb 器械 PSUR 怎么写？"
→ 按 MDCG 2022-21 指南组织：产品概况 → 上市后数据汇总（不良事件/PMCF/趋势）→ 获益-风险再评估 → 纠正措施结论；更新频率按风险等级（IIb 至少每 2 年，III 类至少每年，可合并入技术文档更新）。

## 边界说明

- 本技能提供框架与要点，不替代各国监管机构的个案裁定；具体事件报告时限与格式，以产品所在市场最新法规和监管机构最新通知为准。
- 法规会更新（FDA 指南改版频繁、EU 协调标准滚动更新），使用前点开链接复核版本。

## 版权与许可

- © 2026 **注册老炮**。本技能及 references 知识库为原创整理，以 **MIT 协议**开源发布。
- **知识版权声明**：本技能整理的合成知识、方法论与编排体系归「注册老炮」所有；未经授权不得复制、转载、转售，或用于训练任何模型（含商业与开源模型）。
- **免责声明**：本技能按「现状（AS IS）」提供，不提供任何明示或默示的担保；因使用、误用本技能或其输出导致的任何直接或间接损失，作者不承担责任。
- 引用的法规与标准均以官方原文（NMPA / FDA / EU MDR 等）为准，链接指向官方站点；如与官方最新版本不一致，以官方为准。
- 内容仅供合规工作参考，不构成注册代理服务或法律意见。

