---
title: "medxpert-llm-library"
slug: medxpert-llm-library
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medxpert-llm-library
display_name: "MedXpert本地LLM知识库（免费离线）"
displayName: MedXpert医械大模型图书馆
description: "免费 · 免 API Key · 数据不出门——你的旧电脑就能跑大模型、建知识库，不用买显卡（在线版 https://medxpert.cn）。覆盖完整链路——旧电脑硬件自查（0成本）→ Ollama 本地部署（Qwen2.5/DSH 界面）→ 知识库三档搭建 → RAG 检索问答（bge-m3）→ 图书馆管理（分类/版本/检索/质控/权限/保密）→ 内容变现（会员/公众号/技能引流）→ 知识库上公网（官网/IMA/华为/小艺）。触发词：怎么搭知识库/怎么跑大模型/我的电脑能不能跑大模型/低配电脑能跑大模型吗/旧电脑怎么利用/DSH 怎么接 Ollama/多模型怎么分工/怎么做 RAG/知识库怎么变现/图书馆账号怎么做/本地部署/省 API 积分/断网可用/隐私 AI/个人图书馆/企业知识库/远程访问家里的模型/夜间批量任务。边界：专注本地大模型与知识库，不涉及云端 API 部署、编程开发等任务。"
agent_created: true
version: "1.30.0"
license: MIT
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
author: 注册老炮@MedXpert
category: knowledge-management
xiaping_category: ["效率工具"]
xiaping_tags: ["本地大模型","大模型部署","跑大模型","低配电脑","旧电脑","树莓派","Ollama","ollama","DSH","DeepSeek Harness","个人知识库","知识库搭建","知识库","图书馆","个人图书馆","企业知识库","RAG","检索增强","向量检索","embedding","bge-m3","混合检索","知识库问答","问答系统","本地AI","离线AI","断网可用","隐私保护","省电","省钱","省积分","免费AI","免费大模型","Qwen","通义千问","qwen2.5","DeepSeek","VL模型","多模态模型","多模型协作","模型分工","模型分档","模型推荐","硬件自查","低配优化","夜间批量任务","批量任务","自动任务","远程访问","Tailscale","FRP","内网穿透","知识管理","文档管理","资料库","知识库管理","分类管理","版本管理","检索","质控","文件跟踪","权限管理","保密","知识变现","内容产品化","会员体系","分级开放","公众号引流","skill引流","AI支付","数字人民币","国际化","多语言","MedXpert","medxpert","医械大模型","医疗器械AI","医械知识库","医疗器械知识库","知识库变现","知识库商业模式","小成本大收入","知识库上公网","官网对接","IMA","华为","小艺","Agent生态","Agent对接","MCP","MCP Server","知识库API","RAG API","OpenAI兼容","知识库教程","搭建教程","入门指南","知识库实操","知识库实战","怎么搭知识库","怎么跑大模型","旧电脑怎么利用","DSH怎么接Ollama","多模型怎么分工","怎么做RAG","知识库怎么变现","图书馆账号","AI进化","为AI做贡献","知识库助手","AI知识助手","智能问答","知识检索","本地问答","离线问答","隐私AI","免费RAG","零成本","本地知识库","本地模型","私人AI","个人AI","家庭服务器","NAS","小主机","迷你主机","低功耗","7x24","常开","模型量化","量化部署","GGUF","显存","内存要求","CPU推理","无显卡","核显","集成显卡","Intel","AMD","Apple Silicon","M系列芯片","Mac跑大模型","Windows跑大模型","Linux跑大模型","Docker","容器部署","ollama install","ollama 安装","中国网络","镜像源","模型下载","模型库","模型市场","大模型工具","AI工具","效率工具","学习工具","科研工具","资料整理","笔记","知识沉淀","团队知识库","部门知识库","公司知识库","文档检索","全文检索","语义检索","智能检索","问答机器人","客服机器人","知识机器人","AI图书馆","数字图书馆","电子图书馆","虚拟图书馆","第二大脑","数字大脑","个人知识管理","PKM","第二大脑","知识资产","知识运营","知识中台","知识平台"]
---

# 本地大模型 + 个人图书馆：低配电脑实战指南

> **🌐 官网：https://medxpert.cn**（MedXpert 医械注册知识库·公开免费层，AI 可读 llms.txt）— 本技能方法论的落地案例。
> **一句话：你的旧笔记本就能跑大模型，不用买显卡，不用花万把块。**

