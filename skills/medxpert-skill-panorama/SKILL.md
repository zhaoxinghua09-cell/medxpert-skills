---
title: "medxpert-skill-panorama"
slug: medxpert-skill-panorama
displayName: "medxpert-skill-panorama"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medxpert-skill-panorama
description: "将 WorkBuddy Skill 生成 MedXpert + 公司 VI 风格的高清三角度全景图（价值/服务/能力）及评测类雷达图，并按 plugin 编号命名。何时用：需要给新 Skill 补上全景图上架物料"
author: 潘布达(Buda Pan)@SynomosAI
category: tooling
platforms: [workbuddy]
license: MIT
agent_created: true
---

# medxpert-skill-panorama

把任意 Skill 一键变成「价值 / 服务 / 能力」三角度高清全景图 + 评测类雷达图，统一 MedXpert 品牌 VI 与 plugin 编号命名。

## 触发场景

- 需要给新 Skill 补上全景图上架物料
- 需要批量重刷现有 Skill 的全景图
- 需要为评测/安全/稳定性类 Skill 生成雷达对比图
- 需要输出「本机全部技能」主全景总览图

## 前置依赖

- Python 3.13+（管理工作区脚本）
- Node.js 22 + playwright（`~/.workbuddy/binaries/node/workspace/node_modules/playwright`）
- Chromium（`ms-playwright/chromium-1234` 已存在）
- 本工作区脚本：`enumerate_skills.py` / `categorize_skills.py` / `generate_skill_panorama.py` / `render_pano.js`

## 标准约定

### plugin 编号

`PLG-<大类>-<NNN>`

- MED 医械注册 / BRD 品牌内容 / SEC 质量安全 / EVO AI进化 / LLM 本地模型 / OPS 平台工程 / RSR 搜索调研 / EFF 效率助手 / LIFE 生活工具 / PUB 发布上架

### 三角度文件名

- `PLG-<CAT>-<NNN>_价值全景.png`
- `PLG-<CAT>-<NNN>_服务全景.png`
- `PLG-<CAT>-<NNN>_能力全景.png`
- 评测类：`<PLG>_安全稳定性雷达.png`

### VI

- 页眉：深蓝 `#0E2A4D` → `#143C6B`
- 强调：橙 `#F04A23`
- 企业标准：医疗青 `#00C2A8`
- 品牌文案：MedXpert · 注册老炮 · medxpert.cn · 公众号 MedXpert/注册老炮

## 快速生成单个技能

```bash
cd <workbuddy-root>\<当前工作区>
python generate_skill_panorama.py medxpert-reg-hub
set NODE_PATH=~\.workbuddy\binaries\node\workspace\node_modules
~\.workbuddy\binaries\node\versions\22.22.2\node.exe render_pano.js
```

输出在 `pano_out/PLG-MED-007_价值全景.png` 等。

## 生成主全景总览图

```bash
python gen_panorama_svg.py
node render_pano.js
```

输出 `pano_out/master_panorama.png`（10 大类 + PLG 范围 + 自研数）。

## 生成评测雷达图

修改 `gen_panorama_svg.py` 中对应技能的维度与分值，然后：

```bash
python gen_panorama_svg.py
node render_pano.js
```

雷达必须包含三系列：实测(ours) / 行业基线 / 企业级标准。

## 高清参数

- SVG viewBox 680×900/920
- 2x 渲染 → PNG 1360×1800~1840

## 注意事项

- SVG 中 gradient stop-color 必须加引号，否则 chromium 白图
- 评测类雷达数据须来自真实测试；暂无实测时标注「待实测」
- 最终 PNG 需目视检查：无文字溢出、CTA 完整、颜色符合 VI
## 合规 · AI 生成内容标识（GB45438-2025）

> 本技能属于**公众面向内容生成（A 级）**，须严格执行以下合规加闸（依据《技能包国家合规适配方案 v20260911》铁律一）。

- **显式标识**：本技能产出的文本/图文/音视频等**均为 AI 生成内容**，对外发布时**须在显著位置标注"AI 生成"角标**（如文首/文末"本文由 AI 辅助生成"），不得冒充自然人创作。
- **隐式元数据**：按 GB45438-2025 在生成内容中嵌入机器可读标识（生成工具、生成时间、内容类型），便于平台识别与溯源。
- **备案评估**：涉及舆论属性或面向公众大规模传播的，须评估《生成式人工智能服务管理暂行办法》第十七条之**生成式 AI 服务备案**及《互联网信息服务算法推荐管理规定》之**算法备案**触发条件（以属地网信办认定为准，本声明非法律意见）。
- **人工复核与责任**：输出须附责任主体与人工复核声明；不得生成违法违规、侵权或误导内容。
- 延伸：上架三铁律（国家+国际合规 / AI 特别友好 / 理念文化·强 IP）· 合规闸门 skill-release-gate。
