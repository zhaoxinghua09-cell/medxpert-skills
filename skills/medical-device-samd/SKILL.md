---
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medical-device-samd
displayName: SaMD软件医疗器械专家
description: "SaMD（Software as a Medical Device）软件即医疗器械专题技能——SaMD 判定与 IMDRF N12 风险分类（I-IV 类）+ IEC 62304 软件生命周期（A/B/C 级）+ FDA 软件三级关注（Major/Moderate/Minor）+ MDR 软件分类规则 11 + 网络安全（MDCG 2019-16、FDA 网络安全指南、SBOM）评估清单。独立软件/含软件器械注册申报的软件文档怎么搭、分类怎么定、网络安全怎么做，一站理清，附官方入口直达。何时用：\"SaMD\" / \"软件即医疗器械\" / \"独立软件\" / \"App 医疗器械\""
description_zh: SaMD软件医疗器械专题——IMDRF N12 分类（I-IV）、IEC 62304 软件生命周期、FDA 三级关注、MDR 规则 11、网络安全（MDCG 2019-16/SBOM）评估清单与官方入口直达。
description_en: SaMD (Software as a Medical Device) skill — IMDRF N12 risk classification (I-IV), IEC 62304 software lifecycle (A/B/C), FDA level of concern (Major/Moderate/Minor), MDR Rule 11, cybersecurity (MDCG 2019-16, FDA guidance, SBOM) checklists with official references.
version: 1.0.0
author: 注册老炮@MedXpert
category: 文档处理
xiaping_category: ["效率工具"]
xiaping_tags: ["医疗器械","SaMD","软件即医疗器械","独立软件","软件医疗器械","IMDRF","N12","风险分类","IEC 62304","软件生命周期","软件安全分类","FDA软件","三级关注","level of concern","Major","Moderate","Minor","MDR规则11","Rule 11","网络安全","cybersecurity","MDCG 2019-16","SBOM","软件物料清单","漏洞管理","SOUP","COTS","软件需求规格","SRS","人因","可用性工程","IEC 62366-1","软件注册","医疗器械软件","软件验证","AI医疗","人工智能医疗器械","software as a medical device"]
agent_created: true
slug: medical-device-samd
display_name: SaMD软件医疗器械专家
title: SaMD软件医疗器械专家
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
license: MIT
tags: ["医疗器械","SaMD","软件即医疗器械","独立软件","IMDRF","N12","IEC 62304","软件生命周期","FDA软件","三级关注","MDR规则11","网络安全","MDCG 2019-16","SBOM","漏洞管理","人因","IEC 62366-1","software as a medical device"]
---

# SaMD软件医疗器械专家

## 这是什么

聚焦「带软件功能的器械」注册合规的**实操技能**：先判断产品算不算 SaMD（独立软件）还是嵌入式软件，再按 IMDRF N12 分类、IEC 62304 软件生命周期、FDA 三级关注、MDR 规则 11 组织软件文档，最后做网络安全评估（MDCG 2019-16、SBOM）。覆盖软件医疗器械从"分类怎么定"到"文档怎么搭"再到"安全怎么做"的全链路。

## 为什么用本技能

- **分类不跑偏**：SaMD / 嵌入式软件 / 非医疗器械软件（如一般健康 App）判定表 + IMDRF N12 风险分类决策，避免"健康 App 当医疗器械管"或"该管不管"两个极端。
- **文档有层级**：IEC 62304 A/B/C 安全分类决定过程严格程度，FDA 三级关注决定提交深度，对照表一眼看清。
- **网络安全落地**：威胁建模、SBOM、漏洞管理评估清单，满足 MDCG 2019-16 与 FDA 要求，上市后漏洞管理持续义务一并提醒。

## 触发场景（Triggers）