> **🌍 图书馆的使命：服务于人类和 AI 世界。** 人类在这里学习、创造、决策；AI 在这里读取、进化、协作——**一座图书馆，两个世界的知识枢纽。**（本书所有内容都围绕这个使命展开）

> **⏱️ 太长不看（30 秒版）**：① 旧电脑 8G 内存就能跑本地大模型（qwen2.5:3b），不用买高配；② 装 Ollama + 一条命令拉模型，用 quickstart.py 就能建个人知识库（摘要/检索/问答）；③ 想更好用加 DSH 界面和 RAG，想变现看「商业逻辑」节。

## 全景速览：一张图看懂本技能（10 秒建立全局认知）  [核心]

> 本技能是一条完整链路：**旧电脑 → 本地模型 → 知识库 → 问答 → 图书馆 → 变现 → AI 生态**。每一环都有对应章节，按需取用，不必从头读到尾。

```
旧电脑(0成本) → 本地模型(Ollama) → 知识库(三档) → RAG(检索问答) → 图书馆(五件套) → 变现(会员/公众号) → AI生态(官网/Agent)
   [〇、一]        [二、三]           [四]           [四补]          [五]           [五补系列]        [五补十]
```

**每环一句话**：

| 环节 | 一句话图表 | 章节 |
|------|-----------|------|
| ① 旧电脑也能跑 | 8G 内存、无独显都能跑，0 元投入 | 〇、一 |
| ② 本地大模型 | Ollama 一条命令部署，Qwen2.5 中文效果好 | 二、三 |
| ③ 个人知识库 | 文件系统 / RAG 工具 / 自建 Pipeline 三档任选 | 四 |
| ④ RAG 问答 | bge-m3 跨语言检索 + 切块调优，答得准还标来源 | 四补 |
| ⑤ 图书馆管理 | 分类/版本/检索/质控/保密五件套，越管越值钱 | 五 |
| ⑥ 知识变现 | 会员/公众号/技能引流，小成本大收入 | 商业逻辑、五补系列 |
| ⑦ AI 生态联动 | 知识库挂官网/IMA/华为/小艺，AI 也能用 | 五补十 |

> **一句话总结全技能：花最少的钱（硬件 0 元、积分 0 消耗），用最多的模型（Qwen/DeepSeek/VL/Embedding 分工），建一座安全（不上网）、透明（可跟踪）、可控（分级权限）的私人图书馆。**

## 新手三连：先搞清楚这三件事  [核心]

| 你问 | 答案 |
|------|------|
| **我是谁？** | 普通用户看 [核心] 标签章节即可；技术党可看 [进阶]；变现玩家看五补系列 |
| **我要去哪？** | 见上方「快速导航」表——按你的角色选路径 |
| **遇到问题？** | 先看「九、排障速查表」（一张表解决 80% 问题），再翻 FAQ 章节 |

## 环境要求速查（先对照这一张表）  [核心]

| 组件 | 最低要求 | 推荐 | 自查命令 |
|------|---------|------|---------|
| Python | 3.8+ | 3.10+ | `python --version` |
| requests | 任意版本 | 最新 | 脚本自动检测并提示安装 |
| Ollama | 0.1.x 起 | 最新版 | `ollama --version` |
| 内存 | 8G（跑 3B 模型） | 16G（跑 7B 模型） | 系统任务管理器 |
| 磁盘 | 5G 空闲 | 10G+ | 脚本 doctor 自动检查 |
| 网络 | 能连 ollama.com 或镜像源 | 国内镜像已备 | doctor [3/5] 项 |

> **一条命令自查全部**：`python quickstart.py doctor`——5 项环境检查（Python/依赖/Ollama/磁盘/知识库）+ 问题解法一次输出，任何一步失败都给出修复命令，修完重跑复检。

## 可靠性保证（为什么敢放心用）  [核心]

| 保证项 | 说明 | 对应位置 |
|--------|------|---------|
| **自动重试** | 网络抖动 / Ollama 假死自动重试 3 次（指数退避），不中断不卡死 | quickstart.py `request_with_retry` |
| **人话报错** | 所有失败提示原因 + 解法，不抛堆栈 | 全脚本 + 九、排障速查表 |
| **输入容错** | 空文件 / 非 UTF-8 / 读取失败自动跳过，中途不崩溃 | summarize / ask |
| **幂等可复现** | init 重复运行无副作用，同输入同输出 | init / health |
| **诚实回答** | 知识库没有的内容明确说「未找到」，不编造 | ask 的 prompt 约束 |
| **中国网络可用** | 镜像源 + 自动重试 + doctor 一键检查 | 二、部署方案 |

