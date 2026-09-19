---
slug: medxpert-kb-distribution
displayName: "medxpert-kb-distribution"
category: "ai-agent"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
title: "MedXpert 知识分发流水线"
name: medxpert-kb-distribution
description: 从 MedXpert 项目知识库批量生成分发物料：知识手册（本地模型深度学习）、引流 PDF、GitHub 开源库打包、FAQ 法规引用一致性检查。当用户提到"知识手册"、"引流 PDF"、"github-kb"、"开源知识库"、"检查法规引用"、"check_faq_refs"、"分发物料"、"生成手册"时使用。
version: 1.0.0
agent_created: true
---

# MedXpert 知识分发流水线

把项目知识库变成可对外分发的多种形态（手册/PDF/GitHub/公众号），**所有内容从单一事实源（《法规文号事实库.md》/ 乐享知识库）出发，脚本生成，禁止手工转录**。

## 背景与原则

- 项目工作区：`~\WorkBuddy\2026-08-15-08-06-22\`
- **SSOT 延伸原则（2026-08-16 复盘得出）**：内容层已实现单一事实源（乐享管内容），**分发层（PDF/GitHub/公众号回复）也必须从源头脚本生成**，否则法规一变，多处手工转录全部要返工。
- 事实源：`法规文号事实库.md`（文号单点维护）→ 乐享（内容）→ 脚本（渲染官网 + 生成分发物料）

## 流水线（5 步）

### 1. 知识手册生成（本地模型深度学习）
```bash
cd ~\WorkBuddy\2026-08-15-08-06-22
python _kb_study/study_kb.py        # 对项目知识库分块 + 本地 qwen2.5:7b 逐块精读 → chunks/
python _kb_study/merge_summary.py   # 汇总合并 → 速查手册 + 详细版
```
- 产出：`_kb_study/MedXpert知识手册.md`（速查索引）+ `_kb_study/MedXpert知识手册_详细版.md`（49 块精读，131KB）
- 新增知识后重跑 study_kb.py 增量学习
- 任何对话框要查 MedXpert 法规/工具/项目知识时**先读速查手册**，不用重新学习

### 2. 引流 PDF 生成
```bash
python _kb_study/gen_pdfs.py
```
- 产出：`website/assets/MedXpert_法规文号速查表.pdf` + `MedXpert_全球注册周期费用对比.pdf`
- 同时产出预览图 `_kb_study/preview_p*.png`（供检查排版）

### 3. FAQ 法规引用一致性检查（发布前必跑）
```bash
python _kb_study/check_faq_refs.py
```
- 功能：逐条核对 FAQ 引用法规与《法规文号事实库》是否一致
- 状态：2026-08-16 首跑通过（30 条全部一致）
- **法规更新后：改事实库 → 改乐享 → 重新同步官网 → 重跑本检查**

### 4. GitHub 开源库打包（国际引流）
- 目录：`github-kb/`（README.md 中文 + README.en.md 英文 + docs/ 6 份法规速查 + 2 PDF + qrcode.png + LICENSE MIT）
- README 引流核心：关键词开头 200 字 + 公众号二维码 + 「回复关键词免费领 PDF」
- 平台：GitHub（国际）→ Gitee 导入同步（国内）
- SEO：仓库 topic 打 `medical-device` `regulatory` `NMPA` `FDA` `MDR` `ISO-13485`

### 5. 公众号关键词回复（私域承接）
- 配置指引：`公众号关键词回复配置指引.md`（5 关键词：标准/周期/文号/MDR/目录 + 被添加回复 + 兜底回复）
- PDF 上传素材库后取图文链接填进关键词回复

## 分发闭环

```
事实库/乐享（源头）
   ├─→ sync_lexiang_website.py → 官网 HTML（AI 可读）
   ├─→ gen_pdfs.py → 引流 PDF（公众号/网站下载）
   ├─→ 知识手册（内部学习/二次创作）
   └─→ github-kb → GitHub/Gitee → README 引流公众号
                          ↓
                    公众号关键词回复 → 领 PDF → 私域沉淀
```

## 关键文件索引

| 文件 | 位置 | 用途 |
|---|---|---|
| 法规文号事实库.md | 项目根 | 文号单点维护（唯一源头） |
| sync_lexiang_website.py | 项目根 | 官网渲染 |
| _kb_study/study_kb.py | 项目根 | 知识库分块学习 |
| _kb_study/gen_pdfs.py | 项目根 | 引流 PDF |
| _kb_study/check_faq_refs.py | 项目根 | 法规引用检查 |
| github-kb/ | 项目根 | 开源库内容 |
| 全渠道引流账号清单.md | 项目根 | 9 平台账号/素材/引流方案 |
| AI可调用上线准备清单.md | 项目根 | 官网上线三步 + 验证清单 |

## 注意事项

- **不要手工转录法规文号到任何分发物料**——只从事实库/脚本生成
- 上线外部动作（注册域名/注册平台账号/提交收录/发布）属外部可见操作，需 Steven 本人确认后执行
- 敏感信息（公网 IP、个人账号）不写入乐享/公开仓库，脱敏后展示
## 合规 · AI 生成内容标识（GB45438-2025）

> 本技能属于**公众面向内容生成（A 级）**，须严格执行以下合规加闸（依据《技能包国家合规适配方案 v20260911》铁律一）。

- **显式标识**：本技能产出的文本/图文/音视频等**均为 AI 生成内容**，对外发布时**须在显著位置标注"AI 生成"角标**（如文首/文末"本文由 AI 辅助生成"），不得冒充自然人创作。
- **隐式元数据**：按 GB45438-2025 在生成内容中嵌入机器可读标识（生成工具、生成时间、内容类型），便于平台识别与溯源。
- **备案评估**：涉及舆论属性或面向公众大规模传播的，须评估《生成式人工智能服务管理暂行办法》第十七条之**生成式 AI 服务备案**及《互联网信息服务算法推荐管理规定》之**算法备案**触发条件（以属地网信办认定为准，本声明非法律意见）。
- **人工复核与责任**：输出须附责任主体与人工复核声明；不得生成违法违规、侵权或误导内容。
- 延伸：上架三铁律（国家+国际合规 / AI 特别友好 / 理念文化·强 IP）· 合规闸门 skill-release-gate。
