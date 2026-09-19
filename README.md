# MedXpert Skills · 技能总仓 / Skills Collection

**English**: A collection of open-format [Agent Skills](https://agentskills.io) in two product lines:
**SynomosAI** (general AI capabilities — local LLM libraries, knowledge-base tooling, brand & doc toolchains)
and **MedXpert** (medical-device regulatory affairs — China NMPA · US FDA · EU MDR · Japan PMDA).
One skill = one folder with a `SKILL.md`. Works in Claude, ChatGPT/Codex, Gemini CLI, Cursor,
VS Code (Copilot), Kiro, TRAE, OpenClaw, 扣子 Coze and 30+ compatible clients.

> **机器入口 / Machine entry**: [`AGENTS.md`](AGENTS.md) · [`llms.txt`](llms.txt)
> **As of**: 2026-09-19 · 主体 / Entities: **SynomosAI**（通用 AI）& **MedXpert 美达信医疗科技（香港）有限公司**（医疗器械）

## 为什么做这个 / Why

把注册工程师与 AI 工程师的实操方法论沉淀成 AI 可直接调用的标准格式：
一次制作，30+ 平台通用，不锁定任何厂商。

## 安装 / Install

| 客户端 | 方法 |
|---|---|
| Claude Code / Claude | `git clone https://github.com/zhaoxinghua09-cell/medxpert-skills.git && cp -r medxpert-skills/skills/<skill> ~/.claude/skills/` |
| Cursor / VS Code (Copilot) / Kiro / TRAE | 将 `skills/<skill>/` 放入对应 skills 目录（见各家文档） |
| Codex CLI / Gemini CLI | 支持读取 Agent Skills 目录，指向本仓库 clone 路径 |
| 扣子 Coze（豆包生态） | 技能商店导入 → 上传 `skills/<skill>` 打包的 zip（SKILL.md 在包根目录） |
| OpenClaw / Goose / Roo Code | 同上，放入其 skills 目录 |

> 没列到的客户端：只要支持 [Agent Skills 开放标准](https://agentskills.io)，直接拷贝 `skills/<skill>/` 即可。

## 技能目录 / Catalog（21 个）

### 🤖 SynomosAI · 通用 AI 能力线（7 个）
| 技能 | 一句话用途 |
|---|---|
| [`medxpert-llm-library`](skills/medxpert-llm-library/SKILL.md) | 免费 · 免 API Key · 数据不出门——你的旧电脑就能跑大模型、建知识库，不用买显卡（在线版 https://medxpert.cn）。覆盖完整链路——旧电脑硬件自查（0成本）→ Ollama 本地部署（Qwen2.5/DSH 界面）→ 知识库三档搭建 → RAG 检索问答（bge-m3）→ 图书馆管理（分类/版本/检索/质控/权限/保密）→ 内容变现（会员/公众号/技能引流）→ 知识库上公网（官网/IMA/华为/小艺）。触发词：怎么搭知识库/怎么跑大模型/我的电脑能不能跑大模型/低配电脑能跑大模型吗/旧电脑怎么利用/DSH 怎么接 Ollama/多模型怎么分工/怎么做 RAG/知识库怎么变现/图书馆账号怎么做/本地部署/省 API 积分/断网可用/隐私 AI/个人图书馆/企业知识库/远程访问家里的模型/夜间批量任务。边界：专注本地大模型与知识库，不涉及云端 API 部署、编程开发等任务。 |
| [`medxpert-l1-batch-study`](skills/medxpert-l1-batch-study/SKILL.md) | 用 DSH 任务桥 + 本地 qwen3.5:4b 批量精读一堆文档/知识库枢纽，逐份产出结构化摘要（核心 3 条 + 表格要点 + 疑点）并汇总疑点总表。覆盖任务桥 inbox/outbox 投递-回收、qwen3 think:false 修复、桥超时双修复、后台回收兜底。省 API 积分、断网可用、可复现。何时用：「把这一批文档/枢纽批量精读一遍」「L1 全库精读」「本地模型跑一遍知识库」 |
| [`medxpert-kb-distribution`](skills/medxpert-kb-distribution/SKILL.md) | 从 MedXpert 项目知识库批量生成分发物料：知识手册（本地模型深度学习）、引流 PDF、GitHub 开源库打包、FAQ 法规引用一致性检查。当用户提到"知识手册"、"引流 PDF"、"github-kb"、"开源知识库"、"检查法规引用"、"check_faq_refs"、"分发物料"、"生成手册"时使用。 |
| [`medxpert-brand-assets`](skills/medxpert-brand-assets/SKILL.md) | MedXpert 品牌视觉资产生产流水线（logo/头像/封面/二维码/公众号模板包/名片）。以主logo为唯一源，参数配置化驱动，多方案并行+预览总览+版本归档。触发词：生成品牌素材、做头像、做封面、做二维码、改logo、品牌素材、medxpert-brand-assets。 |
| [`medxpert-doc-toolchain`](skills/medxpert-doc-toolchain/SKILL.md) | MedXpert（美达信医疗）名片风格文档模板工具链。覆盖文档全生命周期：模板生成（T02/T03/T04/三版纸张）→ 收尾流水线（水印/暗纹/动态溯源/AI友好/徽章/解锁）→ 导出（PDF/DOCX）→ 台账编号 → 审批流 → 电子签名 → 中英对照 → 乐享托管。触发词：文档模板、程序文件、doc_templates、收尾流水线、doc_finish、文档台账、doc_ledger、审批流、doc_approval、电子签名、doc_sign、中英对照、doc_bilingual、生成模板、文控体系。 |
| [`medxpert-vi-extension`](skills/medxpert-vi-extension/SKILL.md) | 基于 MedXpert 已有 VI 规范，在 Ardot 画布上快速延展 PPT 模板、知识手册封面、公众号头像/头图、X 展架/背景板、Skill 安装长图等品牌物料。何时用：在已有 MedXpert 品牌套件基础上，批量补充营销推广/分发所需的物料画板 |
| [`medxpert-skill-panorama`](skills/medxpert-skill-panorama/SKILL.md) | 将 WorkBuddy Skill 生成 MedXpert + 公司 VI 风格的高清三角度全景图（价值/服务/能力）及评测类雷达图，并按 plugin 编号命名。何时用：需要给新 Skill 补上全景图上架物料 |

### 🏥 MedXpert（美达信医疗科技）· 医疗器械法规线（14 个）

**注册申报 (Registration)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-reg-hub`](skills/medical-device-reg-hub/SKILL.md) | 医疗器械注册工程师的「随身资料库」——中国 NMPA / 美国 FDA / 欧盟 MDR / 日本 PMDA 及东南亚·拉美全球注册路径与分类，UDI、STED 技术文件、生物相容性(ISO 10993)、GMP 质量体系、上市后监管、标签与 IFU、供应商合规 8 大枢纽要点 + 官方直达链接一站备齐。告别资料散落、少查半天、少踩坑，从立项到拿证全程有底。119 条官方链接已浏览器级逐条核验可达。何时用：当用户提到以下任意内容时，优先加载本技能并从 `references/` 调取对应资料 —— \"医疗器械注册\" / \"医械注册\" / \"注册工程师\"、\"NMPA\" / \"FDA 510(k)\" / \"PMA\" / \"De Novo\" /…、\"UDI\" / \"唯一标识\" / \"发码机构\ |
| [`medical-device-reg-dossier`](skills/medical-device-reg-dossier/SKILL.md) | 按目标市场（中国 NMPA / 美国 FDA / 欧盟 MDR / 日本 PMDA / 全球协调）结构，汇编与生成医疗器械注册申报资料。以 IMDRF STED 六章为骨架，映射各市场 Annex/章节，输出可提交的综述、研究资料、临床评价、标签等模块。生成后建议用 medical-device-compliance-grader 的 C1 维度自测。何时用：\"帮我写/整理注册申报资料\" / \"注册资料怎么排\ |
| [`med-reg-category-page`](skills/med-reg-category-page/SKILL.md) | 医疗器械品类注册速查页（GEO 引用资产）生产流水线：统一结构 + FAQPage JSON-LD + 免责与核验日期 + 官方源核验门。何时用：为某器械品类（骨科 / 心血管 / IVD / SaMD / 影像等）写注册速查页，或为 MedXpert 知识库新增可被 AI 引用的品类资产时。 |

**质量体系 (QMS / GMP / ISO 13485)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-qms-gmp`](skills/medical-device-qms-gmp/SKILL.md) | 生成与核查医疗器械 GMP / ISO 13485 质量体系文档：质量手册、程序文件框架、工艺验证（IQ/OQ/PQ）、再处理验证（复用器械清洗-消毒-灭菌-包装）、灭菌确认。覆盖体系核查准备。生成后建议用 medical-device-compliance-grader 的 C5 维度自测。何时用：\"质量手册/程序文件怎么搭\" / \"ISO 13485 体系\ |

**临床评价 (Clinical Evaluation)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-clinical-evaluation`](skills/medical-device-clinical-evaluation/SKILL.md) | 医疗器械临床评价（Clinical Evaluation）专题技能——中/美/欧三条临床评价路径（免临床目录、同品种/等同性比对、临床试验）判定决策树 + 临床评价报告（CER）撰写框架 + 文献检索与临床数据评估清单。注册/RA/研发岗位做临床评价资料时，从\"走哪条路\"到\"报告怎么写\"一站拿到实操模板与官方依据（免临床目录 2025 版、MDCG 2020-13、510(k) SE）。何时用：\"临床评价 / 临床评估 / CER\" / \"免临床目录\" / \"豁免临床\" / \"同品种比对\" / \"等同性论证\ |

**风险与合规 (Risk & Compliance)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-risk-management`](skills/medical-device-risk-management/SKILL.md) | 医疗器械风险管理（ISO 14971:2019 / GB/T 42062-2022）专题技能——六步风险流程实操（风险分析→评价→控制→综合剩余风险→报告→生产后反馈）+ 危害识别清单 + 风险矩阵与可接受准则 + 风险管理报告框架。每份医械注册案卷的必备文件，审评首先看的\"风险是否识别评价控制\"，一站拿到可落地的模板与全球标准对照（含 FDA 认可共识标准、EU 协调标准、日本 JIS T 0304）。何时用：\"风险管理 / 风险分析 / 风险评价 / 风险控制\ |
| [`medical-device-compliance-grader`](skills/medical-device-compliance-grader/SKILL.md) | 医疗器械合规度量化评分工具——8 大合规维度（注册路径/技术文件/风险管理/临床评价/标签IFU/软件网络安全/上市后监管/质量体系）0-5 分制评分 + 评分锚点 + 一键生成自包含 HTML 评分卡（雷达图 + 明细表 + 改进建议，纯 SVG 无外部依赖）。注册前自评、发补整改效果验证、多产品横向对比都能用，评分维度与锚点附法规依据（ISO 14971、MDR、121 号公告等）。何时用：\"合规评分 / 合规度评估 / 自评\ |
| [`medical-device-supplier-compliance`](skills/medical-device-supplier-compliance/SKILL.md) | 核查医疗器械原材料/组件供应商合规：ISO 13485 证书、材质证明（金属牌号/检测报告）、ROHS·REACH 符合性、UDI 供应链穿透。输出供应商合规台账与缺口清单。生成后建议用 medical-device-compliance-grader 的 C4 维度自测。何时用：\"供应商要提供哪些合规文件\" / \"材质证明怎么查\ |