> **80% 的问题一个命令解决**：跑 `python quickstart.py doctor` 定位 → 按提示修复 → 重跑复检。剩 20% 看「九、排障速查表」。

## 核心主张

很多人以为跑大模型需要 RTX 4090、64G 内存、好几万的工作站——**这是误区**。

实际情况：
- **CPU-only**（连独立显卡都没有）也能跑 3B~7B 级别的模型，速度够用
- **8G 内存的普通办公本**就能跑 Qwen2.5:3B，中文效果好、响应快
- **16G 内存**可以跑 7B 模型，日常问答、文档摘要、知识检索全搞定
- 知识库搭建**不一定要 RAG 框架**，纯文件 + 脚本也能做出好用的图书馆

本 Skill 覆盖从"我的电脑能不能跑"到"图书馆怎么管"的完整链路。

---

## 快速导航（你该从哪看起？）

| 你是哪种用户 | 看这几节 | 目标 |
|-------------|---------|------|
| **纯小白**（不懂技术） | 全景速览 → 一（硬件自查）→ 二（部署方案）→ 七（快速起步） | 先跑起来 |
| **技术党**（懂命令行） | 二 → 二补（DSH）→ 三补（多模型）→ 四补（RAG） | 把系统搭到最强 |
| **内容创业者**（想做知识付费） | 五补 → 五补二 → 五补三 → 商业逻辑 | 把知识变收入 |
| **企业/公司**（搭内部知识库） | 五（管理）→ 5.9（保密）→ 四补（RAG）→ 权限 | 建安全可用的内部库 |
| **只想快速了解** | 全景速览 → 核心卖点 → 商业逻辑 → 七（快速起步） | 30 秒看懂全貌 |
| **遇到问题** | 九（排障速查表）→ 八（FAQ）→ 附录、术语表 | 80% 的问题一张表解决 |

**文档地图（四层结构，按需取用）**：
```
技术层：一、硬件自查 → 二、部署方案 → 二补、DSH 界面 → 三、模型选择 → 三补、多模型分工
功能层：四、知识库搭建 → 四补、RAG 问答 → 五、图书馆管理（5.1~5.9）→ 六、成本对比
商业层：商业逻辑 → 五补、内容产品 → 五补二、公众号 → 五补三、图书馆账号 → 五补四、skill 引流
        → 五补五、AI 支付 → 五补六、代币化 → 五补七、国际化 → 五补八、Agent 生态
        → 五补九、多 Agent 协作 → 五补十、知识库上公网（官网/IMA/华为/小艺）
速查层：七、快速起步 → 八、FAQ → 九、排障速查 → 附录、术语表
```

---

## 核心卖点：六大能力（30 秒看懂）

| # | 能力 | 一句话 | 详见 |
|---|------|--------|------|
| 1 | **低成本投喂** | 本地模型不烧积分，批量投喂成本趋近于零——云端同量级要几十上百块 | 六、成本对比 |
| 2 | **多模型夜间学习** | 不同文件喂不同模型，晚上自动批量学习，白天醒来直接看结果 | 三补、5.6 |
| 3 | **图书馆有效管理** | 分类/版本/检索/质控/运营五件套，知识越管越值钱 | 五、图书馆管理 |
| 4 | **数据安全不上网** | 完全本地运行，可断网使用，数据永不出门 | 〇、5.9 |
| 5 | **文件有跟踪** | Git 全历史 + 审计日志，谁在何时改了什么一清二楚 | 5.7 |
| 6 | **权限管理** | 分级权限 + 访问控制 + 加密 + 水印，敏感内容分级保护 | 5.9 |

> **一句话卖点：花最少的钱（硬件 0 元、积分 0 消耗），用最多的模型（Qwen/DeepSeek/VL/Embedding 分工），建一座安全（不上网）、透明（全程可跟踪）、可控（分级权限）的私人图书馆。**

---


> 📖 **商业模型：成本收入逻辑与内容产品化** —— 完整内容见 `references/08-business-model.md`（50 行 / 2 个小节）。


