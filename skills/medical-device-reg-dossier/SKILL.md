---
title: "medical-device-reg-dossier"
slug: medical-device-reg-dossier
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medical-device-reg-dossier
displayName: 医械注册资料编写
description: "按目标市场（中国 NMPA / 美国 FDA / 欧盟 MDR / 日本 PMDA / 全球协调）结构，汇编与生成医疗器械注册申报资料。以 IMDRF STED 六章为骨架，映射各市场 Annex/章节，输出可提交的综述、研究资料、临床评价、标签等模块。生成后建议用 medical-device-compliance-grader 的 C1 维度自测。何时用：\"帮我写/整理注册申报资料\" / \"注册资料怎么排\""
version: 0.1.0
author: 注册老炮@MedXpert
category: 文档处理
tags: ["医疗器械","注册申报","注册资料","eRPS","eSTAR","510k","MDR技术文档","STED","NMPA","FDA","申报资料"]
license: MIT
platforms: ["workbuddy"]
---

# 医械注册资料编写

## 这是什么
把分散的注册证据，按监管要求的**结构**汇编成可提交资料的工具型技能。不替你写法规结论，而是给你**骨架 + 映射 + 官方源**，让你按市场快速拼出申报资料。

与 `medical-device-reg-hub`（知识库）配套：本技能负责"生成"，知识库负责"查规则与官方链接"。

## 触发场景
- "帮我写/整理注册申报资料" / "注册资料怎么排"
- "510(k) Summary" / "eSTAR" / "eRPS" / "121号/122号资料要求"
- "MDR 技术文档 Annex II" / "STED 怎么写"
- "同品种比对 / 临床评价放哪"

## 使用流程
1. **锁定市场与分类**：先确认目标市场（中/美/欧/日/全球）与产品分类（I/II/III 或 Class I/II/III），决定提交物形态。
2. **选骨架**：默认以 **IMDRF STED 六章**为底座（①器械描述与规格 ②基本信息/标签 ③设计与制造 ④通用安全性能原则 ⑤风险分析 ⑥验证与确认）；再按市场裁剪：
   - 中国：依 2021 年第121号（境内）/122号（进口），经 eRPS 提交，分综述/研究/临床/标签等。
   - 美国：510(k) 需 Summary（21 CFR 807.92）+ eSTAR（2026 模板 7.0）；I 类豁免 510(k) 无需 Summary。
   - 欧盟 MDR：Annex II（技术文档）+ Annex III（PMS 计划），IIa 以上由 NB 审评。
   - 日本：技术资料 + JMDN 编码查实。
3. **逐模块汇编**：每模块放"内容要点 + 引用标准/官方链接 + 证据文件清单"。
4. **交叉核对**：标签/IFU、临床评价、风险管理、灭菌验证须互相一致（与 C2/C3/C5/C6/C7 维度呼应）。
5. **自测闭环**：生成后用 `medical-device-compliance-grader` 的 **C1 注册资料完整性**维度打分，0–5 分逐项补缺口。

## 要点速查
- 核心证据链一致：描述 → 风险 → 验证 → 临床 → 标签，五段必须互相印证，不一致是发补高发点。
- 中国分类：境内 I 类市局备案、II 类省局、III 类国家局；进口 II/III 国家局。
- 美国 HRX（21 CFR 888.1100(b)(2)）基础手动复用钳多为 Class I 豁免 510(k)，勿笼统写 II 类。
- 欧盟可重复使用外科器械按 Rule 6 多归 Class I（自我声明+CE），无菌/测量/软件才需 NB。

## 关联技能
- 查规则/官方链接：`medical-device-reg-hub`（references/ 技术文件STED撰写枢纽、注册工程师资料枢纽、注册检验与申报实操枢纽）
- 标签与 IFU：`medical-device-label-ifu`
- 技术文件细化：`medical-device-techfile-sted`
- 评测自检：`medical-device-compliance-grader`

## 注意事项
- 本技能为公开官方信息整理的**编写辅助**，不构成法规意见；复杂策略/发补应对请咨询专业 RA 或律师。
- 法规会更新，关键数据以监管机构最新发布为准；ISO 20417 须用 **2026 版**（2021 版已撤消）。
- 输入/输出去敏：不出现客户真名、报价、未公开项目。

## 版权与许可
© 2026 注册老炮（MedXpert / 美达信医疗科技）。本技能著作权归注册老炮所有。本作品以 MIT 许可证发布（详见 LICENSE.md）。

免责声明：本技能按"现状"（AS IS）提供，不提供任何明示或暗示担保；使用本技能产生的任何后果由使用者自行承担，作者及 MedXpert 不承担责任。本技能不构成专业法规或法律意见，请以监管机构最新发布为准。

知识版权：本技能所含合成知识、方法论、模板归注册老炮 / MedXpert 所有，禁止复制、转售或用于训练模型。