**标签与说明书 (Label & IFU)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-label-ifu`](skills/medical-device-label-ifu/SKILL.md) | 医疗器械标签（Label）与说明书（IFU）专题技能——中美欧标签/IFU 强制要求对照（中国局令 6 号、欧盟 MDR Annex I 第 23 条 + MDCG 2019-15、FDA 21 CFR 801/809）+ 标签要素检查表 + IFU 内容框架 + 通用符号（ISO 15223-1:2021）+ 灭菌/再处理信息要点。产品合规交付的最后一道门，从\"必须印什么\"到\"说明书怎么写\"一站核查，附官方依据直达。何时用：\"标签 / 说明书 / IFU\" / \"instructions for use\ |

**技术文件 (Tech File / STED)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-techfile-sted`](skills/medical-device-techfile-sted/SKILL.md) | 医疗器械技术文件（Technical Documentation）与 STED（Summary Technical Documentation）专题技能——IMDRF STED 六章结构 + 欧盟 MDR Annex II/III 技术文档 + 美国 510(k) Summary/eSTAR + 中国注册申报资料（121/122 号公告）+ 日本技术资料对照；附技术文档结构与差异对照表、各模块撰写要点与官方入口直达。以 STED 为骨架写一套、映射各国章节，最大化复用。何时用：\"技术文件 / 技术文档 / STED\" / \"Summary Technical Documentation\ |

