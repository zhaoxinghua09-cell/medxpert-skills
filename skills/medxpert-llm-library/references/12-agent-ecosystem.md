# 接入 Agent 生态与上公网（MCP / 编排 / 官网 / IMA / 华为）

> 本文件由 `medxpert-llm-library/SKILL.md` 下沉而来（渐进披露）。
> 主技能文件保留**决策路径与高频操作**；本文件承载完整细节，按需加载。

---

## MedXpert-五补八、图书馆接入 AI 世界（Agent 生态）

> **使命落地：图书馆服务于人类和 AI 世界。** 人类用的部分前面都讲了，这一节讲 AI 世界怎么用你的图书馆——**让 AI 智能体（Agent）直接把你的图书馆当知识底座**。

### 1. 知识库 → Agent 工具（MCP，标准接入）

**MCP（Model Context Protocol）** 是让 AI 工具/智能体标准调用外部能力的协议——把你的图书馆包成一个 MCP Server，任何支持 MCP 的 Agent 都能直接检索你的知识库。

| 做法 | 说明 | 难度 |
|------|------|------|
| **轻量 MCP Server** | 写一个检索接口（接收查询 → 从知识库检索 Top-K → 返回片段） | ⭐⭐ |
| **复用现成工具** | AnythingLLM / Open WebUI 已提供 API，Agent 通过 API 调用 | ⭐ |
| **DSH Agent 模式** | DSH 本身支持 Agent 调用本地模型（见二补） | ⭐ |

**MCP Server 核心逻辑（伪代码）**：
```python
# 图书馆 MCP Server：让 Agent 检索你的知识库
@mcp.tool("library_search")
def library_search(query: str, top_k: int = 5):
    """从 MedXpert 图书馆检索与问题最相关的片段"""
    results = vector_store.search(query, top_k)  # bge-m3 向量检索
    return [{"content": r.content, "source": r.file, "score": r.score} for r in results]
```

### 2. 多 Agent 共享知识层

**一个图书馆，多个 AI 消费**——团队/个人的多个 Agent（问答助手、写作助手、分析助手）共享同一个知识源：

```
         ┌── 问答 Agent（RAG 问答）
图书馆 ──┼── 写作 Agent（引用知识写稿）
（单一事实源）┼── 分析 Agent（基于知识做分析）
         └── 你的 DSH/助手（日常对话）
```

> **好处**：知识只维护一份，所有 AI 读到的是同一个"真相"——避免各 Agent 各说各话。

### 3. 人类与 AI 分工（human-in-the-loop）

| 环节 | 谁做 | 为什么 |
|------|------|--------|
| 数据采集 | 人（判断来源可信） | AI 判断不了来源权威性 |
| 知识整理 | AI 辅助 + 人终审 | 法规/标准必须人工核实 |
| 检索问答 | AI（快） | 效率 |
| 关键决策 | **人（最终拍板）** | 责任在人 |
| 质量监控 | AI 体检 + 人抽查 | 双重保障 |

> **原则：AI 世界可以自动，但方向盘在人手里。**

### 4. 图书馆在 AI 世界的角色全景

```
对人类：学习 / 工作 / 决策支持 / 知识传承
对 AI ：RAG 知识源 / Agent 工具库 / 语料贡献 / 进化养分
对生态：开放（llms.txt）/ 贡献（开源语料）/ 收费（Pay Skill）
```

> **这就是"服务于人类和 AI 世界"的完整含义**——人类用好它，AI 依赖它，生态受益于它。

### 5. AI 世界接入清单（照着打勾）

- [ ] 知识库通过 MCP/API 暴露给 Agent（只读权限）
- [ ] Agent 检索有来源标注（回答可溯源）
- [ ] 多 Agent 共享时用同一事实源（避免口径不一）
- [ ] 关键决策流程保留人工确认（human-in-the-loop）
- [ ] 接入 Agent 的日志可审计（谁查了什么）
- [ ] 对外暴露只读，禁止 Agent 修改知识库

---

## MedXpert-五补九、多 Agent 协作编排（让 AI 团队干活）

> **多 Agent 协作 = 多个专门化的 Agent 分工，像一支团队一样完成复杂任务**——不只共享知识，还互相配合：有人做、有人审、有人查。你的图书馆就是这支"AI 团队"的知识底座和协作中枢。

### 1. 四种编排模式

