# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

企业级、人工智能驱动的 Google Ads 管理系统，具有 **28 个自定义工具**、**6 个专门的子代理**，以及通过 Google Ads API v22 对 Google Ads 帐户的**实时读/写访问权限**。

生产版本在 Cloudflare 边缘的 **[googleadsagent.ai](https://googleadsagent.ai)** (Buddy) 上运行 — 具有语义内存、加密密钥存储、自动监控和基于信用的计费系统。该存储库是提供相同功能的开源 Python 代理。

---

## v2.0 中的新增功能

- **安全强化** — CORS 限制、速率限制、错误清理、GAQL 注入预防
- **可安装包** — `pip install google-ads-agent`（或从 [Releases](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases) 下载）
- **MIT 许可证** — 适当的开源许可
- **生产架构文档** — [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md) 中完整的 Cloudflare Buddy 参考
- **安全策略** — [`SECURITY.md`](SECURITY.md) 包含漏洞报告和最佳实践
- **贡献者指南** — [`CONTRIBUTING.md`](CONTRIBUTING.md) 包含优先领域和代码风格
- **环境模板** — [`.env.example`](.env.example) 以及所有凭证占位符

有关详细信息，请参阅完整的 [CHANGELOG](CHANGELOG.md)。

---


## 目录

- [快速入门](#快速入门)
- [三种部署路径](#三种部署路径)
  - [Buddy 添加了什么（路径 C）](#buddy-添加了什么路径-c)
- [路径 A：通过 Anthropic API 部署](#路径-a通过-anthropic-api-部署)
  - [它是如何运作的](#它是如何运作的)
  - [A-1：获取您的 Anthropic API 密钥](#a-1获取您的-anthropic-api-密钥)
  - [A-2：安装并运行 (Python)](#a-2安装并运行-python)
  - [A-3：在您自己的代码中使用](#a-3在您自己的代码中使用)
  - [A-7：已知问题](#a-7已知问题)
  - [A-8：部署包 — 文件参考](#a-8部署包-文件参考)
- [路径 B：在代理平台上部署（手动 UI）](#路径-b在代理平台上部署手动-ui)
- [先决条件](#先决条件)
- [第 1 步：获取 API 凭证](#第-1-步获取-api-凭证)
  - [1A：Google Ads API 凭据](#1agoogle-ads-api-凭据)
  - [1B：Cloudinary 凭证](#1bcloudinary-凭证)
  - [1C：SearchAPI.io 凭证](#1csearchapiio-凭证)
  - [1D：Google AI / Gemini 凭证](#1dgoogle-ai-gemini-凭证)
  - [摘要：所有凭证](#摘要所有凭证)
- [第 2 步：创建主代理](#第-2-步创建主代理)
  - [2.1 — 创建代理外壳](#21-创建代理外壳)
  - [2.3 — 启用内置工具](#23-启用内置工具)
- [步骤 3：安装自定义操作（共 28 个）](#步骤-3安装自定义操作共-28-个)
  - [了解凭证模式](#了解凭证模式)
  - [逐个操作安装](#逐个操作安装)
- [步骤 4：创建子代理（共 6 个）](#步骤-4创建子代理共-6-个)
  - [子代理 1：报告与分析](#子代理-1报告与分析)
  - [副特工 2：研究与情报](#副特工-2研究与情报)
  - [子代理 3：优化](#子代理-3优化)
  - [副特工 4：购物和 PMax](#副特工-4购物和-pmax)
  - [副特工 5：创意](#副特工-5创意)
  - [副特工 6：Baymax — 创意创新](#副特工-6baymax-创意创新)
- [步骤 5：将子代理链接到主代理](#步骤-5将子代理链接到主代理)
- [步骤 6：授予用户访问权限](#步骤-6授予用户访问权限)
- [步骤 7：验证和测试](#步骤-7验证和测试)
  - [测试1：包安装](#测试1包安装)
- [凭证模式参考](#凭证模式参考)
  - [模式 A：5 个关键 Google Ads](#模式-a5-个关键-google-ads)
  - [模式 C：3 键 Cloudinary](#模式-c3-键-cloudinary)
- [架构概述](#架构概述)
  - [这个存储库与其他 AI 代理相比如何](#这个存储库与其他-ai-代理相比如何)
- [已知问题](#已知问题)
- [故障排除](#故障排除)
  - [子代理没有响应](#子代理没有响应)
- [安全](#安全)
- [许可证](#许可证)
- [贡献](#贡献)
- [相关项目](#相关项目)

---
## 快速入门

```bash
# Option 1: Install as a package
pip install google-ads-agent

# Option 2: Clone and install from source
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
pip install -r requirements.txt

# Configure credentials
cp .env.example .env
# Edit .env with your API keys (see Step 1 below)

# Validate setup
python scripts/validate.py

# Run the interactive agent
python scripts/cli.py

# Or start the REST API server
uvicorn deploy.server:app --port 8000

# Or run with Docker
docker compose up
```---

## 三种部署路径

|路径|最适合 |您需要什么 |
|------|----------|----------------|
| **A: Anthropic API（程序化）** |生产应用程序、SaaS、自动化管道 | Anthropic API 密钥 + Python |
| **B：代理平台（手动 UI）** |快速原型设计、单用户、可视化构建器 |代理平台账号|
| **C：Cloudflare 生产（好友）** |带内存、计费、监控的全栈 | Cloudflare 帐户 |

**路径 A** 是此存储库提供的开箱即用的路径。路径 C 是 [googleadsagent.ai](https://googleadsagent.ai) 上的生产系统 - 请参阅 [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md) 了解完整架构。

### Buddy 添加了什么（路径 C）

|能力|技术 |
|------------|------------|
|每用户持久状态 |持久对象+ SQLite |
|语义记忆|矢量化嵌入 |
|加密 BYOK 存储 | AES-256-GCM |
|实时WebSocket | Cloudflare 代理 SDK |
|自动化监控| Cron 工人 |
|基于信用的计费 | D1+条纹|
|多供应商人工智能 |克劳德、GPT、双子座路由 |
|文件导出| R2 对象存储 |

---

## 路径 A：通过 Anthropic API 部署

这是**程序化部署** — 无需手动 UI，无需点击。一切都通过 Claude 的消息 API 和工具使用来运行。

### 它是如何运作的

此存储库中的操作文件最初是为代理平台构建的。 `deploy/` 包使它们能够通过 Anthropic API 独立运行。以下是当您运行“python script/cli.py”时会发生的情况：

```
YOU: "Show me campaigns for Acme Corp"
 │
 ▼
┌─────────────────────────────────────────────────────────────────┐
│  orchestrator.py — sends to Anthropic Messages API:             │
│                                                                 │
│  client.messages.create(                                        │
│      model="claude-opus-4-5-20251101",                          │
│      system=<your system prompt from prompts/>,                 │
│      tools=<28 tool JSON schemas from tool_schemas.py>,         │
│      messages=[{"role": "user", "content": "Show me..."}]       │
│  )                                                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼ Claude returns stop_reason="tool_use"
┌─────────────────────────────────────────────────────────────────┐
│  Claude's response:                                             │
│  tool_use: name="campaign_adgroup_manager"                      │
│            input={"action": "list_campaigns",                   │
│                    "search": "Acme Corp",                       │
│                    "status_filter": "ENABLED"}                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  tool_executor.py — the adapter layer:                          │
│                                                                 │
│  1. Loads actions/main-agent/09_campaign_adgroup_manager.py     │
│  2. Injects secrets={"DEVELOPER_TOKEN": "...", ...}             │
│     into module namespace (replicating agent platform runtime)    │
│  3. Suppresses subprocess pip install calls                     │
│  4. Inspects run() signature, drops any extra params            │
│  5. Calls: run(action="list_campaigns", search="Acme Corp",    │
│              status_filter="ENABLED")                           │
│  6. Returns JSON result to orchestrator                         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  orchestrator.py — sends tool_result back to Claude:            │
│                                                                 │
│  messages.append({"role": "user", "content": [{                 │
│      "type": "tool_result",                                     │
│      "tool_use_id": "toolu_xxx",                                │
│      "content": "<JSON campaign data>"                          │
│  }]})                                                           │
│                                                                 │
│  → Loop repeats until Claude returns final text                 │
└─────────────────────────────────────────────────────────────────┘
```

**适配器层（`tool_executor.py`）解决的问题：**

|问题 |操作文件的作用 |适配器的作用 |
|---------|------------------------------------|----------------------|
| **秘密** |引用 `secrets["KEY"]` 作为代理平台注入的裸全局变量 |在 `exec_module()` 之前将 `secrets` 字典注入模块 `__dict__` |
| **Pip 安装** |在导入时运行 `subprocess.check_call(["pip", "install", "google-ads"])` | Monkey-patches 子进程以跳过 pip 命令（deps 已在“requirements.txt”中）|
| **参数不匹配** | 26/28 `run()` 函数具有显式参数（没有 `**kwargs`）|通过“inspect.signature()”检查“run()”签名，删除 Claude 发送的任何不在函数中的参数 |

### A-1：获取您的 Anthropic API 密钥

1. 前往 **[Anthropic 控制台](https://console.anthropic.com)**
2. 注册或登录
3. 转到 **[设置 → API 密钥](https://console.anthropic.com/settings/keys)**
4. 单击“**创建密钥**”
5. 复制密钥 → 这是您的“ANTHROPIC_API_KEY”

> 💡 密钥以 `sk-ant-api03-...` 开头。安全地存储它 — 它授予完整的 API 访问权限。

**这如何与系统联系在一起：** 每次调用 Claude 的消息 API 都需要“x-api-key”标头中的此密钥。 `anthropic` Python SDK 自动从 `ANTHROPIC_API_KEY` 环境变量中读取它。

### A-2：安装并运行 (Python)

**当您运行此命令时，一步一步会发生什么：**```bash
# 1. Clone — gets all 66 files: action code, prompts, schemas, adapter layer
git clone https://github.com/YOUR_USERNAME/google-ads-api-agent.git
cd google-ads-api-agent

# 2. Virtual env — isolates dependencies
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install deps — this is what replaces the inline pip installs
#    google-ads, anthropic, fastapi, cloudinary, etc. all install here
pip install -r requirements.txt

# 4. Configure — the .env file feeds all 5 services' credentials
cp .env.example .env
# Edit .env — you need at minimum:
#   ANTHROPIC_API_KEY (to talk to Claude)
#   GOOGLE_ADS_* keys (to talk to Google Ads API)
#   Others are optional depending on which tools you use

# 5. Validate — checks files exist, imports work, credentials are set,
#    optionally makes a live API call to verify Claude responds
python scripts/validate.py

# 6. Run the agent — this starts the agentic loop:
#    Your message → Claude + 28 tool schemas → tool_use → execute → repeat
python scripts/cli.py
```

**第6步之后，您将看到：**```
┌─────────────────────────────────────────┐
│    Google Ads API Agent — Interactive CLI    │
│    Type 'quit' to exit, 'reset' to      │
│    clear conversation history            │
└─────────────────────────────────────────┘
  Model: claude-opus-4-5-20251101
  Tools: 28 loaded

You: Show me an account summary for Acme Corp
  [thinking...]

Agent: Here's the account summary for Acme Corp (ID: 123-456-7890):
       Total Spend (Last 30 Days): $12,345.67
       Active Campaigns: 8
       ...
```就是这样。代理正在运行，通过您的凭据进行真正的 Google Ads API 调用，Claude 会协调调用哪些工具以及如何解释结果。

### A-3：在您自己的代码中使用

```python
from dotenv import load_dotenv
load_dotenv()

from deploy import create_agent_system

# Create the full agent with all 28 tools + sub-agents
agent = create_agent_system()

# Single question
response = agent.chat("Show me an account summary for Acme Corp")
print(response)

# Multi-turn conversation (history is maintained automatically)
response = agent.chat("Drill into the top campaign by spend")
print(response)

# Reset conversation when done
agent.reset_conversation()
```### A-4：部署为 REST API

附带的 FastAPI 服务器为您提供任何前端或集成的 HTTP 端点：

```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**端点：**

|方法|路径|描述 |
|--------|------|-------------|
| `发布` | `/聊天` |发送消息，获取响应（自动创建会话）|
| `发布` | `/会话` |创建新的对话会话 |
| `获取` | `/sessions/{id}` |获取会话信息和消息计数 |
| `删除` | `/sessions/{id}` |删除会话 |
| `获取` | `/健康` |健康检查（凭证状态）|
| `获取` | `/工具` |列出所有 28 个工具及其文件状态 |

**请求示例：**```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**响应示例：**```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5：使用 Docker 进行部署```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6：扩展考虑因素

|关注|当前状态 |生产升级|
|--------|--------------|--------------------|
| **会议** |内存中的字典 |切换到 Redis — 在 docker-compose 中添加 `redis` 服务，用 Redis 客户端替换 `sessions` 字典 |
| **速率限制** |每层人为 API 限制 |使用 `celery` 或 `asyncio.Semaphore` 添加请求队列 |
| **多租户** |单一凭证集 |从机密管理器（AWS Secrets Manager、HashiCorp Vault）加载每个租户的凭证 |
| **授权** |无 |将 API 密钥中间件或 OAuth2 添加到 FastAPI 服务器 |
| **监控** |基本日志记录 |添加结构化日志记录 + 导出到 Datadog/CloudWatch |
| **成本控制** |无 |通过“response.usage”跟踪代币使用情况并设置预算警报 |
| **重试逻辑** | SDK 默认（重试 2 次）|调整“max_retries”并为 Google Ads API 调用添加指数退避 |

### A-7：已知问题

第一次运行时可能会遇到麻烦的事情：

|问题 |发生了什么 |修复|
|--------|-------------|-----|
| **google-ads 导入失败** |操作文件需要具有 C 依赖项的 `google-ads>=28.1.0`首先运行 `pip install -rrequirements.txt` — 这就是适配器抑制内联 pip 安装的原因 |
| **`秘密`KeyError** |某个操作尝试访问您未在 `.env` 中设置的凭据 |检查该工具使用哪种凭证模式 (A/B/C/D) 并验证 `.env` 具有这些密钥 |
| **运行时出现类型错误** | Claude 发送了 run() 函数不接受的参数 |参数过滤器应该捕获这个 - 如果没有，请检查 `python -c "from deploy import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"` |
| **速率限制** | Google Ads API 基本访问 = 15K 操作/天，4 请求/秒 |使用 `cost_min`、`status`、`limit` 参数来减少结果集 |
| **第一次加载很慢** |模块加载 + pip 抑制在第一次工具调用时增加了约 1-2 秒 |后续调用使用缓存模块 - 即时 |
| **代币成本** | claude-opus-4-5 具有 28 个工具定义 = 每个工具请求约 4K 个令牌 |为了成本优化，请在构造函数中切换到“claude-sonnet-4-5-20250929” |

### A-8：部署包 — 文件参考

```
deploy/
├── __init__.py          ← Package exports
├── tool_schemas.py      ← All 28 tools in Anthropic tool_use JSON Schema format
├── tool_executor.py     ← Maps tool_use calls → action Python files, injects credentials
├── orchestrator.py      ← Agentic loop: send → tool_use → execute → return → repeat
└── server.py            ← FastAPI REST API with session management

scripts/
├── cli.py               ← Interactive terminal agent
└── validate.py           ← Deployment validation (files, imports, credentials, live API)
```---

## 路径 B：在代理平台上部署（手动 UI）

如果您更喜欢视觉生成器（OpenAI 或类似的），请按照下面的步骤 2-7 操作。您将系统提示、操作代码和凭据粘贴到平台的 UI 中。

---```
google-ads-agent/
├── README.md                          ← You are here
├── .env.example                       ← Template for all required credentials
├── .gitignore
├── requirements.txt                   ← Python dependencies
├── Dockerfile                         ← Container build
├── docker-compose.yml                 ← Multi-service orchestration
│
├── deploy/                            ← PROGRAMMATIC DEPLOYMENT (Path A)
│   ├── __init__.py
│   ├── tool_schemas.py                ← 28 tools in Anthropic JSON Schema format
│   ├── tool_executor.py               ← Maps tool_use → action files + credential injection
│   ├── orchestrator.py                ← Agentic loop: Claude ↔ tools ↔ sub-agents
│   └── server.py                      ← FastAPI REST API with session management
│
├── scripts/
│   ├── cli.py                         ← Interactive terminal agent
│   └── validate.py                    ← Deployment validation suite
│
├── actions/
│   ├── main-agent/                    ← 28 Python action files for the main agent
│   │   ├── 01_label_manager.py
│   │   ├── 02_conversion_tracking_manager.py
│   │   ├── 03_audience_manager.py
│   │   ├── ...
│   │   └── 28_pmax_asset_group_manager.py
│   │
│   └── sub-agents/
│       ├── reporting/                 ← 8 action files for Reporting sub-agent
│       │   ├── 01_performance_reporter.py
│       │   ├── 02_search_terms_analyzer.py
│       │   ├── ...
│       │   └── 08_package_installer.py
│       ├── research/                  ← 4 action files for Research sub-agent
│       │   ├── 01_keyword_planner.py
│       │   ├── 02_google_search_api.py
│       │   ├── 03_ads_transparency_center.py
│       │   └── 04_google_trends_analyzer.py
│       ├── creative/                  ← 2 action files for Creative sub-agent
│       │   ├── 01_responsive_display_ads_manager.py
│       │   └── 02_demand_gen_ads_manager.py
│       └── creative-innovate/         ← 2 action files for Baymax — Creative Innovate
│           ├── 01_cloudinary_tools.py
│           └── 02_gemini_vision.py
│
├── prompts/
│   ├── main_agent_system_prompt.md    ← Full system prompt for the main agent
│   └── sub-agents/
│       ├── 01_reporting_analysis.md
│       ├── 02_research_intelligence.md
│       ├── 03_optimization.md
│       ├── 04_shopping_pmax.md
│       ├── 05_creative.md
│       └── 06_creative_innovate.md
│
├── configs/
│   └── agent_registry.json            ← Complete agent/action metadata & IDs
│
└── docs/
    └── ARCHITECTURE.md                ← Full technical architecture document
```---

## 先决条件

在开始之前，您需要：

|要求 |为什么 |成本|
|----------|-----|------|
| **人为 API 密钥** |通过消息 API 为 Claude 代理提供支持 |按使用付费（[定价](https://docs.anthropic.com/en/docs/about-claude/pricing)）|
| **Google 广告帐户** |用于管理营销活动的 API 访问权限 |免费（广告费用分开）|
| **Google Ads Manager (MCC) 帐户** |多账户访问 |免费|
| **谷歌云平台项目** | Google Ads API 的 OAuth2 凭据 |免费套餐可用 |
| **云账户** |创意资产的图像/视频处理 |免费套餐（25 积分/月）|
| **SearchAPI.io 帐户** |实时 Google 搜索、趋势、广告透明度 |免费套餐（每月 100 次搜索）|
| **Google AI Studio 帐户** |用于 AI 创意生成的 Gemini API |免费套餐可用 |
| **代理平台账号** |在哪里部署代理（例如 OpenAI 或类似的）|变化 |

---

## 第 1 步：获取 API 凭证

您需要 **4 项服务** 的凭据。本节将通过准确的 URL、屏幕截图指导以及要复制的内容来逐步介绍每个内容。

---

### 1A：Google Ads API 凭据

这是最复杂的设置。您需要 **5 个值** 协同工作：

|资质证书 |它是什么 |它住在哪里|
|------------|------------------------|----------------|
| `DEVELOPER_TOKEN` |您来自 Google Ads 的 API 访问密钥 |谷歌广告用户界面 |
| `CLIENT_ID` | OAuth2 应用程序标识符 |谷歌云控制台 |
| `客户端_秘密` | OAuth2 应用程序秘密 |谷歌云控制台 |
| `刷新令牌` |长期存在的 OAuth2 令牌 |通过 OAuth 流程生成 |
| `LOGIN_CUSTOMER_ID` |您的 MCC 帐户 ID |谷歌广告用户界面 |

#### 步骤 1A-1：获取您的开发者令牌

1. 转至 **[Google Ads](https://ads.google.com)** 并使用您的经理 (MCC) 帐户登录
2. 单击顶部导航中的 **工具和设置** 图标（扳手）
3. 在**设置**下，单击**API 中心**
   - 如果您没有看到 API Center，您可能需要先请求访问权限
4. 此页面显示您的**开发者令牌**
5. **令牌访问级别：**
   - “测试帐户”——仅适用于测试帐户（有利于开发）
   - “基本访问” — 每天最多 15,000 次操作（为此申请）
   - “标准访问” - 无限制（证明使用后应用）
6. **复制令牌** → 这是您的“GOOGLE_ADS_DEVELOPER_TOKEN”

> ⚠️ 如果您的代币显示“待处理”状态，您仍然可以在测试帐户中使用它。对于生产，您需要[申请基本访问权限](https://developers.google.com/google-ads/api/docs/access-levels)。

#### 步骤 1A-2：在 Google Cloud 中创建 OAuth2 凭据

1. 前往 **[Google Cloud Console](https://console.cloud.google.com)**
2. 创建一个新项目（或选择现有项目）：
   - 单击顶部的项目下拉菜单 → **新项目**
   - 名称：“google-ads-agent”（或任何您喜欢的名称）
   - 单击**创建**
3. **启用 Google Ads API：**
   - 转到 **[API 和服务 → 库](https://console.cloud.google.com/apis/library)**
   - 搜索“Google Ads API”
   - 单击它→单击**启用**
4. **配置 OAuth 同意屏幕：**
   - 转到 **[API 和服务 → OAuth 同意屏幕](https://console.cloud.google.com/apis/credentials/consent)**
   - 选择**外部**（除非您有 Google Workspace，然后选择内部）
   - 填写：
     - 应用名称：“Google Ads Agent”
     - 用户支持电子邮件：您的电子邮件
     - 开发者联系方式：您的电子邮件
   - 单击**保存并继续**
   - **范围：** 点击 **添加或删除范围** → 搜索“Google Ads API” → 选中“https://www.googleapis.com/auth/adwords” → **更新** → **保存并继续**
   - **测试用户：** 添加您的 Google Ads 帐户电子邮件 → **保存并继续**
   - 单击**返回仪表板**
5. **创建OAuth2客户端ID：**
   - 转到 **[API 和服务 → 凭证](https://console.cloud.google.com/apis/credentials)**
   - 单击 **+ 创建凭证** → **OAuth 客户端 ID**
   - 应用程序类型：**网络应用程序**
   - 名称：“Google 广告代理”
   - 授权重定向 URI：添加 `http://localhost:8080` （令牌生成步骤所需）
   - 单击**创建**
   - **复制客户端 ID** → 这是您的“GOOGLE_ADS_CLIENT_ID”- **复制客户端密钥** → 这是您的“GOOGLE_ADS_CLIENT_SECRET”

#### 步骤 1A-3：生成刷新令牌

刷新令牌允许代理在无需用户交互的情况下进行身份验证。您生成一次并且无限期地持续（除非被撤销）。

**选项 A：使用 Google 的 OAuth2 Playground（最简单）**

1. 前往 **[OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)**
2. 单击 **齿轮图标** ⚙️（右上角）
   - 检查 **使用您自己的 OAuth 凭据**
   - 输入步骤 1A-2 中的“客户端 ID”和“客户端密钥”
   - 关闭设置
3. 在左侧面板中，滚动到 **Google Ads API v18** → 检查“https://www.googleapis.com/auth/adwords”
4. 点击**授权API**
5. 使用有权访问您的 Google Ads 帐户的 Google 帐户登录
6.授予请求的权限
7. 点击**兑换授权码换取令牌**
8. **复制刷新令牌** → 这是您的“GOOGLE_ADS_REFRESH_TOKEN”

**选项 B：使用 google-ads Python 库**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```这将打开浏览器以获取 OAuth 同意并打印刷新令牌。

**选项C：使用curl**```bash
# 1. Get authorization code (open this URL in browser)
echo "https://accounts.google.com/o/oauth2/v2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost:8080&response_type=code&scope=https://www.googleapis.com/auth/adwords&access_type=offline&prompt=consent"

# 2. After authorizing, grab the 'code' parameter from the redirect URL

# 3. Exchange code for refresh token
curl -X POST https://oauth2.googleapis.com/token \
  -d "code=AUTHORIZATION_CODE" \
  -d "client_id=YOUR_CLIENT_ID" \
  -d "client_secret=YOUR_CLIENT_SECRET" \
  -d "redirect_uri=http://localhost:8080" \
  -d "grant_type=authorization_code"

# The response JSON contains your refresh_token
```#### 步骤 1A-4：获取您的登录客户 ID (MCC)

1. 转至 **[Google Ads](https://ads.google.com)**
2. 登录您的**经理帐户** (MCC)
3.您的**客户ID**显示在右上角，格式为“XXX-XXX-XXXX”
4. **复制** → 这是您的“GOOGLE_ADS_LOGIN_CUSTOMER_ID”

> 💡 仅当您使用 MCC 管理多个帐户时才需要登录客户 ID。如果您直接管理单个帐户，则可以将此留空。

#### 步骤 1A-5：验证您的凭据

创建一个测试文件来验证一切正常：

```python
from google.ads.googleads.client import GoogleAdsClient

client = GoogleAdsClient.load_from_dict({
    "developer_token": "YOUR_DEVELOPER_TOKEN",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "refresh_token": "YOUR_REFRESH_TOKEN",
    "login_customer_id": "YOUR_MCC_ID_NO_DASHES",
    "use_proto_plus": True
})

# Test: list accessible accounts
ga_service = client.get_service("GoogleAdsService")
customer_service = client.get_service("CustomerService")
accessible = customer_service.list_accessible_customers()
print("Accessible accounts:", accessible.resource_names)
```如果这会打印帐户资源名称，则表明您的 Google Ads 凭据正常工作。

---

### 1B：Cloudinary 凭证

Cloudinary 处理所有图像/视频处理 - 调整大小、AI 生成填充、特定于平台的格式。

1. 前往 **[Cloudinary 注册](https://cloudinary.com/users/register_free)** 并创建一个免费帐户
   - 免费套餐包括 25 个积分/月（足以进行约 1,000 次转换）
2. 注册后，前往**[Dashboard](https://console.cloudinary.com/pm/getting-started/dashboard)**
3. 您的凭据将显示在仪表板上：
   - **云名称** → `CLOUDINARY_CLOUD_NAME`
   - **API 密钥** → `CLOUDINARY_API_KEY`
   - **API Secret** → `CLOUDINARY_API_SECRET`（点击“显示”即可查看）

> 💡 免费套餐对于开发来说非常慷慨。对于需要大量创意处理的制作，Plus 计划（89 美元/月）提供 225 个积分。

#### Cloudinary 如何连接到代理

**Cloudinary Creative Tools** 操作（主代理上的操作 #18）和 **Baymax — Creative Innovate** 子代理都使用这些凭据。它们能够：
- 从 URL 上传图像/视频
- 针对 20 多个平台预设调整大小（Instagram、TikTok、YouTube、展示广告等）
- AI 生成填充，可将图像扩展到非标准纵横比
- 跨多个平台的批处理

---

### 1C：SearchAPI.io 凭证

SearchAPI.io 为研究与情报子代理提供实时 Google 搜索结果、Google 趋势数据和 Google Ads 透明度中心访问权限。

1. 前往 **[SearchAPI.io 注册](https://www.searchapi.io/signup)**
   - 免费套餐：100 次搜索/月
2. 注册后，前往 **[Dashboard → API Key](https://www.searchapi.io/dashboard)**
3. **复制您的 API 密钥** → `SEARCHAPI_API_KEY`

#### SearchAPI 如何连接到代理

**Nemo — 研究与情报**通过三个自定义操作使用 SearchAPI：
- **Google 搜索 API** — 带广告、有机、知识图谱的实时 SERP 结果
- **Google Ads 透明度中心** — 查看竞争对手正在投放哪些广告
- **Google 趋势分析器** — 趋势数据、相关查询、地理兴趣

这些操作通过每个操作源代码中的“secrets["SEARCHAPI_API_KEY"]”传递 API 密钥。

---

### 1D：Google AI / Gemini 凭证

Baymax — Creative Innovate 使用 Google 的 Gemini API 进行人工智能驱动的图像生成和视觉分析。

1. 前往 **[Google AI Studio](https://aistudio.google.com)**
2. 使用您的 Google 帐户登录
3. 点击左侧边栏中的**获取 API 密钥**（或直接转到**[API 密钥](https://aistudio.google.com/apikey)**）
4. 单击**创建 API 密钥**
   - 选择您在步骤 1A-2 中创建的 Google Cloud 项目（或创建一个新项目）
5. **复制 API 密钥** → `GOOGLE_AI_API_KEY`

> 💡 免费套餐为 Gemini 2.0 Flash 提供 15 RPM（每分钟请求数）。对于生产来说，即用即付的费率非常实惠。

#### Gemini 如何连接到代理

**Baymax — Creative Innovate** 子代理使用 Gemini 来：
- 社交媒体格式的人工智能图像生成/扩展
- 现有创意资产的愿景分析
- 从源图像生成展示广告变体

Gemini 操作文件位于“actions/sub-agents/creative-innovate/02_gemini_vision.py”。

---

### 摘要：所有凭证

完成步骤 1A–1D 后，您的“.env”文件应如下所示：

```env
# Google Ads API
GOOGLE_ADS_DEVELOPER_TOKEN=aBcDeFgHiJkLmNoPqR
GOOGLE_ADS_CLIENT_ID=123456789-abcdef.apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=GOCSPX-AbCdEfGhIjKlMnOpQrStUvWx
GOOGLE_ADS_REFRESH_TOKEN=1//0abCdEfGhIjKl-MnOpQrStUvWxYz_AbCdEfGhIjKlMnO
GOOGLE_ADS_LOGIN_CUSTOMER_ID=123-456-7890

# Cloudinary
CLOUDINARY_CLOUD_NAME=my-cloud-name
CLOUDINARY_API_KEY=123456789012345
CLOUDINARY_API_SECRET=AbCdEfGhIjKlMnOpQrStUvWx

# SearchAPI
SEARCHAPI_API_KEY=abc123def456ghi789

# Google AI (Gemini)
GOOGLE_AI_API_KEY=AIzaSyAbCdEfGhIjKlMnOpQrStUvWxYz
```---

## 第 2 步：创建主代理

> 这些说明使用通用术语。为您的特定代理平台（例如 OpenAI 或类似平台）调整按钮名称/菜单。

### 2.1 — 创建代理外壳

1. 在您的代理平台上，使用以下设置创建一个新代理：

|设置|价值|
|--------|--------|
|名称 | `Google Ads API 代理` |
|型号| `claude-opus-4-5`（人类）|
|访问 |私人|

2. **设置描述：**```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — 粘贴系统提示符

1.打开文件：`prompts/main_agent_system_prompt.md`
2.复制**全部内容**
3. 粘贴到您代理的系统提示/说明字段中
4. 保存

### 2.3 — 启用内置工具

启用这 10 个内置工具（名称可能因平台而异）：

- [x] 代码解释器
- [x] 网络搜索（Google）
- [x] 研究员
- [x] 待办事项/任务列表
- [x] 网页抓取工具
- [x] 查询执行器 (SQL)
- [x] CSV 阅读器
- [x] 字符串匹配器
- [x] 显示文件
- [x] 文件搜索

---

## 步骤 3：安装自定义操作（共 28 个）

每个自定义操作都是一个 Python 文件，该文件将粘贴到代理平台的自定义操作生成器中。您需要：

1. 创建动作
2.粘贴源码
3. 配置凭证（秘密）

### 了解凭证模式

有 4 种凭证模式。在开始之前了解每个操作使用哪一个：

|图案| # 秘密 |使用它的行动|
|--------|-------------|-----------------|
| **A**（5 键 Google 广告）| 5 | 12 个操作 — 包括“LOGIN_CUSTOMER_ID”作为秘密 |
| **B**（4 键 Google 广告）| 4 | 13 个操作 — 将 `login_customer_id` 作为函数参数传递 |
| **C**（3 键云音）| 3 | 1 个操作 — Cloudinary 创意工具 |
| **D**（无凭据）| 0 | 3 个操作 — 包安装程序、会话管理器、重建文档 |

有关完整详细信息，请参阅[凭据模式参考](#credential-patterns-reference)。

### 逐个操作安装

对于下面的**每项操作**，请遵循以下流程：

```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### 模式 A 操作（5 个关键 Google Ads）— 12 个操作

对于每个秘密，添加以下 5 个秘密：

|秘密钥匙|来自 .env 的值 |
|------------------------|----------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` |您的开发者令牌 |
| `GOOGLE_ADS_CLIENT_ID` |您的 OAuth2 客户端 ID |
| `GOOGLE_ADS_CLIENT_SECRET` |您的 OAuth2 客户端密钥 |
| `GOOGLE_ADS_REFRESH_TOKEN` |您的刷新令牌 |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` |您的 MCC 客户 ID |

| ＃|动作名称 |源文件|
|---|-------------|------------|
| 1 |标签经理 | `actions/main-agent/01_label_manager.py` |
| 2 |转化跟踪管理器 | `actions/main-agent/02_conversion_tracking_manager.py` |
| 12 | 12脚本经理 | `actions/main-agent/12_scripts_manager.py` |
| 13 |实验经理| `actions/main-agent/13_experiments_manager.py` |
| 19 | 19查询计划器和预算管理器| `actions/main-agent/19_query_planner.py` |
| 20 |推荐经理 | `actions/main-agent/20_recommendations_manager.py` |
| 23 | 23设备性能管理器| `actions/main-agent/23_device_performance_manager.py` |
| 24 |变更历史管理器 | `actions/main-agent/24_change_history_manager.py` |
| 25 | 25活动创建者 | `actions/main-agent/25_campaign_creator.py` |
| 26 | 26广告计划管理器 | `actions/main-agent/26_ad_schedule_manager.py` |
| 27 | 27竞价策略经理| `actions/main-agent/27_bidding_strategy_manager.py` |
| 28 | 28 PMax 资产组经理 | `actions/main-agent/28_pmax_asset_group_manager.py` |

#### 模式 B 操作（4 键 Google Ads）— 13 个操作

对于每个秘密，添加以下 4 个秘密：

|秘密钥匙|来自 .env 的值 |
|------------------------|----------------|
| `DEVELOPER_TOKEN` |您的开发者令牌 |
| `CLIENT_ID` |您的 OAuth2 客户端 ID |
| `客户端_秘密` |您的 OAuth2 客户端密钥 |
| `刷新令牌` |您的刷新令牌 |

> ⚠️ 注意：**键名称**与模式 A 不同（没有“GOOGLE_ADS_”前缀）。这是设计使然——这些操作接受“login_customer_id”作为函数参数。

| ＃|动作名称 |源文件|
|---|-------------|------------|
| 3 |观众经理| `actions/main-agent/03_audience_manager.py` |
| 4 |资产经理| `actions/main-agent/04_asset_manager.py` |
| 5 |预算经理| `actions/main-agent/05_budget_manager.py` |
| 6 | RSA 广告管理器 | `actions/main-agent/06_rsa_ad_manager.py` |
| 7 |出价和关键字管理器 | `actions/main-agent/07_bid_keyword_manager.py` |
| 8 |否定关键词管理器 | `actions/main-agent/08_negative_keywords_manager.py` |
| 9 |营销活动和广告组经理 | `actions/main-agent/09_campaign_adgroup_manager.py` |
| 10 | 10谷歌广告突变| `actions/main-agent/10_google_ads_mutate.py` |
| 11 | 11帐户访问检查器 | `actions/main-agent/11_account_access_checker.py` |
| 15 | 15检查用户访问级别 | `actions/main-agent/15_check_user_access.py` |
| 16 | 16 API 网关 - 上下文管理器 | `actions/main-agent/16_api_gateway.py` |
| 21 | 21搜索词管理器 | `actions/main-agent/21_search_term_manager.py` |
| 22 | 22地理和位置定位经理 | `actions/main-agent/22_geo_location_manager.py` |

#### 模式 C 动作（3 键 Cloudinary） — 1 个动作

|秘密钥匙|来自 .env 的值 |
|------------------------|----------------|
| `CLOUDINARY_CLOUD_NAME` |您的 Cloudinary 云名称 |
| `CLOUDINARY_API_KEY` |您的 Cloudinary API 密钥 |
| `CLOUDINARY_API_SECRET` |您的 Cloudinary API 秘密 |

| ＃|动作名称 |源文件|
|---|-------------|------------|
| 18 | 18 Cloudinary 创意工具 | `actions/main-agent/18_cloudinary_creative_tools.py` |

#### 模式 D 操作（无凭证）— 3 个操作

只需粘贴代码即可 - 无需任何秘密。

| ＃|动作名称 |源文件|
|---|-------------|------------|
| 14 | 14软件包安装程序 | `actions/main-agent/14_package_installer.py` |
| 17 | 17会话和状态管理器 | `actions/main-agent/17_session_state_manager.py` |

> 📌 **提示：** 如果您的平台支持批量导入操作，请使用 `configs/agent_registry.json` 作为 ID、名称和凭证模式的真实来源。

---

## 步骤 4：创建子代理（共 6 个）

每个子代理都是一个独立的代理，主代理将任务委托给它。它们都有自己的系统提示、工具和自定义操作。

### 子代理 1：报告与分析

|设置|价值|
|--------|--------|
|名称 | “Simba — 报告与分析” |
|型号| `克劳德-opus-4-5` |
|访问 |仅聊天 |
|系统提示| `提示/子代理/01_reporting_analysis.md` |

**自定义操作 (8):** 从 `actions/sub-agents/reporting/` 安装

| ＃|行动|源文件|证书 |
|---|--------|------------|-------------|
| 1 |绩效记者| `01_performance_reporter.py` | 4 键 Google Ads（模式 B）|
| 2 |搜索词分析器 | `02_search_terms_analyzer.py` | 4 键 Google Ads（模式 B）|
| 3 |交互式关键字查看器 | `03_interactive_keyword_viewer.py` | 4 键 Google Ads（模式 B）|
| 4 |互动广告查看器 | `04_interactive_ad_viewer.py` | 4 键 Google Ads（模式 B）|
| 5 |拍卖洞察记者| `05_auction_insights_reporter.py` | 4 键 Google Ads（模式 B）|
| 6 |变更历史审核员| `06_change_history_auditor.py` | 4 键 Google Ads（模式 B）|
| 7 | PMax 增强报告 | `07_pmax_enhanced_reporting.py` | 4 键 Google Ads（模式 B）|
| 8 |软件包安装程序 | `08_package_installer.py` |无（模式 D）|

**内置工具（9）：** code_interpreter、query_executor、csv_reader、string_matcher、display_file、file_search、browser_use、researcher、google_web_search

> ⚠️ 操作 3 和 4（互动关键字/广告查看者）使用 Google Ads API **v18**，而其他操作则使用 **v19**。验证“google-ads” pip 软件包支持两者。

---

### 副特工 2：研究与情报

|设置|价值|
|--------|--------|
|名称 | “尼莫——研究与情报” |
|型号| `克劳德-opus-4-5` |
|访问 |仅聊天 |
|系统提示| `提示/子代理/02_research_intelligence.md` |

**自定义操作 (4+1)：** 从 `actions/sub-agents/research/` 安装

| ＃|行动|源文件|证书 |
|---|--------|------------|-------------|
| 1 |关键词规划师 | `01_keyword_planner.py` | 4 键 Google Ads（模式 B）|
| 2 |谷歌搜索 API | `02_google_search_api.py` | 1 个秘密：`SEARCHAPI_API_KEY` |
| 3 |广告透明度中心 | `03_ads_transparency_center.py` | 1 个秘密：`SEARCHAPI_API_KEY` |
| 4 |谷歌趋势分析器| `04_google_trends_analyzer.py` | 1 个秘密：`SEARCHAPI_API_KEY` |
| 5 |软件包安装程序 | *（从主代理重用）* |无（模式 D）|

**内置工具（10）：** code_interpreter、query_executor、csv_reader、string_matcher、display_file、file_search、browser_use、researcher、google_web_search、web_scraper

---

### 子代理 3：优化

|设置|价值|
|--------|--------|
|名称 | 《艾尔莎 — 优化》 |
|型号| `克劳德-opus-4-5` |
|访问 |仅聊天 |
|系统提示| `提示/子代理/03_optimization.md` |

**自定义操作：** ⚠️ **尚不存在**

该子代理的系统提示引用了两个需要构建的自定义操作：
- **推荐管理器 - API** — `list`、`apply`、`dismiss`、`get_score`
- **批量操作管理器 - API** — `bulk_pause`、`bulk_enable`、`bulk_bid_change`、`bulk_budget_change`、`export`

> 🔧 **TODO：** 使用 Google Ads API 构建这些操作。参数签名记录在系统提示文件中。两者都将使用模式 B（4 键 Google Ads）凭据。

**内置工具（10）：** code_interpreter、query_executor、csv_reader、string_matcher、display_file、file_search、browser_use、researcher、google_web_search、web_scraper

---

### 副特工 4：购物和 PMax

|设置|价值|
|--------|--------|
|名称 | “阿拉丁 — 购物和 PMax” |
|型号| `克劳德-opus-4-5` |
|访问 |仅聊天 |
|系统提示| `提示/子代理/04_shopping_pmax.md` |

**自定义操作：** ⚠️ **尚不存在**

该子代理的系统提示引用了一个需要构建的自定义操作：
- **购物和 PMax 管理器 - API** — `list_shopping`、`list_pmax`、`list_asset_groups`、`get_product_performance`、`get_pmax_performance`、`get_pmax_insights`、`pause_asset_group`、`enable_asset_group`

> 🔧 **TODO：** 使用 Google Ads API（`google-ads` Python SDK）构建此操作。将使用模式 B 凭据。主代理的 PMax 资产组管理器（操作 #28）涵盖了其中一些功能，并且可以作为起始模板。**内置工具（10）：** code_interpreter、query_executor、csv_reader、string_matcher、display_file、file_search、browser_use、researcher、google_web_search、web_scraper

---

### 副特工 5：创意

|设置|价值|
|--------|--------|
|名称 | “莫阿娜——创意”|
|型号| `克劳德-opus-4-5` |
|访问 |仅聊天 |
|系统提示| `提示/子代理/05_creative.md` |

**自定义操作 (2):** 从 `actions/sub-agents/creative/` 安装

| ＃|行动|源文件|证书 |
|---|--------|------------|-------------|
| 1 |响应式展示广告管理器 | `01_responsive_display_ads_manager.py` | 4 键 Google Ads（模式 B）|
| 2 |需求生成广告经理 | `02_demand_gen_ads_manager.py` | 4 键 Google Ads（模式 B）|

**内置工具（10）：** code_interpreter、query_executor、csv_reader、string_matcher、display_file、file_search、browser_use、google_web_search、researcher、web_scraper

---

### 副特工 6：Baymax — 创意创新

|设置|价值|
|--------|--------|
|名称 | 《大白——创意创新》|
|型号| `claude-sonnet-4-5` ⚡ *（更轻的型号 - 有意）* |
|访问 |仅聊天 |
|系统提示| `提示/子代理/06_creative_innovate.md` |

**自定义操作 (2+1)：** 从 `actions/sub-agents/creative-innovate/` 安装

| ＃|行动|源文件|证书 |
|---|--------|------------|-------------|
| 1 |云工具| `01_cloudinary_tools.py` | 3 键 Cloudinary（模式 C）|
| 2 |双子座愿景| `02_gemini_vision.py` | 1 个秘密：`GOOGLE_AI_API_KEY` |
| 3 |软件包安装程序 | *（从主代理重用）* |无（模式 D）|

---

## 步骤 5：将子代理链接到主代理

创建所有 6 个子代理后，您需要将它们注册到主代理，以便主代理可以委派任务。

1. 进入**主代理**设置
2. 找到**子代理**部分
3. 通过搜索名称或 ID 添加每个子代理：

| ＃|子代理名称 |代理 ID |
|---|----------------|----------|
| 1 | Simba — 报告与分析 | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Nemo — 研究与情报 | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 |艾尔莎 — 优化 | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 |阿拉丁 — 购物和 PMax | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 |莫阿娜 — 创意 | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 |大白——创意创新| `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 注意：如果您创建新代理（它们是自动生成的），代理 ID 将**不同**。上面的 ID 来自原始版本，仅供参考。

主代理的系统提示包括**子代理委托协议**，告诉它何时直接处理任务或委托处理任务。 **会话和状态管理器**（操作#17）协调切换。

---

## 步骤 6：授予用户访问权限

如果您需要与团队成员共享代理：

1. 进入主代理设置 → **共享/访问**
2.添加具有**CAN_EDIT**权限的用户
3.他们将能够使用和修改代理

---

## 步骤 7：验证和测试

运行这些测试以验证整个系统是否正常工作：

### 测试1：包安装

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### 测试2：账户连接```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### 测试 3：账户摘要```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### 测试 4：读操作```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### 测试 5：写操作（安全）```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### 测试 6：子代理委托```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### 测试 7：Cloudinary```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## 凭证模式参考

### 模式 A：5 个关键 Google Ads

由 **12 个操作** 使用，其中 MCC 登录客户 ID 作为秘密存储。```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### 模式 B：4 键 Google Ads

由 **13 个操作** 使用，其中登录客户 ID 作为函数参数传递。```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ **值**与模式 A 相同。仅**键名称**不同。这是因为某些操作是使用不同的命名约定编写的。底层凭证是相同的。

### 模式 C：3 键 Cloudinary

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### 模式 D：无凭证

不调用外部 API 的操作：包安装程序、会话和状态管理器。

---

## 架构概述

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GOOGLE ADS AGENT (Main)                          │
│                    claude-opus-4-5 · PRIVATE                        │
│                    28 Custom Actions · 10 Builtin Tools             │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐  │
│  │ Filter-First │  │    CEP       │  │  Session & State Manager │  │
│  │ Architecture │  │  Protocol    │  │  (Coordination Bus)      │  │
│  └──────────────┘  └──────────────┘  └──────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────────┘
                             │ Delegates via handoff protocol
          ┌──────────┬───────┼───────┬──────────┬──────────┐
          │          │       │       │          │          │
     ┌────┴───┐ ┌───┴──┐ ┌─┴──┐ ┌──┴───┐ ┌───┴───┐ ┌───┴────────┐
     │Report- │ │Rese- │ │Opt-│ │Shop- │ │Creat- │ │Creative    │
     │ing &   │ │arch &│ │imi-│ │ping &│ │ive    │ │Innovate    │
     │Analysis│ │Intel │ │zat-│ │PMax  │ │       │ │Tool        │
     │[Simba]  │ │[Nemo]│ │ion │ │[Aladdin]│ │[Moana] │ │(Sonnet 4.5)│
     │        │ │      │ │[3] │ │      │ │       │ │            │
     │8 acts  │ │5 acts│ │⚠️0 │ │⚠️0   │ │2 acts │ │3 acts      │
     └────────┘ └──────┘ └────┘ └──────┘ └───────┘ └────────────┘
```有关包含操作模式、参数签名和委托流程的完整技术架构，请参阅 **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**。

有关 Cloudflare Buddy 生产架构（Durable Objects、Vectorize、D1、R2、Agents SDK），请参阅 **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**。

### 这个存储库与其他 AI 代理相比如何

|特色|这个代理|谷歌广告脚本|微软副驾驶 |困惑|通用克劳德|
|--------|---------|--------------------|--------------------|------------|---------------|
|实时 Google Ads API 读/写 | 28 个行动 |纯 JS 脚本 |没有广告访问权限 |没有API |没有API |
|写入安全（CEP）|确认/执行/发布 |无 |不适用 |不适用 |不适用 |
|多供应商人工智能 |克劳德+GPT+双子座|不适用 |仅限 GPT |自有车型|仅克劳德|
|子代理授权| 6 名专家 |不适用 |不适用 |不适用 |不适用 |
|语义记忆|矢量化（产品）|无 |有限公司|内置|仅对话 |
|可自行部署| 3 条路径 |脚本编辑器|仅限 SaaS |仅限 SaaS |仅限 API |

---

## 已知问题

|问题 |严重性 |详情 |解决方法|
|--------|----------|---------|------------|
| **优化子代理没有任何操作** | 🔴 关键 |系统提示描述了推荐管理器和批量操作管理器，但两个操作都不存在 |使用 Google Ads API 构建它们，或直接使用主代理的推荐管理器 (#20) |
| **Shopping 和 PMax 子代理没有任何操作** | 🔴 关键 |系统提示描述 Shopping & PMax Manager，但不存在任何操作 |构建它，或使用主代理的 PMax Asset Group Manager (#28) 作为起点 |
| **报告中的 API 版本不匹配** | 🟡 中等 |交互式关键字/广告查看器使用 v18，其他报告操作使用 v19 |验证 `google-ads` pip 包可以处理这两者；考虑升级 v18 actions |
| **模式 A 与 B 命名不一致** | 🟡低|跨操作以不同密钥名称存储相同的凭据 |只需输入相同的值 - 工作正常，只是在设置过程中令人困惑 |

---

## 故障排除

###“未找到匹配的帐户...”

`resolve_customer_id()` 函数搜索您的 MCC 下的帐户。确保：
- 您的“LOGIN_CUSTOMER_ID”是 MCC（经理）帐户，而不是儿童帐户
- 您正在搜索的帐户已链接到您的 MCC
- 搜索字符串与帐户描述性名称的一部分相匹配

###“未找到 google-ads 包”

系统提示指示代理在每次对话开始时运行“pip install google-ads>=28.1.0”。如果失败：
- 确保“code_interpreter”已启用
- 尝试在第一条消息中手动运行安装

###“OAuth 凭据已过期”

刷新令牌通常不会过期，但在以下情况下可以撤销：
- 您更改了 Google 帐户密码
- 您在 [Google 安全设置](https://myaccount.google.com/permissions) 中删除了该应用程序的访问权限
- 令牌已超过 6 个月未使用

**修复：** 重新运行步骤 1A-3 中的刷新令牌生成。

###“开发者令牌未获批准”

如果您的开发者令牌处于“测试帐户”模式：
- 它仅适用于 [Google Ads 测试帐户](https://developers.google.com/google-ads/api/docs/first-call/test-accounts)
- 在 [Google Ads API 中心](https://ads.google.com/aw/apicenter) 申请基本访问权限
- 批准通常需要 1-3 个工作日

###“超出速率限制”

Google Ads API 具有以下限制：
- **基本访问：** 15,000 次操作/天，4 个请求/秒
- **标准访问：** 无限操作，每秒 100 个请求

如果达到限制，系统的过滤优先架构应该会有所帮助 - 使用“cost_min”、“status”和“limit”参数来减少结果集。

### 子代理没有响应

- 验证子代理是否已链接到主代理的子代理列表中
- 检查会话和状态管理器操作 (#17) 是否已安装
- 确保子代理配置了自己的凭据（它们不与主代理共享）

---

## 安全

请参阅 [`SECURITY.md`](SECURITY.md) 了解：
- 漏洞报告流程
- CORS、速率限制和输入验证实践
- 凭证管理指南
- 编写安全协议（CEP：确认→执行→后检查）v2.0 中的主要安全功能：
- **无通配符 CORS** — 服务器默认为 localhost；通过“ALLOWED_ORIGINS”进行配置
- **速率限制** — 每个 IP 30 请求/分钟（可通过“RATE_LIMIT_MAX”配置）
- **错误清理** — 一般客户端错误，完整的服务器端日志记录
- **GAQL 注入预防** — 周期值列入白名单
- **没有硬编码的秘密** - 一切都通过`.env`/环境变量

---

## 许可证

麻省理工学院许可证。请参阅 [`LICENSE`](L​​ICENSE) 了解全文。

Google Ads API 须遵守 Google 的[服务条款](https://developers.google.com/google-ads/api/docs/terms)。第三方服务（Cloudinary、SearchAPI、Stripe）受其各自条款的约束。

---

## 贡献

请参阅 [`CONTRIBUTING.md`](CONTRIBUTING.md) 获取完整指南。优先领域：

1. **优化子代理动作**——系统提示存在，需要构建API动作
2. **购物和 PMax 子代理操作** — 同上
3. **测试覆盖率** — 部署包的单元测试
4. **语义记忆** — 将向量化记忆从 Buddy 移植到 Python (pgvector/Pinecone)
5. **流式响应** — 添加 SSE 端点以进行实时工具执行```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## 相关项目

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — Claude 的人类代理技能（分析、审核、写作、数学、MCP）
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)** — Python MCP 服务器，包含 29 个工具，适用于 Claude Code、Claude Desktop、Cursor、OpenAI Agents SDK 和任何 MCP 客户端
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)** — Gemini CLI 扩展，包含 22 个 MCP 工具、技能、命令和主题
- **[googleadsagent.ai](https://googleadsagent.ai)** — Cloudflare 上的生产部署 (Buddy)，具有语义记忆、计费和监控功能

---

> **直播地址：** [googleadsagent.ai](https://googleadsagent.ai)  
> **版本：** 2.0.0  
> **许可证：** 麻省理工学院  
> **最后更新：** 2026-03-05