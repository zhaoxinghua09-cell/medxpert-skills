---
title: "medxpert-brand-assets"
slug: medxpert-brand-assets
displayName: "medxpert-brand-assets"
category: "general"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medxpert-brand-assets
description: MedXpert 品牌视觉资产生产流水线（logo/头像/封面/二维码/公众号模板包/名片）。以主logo为唯一源，参数配置化驱动，多方案并行+预览总览+版本归档。触发词：生成品牌素材、做头像、做封面、做二维码、改logo、品牌素材、medxpert-brand-assets。
agent_created: true
---

# MedXpert 品牌视觉资产生产流水线

> 沉淀：2026-08-16（视觉资产 V0 定稿复盘）· 归属：记忆管家/品牌视觉
> 目标：**改配置即可改效果，一次多方案，旧版可追溯**——减少与用户的往返修改。

## 一、核心文件

| 文件 | 路径 | 用途 |
|---|---|---|
| 主 logo 源（唯一源） | `<workbuddy-root>/Claw/AI集团视觉资产/_brand/logo_source_v20260816.png` | 所有素材的 logo 来源（SRC_LOGO） |
| logo 透明版 | `_brand/logo_transparent_v20260816.png` | flood-fill 去白底+白字纯白化，叠场景用 |
| 矢量母版 | `_brand/logo-master.svg` | SVG 内嵌主 logo PNG，导出用 |
| 品牌配置 | `<workbuddy-root>/Claw/知识库工具/brand_config.json` | **改这里即可改效果，不用改代码** |
| 素材生成器 | `<workbuddy-root>/Claw/知识库工具/promo_gen.py` | 头像/封面/二维码/公众号包/名片 |
| 版本清单 | `_brand/LOGO-VERSIONS.md` | 版本表 + 变更 SOP + 红线 |
| 版本归档 | `_brand/versions/V{n}_{日期}/` | 每个定稿版只读快照 |

## 二、设计规范（V0 定稿）

| 元素 | 规范 |
|---|---|
| 主 logo | 红胶囊渐变 #FF4A36→#E8281B + 白色完整英文 MedXpert（斜体800） |
| 头像 | 浅蓝渐变 `#E8F1FB→#D5E6F8→#C0D8F4` + 白卡(圆角36,436×400) + logo居中(380px) + 左上MEDXPERT™ + 右下红平台标签 |
| 封面 | 同色系浅蓝渐变 + 白卡大logo + 品牌口号 |
| 二维码 | 渐变蓝 #2D6CDF→#16325C + 中心白卡完整logo + 白字纯白 |
| 平台 | 微信/小红书/抖音/X/LinkedIn + 公众号 + 名片 |

## 三、使用流程

### 1. 生成全部素材
```bash
# 默认 env（无 qrcode）：
python <workbuddy-root>/Claw/知识库工具/promo_gen.py

# qrcode/封面/公众号包需要 default env（含 qrcode/PIL）：
~/.workbuddy/binaries/python/envs/default/Scripts/python.exe <workbuddy-root>/Claw/知识库工具/promo_gen.py
```

### 2. 只生成某类
```bash
python promo_gen.py --avatar   # 头像（5平台）
python promo_gen.py --cover    # 封面（5平台）
python promo_gen.py --qr       # 二维码（官网+公众号占位）
python promo_gen.py --wechat   # 公众号模板包
python promo_gen.py --misc     # 周边物料（名片）
```

### 3. 改需求 → 改配置
编辑 `brand_config.json` 即可，**不要改 promo_gen.py 代码**：
- `avatar_bg`：头像背景渐变
- `cover_bg`：封面背景渐变
- `qr_gradient_start/end`：二维码渐变蓝
- `avatar.*`：白卡位置/尺寸/圆角/logo 宽
- `cover.*`：logo 占比/口号字号
- `qr.*`：二维码数据/纠错/logo 比例

改完重新跑生成即可。

### 4. 换 logo → 版本化流程
```
1. 存新源图 _brand/logo_source_vYYYYMMDD.png
2. flood-fill 去白底 + 白字纯白化 → logo_transparent_vYYYYMMDD.png
3. 更新 logo-master.svg（内嵌新 PNG）
4. promo_gen.py 重新生成全部
5. 确认满意 → 归档 versions/V{n}_{日期}/（复制全部资产）
6. 更新 LOGO-VERSIONS.md 版本清单（V0→V1→V2…）
7. 旧版保留不删
```

## 四、防坑经验（血的教训，务必遵守）

### 坑 1：CSS 百分号 vs Python % 格式化
`linear-gradient(...,0%,100%)` 中的 `%` 会被 Python `%s` 格式化误当格式符。
**解法**：模板用 `.replace("__TOKEN__", 值)` 或普通字符串拼接，不要把 `%` 塞进 `%` 格式串。

### 坑 2：Python 三引号截断
`data:image/png;base64,"""` 中的 `"""` 会被识别为字符串结束符 → 后面 `/>` 的 `/` 字符窜入 base64 末尾，破坏编码，图片渲染空白。
**解法**：base64 用普通字符串拼接（`"<img src='data:image/png;base64," + b64 + "'>"`），或 `.replace("__LOGO__", b64)`。

### 坑 3：白底图贴白卡 = 一片白
源 logo 常是白底图（白色占 80%），直接贴白卡后白+白融合，视觉只剩中间一条。
**解法**：flood-fill 从四边白色像素灌透明（保留胶囊内白字，被红边界隔开不灌）→ 内容 bbox 裁剪。

### 坑 4：白字不纯白显脏
白字边缘混入红色渐变抗锯齿（RGB ~248,224,224 非纯白）。
**解法**：白字纯白化——`if r>200 and g>185 and b>185: px=(255,255,255,a)`。

### 坑 5：Logo 形状不一致
同一份 logo 源才能保证形状一致。头像用 SRC_LOGO 完整版，二维码若用透明裁剪版（只红胶囊）→ 比例完全不同（3.78 vs 6.71）。
**解法**：所有素材统一用 SRC_LOGO 完整版；透明版仅用于不需要白底的叠加场景。

### 坑 6：宽高比控制
扁胶囊 logo（299×79, 比例 3.78）按高度 resize 会导致宽度爆炸超界。
**解法**：宽度优先 `max_w = 画布边长 × 比例`，再反推高度。

## 五、多方案并行 + 预览（减少往返）

设计类需求（头像/封面/章/配色）默认出 **3-10 个方案**，合成一张对比总览 HTML + 截图，配推荐理由，让用户"选方案"而不是"挑毛病"。

快速出多方案：
```python
# 在脚本里循环改 bg 生成 10 个变体 → 合成总览页
shots = []
for bg in ["浅蓝","米黄","浅粉","薄荷绿","蓝网格","浅紫","暖橙","灰点阵","品牌红","科技蓝"]:
    png = shot(mk(label, bg))
    shots.append(png)
# 生成 HTML 总览 + Chrome 截图
```

## 六、验证二维码可识别
- 中心 logo 覆盖 ≤ 30% 面积（H 纠错容错）
- 渐变用深色（如 #2D6CDF→#16325C），保持对比度
- 生成后建议真机扫码验证

## 七、关联资产
- 品牌工具：`<workbuddy-root>/Claw/知识库工具/brand_tools.py`（generate/scan/inject/pdfcheck）
- 文档水印：`brand_tools.py inject --file x --kind=library`
- 版本管理：`_brand/LOGO-VERSIONS.md`
- 复盘文档：`<workbuddy-root>/Claw/今日工作复盘与流程改进.md`
