# 知识库搭建：进阶档与高级档

> 本文件由 `medxpert-llm-library/SKILL.md` 下沉而来（渐进披露）。
> 主技能文件保留**决策路径与高频操作**；本文件承载完整细节，按需加载。

---

### 进阶档：Ollama + RAG 工具

**引入向量检索，支持大规模知识库。**

推荐工具（按易用性排序）：

| 工具 | 特点 | 难度 | 本地化 |
|------|------|------|--------|
| **AnythingLLM** | 开箱即用，支持文档对话，内置向量库 | ⭐ | 完全本地 |
| **Cherry Studio** | 国产，界面友好，支持多模型 | ⭐ | 完全本地 |
| **Open WebUI** | 类 ChatGPT 界面，支持知识库 | ⭐⭐ | 完全本地 |
| **Dify** | 功能全面，可做工作流 | ⭐⭐⭐ | 可本地部署 |
| **RAGFlow** | 专注 RAG，文档解析强 | ⭐⭐⭐ | 可本地部署 |

**AnythingLLM 快速上手**：
1. 下载：https://anythingllm.com（桌面版）
2. 设置 → LLM Provider → Ollama → 填 `localhost:11434`
3. 选模型 → 创建 Workspace → 上传文档
4. 直接对话，它会自动检索相关文档片段

**Cherry Studio 快速上手**：
1. 下载：https://cherry-ai.com
2. 设置 → 模型服务 → Ollama → 自动检测本地模型
3. 创建知识库 → 上传文件 → 对话时选择知识库

> RAG 原理简述：文档切块 → 每块用 Embedding 模型转成向量 → 存入向量数据库 → 提问时把问题也转向量 → 找最相似的文档块 → 拼到 prompt 里给大模型 → 模型基于相关内容回答。**你不需要懂这些，工具自动搞定。**

### 高级档：Ollama + 向量数据库 + 自定义 Pipeline

**完全自定义，适合有开发能力的团队。**

技术栈：
- 大模型：Ollama（qwen2.5:7b）
- Embedding 模型：`nomic-embed-text`（Ollama 直接拉）或 `bge-m3`（中文效果好）
- 向量数据库：Chroma（轻量）/ Qdrant（功能全）/ Milvus（大规模）
- 文档解析：unstructured / LangChain 文档加载器
- 编排框架：LangChain / LlamaIndex

```python
# 最小 RAG 示例（LangChain + Chroma + Ollama）
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import DirectoryLoader

# 1. 加载文档
loader = DirectoryLoader("my-library/", glob="**/*.md")
docs = loader.load()

# 2. 分块
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. 向量化 + 存储
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

# 4. 问答
llm = Ollama(model="qwen2.5:7b")
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever(search_kwargs={"k": 5}))
answer = qa.run("GMP 2025版和2014版有什么主要区别？")
print(answer)
```

优点：完全可控、可定制、可扩展
缺点：需要编程能力、维护成本高
适合：企业级知识库、有开发资源的团队