| 模式 | 怎么工作 | 适合 | 示例 |
|------|---------|------|------|
| **流水线 Pipeline** | 串行：A 做完给 B，B 做完给 C | 有固定步骤的任务 | 入库流水线：筛选→摘要→校验 |
| **并行扇出 Fan-out** | 多个 Agent 同时干不同活，最后汇总 | 可拆分的任务 | 同时摘要 5 篇文档 |
| **评审循环 Critic** | 生成 Agent 产出 + 评审 Agent 挑错，循环优化 | 质量要求高 | 报告生成 + 多轮校对 |
| **路由 Router** | 按问题类型分发给对应专家 Agent | 领域多样 | 法规问题→法规 Agent，技术问题→技术 Agent |

> **核心：一个复杂任务拆成小任务，交给最合适的 Agent，再加一道"审核"兜底——这就是 AI 团队。**

### 2. 图书馆场景的 Agent 编排（知识流水线）

**入库流水线（从文档到知识）**：
```
采集 Agent（判断来源可信）→ 筛选 Agent（小模型，快，值不值得入）
→ 摘要 Agent（Qwen，中文摘要）→ 校验 Agent（DeepSeek，查矛盾）
→ 入库 Agent（写入 + frontmatter + 索引更新）
```

**问答流水线（从问题到答案）**：
```
路由 Agent（判断问题领域）→ 检索 Agent（bge-m3 从图书馆检索）
→ 生成 Agent（Qwen 基于片段回答）→ 校验 Agent（DeepSeek 查编造/查来源）
→ 返回（带来源标注）
```

### 3. 轻量编排器代码示例（本地模型直接跑）

```python
import requests

OLLAMA = "http://localhost:11434/api/generate"
def call(model, prompt, timeout=300):
    r = requests.post(OLLAMA, json={"model": model, "prompt": prompt, "stream": False}, timeout=timeout)
    return r.json()["response"]

# 简单编排器：流水线模式
def pipeline(steps, doc):
    """steps: [(model, prompt_template), ...]"""
    result = doc
    for model, template in steps:
        result = call(model, template.format(content=result))
    return result

# 入库流水线：筛选(3B) → 摘要(7B) → 校验(DeepSeek)
steps = [
    ("qwen2.5:3b", "这份文档是否值得入库？只回答值得/不值得：{content}"),
    ("qwen2.5:7b", "为以下文档生成 200 字中文摘要：{content}"),
    ("deepseek-r1:7b", "检查摘要是否有错误或矛盾，无则回答OK：{content}"),
]
result = pipeline(steps, "文档内容...")
print(result)
```

> **低配电脑也能跑**：串行执行（一个 Agent 一个 Agent 来）+ 小模型干粗活 + 大模型干细活——正好用上"低配优化三板斧"。

### 4. 编排框架（进阶，需要更强编排时）

| 框架 | 特点 | 适合 |
|------|------|------|
| **LangGraph** | 图编排，状态管理强 | 复杂流程（Python） |
| **CrewAI** | 角色化团队，上手快 | 团队协作任务 |
| **Dify 工作流** | 可视化拖拽，零代码 | 非程序员 |
| **AutoGen** | 多 Agent 对话协商 | 研究/协商场景 |

> **建议**：先在本地用"轻量编排器"跑通流程（0 成本），确有必要再上框架——别一上来就引一堆依赖。

### 5. 多 Agent 协作清单（照着打勾）

- [ ] 任务拆成了小步骤，每步有明确 Agent 负责
- [ ] 每个 Agent 的角色和职责写清楚（prompt 里说明）
- [ ] 关键输出有校验 Agent 兜底（防编造）
- [ ] 串行执行，低配电脑内存可控
- [ ] Agent 之间通过"输入→输出"传递，不共享临时状态
- [ ] 全程日志留痕（谁做了什么、用了什么模型）
- [ ] 最终产物人工抽查（human-in-the-loop）

> **一句话：多 Agent 协作 = 分工 + 编排 + 校验——你的图书馆既是团队的"知识库"，也是团队的"会议室"。**

---

## MedXpert-五补十、知识库上公网与生态联动（官网 / IMA / 华为 / 小艺）

> **2026-08-20 新增**：medxpert.cn 官网上线 + 华为生态占位完成后，图书馆从"本地私库"升级为"生态枢纽"——**本地库深度工作，公网做公开橱窗，云端做跨设备协同，Agent 做分发入口。** 一条内容，四方联动。

### 1. 知识库 → 官网（公开橱窗）

**官网 = 图书馆对外的"橱窗"**——把知识库 L0 免费层（精选解读/目录/llms.txt）挂到自己的域名下：