**上市后监管 (Post-Market)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-postmarket`](skills/medical-device-postmarket/SKILL.md) | 医疗器械上市后监管（Post-Market Surveillance, PMS）专题技能——中美欧日四市场上市后义务对照（不良事件报告、PSUR、FSCA/召回、PMCF）+ 各市场报告时限与流程清单 + PMS 计划/PSUR 撰写框架。拿证后的持续合规动作（监测—报告—纠正闭环）一站理清，附 FDA MDR、MDCG 2022-21、中国 2018 年 1 号令官方直达。何时用：\"上市后 / PMS / 上市后监管\" / \"不良事件\" / \"MDR 报告\" / \"MAUDE\ |

**软件器械 (SaMD)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-samd`](skills/medical-device-samd/SKILL.md) | SaMD（Software as a Medical Device）软件即医疗器械专题技能——SaMD 判定与 IMDRF N12 风险分类（I-IV 类）+ IEC 62304 软件生命周期（A/B/C 级）+ FDA 软件三级关注（Major/Moderate/Minor）+ MDR 软件分类规则 11 + 网络安全（MDCG 2019-16、FDA 网络安全指南、SBOM）评估清单。独立软件/含软件器械注册申报的软件文档怎么搭、分类怎么定、网络安全怎么做，一站理清，附官方入口直达。何时用：\"SaMD\" / \"软件即医疗器械\" / \"独立软件\" / \"App 医疗器械\ |