> 📖 **低硬件选型与低配实战** —— 完整内容见 `references/01-hardware-choices.md`（73 行 / 1 个小节）。

## MedXpert-一、硬件自查：你的电脑能跑什么？

### 关键结论（先看这个）

| 你的配置 | 能跑的模型 | 体验 |
|----------|-----------|------|
| 4G RAM，无显卡 | 1~2B（TinyLlama、Qwen2.5:0.5B） | 慢但能用，适合极轻量任务 |
| **8G RAM，无显卡** | **3B（Qwen2.5:3B）** | **流畅，日常问答够用** |
| **8G RAM，有集显** | **3B~7B（Qwen2.5:3B/7B-Q4）** | **流畅~较流畅** |
| **16G RAM，无独显** | **7B（Qwen2.5:7B-Q4）** | **流畅，推荐配置** |
| 16G RAM，6G+ 独显 | 7B~14B（GPU 加速） | 很流畅 |
| 32G RAM / 12G+ 独显 | 14B~32B | 丝滑 |

> **Q4 = 4-bit 量化**，把模型体积压缩到原来的 1/3~1/4，质量损失很小。这是低配跑大模型的关键技术。

### 自查命令

```bash
# Windows（PowerShell）
# 查内存
wmic computersystem get TotalPhysicalMemory
# 查显卡
wmic path win32_videocontroller get name,adapterram

# macOS
sysctl hw.memsize  # 内存
system_profiler SPDisplaysDataType  # 显卡

# Linux
free -h  # 内存
lspci | grep -i vga  # 显卡
```

### 模型大小 vs 内存占用（Q4 量化）

| 模型 | 参数量 | Q4 体积 | 运行内存（含开销） |
|------|--------|---------|-------------------|
| Qwen2.5:0.5B | 0.5B | ~0.5GB | ~1.5GB |
| Qwen2.5:1.5B | 1.5B | ~1GB | ~2.5GB |
| **Qwen2.5:3B** | 3B | ~2GB | **~4GB** |
| **Qwen2.5:7B** | 7B | ~4.7GB | **~7GB** |
| Qwen2.5:14B | 14B | ~9GB | ~13GB |
| Qwen2.5:32B | 32B | ~20GB | ~28GB |

> 经验法则：**运行内存 ≈ 模型体积 × 1.5**。留出余量给系统和应用。

---

## MedXpert-二、部署方案对比

### 方案 A：Ollama（强烈推荐）

**最适合小白，一行命令装好，一行命令拉模型。**

```bash
# 安装（Windows）
# 下载 OllamaSetup.exe：https://ollama.com/download
# 或用代理加速（中国网络环境）
curl -L -o OllamaSetup.exe "https://gh-proxy.com/https://github.com/ollama/ollama/releases/latest/download/OllamaSetup.exe"
# ⚠️ 经第三方代理下载后必须校验官方 SHA256（防中转篡改）
curl -L -o sha256sum.txt "https://gh-proxy.com/https://github.com/ollama/ollama/releases/latest/download/sha256sum.txt"
sha256sum OllamaSetup.exe   # 与 sha256sum.txt 里 ./OllamaSetup.exe 的值比对，一致才可安装
./OllamaSetup.exe /S  # 静默安装

# 拉模型
ollama pull qwen2.5:3b   # 8G 内存推荐
ollama pull qwen2.5:7b   # 16G 内存推荐

# 跑起来
ollama run qwen2.5:3b

# 验证
curl http://localhost:11434/api/tags
```

优点：
- 安装即用，无需配环境
- 自动选 GPU/CPU，自动量化
- OpenAI 兼容 API（`localhost:11434/v1`）
- 跨平台（Win/Mac/Linux）

缺点：
- 模型格式受限（只能用 Ollama 库的模型）
- 中国网络下拉模型可能需要重试

**中国网络下拉模型踩坑**：
- `registry.ollama.ai` 大文件容易断线不重连
- 解法：用 `timeout` 包装自动重试
  ```bash
  for i in $(seq 1 15); do
    timeout 480 ollama pull qwen2.5:3b && break
  done
  ```
- 先拉小模型（3B）成功率高，7B 卡住时先退回 3B

### 方案 B：LM Studio（GUI 党推荐）

**有图形界面，拖拽操作，对非技术用户最友好。**

