---
title: "medxpert-l1-batch-study"
compliance_review: "待核验：上架三铁律 ①国家/国际合规 ②AI特别友好 ③理念文化传播+强IP；发布前由 skill-release-gate 审查"
name: medxpert-l1-batch-study
display_name: "MedXpert文档批量精读器"
slug: medxpert-l1-batch-study
displayName: MedXpert·本地模型批量精读（L1）
description: "用 DSH 任务桥 + 本地 qwen3.5:4b 批量精读一堆文档/知识库枢纽，逐份产出结构化摘要（核心 3 条 + 表格要点 + 疑点）并汇总疑点总表。覆盖任务桥 inbox/outbox 投递-回收、qwen3 think:false 修复、桥超时双修复、后台回收兜底。省 API 积分、断网可用、可复现。何时用：「把这一批文档/枢纽批量精读一遍」「L1 全库精读」「本地模型跑一遍知识库」"
description_zh: 本地大模型 + DSH 任务桥批量精读知识库：投递 inbox → 本地 qwen3 精读 → 回收 outbox → 落盘结构化摘要 + 疑点总表，含两处必做修复（qwen3 thinking 关闭、桥超时 120s→300s）与失败自动重投兜底。
description_en: Batch deep-reading of a document/knowledge-base corpus via the DSH task bridge and a local qwen3.5:4b model — dispatch to inbox, local LLM reading, recover from outbox, persist structured summaries + a consolidated doubt list. Includes two mandatory fixes (qwen3 think:false, bridge timeout 120s→300s) and auto-retry fallback.
version: 1.1.0
license: MIT
platforms: [WorkBuddy, QClaw, ima, Claude Code, Cursor]
author: 注册老炮@MedXpert
category: 文档处理
xiaping_category: ["效率工具"]
xiaping_tags: ["本地大模型","批量精读","知识库","DSH","任务桥","qwen3","Ollama","RAG","摘要","疑点清单","断网可用","省积分","MedXpert","医械知识库","注册知识库","L1精读","结构化摘要","知识消化","图书馆","个人图书馆"]
agent_created: true
---

# MedXpert·本地模型批量精读（L1）

> 一句话：把一整个知识库/文档集「喂」给本地模型，逐份产出**结构化摘要 + 疑点清单**，最后汇总成一张疑点总表——全程本地跑、不花 API 积分、断网可用。

## 这是什么

针对「我已经攒了一堆资料（枢纽 / 标准 / 竞品情报 / 法规文档），想快速消化成可检索的结构化笔记」的场景。核心是一个可复现的闭环：

```
文档集(目录) → 写任务单(清单+文件名映射) → 投递 inbox(qwen3-local)
   → DSH 本地精读 → 回收 outbox → 落盘 <枢纽名>_摘要.md
   → 汇总 L1疑点总表.md（喂下一阶段 L2 缺口定位）
```

## 触发场景 / 触发词

- 「把这一批文档/枢纽批量精读一遍」「L1 全库精读」「本地模型跑一遍知识库」
- 「逐份出摘要 + 疑点」「消化这堆资料成笔记」
- 「省积分批量读文档」「断网用本地模型读资料」
- 边界：**只做 L1 精读（理解+疑点），不做 L2 缺口补齐 / L3 改写 / L4 产物发布**。那几步是后续阶段。

## 前置条件（务必先确认）

1. DSH 服务全 UP：主进程、SSE 代理、Ollama（本地模型端口）均健康。
2. 本地模型 `qwen3.5:4b` 已拉取（**2026-08-24 20:05 起主力**；`qwen3-local` 逻辑名经 `medxpert-rag-proxy.mjs` 映射到它，实测 51 tokens/s、think 关闭正常。9B 档 qwen3.5:9b 在 Intel Arc A750 上实测仅 4.2 tok/s，已弃用。非 qwen3 系列可跳过修复①）。
3. 任务桥目录存在：`~/.dsh-bridge/inbox/`（投递）、`~/.dsh-bridge/outbox/`（回收）。
4. 待精读文档已归到一个目录（下称 `<HUB>`），文件名稳定。

> 路径一律用 `~` 或相对/可配置，不要硬编码本机绝对路径（见「安全与脱敏」）。

