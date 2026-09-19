---
title: "medxpert-vi-extension"
slug: medxpert-vi-extension
displayName: "medxpert-vi-extension"
category: "skill-ops"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medxpert-vi-extension
description: "基于 MedXpert 已有 VI 规范，在 Ardot 画布上快速延展 PPT 模板、知识手册封面、公众号头像/头图、X 展架/背景板、Skill 安装长图等品牌物料。何时用：在已有 MedXpert 品牌套件基础上，批量补充营销推广/分发所需的物料画板"
version: 1.0.0
agent_created: true
---

# MedXpert VI 延展素材生成

## 适用场景

在已有 MedXpert 品牌套件基础上，批量补充营销推广/分发所需的物料画板。

## 前置依赖

- Ardot 画布文件已打开，URL 形如 `https://ardot.tencent.com/file/{fileId}`。
- 品牌套件页（3:1）及 logo 锁定组合来源节点可用：
  - `3:15` 标准版（白底红字）
  - `3:18` 透明版（浅蓝底红字）
  - `3:21` 深底版（深蓝渐变底白字）
- 字体：英文 `DM Sans Bold Italic`，中文 `Noto Sans SC`（Bold / Regular）。

## 品牌色

- 品牌红：`#E8281B` = `rgb(0.910, 0.157, 0.106)`
- 二维码蓝 / 深蓝渐变起：`#16325C` = `rgb(0.086, 0.196, 0.361)`
- 深蓝渐变止：`#2D6DDF` ≈ `rgb(0.176, 0.427, 0.875)`
- 浅背景：`#F2F3F7` ≈ `rgb(0.949, 0.961, 0.980)`
- 文字灰：`#555555`

## 胶囊 mark 矢量规格

- 圆角矩形 `34×24`，`cornerRadius: 12`
- 根据背景切换填充：白底/深色上用白色或红色

## 推荐画板尺寸

| 物料 | 尺寸 |
|---|---|
| PPT 模板 | 单张 1260×720（可在画板内并排展示多套） |
| 知识手册封面 | 800×1130（A4 竖版比例） |
| 公众号头像 | 240×240 |
| 公众号头图 | 900×383 |
| X 展架 | 600×1600 |
| 活动背景板 | 1920×1080 |
| Skill 安装长图 | 800×2600 |

## 工作流

1. `create_new_page` 按需新建页面。
2. 用 `batch_edit` 插入根画板，套用对应尺寸和背景（深蓝渐变 / 品牌红 / 白色）。
3. 用胶囊 mark + `MedXpert` 单词标组合 logo，根据背景切换颜色。
4. 添加标题、副标题、步骤/要点卡片、二维码占位框（建议给浅灰填充+浅灰描边，避免在白色背景上消失）。
5. `capture_screenshot` 抽检关键页面。
6. `export_nodes` 以 `png`、`scale: 2` 导出；用 `curl` 在 10 分钟内下载到 `outputs/`。

## 占位项（上线前替换）

- 二维码占位 → 替换为 `outputs/qr/` 下的真实 QR 素材。
- 电话 400-XXX-XXXX、邮箱 contact@medxpert.cn、网址 medxpert.cn。
- 展会/峰会/卷期信息。

## 交付物命名示例

```
outputs/MedXpert_12_PPT模板.png
outputs/MedXpert_13_知识手册封面.png
outputs/MedXpert_14_公众号头像.png
outputs/MedXpert_15_公众号头图.png
outputs/MedXpert_16_X展架.png
outputs/MedXpert_17_背景板.png
outputs/MedXpert_18_Skill安装长图.png
outputs/MedXpert_Logo_标准版_来源.png
outputs/MedXpert_Logo_透明版_来源.png
outputs/MedXpert_Logo_深底版_来源.png
```
## 合规 · AI 生成内容标识（GB45438-2025）

> 本技能属于**公众面向内容生成（A 级）**，须严格执行以下合规加闸（依据《技能包国家合规适配方案 v20260911》铁律一）。

- **显式标识**：本技能产出的文本/图文/音视频等**均为 AI 生成内容**，对外发布时**须在显著位置标注"AI 生成"角标**（如文首/文末"本文由 AI 辅助生成"），不得冒充自然人创作。
- **隐式元数据**：按 GB45438-2025 在生成内容中嵌入机器可读标识（生成工具、生成时间、内容类型），便于平台识别与溯源。
- **备案评估**：涉及舆论属性或面向公众大规模传播的，须评估《生成式人工智能服务管理暂行办法》第十七条之**生成式 AI 服务备案**及《互联网信息服务算法推荐管理规定》之**算法备案**触发条件（以属地网信办认定为准，本声明非法律意见）。
- **人工复核与责任**：输出须附责任主体与人工复核声明；不得生成违法违规、侵权或误导内容。
- 延伸：上架三铁律（国家+国际合规 / AI 特别友好 / 理念文化·强 IP）· 合规闸门 skill-release-gate。