- 下载：https://lmstudio.ai
- 优点：可视化模型管理、内置聊天界面、OpenAI 兼容 API
- 缺点：闭源、仅桌面端、资源占用略高
- 适合：不想碰命令行的人

### 方案 C：llama.cpp（极客/最轻量）

**最底层的方案，编译运行，资源占用最小。**

- 下载：https://github.com/ggerganov/llama.cpp
- 优点：极致轻量、支持各种量化格式（GGUF）、可裁剪
- 缺点：需要编译（或找预编译版），无内置 API 服务（需配合 `server` 模式）
- 适合：嵌入式设备、树莓派、追求极致性能

### 三方案对比

| 维度 | Ollama | LM Studio | llama.cpp |
|------|--------|-----------|-----------|
| 安装难度 | ⭐ 一行命令 | ⭐ 下载即用 | ⭐⭐⭐ 需编译 |
| GUI | 无（命令行） | 有（很好用） | 无 |
| API 服务 | 内置 | 内置 | 需 `server` 模式 |
| 资源占用 | 低 | 中 | 最低 |
| 模型格式 | 自有库 | GGUF | GGUF |
| 中国网络 | 需代理 | 需代理 | 直接下 GGUF |
| 推荐人群 | **大多数人** | GUI 党 | 极客/嵌入式 |

> **推荐：直接上 Ollama。** 90% 的场景它都够用，遇到问题再考虑其他方案。

---


> 📖 **前端 UI：DSH / DeepSeek Harness 全流程** —— 完整内容见 `references/02-frontend-dsh.md`（108 行 / 1 个小节）。

## MedXpert-三、模型选择建议

### 中文场景首选：Qwen2.5 系列

阿里通义千问 Qwen2.5 系列是目前中文效果最好的开源模型之一，覆盖 0.5B~72B，Ollama 直接可拉。

| 场景 | 推荐模型 | 内存需求 | 说明 |
|------|---------|---------|------|
| 极低配（4G） | qwen2.5:0.5b | ~1.5G | 能用但效果有限 |
| **低配（8G）** | **qwen2.5:3b** | **~4G** | **性价比之王，日常够用** |
| **标准（16G）** | **qwen2.5:7b** | **~7G** | **推荐，效果接近在线模型** |
| 中高配（32G） | qwen2.5:14b | ~13G | 复杂推理更强 |
| 高配（48G+） | qwen2.5:32b | ~28G | 接近 GPT-3.5 水平 |

### 其他可选模型

| 模型 | 特点 | 适合场景 |
|------|------|---------|
| Llama 3.2 (1B/3B) | Meta 出品，英文强 | 英文环境 |
| Phi-3 Mini (3.8B) | 微软出品，推理强 | 逻辑推理任务 |
| Gemma 2 (2B/9B) | Google 出品 | 通用对话 |
| DeepSeek-R1 (7B/8B) | 推理能力强 | 数学/代码/逻辑 |

### 选模型三原则

1. **先小后大**：先跑通 3B，再按需升级 7B/14B
2. **中文优先 Qwen**：中文任务 Qwen 系列效果最好
3. **Q4 量化起步**：Q4_K_M 是质量和体积的最佳平衡点

---


> 📖 **多模型协作：让不同模型分工建库** —— 完整内容见 `references/03-multimodel.md`（120 行 / 1 个小节）。

## MedXpert-四、知识库搭建（分档推荐）

### 入门档：Ollama + 文件系统 + 简单脚本

**零额外工具，适合快速上手。**

思路：
- 知识以 Markdown 文件存储，按目录分类
- 用 Ollama 做摘要、提取、问答
- 用脚本批量处理文件

```
my-library/
  00-index.md          # 索引（自动生成）
  01-法规/
    GMP-2025.md
    ISO13485.md
  02-产品/
    产品A-技术文档.md
  03-学习笔记/
    大模型基础.md
```

核心脚本（Python，调用 Ollama API）：