## 两处必做修复（不做必卡：整 2 分钟超时 abort）

本地 qwen3 默认开启 thinking 思考，叠加桥硬编码 2 分钟超时，单任务稍长就 `This operation was aborted`。**先修这两处再投任务**：

### 修复①：qwen3 thinking 关闭（代理层）【2026-08-22 升级版】

在 RAG/SSE 代理（形如 `~/.dsh/medxpert-rag-proxy.mjs`）转发 qwen3 上游时，注入 `think:false`：

```js
// 在构造 upstreamPayload 之后、fetch 之前插入
if (isQwen) upstreamPayload.think = false;
```

> ⚠️ **2026-08-22 关键升级（务必照做）**：仅注入 `think:false` 在 **Ollama 0.32.x 的 OpenAI 兼容接口（/v1/chat/completions）上无效**——该接口忽略 think/enable_thinking 参数，qwen3 思考全开会把 max_tokens 吃光，`content` 恒空、`finish_reason=length`，下游表现就是「本地调用失败/空输出」。**qwen3-local 分支必须改走 Ollama 原生 `/api/chat` 接口**（`think:false` 在此真正生效），非流式拿 JSON 再包 SSE 回流。`medxpert-rag-proxy.mjs` 已于 2026-08-22 内置此逻辑（qwen 分支独立 fetch `/api/chat`，构造 OpenAI 格式后 jsonToSse），升级 DSH 后只需确认该分支仍在（代理文件位于 `~/.dsh/`，**不属于 DSH 安装目录、不被 DSH 升级覆盖**）。

诊断命令（区分原生 vs 兼容接口）：
```bash
# ✅ 原生接口 + think:false → 应秒回正常 content（模型名随主力更新：qwen3.5:4b）
curl -s localhost:11434/api/chat -d '{"model":"qwen3.5:4b","messages":[{"role":"user","content":"说一个字：好"}],"think":false,"options":{"num_predict":20}}'
# ❌ 兼容接口 + think:false → content 空、completion_tokens 被吃光、finish=length（0.32.x 的坑）
curl -s localhost:11434/v1/chat/completions -d '{"model":"qwen3.5:4b","messages":[{"role":"user","content":"说一个字：好"}],"think":false,"max_tokens":100}'
```

效果：简单问答实测 19.6s → 2.6s，长精读不再触发思考超时。

### 修复②：桥超时 120s → 300s（桥插件层）

桥插件 `~/.dsh/profiles/web/node_modules/dsh-workbuddy-bridge/lib/llm.js` 第 8 行左右硬编码 `timeoutMs = 120000`；其 `index.js` 调用 chat 时未传 timeoutMs，故默认 2 分钟。改为：

```js
const timeoutMs = 300000; // 原 120000
```

### 重启

DSH 由看门狗托管：杀掉对应 PID，看门狗会自拉起新进程（无需手动重启命令）。修完用简单问答验证一次（应 < 30s 返回）。

> ⚠️ 这两处改动位于 DSH 安装目录，**DSH 升级会被覆盖**，需在升级后重打 / 重新应用。

## 核心流程（5 步）

1. **准备实体 + 写任务单**：列出全部待精读文件清单（如 30 份），建「任务 ID → 文件名 / 输出名」映射（存 `names.json`，供回收脚本用）。
2. **投递 inbox**：按模板写 task JSON（见下「精读提示词模板」），`model: "qwen3-local"`，落到 `~/.dsh-bridge/inbox/task-<时间戳>-<id>.json`。可批量写。
3. **启动回收脚本**：`python scripts/recover_l1.py --inbox <INBOX> --outbox <OUTBOX> --outdir <OUTDIR> --hub <HUB> --names names.json` —— 轮询 outbox，done 的落盘摘要，failed/超时的自动重投（最多 3 次）。
4. **等待全 done**：脚本打印 `进度 done=N/总数`，全部完成退出 0。
5. **汇总疑点总表**：把每份摘要里的「疑点」抽出来，合并为 `L1疑点总表.md`，每条标注来源枢纽，喂 L2 缺口定位。

## 精读提示词模板（投递用）

