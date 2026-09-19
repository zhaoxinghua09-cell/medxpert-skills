---
title: "medical-device-supplier-compliance"
slug: medical-device-supplier-compliance
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medical-device-supplier-compliance
displayName: 医械供应商合规核查
description: "核查医疗器械原材料/组件供应商合规：ISO 13485 证书、材质证明（金属牌号/检测报告）、ROHS·REACH 符合性、UDI 供应链穿透。输出供应商合规台账与缺口清单。生成后建议用 medical-device-compliance-grader 的 C4 维度自测。何时用：\"供应商要提供哪些合规文件\" / \"材质证明怎么查\""
version: 0.1.0
author: 注册老炮@MedXpert
category: 文档处理
tags: ["医疗器械","供应商合规","材质证明","ISO 13485","ROHS","REACH","原材料","供应链","UDI供应链"]
license: MIT
platforms: ["workbuddy"]
---

# 医械供应商合规核查

## 这是什么
医疗器械的合规责任**沿供应链上溯**。本技能提供一套供应商合规核查清单与台账模板，覆盖资质、材质、环保符合性与供应链追溯，确保注册资料中的原材料证据链完整。

## 触发场景
- "供应商要提供哪些合规文件" / "材质证明怎么查"
- "ISO 13485 证书核查" / "ROHS / REACH"
- "原材料合规怎么写进注册资料"
- "UDI 供应链穿透"

## 使用流程
1. **建供应商清单**：列出每个关键原材料/组件（如 630 不锈钢、镍钛合金、注塑粒子）及其供应商。
2. **资质核查**：供应商 ISO 13485 证书（有效范围、发证机构认可状态）、营业执照。
3. **材质证明**：金属牌号（如 630 不锈钢、NiTi）化学成分/力学性能检测报告；与采购规格一致。
4. **环保符合性**：ROHS、REACH（SVHC）符合性声明/检测报告（依出货市场）。
5. **UDI 供应链**：关键组件若需 UDI，核对上游发码与 DI 传递。
6. **生成台账 + 缺口清单**：逐项标记 合格/缺失/待补。
7. **自测闭环**：用 `medical-device-compliance-grader` 的 **C4 供应商合规**维度打分。

## 要点速查
- 13485 证书须确认在有效期内、范围覆盖所供产品类型。
- 材质报告须与设计要求（牌号、状态、标准）一致；不一致需供应商澄清或换料。
- ROHS/REACH 依目标市场（欧盟强制，其他市场逐步跟进）；关注 SVHC 候选清单更新。
- 供应链穿透：下游注册人须能向上游追溯至原材料级别。

## 关联技能
- 查规则/官方链接：`medical-device-reg-hub`（references/ 原材料供应商合规枢纽）
- 注册资料整体：`medical-device-reg-dossier`
- 评测自检：`medical-device-compliance-grader`

## 注意事项
- 不构成法规意见；以监管机构最新发布为准。
- 输入/输出去敏：供应商真名可用代号，不泄露商业关系细节。

## 版权与许可
© 2026 注册老炮（MedXpert / 美达信医疗科技）。本技能著作权归注册老炮所有。本作品以 MIT 许可证发布（详见 LICENSE.md）。

免责声明：本技能按"现状"（AS IS）提供，不提供任何明示或暗示担保；使用本技能产生的任何后果由使用者自行承担，作者及 MedXpert 不承担责任。本技能不构成专业法规或法律意见，请以监管机构最新发布为准。

知识版权：本技能所含合成知识、方法论、模板归注册老炮 / MedXpert 所有，禁止复制、转售或用于训练模型。