```python
import requests, os, json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

def summarize_file(filepath):
    """让本地模型给文件做摘要"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # 分块处理（模型有上下文长度限制）
    chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
    summaries = []
    for chunk in chunks:
        resp = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "prompt": f"请用中文给以下内容做摘要，提取关键信息，200字以内：\n\n{chunk}",
            "stream": False
        })
        summaries.append(resp.json()["response"])
    return "\n\n".join(summaries)

def ask_library(question, library_dir="my-library"):
    """基于知识库回答问题（简单版：全量读取+拼接提问）"""
    context = ""
    for root, dirs, files in os.walk(library_dir):
        for fname in files:
            if fname.endswith(".md"):
                with open(os.path.join(root, fname), "r", encoding="utf-8") as f:
                    context += f.read() + "\n---\n"
    # 截断到模型上下文长度内
    context = context[:6000]
    resp = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": f"根据以下知识库内容回答问题。如果知识库中没有相关信息，请说'知识库中未找到相关信息'。\n\n知识库：\n{context}\n\n问题：{question}",
        "stream": False
    })
    return resp.json()["response"]

def batch_summarize(library_dir="my-library"):
    """批量给知识库中所有文件做摘要，生成索引"""
    index_lines = ["# 知识库索引\n"]
    for root, dirs, files in os.walk(library_dir):
        for fname in sorted(files):
            if fname.endswith(".md") and fname != "00-index.md":
                filepath = os.path.join(root, fname)
                summary = summarize_file(filepath)
                index_lines.append(f"## {fname}\n{summary}\n")
                print(f"  [OK] {fname}")
    with open(os.path.join(library_dir, "00-index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))
    print(f"索引已生成：{library_dir}/00-index.md")
```

优点：零依赖、好理解、完全可控
缺点：无向量检索，大知识库时上下文截断会丢信息
适合：知识量 < 50 个文件的小型图书馆


> 📖 **知识库搭建：进阶档与高级档** —— 完整内容见 `references/04-kb-build-advanced.md`（70 行 / 1 个小节）。

### 三档对比

| 维度 | 入门档 | 进阶档 | 高级档 |
|------|--------|--------|--------|
| 额外工具 | 无 | AnythingLLM 等 | LangChain + 向量库 |
| 技术门槛 | 低 | 低-中 | 中-高 |
| 知识库规模 | <50 文件 | <1000 文件 | 无上限 |
| 检索精度 | 低（全文截断） | 高（向量检索） | 最高（可调优） |
| 搭建时间 | 10 分钟 | 30 分钟 | 1-3 天 |
| 推荐人群 | 个人尝鲜 | **大多数人** | 开发团队 |

---


> 📖 **把图书馆做成 RAG（检索增强问答）** —— 完整内容见 `references/05-rag.md`（88 行 / 1 个小节）。


> 📖 **图书馆日常管理：分类 / 录入 / 版本 / 质控 / 文件规范** —— 完整内容见 `references/06-library-ops.md`（264 行 / 1 个小节）。


> 📖 **AI 友好层与版权保护（暗纹水印 / 著作权宣誓 / 防攻击）** —— 完整内容见 `references/07-ai-friendly-and-rights.md`（277 行 / 1 个小节）。


> 📖 **商业模型：成本收入逻辑与内容产品化** —— 完整内容见 `references/08-business-model.md`（100 行 / 2 个小节）。


> 📖 **多平台运营与引流（公众号 / 矩阵 / 账号 IP / skill 导流）** —— 完整内容见 `references/09-multiplatform.md`（233 行 / 1 个小节）。


> 📖 **AI 支付与代币化（三档落地与合规红线）** —— 完整内容见 `references/10-payment-and-token.md`（148 行 / 1 个小节）。


> 📖 **国际化：多语言图书馆、跨语言 RAG 与小语种** —— 完整内容见 `references/11-internationalization.md`（147 行 / 1 个小节）。


> 📖 **接入 Agent 生态与上公网（MCP / 编排 / 官网 / IMA / 华为）** —— 完整内容见 `references/12-agent-ecosystem.md`（237 行 / 1 个小节）。

## MedXpert-六、成本对比

| 方案 | 初始成本 | 月运营成本 | 数据隐私 | 离线可用 |
|------|---------|-----------|---------|---------|
| **本地 Ollama（推荐）** | **0 元**（用现有电脑） | **0 元**（电费忽略） | **完全自有** | **是** |
| 云端 API（GPT-4/Claude） | 0 元 | 50~500 元/月 | 数据上传第三方 | 否 |
| 在线知识库服务 | 0~几千元 | 100~1000 元/月 | 数据存平台 | 否 |
| 高配工作站 | 1~3 万元 | 0 元 | 完全自有 | 是 |