```
你是 MedXpert 知识库精读员，任务：L1 全库精读第 {idx} 份。请精读文件：
{path}

产出一份「理解摘要 + 疑点清单」，Markdown 格式：
## 核心内容（3 条）
1. ...
2. ...
3. ...
## 数据表格要点
（列出文中关键表格的数据要点，无表格则写"本文无表格"）
## 疑点清单（1-3 条）
1. 疑点：...（说明为什么存疑）

要求：忠实原文，不编造；数据引用原文数值；疑点必须是真实困惑（版本过时/链接失效/条款存疑），无疑点就写"暂无"。
```

## 输出约定

- 每份摘要落盘 `<OUTDIR>/<枢纽名>_摘要.md`，结构：核心 3 条 / 表格要点 / 疑点 1-3 条。
- 汇总 `<OUTDIR>/L1疑点总表.md`：全部疑点 + 来源标注。

## 输入 / 输出约束

| 项 | 约束 |
|---|---|
| 输入 | `<HUB>` 下稳定命名的文档；`names.json` 映射完整（ID→文件名→输出名） |
| 模型 | 本地 `qwen3-local`（省积分）；非 qwen3 可跳过修复① |
| 投递 | inbox 下 `task-<时间戳>-<id>.json`，含 `id/model/prompt/status:pending` |
| 回收 | outbox 下 `result-<id>([-fN]).json`，`status:done` 视为成功 |
| 输出 | `<OUTDIR>/<枢纽名>_摘要.md` + `L1疑点总表.md` |

## 错误处理

- **`This operation was aborted`（整 2 分钟）**：先查修复①（think）与修复②（timeoutMs），二者到位后重投即过。
- **`content` 空 / 输出为空但 `completion_tokens` 大量消耗 / `finish=length`**：Ollama 0.32.x 兼容接口 think 失效的症状（2026-08-22 定位）。确认代理 qwen 分支走的是 `/api/chat` 原生接口而非 `/v1/chat/completions`；代理已内置修复，若被还原按修复①「升级版」重打。
- **outbox 无回执**：任务可能还在跑或投递失败；等一个轮询周期，仍无则检查 inbox 文件格式 / DSH 健康。
- **重投 3 次仍 failed**：脚本留人工，不要无限重投（避免源站永久不可达时刷屏）。
- **摘要文件仅 5.9KB 且非长度问题**：多为超时中断，非内容问题，重投即可。

## 教训（复盘沉淀）

1. **run_in_background 长循环脚本若会话轮次中断，可能丢失任务记录**（回收脚本曾启动失败、任务列表丢失）。关键回收动作应在同一轮内手动兜底，不要依赖跨轮后台任务。
2. **本地模型批处理偶发 `aborted` 且整 2 分钟 → 先查桥 `llm.js` 的 `timeoutMs`**；qwen3 系列慢先关 think。
3. **双修复位于 DSH 安装目录，升级会覆盖**，需随 DSH 版本重打（代理文件在 `~/.dsh/` 不被覆盖，桥的 `llm.js` 在 DSH 安装目录会被覆盖）。
4. **2026-08-22 深坑：Ollama 0.32.x OpenAI 兼容接口忽略 think 参数**。qwen3「调用失败」的排查顺序：先直测 Ollama 原生 `/api/chat`（think:false 应秒回）→ 再测 `/v1/chat/completions`（若 content 空即命中此坑）→ 定位到代理路由。修复= qwen 分支改走原生接口，别在兼容接口上反复试参数。

## FAQ

- **Q：能用云端模型吗？** A：能，但本技能主打本地省积分。换云端把 `model` 改成对应名、跳过修复①即可。
- **Q：文档不是医械的能用吗？** A：能，方法论通用；提示词模板按领域微调即可。
- **Q：names.json 必须吗？** A：回收脚本靠它把任务 ID 映射回输出文件名；不提供则落盘用 ID 命名。

## 安全与脱敏

- 技能内所有路径用 `~` / 相对 / 命令行参数，**不得写入本机绝对路径**（如 `~`、`<workbuddy-root>\Claw`）。
- 精读产物只落本地工作区，不外传；疑点涉及外部资料版本/链接时，标注「以现行版为准」不臆断。
- 本技能为自沉淀工作流（agent_created），不含任何第三方密钥 / token。