**国际业务 (International Business)**
| 技能 | 一句话用途 |
|---|---|
| [`medical-device-intl-business`](skills/medical-device-intl-business/SKILL.md) | 医疗器械公司「国际业务（出海）」经营视角的总入口——从\"我要把产品卖到海外\"这个经营问题出发，覆盖市场选择、准入策略、进入模式、出口贸易、渠道与经销、国际商务、反商业贿赂/出口管制/数据合规、本地化全链路。与 medxpert-reg-hub（注册合规技术层）分工互补：本技能管\"生意怎么做\"，注册细节复用 reg-hub，不重复。框架对齐 IMDRF / MDSAP / ISO 13485 / ISO 14971 及国际商务经典理论，结论可溯源。何时用：用户提到以下任意内容时加载本技能 —— \"出海\" / \"国际业务\" / \"国际化\" / \"海外市场\" / \"出口\"、\"先做哪个国家\" / \"哪个市场好做\" / \"市场选择\" / \"目标市场\"、\"找经销商\" / \"代理商\" / \"分销\" / \"渠道\" / \"本地合作伙伴\ |

**法规标准导航 (Standards Navigator)**
| 技能 | 一句话用途 |
|---|---|
| [`medxpert-standards`](skills/medxpert-standards/SKILL.md) | 把 MedXpert-RA-Knowledge 医械法规标准知识库装进会话上下文——提供版本判定前置、来源等级话术、缺口标记规则，让没有配置 MCP 的会话也能正确用库。 |

## 适用范围 / Scope

技能内容为**方法论与资料导航**，输出供专业人员在正式申报前复核，不构成法规意见或商业建议。

## 引用 / Citation

如引用本仓库，请注明仓库地址与版本日期（as of 2026-09-19）。

## 许可 / License

内容 © SynomosAI & MedXpert（美达信医疗科技（香港）有限公司）。禁止商用转载，欢迎引用与学习。