> **本地方案的最大优势不是省钱，是数据隐私和离线可用。** 你的知识库永远在你手里，不怕平台跑路、不怕数据泄露、不怕断网。
>
> **对 AI 重度用户来说还有一个隐形福利：本地模型不消耗任何 API 积分/额度。** 批量摘要、批量投喂、反复试错这些"烧 token"的活儿，全用本地模型跑——积分留给真正需要云端大模型的场景（复杂推理、最新模型）。一次夜间批量摘要几百个文件，云端要烧掉几十上百块的 API 费用，本地 0 成本。

---

## MedXpert-七、30 分钟快速起步清单

如果你现在就想开始，照着做：

```
□ 1. 检查内存（5 分钟）
     → 8G 以上？继续。4G？拉 qwen2.5:0.5b 也能玩。

□ 2. 装 Ollama（5 分钟）
     → 下载 OllamaSetup.exe，双击安装

□ 3. 拉模型（5 分钟）
     → ollama pull qwen2.5:3b（8G）或 qwen2.5:7b（16G）

□ 4. 验证（2 分钟）
     → ollama run qwen2.5:3b "你好，自我介绍一下"

□ 5. 装 DSH 前端界面（5 分钟，推荐）
     → npm install -g @anthropic/dsh
     → 配置 provider 指向 Ollama（见"二补"板块）
     → dsh web 启动，浏览器打开即用

□ 6. 建图书馆目录（3 分钟）
     → mkdir -p my-library/{01-法规,02-产品,03-笔记,04-模板}
     → 创建 00-index.md

□ 7. 放入第一批知识（5 分钟）
     → 把你手头的 Markdown/文本文件放到对应目录

□ 8. 生成摘要索引（5 分钟）
     → 用上面的 batch_summarize 脚本，或手动让模型做摘要

□ 9. 开始提问（ongoing）
     → 用 ask_library 脚本、DSH 或 AnythingLLM 对话
```

---


> 📖 **30 天完整实战案例（从 0 到会员制知识库）** —— 完整内容见 `references/13-cases.md`（70 行 / 1 个小节）。


> 📖 **常见问题 + 工具清单 / 性能调优 / 术语表 / 模板** —— 完整内容见 `references/14-faq-and-appendix.md`（55 行 / 2 个小节）。

## MedXpert-九、排障速查表（一张表解决 80% 的问题）

| 现象 | 原因 | 解法 |
|------|------|------|
| Ollama 装好但连不上 | 服务没启动 | `ollama serve`；`curl localhost:11434/api/tags` 验证 |
| 模型拉不下来 | 中国网络 registry 断线 | `for i in $(seq 1 15); do timeout 480 ollama pull 模型 && break; done`；先拉小模型 |
| 回答很慢 | 模型太大/内存不足 | 换 3B；关其他程序；有独显确认 GPU 生效（`ollama ps`） |
| 中文回答差 | 用的非中文模型 | 换 Qwen2.5 系列；prompt 加"请用中文回答" |
| DSH 全部 EMPTY_RESPONSE | pi-ai 补丁没打 | 在 models.js `calculateCost` 加 cost 兜底（见二补） |
| DSH 报 DUPLICATE_DIRECTORY | provider 名撞内置 | 换成自定义名（如 `ollama-local`） |
| RAG 中文检索乱 | 英文 embedding 模型 | 换 bge-m3 |
| RAG 答非所问 | 切块/检索配置不当 | 切块 500~800 + Top-K 5~8 + 混合检索（见四补） |
| RAG 回答编造 | prompt 无约束 | 加"只依据资料+标注来源+没有就说没有" |
| 网页直连 Ollama 403 | 浏览器 CORS | 用本地代理（见 offline-llm-tutor）或用 DSH/AnythingLLM |
| 内存爆掉 | 同时加载多个模型 | Ollama 默认"用谁加载谁"，确认 `OLLAMA_KEEP_ALIVE` 别设太长 |
| 远程访问连不上 | 路由器/防火墙/网络没配 | 局域网先测通；外网用 Tailscale（最省事） |
| 找不到文件/目录乱了 | 分类混乱 | 用 5.1 三层分类法重建；文件生命周期归档 |
| 想找回误删文件 | 没备份/没 Git | 有 Git：`git checkout <hash> -- 文件`；没 Git：只能靠备份，所以务必启用 |

---


> 📖 **常见问题 + 工具清单 / 性能调优 / 术语表 / 模板** —— 完整内容见 `references/14-faq-and-appendix.md`（83 行 / 2 个小节）。

