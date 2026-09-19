# 前端 UI：DSH / DeepSeek Harness 全流程

> 本文件由 `medxpert-llm-library/SKILL.md` 下沉而来（渐进披露）。
> 主技能文件保留**决策路径与高频操作**；本文件承载完整细节，按需加载。

---

## MedXpert-二补、前端 UI：给本地模型加个 ChatGPT 界面

> Ollama 装好后只有命令行界面，体验比较原始。**前端 UI = 给你的本地模型套一个好看的壳**，像用 ChatGPT 一样用本地模型。

### 方案 D：DSH / DeepSeek Harness（目前最火，推荐）

**DSH 是 2025 年最火的本地大模型前端之一。** 它原本为 DeepSeek 设计，但支持任意 OpenAI 兼容 API——包括本地 Ollama。装上 DSH 后，你就有了一个**本地版的 ChatGPT**，界面专业、功能丰富，完全离线可用。

#### 为什么选 DSH

- **免费 + 完全本地**：不花一分钱，数据不出本机
- **专业界面**：多轮对话、代码高亮、Markdown 渲染、流式输出
- **Agent 模式**：支持工具调用、多步骤任务（比普通聊天强得多）
- **模型切换**：一个界面里切换不同本地模型（3B/7B/14B）
- **Web + 无头双模式**：`dsh web` 开浏览器界面，`dsh headless` 命令行模式

#### 安装 DSH

```bash
# DSH 需要 Node.js 环境（18+）
# 如果没装 Node.js：
# Windows: 下载 https://nodejs.org LTS 版安装

# 安装 DSH（全局）
npm install -g @anthropic/dsh   # 或按官方文档的最新安装方式

# 验证
dsh --version
```

> **中国网络加速**：如果 npm 慢，用淘宝镜像
> ```bash
> npm config set registry https://registry.npmmirror.com
> npm install -g @anthropic/dsh
> ```

#### 配置 DSH 指向本地 Ollama（关键步骤）

**第 1 步**：编辑 DSH 的 provider 配置文件（`$DSH_HOME/profiles/web/cordis.patch.yml`）：

```yaml
- id: llm-pi-ai
  config:
    providers:
      ollama-local:              # 名字不能跟内置的重复
        displayName: Ollama Local
        api: openai-completions
        baseURL: http://127.0.0.1:11434/v1   # Ollama 的 OpenAI 兼容端点
        apiKeyEnv: OLLAMA_API_KEY  # Ollama 不校验 key，随便填
        models:
          - id: qwen2.5:3b
            name: Qwen2.5 3B
            contextWindow: 32768
            maxTokens: 8192
            input: [text]
        defaultContextWindow: 32768
        defaultMaxTokens: 8192
- id: agent-default-model
  config:
    provider: ollama-local
    model: qwen2.5:3b
```

**第 2 步**：设置环境变量并启动：

```bash
# OLLAMA_API_KEY 随便填个值就行（Ollama 不校验）
# Windows (PowerShell)
$env:OLLAMA_API_KEY = "ollama"
$env:NODE_OPTIONS = ""
dsh web

# Linux / macOS
OLLAMA_API_KEY=ollama NODE_OPTIONS="" dsh web
```

浏览器打开 DSH 显示的地址（通常是 `http://localhost:3000`），就能看到 ChatGPT 风格的界面，背后是你的本地模型。

#### DSH 接 Ollama 踩坑清单（实战总结）

| 问题 | 原因 | 解法 |
|------|------|------|
| **EMPTY_RESPONSE** | DSH 依赖的 pi-ai 库里 `calculateCost` 访问 `model.cost.tiers`，本地免费模型没有 cost 字段 | 打补丁：在 `models.js` 的 `calculateCost` 开头加 `if (!model.cost) model.cost = { input:0, output:0, cacheRead:0, cacheWrite:0, tiers:[] };` |
| **DUPLICATE_DIRECTORY** | provider 名撞了内置 `deepseek-official` | 换自定义名（如 `ollama-local`） |
| **MISSING_CREDENTIAL** | `apiKeyEnv` 对应的环境变量没设 | `export OLLAMA_API_KEY=ollama`（随便填） |
| **headless 模式偶发空回复** | 3B 小模型 + agent 上下文稳定性问题 | 换 7B+ 模型可改善 |
| 模型列表为空 | Ollama 没启动或没拉模型 | `ollama serve` → `ollama pull qwen2.5:3b` |

> **pi-ai 补丁是必打的**，不打的话所有对话都返回 EMPTY_RESPONSE。补丁文件路径：
> `node_modules/@earendil-works/pi-ai/dist/models.js`
> 先备份 `cp models.js models.js.bak`，再改。

#### DSH vs 其他前端 UI

| 维度 | DSH | Open WebUI | Cherry Studio | 直接命令行 |
|------|-----|------------|---------------|-----------|
| 安装难度 | ⭐⭐ npm 装 | ⭐⭐ Docker | ⭐ 下载即用 | ⭐ |
| 界面美观 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 无 |
| Agent/工具调用 | **支持（强项）** | 支持 | 支持 | 不支持 |
| 知识库/RAG | 需自行扩展 | **内置** | **内置** | 不支持 |
| 资源占用 | 低 | 中（Docker） | 中 | 最低 |
| 离线可用 | 是 | 是 | 是 | 是 |
| 推荐场景 | **Agent 任务、专业对话** | **知识库对话** | **日常聊天** | 快速测试 |

> **组合推荐**：Ollama（后端）+ DSH（日常对话/Agent）+ AnythingLLM（知识库 RAG），覆盖全场景。

---

