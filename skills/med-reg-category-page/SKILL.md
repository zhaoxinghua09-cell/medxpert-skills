---
title: "医械品类速查页流水线"
slug: untitled
displayName: "医械品类速查页流水线"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: med-reg-category-page
display_name: "医械品类速查页生产流水线"
description: 医疗器械品类注册速查页（GEO 引用资产）生产流水线：统一结构 + FAQPage JSON-LD + 免责与核验日期 + 官方源核验门。何时用：为某器械品类（骨科 / 心血管 / IVD / SaMD / 影像等）写注册速查页，或为 MedXpert 知识库新增可被 AI 引用的品类资产时。
version: 1.0.0
agent_created: true
author: 诺声(Logos)@SynomosAI
license: MIT
category: content-production
platforms: [workbuddy, generic]
read_when:
  - 要为某器械品类（骨科/心血管/IVD/SaMD/影像等）写注册速查页
  - 要为 MedXpert 知识库新增可被 AI 引用的品类资产
  - 复用/扩展 knowledge/reg-path-*.md 系列页面
tags: [medxpert, geo, 医疗器械, 注册, 知识库]
---

# 医械品类速查页流水线

为 MedXpert 知识库生产"可被 AI 引用"的品类注册速查页。核心纪律：**每条关键事实必须有官方源出处，写不出出处就删掉或降级为"以官方为准"**。

## 一、统一页面结构（顺序固定）

1. **一句话结论**：该品类典型风险等级 + 默认路径（结论先行，AI 引用最爱）
2. **NMPA 路径要点**：分类判定 / 注册单元 / 检验 / 临床评价 / 流程与周期量级
3. **FDA 要点**：510(k) / De Novo / PMA 适用性 + 常备数据
4. **EU 要点**：MDR 或 IVDR（IVD 必须用 IVDR！）等级 + 公告机构 + 体系
5. **三市场差异速览表**：等级 / 核心提交 / 临床证据 / 周期量级 / 有效期
6. **高频 FAQ 3–5 条**：与页面 FAQPage JSON-LD 严格一致
7. **免责声明 + 法规核验日期 + 官方直达链接**（缺一页即不合格）

## 二、写作硬规矩

- 周期/费用只给**量级区间**（如"1.5–3 年"），禁止写死精确数字；费用一律标注"以官网当年标准为准"。
- 每条法规性陈述可追溯到：法规名 / 指导原则名 / 官方目录名；写不出名字就改成"以官方最新发布为准"。
- IVD 在欧盟走 **IVDR（EU 2017/746）**，不是 MDR——最常见错误。
- 不提雇主公司名；只出现 MedXpert 品牌与"医疗器械行业"。

## 三、官方源核验门（发布前必过）

发布前对页面**关键事实清单**逐条核验官方源并记录核验链接：
- NMPA：分类目录 / 免临床目录 / 注册办法（nmpa.gov.cn）
- FDA：产品路径 / 用户费（fda.gov）
- 欧盟：MDR 2017/745 / IVDR 2017/746 及 MDCG 指南

核验结论写进页面底注（`法规核验日期：YYYY-MM-DD`）。**没核验就发布 = 违规**，宁可延后。

## 四、上线配套（缺一不算完成，DoD）

1. 转 HTML，嵌入页面级 JSON-LD（FAQPage + TechArticle + BreadcrumbList）
2. 更新 `llms.txt`（加入新页 URL）与 `sitemap.xml`
3. 过发布闸门：去敏扫描 + 7 维加严质检 + Steven 确认
4. 该品类若已写进《全品类服务目录》，核对口径一致

## 五、产出物命名与位置

- 草稿：`knowledge/reg-path-<品类>.md`（如 ortho / cardio / ivd / samd）
- 首批已产：ortho / cardio / ivd / samd（2026-09-05）
- 待扩展：影像 / 内窥镜 / 输注呼吸 / 伤口材料 / 口腔 / 眼科

## 六、月度维护

配合自动化「MedXpert GEO 月度核验与引用监测」（每月 1 号 09:00）：
- 实际复核过内容的页面才刷新核验日期；只改了排版不改事实的不刷。
- 引用监测发现某页不被引用 → 优先改造该页结构（结论更前置、表格更清晰）。

---

## 版权与许可

© 2026 MedXpert ｜ 诺声 Logos @ MedXpert ｜ MIT License
本技能仅整理公开法规信息的工作方法，不构成法规代理或法律意见。