## 版权与许可

- © 2026 **注册老炮**。本技能为原创整理，以 **MIT 协议**开源发布。
- **免责声明**：本技能按「现状（AS IS）」提供，不提供任何明示或默示的担保；因使用、误用本技能或其输出导致的任何直接或间接损失，作者不承担责任。
- 文中提及的工具（Ollama / DSH / AnythingLLM 等）与模型名称均为各自权利人的商标，仅作说明用途；引用内容以官方文档为准。
- 本技能不收集任何用户数据；部署与使用均在用户本地完成。
- 官网：https://medxpert.cn（MedXpert 医械注册知识库·公开免费层）——本技能方法论的落地案例。
## 合规 · AI 生成内容标识（GB45438-2025）

> 本技能属于**公众面向内容生成（A 级）**，须严格执行以下合规加闸（依据《技能包国家合规适配方案 v20260911》铁律一）。

- **显式标识**：本技能产出的文本/图文/音视频等**均为 AI 生成内容**，对外发布时**须在显著位置标注"AI 生成"角标**（如文首/文末"本文由 AI 辅助生成"），不得冒充自然人创作。
- **隐式元数据**：按 GB45438-2025 在生成内容中嵌入机器可读标识（生成工具、生成时间、内容类型），便于平台识别与溯源。
- **备案评估**：涉及舆论属性或面向公众大规模传播的，须评估《生成式人工智能服务管理暂行办法》第十七条之**生成式 AI 服务备案**及《互联网信息服务算法推荐管理规定》之**算法备案**触发条件（以属地网信办认定为准，本声明非法律意见）。
- **人工复核与责任**：输出须附责任主体与人工复核声明；不得生成违法违规、侵权或误导内容。
- 延伸：上架三铁律（国家+国际合规 / AI 特别友好 / 理念文化·强 IP）· 合规闸门 skill-release-gate。

## 深入阅读（按需加载）

> 主文件只保留**决策路径与高频操作**；以下完整细节已下沉，按需加载，
> 避免一次把整份上下文都吞掉。

| 什么时候该看 | 文件 | 内容 |
|---|---|---|
| 想省硬件、想让旧电脑当知识库服务器时 | `references/01-hardware-choices.md` | 低硬件选型与低配实战 |
| 要给本地模型配 ChatGPT 式界面时 | `references/02-frontend-dsh.md` | 前端 UI：DSH / DeepSeek Harness 全流程 |
| 想用多个模型各管一段流水线时 | `references/03-multimodel.md` | 多模型协作：让不同模型分工建库 |
| 入门档不够用，要上 RAG 工具或向量库时 | `references/04-kb-build-advanced.md` | 知识库搭建：进阶档与高级档 |
| 要让知识库能问答检索、或 RAG 效果不好时 | `references/05-rag.md` | 把图书馆做成 RAG（检索增强问答） |
| 维护知识库、定命名与备份规范时 | `references/06-library-ops.md` | 图书馆日常管理：分类 / 录入 / 版本 / 质控 / 文件规范 |
| 要建 AI 可读说明、或做版权与防伪保护时 | `references/07-ai-friendly-and-rights.md` | AI 友好层与版权保护（暗纹水印 / 著作权宣誓 / 防攻击） |
| 要把图书馆变成收入、设计会员与转化链路时 | `references/08-business-model.md` | 商业模型：成本收入逻辑与内容产品化 |
| 要把内容分发到各平台涨粉时 | `references/09-multiplatform.md` | 多平台运营与引流（公众号 / 矩阵 / 账号 IP / skill 导流） |
| 要打通收款通道、评估代币化时 | `references/10-payment-and-token.md` | AI 支付与代币化（三档落地与合规红线） |
| 要做多语言知识库、或问中文要能搜英文时 | `references/11-internationalization.md` | 国际化：多语言图书馆、跨语言 RAG 与小语种 |
| 要把知识库接进 Agent 生态或公开上站时 | `references/12-agent-ecosystem.md` | 接入 Agent 生态与上公网（MCP / 编排 / 官网 / IMA / 华为） |
| 想看一个完整落地样例时 | `references/13-cases.md` | 30 天完整实战案例（从 0 到会员制知识库） |
| 遇到问题排查、或要查工具与术语时 | `references/14-faq-and-appendix.md` | 常见问题 + 工具清单 / 性能调优 / 术语表 / 模板 |