| 要素 | 做法 | 状态（MedXpert 实例） |
|------|------|---------------------|
| 官网载体 | 腾讯云 COS 静态托管（香港免备案）+ HTTPS | ✅ medxpert.cn 已上线（见 `tencent-cos-static-site` 技能） |
| 公开内容 | 从知识库 L0 层挑选精选解读/服务介绍/目录索引，转成静态 HTML/Markdown | 📋 本周：先放 3-5 篇精选 |
| **llms.txt 域名化** | 官网根目录放 `llms.txt` + `robots.txt`——AI 爬虫/Agent 访问 medxpert.cn/llms.txt 就能读到你的"图书馆地图" | 📋 本周 |
| 更新流程 | 知识库更新 → 挑 L0 内容 → 转静态页 → COS 覆盖上传（一条命令/一个脚本） | 📋 整理脚本 |

**llms.txt 公网版要点**：域名 + 目录结构 + 使用指引 + 版权声明（"以现行版为准"）+ 联系邮箱（info@medxpert.cn）。

### 2. 知识库 ↔ IMA 云端知识库（双活协同）

| 维度 | 本地库（Ollama） | IMA 云端库 |
|------|-----------------|-----------|
| 定位 | 深度工作：夜间批量摘要、RAG、多模型分工 | 跨设备随时查询、分享、检索 |
| 内容 | 全量 + 敏感脱敏层 | 精选公开/内部层（Markdown） |
| 同步 | 本地更新后 → 精选转 Markdown → 上传 IMA（ima-skills 技能） | — |
| 注意 | ⚠️ IMA API 不支持 .html，**只传 Markdown 等价版**（HTML 交付物落本地） | — |

> IMA 实例：主知识库 / 医械法规知识库 / 项目资料库 / 设备手册库——按用途分库，本地库是"母库"，IMA 是"移动分馆"。

### 3. 知识库 → 华为生态（Agent 时代入口）

华为生态占位完成后（AGC 应用 / 小艺 Skill / OBS / ModelArts），知识库的接入路径：

| 入口 | 现状 | 知识库接入方式 |
|------|------|--------------|
| **小艺 Skill「MedXpert 医械法规咨询」** | ✅ 已上架（仅自己使用） | 未来把图书馆包成 **MCP Server** → Skill 调用检索接口（见五补八） |
| 华为云 ModelArts / 盘古 | ✅ 已占位（工作空间 MedXpert） | 本地跑不动的大模型推理走华为云，与本地库互补 |
| 华为云 OBS（medxpert-site） | ✅ 已占位 | **异地备份**（见下） |

> **Agent 时代逻辑**：用户在小艺里问法规问题 → 小艺调用你的 Skill → Skill 从你的知识库检索 → 基于馆藏回答——**图书馆成了 Agent 的知识底座**（使命"服务于 AI 世界"的落地形态）。

### 4. 备份新增：华为云 OBS（异地备份第三份）

原"三份原则"（本地 Git + 网盘 + 移动硬盘）升级为四份，OBS 是最稳的云异地备份：

```bash
# 华为云 OBS 备份（obsutil 命令行，或控制台手动上传 zip）
# 1. 本地 Git 仓库打包
cd my-library && git archive --format=zip -o ../library-backup-$(date +%Y%m%d).zip HEAD
# 2. 上传到华为云 OBS 桶 medxpert-site（香港，跨境合规无忧）
obsutil cp ../library-backup-20260820.zip obs://medxpert-site/backups/
```

- 成本：存储约 0.1 元/GB/月，一个 Git 仓库 zip 几 MB ~ 几十 MB，**月成本几毛钱**
- 频率：每周/每月一次，放 `backups/` 前缀目录，保留最近 N 份

### 5. 生态联动总览图（一条内容，四方联动）

```
                    ┌── 官网 medxpert.cn（L0 公开橱窗 + llms.txt 域名化）
                    │
本地知识库（Ollama 母库）──┼── IMA 云端库（跨设备随时查，Markdown 精选）
   夜间批量/多模型分工      │
                    ├── 华为云 OBS（异地备份，Git 仓库 zip）
                    │
                    └── 小艺 Skill（未来：MCP 接入，Agent 分发入口）
```

> **核心原则**：本地库是唯一"母库"（深度工作+安全），其他三处都是"分馆"（公开/移动/备份/分发）——**知识只维护一份，四处消费**。

### 6. 本周落地清单（MedXpert 实例）

- [ ] 官网根目录放 `llms.txt` + `robots.txt`（公开层开放给 AI）
- [ ] 精选 3-5 篇 L0 内容（法规解读/服务介绍）转静态页挂官网
- [ ] IMA 同步规则跑通一次（本地 Markdown → IMA 上传）
- [ ] OBS 备份脚本跑通（Git archive → obsutil 上传）
- [ ] 设计知识库 → 官网更新流水线脚本（半自动）

> **一句话：官网是脸、IMA 是腿、OBS 是保险箱、小艺是代言人——图书馆一本书，四个世界都在用。**

---