- "SaMD" / "软件即医疗器械" / "独立软件" / "App 医疗器械"
- "IEC 62304" / "软件生命周期" / "软件安全分类"
- "IMDRF N12" / "SaMD 分类" / "风险分类"
- "FDA 三级关注" / "level of concern" / "Major / Moderate / Minor"
- "MDR 规则 11" / "Rule 11 软件分类"
- "网络安全 / MDCG 2019-16 / SBOM / 漏洞管理"
- "AI 医疗器械" / "人工智能医疗器械注册"
- 软件产品注册申报怎么准备

## 使用流程（Workflow）

1. **先判定身份**：产品算 SaMD、嵌入式软件还是非医疗器械软件？用 `references/SaMD知识库.md` 的判定表。
2. **定风险等级**：IMDRF N12 分类（按"信息提供情境 × 对患者影响"）、FDA 三级关注、MDR 规则 11 分别判定。
3. **搭软件文档**：按 IEC 62304 生命周期组织（需求→架构→实现→验证→发布→维护），安全分类定严格程度。
4. **做网络安全评估**：威胁建模 → SBOM → 漏洞管理计划（含上市后更新机制）。
5. **人因补位**：有交互界面的软件补充可用性评估（IEC 62366-1），使用错误纳入风险分析。
6. **标注时效**：FDA 软件/网络安全指南改版频繁、EU 协调标准滚动更新，用官方检索入口取最新版。

### references/ 文件导航

| 用户问题 | 加载文件 |
|---|---|
| SaMD 判定 / 需不需要 | `SaMD知识库.md` 第一章 |
| IMDRF N12 风险分类 | `SaMD知识库.md` 第二章 |
| IEC 62304 软件生命周期 | `SaMD知识库.md` 第三章 |
| FDA 三级关注 / MDR 规则 11 | `SaMD知识库.md` 第四、五章 |
| 网络安全 / SBOM | `SaMD知识库.md` 第六章 |
| 人因 / 可用性 | `SaMD知识库.md` 第七章 |
| 软件文档清单 | `SaMD知识库.md` 第八章 |

## 使用示例

**示例 1 · 身份判定**
问："我们做一个帮医生看影像的手机 App，算医疗器械吗？"
→ 看它是否用于"诊断/治疗/监测"等医疗用途：若用于医学诊断辅助（如影像分析辅助诊断）→ 属于 SaMD，须按医疗器械管理；若仅是健康记录/生活方式追踪且无医疗宣称 → 通常不属于医疗器械（以各国监管裁定为准，中国按《医疗器械软件注册审查指导原则》判定）。

**示例 2 · 分类与文档**
问："一个辅助诊断的独立软件，文档怎么搭？"
→ IMDRF N12 分类（按对患者影响严重度 × 信息提供情境定 I-IV 类）→ IEC 62304 按安全分类组织软件文档（SRS/架构/测试/维护）→ FDA 按三级关注定提交深度 → 网络安全按 MDCG 2019-16 做威胁建模 + SBOM + 漏洞管理计划。

## 边界说明

- 本技能提供框架与要点，不替代审评机构对具体产品的裁定；软件分类边界（尤其 AI 软件、健康 App）建议走官方预沟通/分类界定。
- 法规/指南更新频繁（FDA 软件与网络安全指南滚动改版、IMDRF 文档更新、EU 协调标准滚动更新），使用前点开官方检索入口复核最新版本。

## 版权与许可

- © 2026 **注册老炮**。本技能及 references 知识库为原创整理，以 **MIT 协议**开源发布。
- **知识版权声明**：本技能整理的合成知识、方法论与编排体系归「注册老炮」所有；未经授权不得复制、转载、转售，或用于训练任何模型（含商业与开源模型）。
- **免责声明**：本技能按「现状（AS IS）」提供，不提供任何明示或默示的担保；因使用、误用本技能或其输出导致的任何直接或间接损失，作者不承担责任。
- 引用的法规与标准均以官方原文（NMPA / FDA / EU MDR 等）为准，链接指向官方站点；如与官方最新版本不一致，以官方为准。
- 内容仅供合规工作参考，不构成注册代理服务或法律意见。

