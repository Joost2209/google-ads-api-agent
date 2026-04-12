# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

Google Ads API v22를 통해 **28개의 맞춤 도구**, **6개의 전문 하위 에이전트**, Google Ads 계정에 대한 **실시간 읽기/쓰기 액세스**를 갖춘 엔터프라이즈급 AI 기반 Google Ads 관리 시스템입니다.

프로덕션 버전은 의미 체계 메모리, 암호화된 키 저장소, 자동화된 모니터링 및 신용 기반 청구 시스템을 갖춘 Cloudflare 엣지의 **[googleadsagent.ai](https://googleadsagent.ai)**(Buddy)에서 실행됩니다. 이 리포지토리는 동일한 기능을 제공하는 오픈 소스 Python 에이전트입니다.

---

## v2.0의 새로운 기능

- **보안 강화** — CORS 제한, 속도 제한, 오류 삭제, GAQL 주입 방지
- **설치 가능한 패키지** — `pip install google-ads-agent`(또는 [출시 버전](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)에서 다운로드)
- **MIT 라이선스** — 적절한 오픈 소스 라이선스
- **프로덕션 아키텍처 문서** — [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md)의 전체 Cloudflare Buddy 참조
- **보안 정책** — 취약성 보고 및 모범 사례가 포함된 [`SECURITY.md`](SECURITY.md)
- **기고자 가이드** — 우선순위 영역 및 코드 스타일이 포함된 [`CONTRIBUTING.md`](CONTRIBUTING.md)
- **환경 템플릿** — 모든 자격 증명 자리 표시자가 포함된 [`.env.example`](.env.example)

자세한 내용은 전체 [CHANGELOG](CHANGELOG.md)를 참조하세요.

---


## 목차

- [빠른 시작](#빠른-시작)
- [세 가지 배포 경로](#세-가지-배포-경로)
  - [Buddy가 추가하는 것(경로 C)](#buddy가-추가하는-것경로-c)
- [경로 A: Anthropic API를 통해 배포](#경로-a-anthropic-api를-통해-배포)
  - [작동 방식](#작동-방식)
  - [A-1: Anthropic API 키 받기](#a-1-anthropic-api-키-받기)
  - [A-2: 설치 및 실행(Python)](#a-2-설치-및-실행python)
  - [A-3: 자신의 코드에 사용](#a-3-자신의-코드에-사용)
  - [A-7: 알려진 문제점](#a-7-알려진-문제점)
  - [A-8: 배포 패키지 - 파일 참조](#a-8-배포-패키지-파일-참조)
- [경로 B: 에이전트 플랫폼에 배포(수동 UI)](#경로-b-에이전트-플랫폼에-배포수동-ui)
- [전제 조건](#전제-조건)
- [1단계: API 자격 증명 얻기](#1단계-api-자격-증명-얻기)
  - [1A: Google Ads API 자격증명](#1a-google-ads-api-자격증명)
  - [1B: Cloudinary 자격 증명](#1b-cloudinary-자격-증명)
  - [1C: SearchAPI.io 자격 증명](#1c-searchapiio-자격-증명)
  - [1D: Google AI/Gemini 자격 증명](#1d-google-aigemini-자격-증명)
  - [요약: 모든 자격 증명](#요약-모든-자격-증명)
- [2단계: 주 에이전트 생성](#2단계-주-에이전트-생성)
  - [2.1 — 에이전트 셸 생성](#21-에이전트-셸-생성)
  - [2.3 — 내장 도구 활성화](#23-내장-도구-활성화)
- [3단계: 맞춤 작업 설치(총 28개)](#3단계-맞춤-작업-설치총-28개)
  - [자격 증명 패턴 이해](#자격-증명-패턴-이해)
  - [작업별 설치](#작업별-설치)
- [4단계: 하위 에이전트 생성(총 6개)](#4단계-하위-에이전트-생성총-6개)
  - [하위 에이전트 1: 보고 및 분석](#하위-에이전트-1-보고-및-분석)
  - [하위 에이전트 2: 연구 및 정보](#하위-에이전트-2-연구-및-정보)
  - [하위 에이전트 3: 최적화](#하위-에이전트-3-최적화)
  - [하위 에이전트 4: 쇼핑 및 실적 극대화](#하위-에이전트-4-쇼핑-및-실적-극대화)
  - [하위 에이전트 5: 크리에이티브](#하위-에이전트-5-크리에이티브)
  - [하위 에이전트 6: Baymax — Creative Innovate](#하위-에이전트-6-baymax-creative-innovate)
- [5단계: 하위 에이전트를 주 에이전트에 연결](#5단계-하위-에이전트를-주-에이전트에-연결)
- [6단계: 사용자 액세스 권한 부여](#6단계-사용자-액세스-권한-부여)
- [7단계: 검증 및 테스트](#7단계-검증-및-테스트)
  - [테스트 1: 패키지 설치](#테스트-1-패키지-설치)
- [자격 증명 패턴 참조](#자격-증명-패턴-참조)
  - [패턴 A: 5가지 핵심 Google Ads](#패턴-a-5가지-핵심-google-ads)
  - [패턴 C: 3키 Cloudinary](#패턴-c-3키-cloudinary)
- [아키텍처 개요](#아키텍처-개요)
  - [이 저장소를 다른 AI 에이전트와 비교하는 방법](#이-저장소를-다른-ai-에이전트와-비교하는-방법)
- [알려진 문제](#알려진-문제)
- [문제 해결](#문제-해결)
  - ["일치하는 계정을 찾을 수 없습니다..."](#일치하는-계정을-찾을-수-없습니다)
  - ["google-ads 패키지를 찾을 수 없습니다."](#google-ads-패키지를-찾을-수-없습니다)
  - ["OAuth 자격 증명이 만료되었습니다."](#oauth-자격-증명이-만료되었습니다)
  - ["개발자 토큰이 승인되지 않았습니다."](#개발자-토큰이-승인되지-않았습니다)
  - ["비율 제한이 초과되었습니다."](#비율-제한이-초과되었습니다)
  - [하위 에이전트가 응답하지 않음](#하위-에이전트가-응답하지-않음)
- [보안](#보안)
- [라이선스](#라이선스)
- [기여](#기여)
- [관련 프로젝트](#관련-프로젝트)

---
## 빠른 시작

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

## 세 가지 배포 경로

| 경로 | 최고의 대상 | 당신에게 필요한 것 |
|------|----------|---------------|
| **A: Anthropic API(프로그래밍 방식)** | 프로덕션 앱, SaaS, 자동화 파이프라인 | Anthropic API 키 + Python |
| **B: 에이전트 플랫폼(수동 UI)** | 빠른 프로토타이핑, 단일 사용자, 시각적 빌더 | 에이전트 플랫폼 계정 |
| **C: Cloudflare 프로덕션(버디)** | 메모리, 청구, 모니터링 기능을 갖춘 풀스택 | Cloudflare 계정 |

**경로 A**는 이 저장소가 기본적으로 제공하는 것입니다. 경로 C는 [googleadsagent.ai](https://googleadsagent.ai)의 프로덕션 시스템입니다. 전체 아키텍처는 [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md)를 참조하세요.

### Buddy가 추가하는 것(경로 C)

| 능력 | 기술 |
|------------|------------|
| 사용자별 지속 상태 | 지속형 개체 + SQLite |
| 의미기억 | 임베딩 벡터화 |
| 암호화된 BYOK 스토리지 | AES-256-GCM |
| 실시간 웹소켓 | Cloudflare 에이전트 SDK |
| 자동화된 모니터링 | 크론 작업자 |
| 크레딧 기반 과금 | D1 + 스트라이프 |
| 다중 제공자 AI | Claude, GPT, Gemini 라우팅 |
| 파일 내보내기 | R2 객체 스토리지 |

---

## 경로 A: Anthropic API를 통해 배포

이것은 **프로그래밍 방식 배포**입니다. 수동 UI도 없고 클릭도 없습니다. 모든 것은 도구를 사용하여 Claude의 메시지 API를 통해 실행됩니다.

### 작동 방식

이 저장소의 작업 파일은 원래 에이전트 플랫폼용으로 구축되었습니다. `deploy/` 패키지는 Anthropic API를 통해 독립 실행형으로 실행되도록 조정합니다. `python scripts/cli.py`를 실행할 때 내부적으로 일어나는 일은 다음과 같습니다:

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

**어댑터 계층(`tool_executor.py`)이 해결하는 것:**

| 문제 | 작업 파일의 기능 | 어댑터의 기능 |
|---------|------------|---------|
| **비밀** | 에이전트 플랫폼에 의해 주입된 베어 전역으로 `secrets["KEY"]` 참조 | `exec_module()` 전에 `secrets` dict를 모듈 `__dict__`에 삽입합니다 |
| **Pip 설치** | 가져오기 시 `subprocess.check_call(["pip", "install", "google-ads"])` 실행 | pip 명령을 건너뛰기 위해 원숭이 패치 하위 프로세스(deps는 이미 'requirements.txt'에 있음) |
| **매개변수 불일치** | 26/28 `run()` 함수에는 명시적인 매개변수가 있습니다(`**kwargs` 없음) | `inspect.signature()`를 통해 `run()` 서명을 검사하고, Claude가 보낸 매개변수 중 함수에 없는 모든 매개변수를 삭제합니다. |

### A-1: Anthropic API 키 받기

1. **[Anthropic 콘솔](https://console.anthropic.com)**으로 이동합니다.
2. 회원가입 또는 로그인
3. **[설정 → API 키](https://console.anthropic.com/settings/keys)**로 이동합니다.
4. **키 생성**을 클릭합니다.
5. 키를 복사하세요 → 이것이 'ANTHROPIC_API_KEY'입니다

> 💡 키는 `sk-ant-api03-...`로 시작합니다. 안전하게 저장하면 전체 API 액세스 권한이 부여됩니다.

**이것이 시스템과 연결되는 방식:** Claude의 메시지 API에 대한 모든 호출에는 'x-api-key' 헤더에 이 키가 필요합니다. `anthropic` Python SDK는 `ANTHROPIC_API_KEY` 환경 변수에서 자동으로 이를 읽습니다.

### A-2: 설치 및 실행(Python)

**이를 실행하면 단계별로 어떤 일이 발생합니까?**```bash
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

**6단계 후에는 다음이 표시됩니다.**```
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
```그게 다야. 에이전트가 실행되어 자격 증명을 통해 실제 Google Ads API 호출을 수행하고 Claude는 호출할 도구와 결과 해석 방법을 조정합니다.

### A-3: 자신의 코드에 사용

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
```### A-4: REST API로 배포

포함된 FastAPI 서버는 모든 프런트엔드 또는 통합을 위한 HTTP 엔드포인트를 제공합니다.```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**엔드포인트:**

| 방법 | 경로 | 설명 |
|---------|------|-------------|
| '포스트' | `/채팅` | 메시지 보내기, 응답 받기(세션 자동 생성) |
| '포스트' | `/세션` | 새 대화 세션 만들기 |
| `GET` | `/세션/{id}` | 세션 정보 및 메시지 수 가져오기 |
| `삭제` | `/세션/{id}` | 세션 삭제 |
| `GET` | `/건강` | 건강검진(자격현황) |
| `GET` | `/도구` | 28개 도구와 해당 파일 상태 모두 나열 |

**요청 예시:**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**예제 응답:**

```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5: Docker를 사용하여 배포```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6: 확장 고려 사항

| 우려사항 | 현재 상태 | 생산 업그레이드 |
|---------|---------------|------|
| **세션** | 메모리 내 사전 | Redis로 전환 — docker-compose에 `redis` 서비스를 추가하고 `sessions` dict를 Redis 클라이언트로 교체 |
| **비율 제한** | 계층당 인류 API 제한 | `celery` 또는 `asyncio.Semaphore`를 사용하여 요청 대기열 추가 |
| **다중 테넌트** | 단일 자격 증명 세트 | 비밀 관리자(AWS Secrets Manager, HashiCorp Vault)에서 테넌트별 자격 증명 로드 |
| **인증** | 없음 | FastAPI 서버에 API 키 미들웨어 또는 OAuth2 추가 |
| **모니터링** | 기본 로깅 | 구조화된 로깅 추가 + Datadog/CloudWatch로 내보내기 |
| **비용 관리** | 없음 | `response.usage`를 통해 토큰 사용량을 추적하고 예산 알림 설정 |
| **재시도 논리** | SDK 기본값(2회 재시도) | 'max_retries' 조정 및 Google Ads API 호출에 대한 지수 백오프 추가 |

### A-7: 알려진 문제점

처음 실행할 때 넘어질 수 있는 사항:

| 이슈 | 무슨 일이 일어나는지 | 수정 |
|-------|-------------|------|
| **google-ads 가져오기 실패** | 작업 파일에는 C 종속성이 있는 `google-ads>=28.1.0`이 필요합니다 | `pip install -r 요구 사항.txt`를 먼저 실행하세요. 이것이 어댑터가 인라인 pip 설치를 억제하는 이유입니다. |
| **`비밀` KeyError** | 작업이 `.env`에 설정하지 않은 자격 증명에 액세스하려고 시도합니다 | 도구가 어떤 자격 증명 패턴(A/B/C/D)을 사용하는지 확인하고 '.env'에 해당 키가 있는지 확인 |
| **실행 시 TypeError()** | Claude가 run() 함수가 허용하지 않는 매개변수를 보냅니다. | param 필터는 이를 포착해야 합니다. 그렇지 않은 경우 `python -c "from 배포 import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"`를 확인하세요 |
| **비율 제한** | Google Ads API 기본 액세스 = 일일 15,000개 작업, 초당 요청 4개 | `cost_min`, `status`, `limit` 매개변수를 사용하여 결과 세트 줄이기 |
| **첫 번째 로드가 느림** | 모듈 로딩 + pip 억제로 인해 첫 번째 도구 호출 시 ~1-2초 추가 | 후속 호출은 캐시된 모듈을 사용합니다 — 즉시 |
| **토큰 비용** | 28개의 도구 정의가 있는 claude-opus-4-5 = 도구에 대한 요청당 최대 4K 토큰 | 비용 최적화를 위해 생성자에서 `claude-sonnet-4-5-20250929`로 전환 |

### A-8: 배포 패키지 - 파일 참조

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

## 경로 B: 에이전트 플랫폼에 배포(수동 UI)

시각적 빌더(OpenAI 등)를 선호하는 경우 아래 2~7단계를 따르세요. 시스템 프롬프트, 작업 코드 및 자격 증명을 플랫폼의 UI에 붙여넣습니다.

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

## 전제 조건

시작하기 전에 다음이 필요합니다.

| 요구사항 | 왜 | 비용 |
|-------------|------|------|
| **인류적 API 키** | 메시지 API를 통해 Claude 에이전트를 강화합니다 | 종량제([가격](https://docs.anthropic.com/en/docs/about-claude/pricing)) |
| **Google Ads 계정** | 캠페인 관리를 위한 API 액세스 | 무료(광고비 별도 지출) |
| **Google Ads 관리자(MCC) 계정** | 다중 계정 액세스 | 무료 |
| **Google Cloud Platform 프로젝트** | Google Ads API용 OAuth2 자격 증명 | 무료 등급 사용 가능 |
| **흐린 계정** | 크리에이티브 자산의 이미지/비디오 처리 | 무료 등급(25크레딧/월) |
| **SearchAPI.io 계정** | 실시간 Google 검색, 트렌드, 광고 투명성 | 무료 등급(100회 검색/월) |
| **Google AI Studio 계정** | AI 창의적 생성을 위한 Gemini API | 무료 등급 사용 가능 |
| **에이전트 플랫폼 계정** | 에이전트를 배포하는 위치(예: OpenAI 또는 유사) | 다양함 |

---

## 1단계: API 자격 증명 얻기

**4개 서비스**의 사용자 인증 정보가 필요합니다. 이 섹션에서는 정확한 URL, 스크린샷 안내, 복사할 내용을 각 항목별로 안내합니다.

---

### 1A: Google Ads API 자격증명

이것은 가장 복잡한 설정입니다. 함께 작동하는 **5가지 값**이 필요합니다.

| 자격 증명 | 그것은 무엇입니까 | 그것이 사는 곳 |
|------------|------------|---|
| `개발자_토큰` | Google Ads의 API 액세스 키 | Google 광고 UI |
| `CLIENT_ID` | OAuth2 앱 식별자 | 구글 클라우드 콘솔 |
| `CLIENT_SECRET` | OAuth2 앱 비밀 | 구글 클라우드 콘솔 |
| `새로고침_토큰` | 수명이 긴 OAuth2 토큰 | OAuth 흐름을 통해 생성됨 |
| `LOGIN_CUSTOMER_ID` | 귀하의 MCC 계정 ID | Google 광고 UI |

#### 1A-1단계: 개발자 토큰 받기

1. **[Google Ads](https://ads.google.com)**로 이동하여 관리자(MCC) 계정으로 로그인합니다.
2. 상단 탐색 메뉴에서 **도구 및 설정** 아이콘(렌치)을 클릭합니다.
3. **설정**에서 **API 센터**를 클릭합니다.
   - API 센터가 보이지 않는 경우 먼저 접근권한을 요청해야 할 수도 있습니다.
4. 귀하의 **개발자 토큰**이 이 페이지에 표시됩니다.
5. **토큰 액세스 수준:**
   - `Test Account` — 테스트 계정에서만 작동합니다(개발에 적합).
   - '기본 액세스' — 일일 최대 15,000회 작업(신청)
   - '표준 액세스' — 무제한(사용 증명 후 신청)
6. **토큰 복사** → 이것이 `GOOGLE_ADS_DEVELOPER_TOKEN`입니다.

> ⚠️ 토큰이 "보류 중" 상태로 표시되는 경우에도 테스트 계정으로 사용할 수 있습니다. 제작을 위해서는 [기본 액세스를 신청](https://developers.google.com/google-ads/api/docs/access-levels)해야 합니다.

#### 1A-2단계: Google Cloud에서 OAuth2 사용자 인증 정보 만들기

1. **[Google Cloud Console](https://console.cloud.google.com)**로 이동합니다.
2. 새 프로젝트를 생성합니다(또는 기존 프로젝트 선택).
   - 상단의 프로젝트 드롭다운 클릭 → **새 프로젝트**
   - 이름: `google-ads-agent`(또는 원하는 이름)
   - **만들기**를 클릭하세요.
3. **Google Ads API를 활성화합니다:**
   - **[API 및 서비스 → 라이브러리](https://console.cloud.google.com/apis/library)**로 이동합니다.
   - 'Google Ads API'를 검색하세요.
   - 클릭 → **활성화** 클릭
4. **OAuth 동의 화면 구성:**
   - **[API 및 서비스 → OAuth 동의 화면](https://console.cloud.google.com/apis/credentials/consent)**으로 이동합니다.
   - **외부**를 선택합니다(Google Workspace가 없으면 내부를 선택하세요).
   - 작성:
     - 앱 이름: `Google Ads Agent`
     - 사용자 지원 이메일: 귀하의 이메일
     - 개발자 연락처 : 이메일
   - **저장하고 계속하기**를 클릭하세요.
   - **범위:** **범위 추가 또는 제거** 클릭 → `Google Ads API` 검색 → `https://www.googleapis.com/auth/adwords` 확인 → **업데이트** → **저장하고 계속하기**
   - **테스트 사용자:** Google Ads 계정 이메일 추가 → **저장하고 계속하기**
   - **대시보드로 돌아가기**를 클릭하세요.
5. **OAuth2 클라이언트 ID 생성:**
   - **[API 및 서비스 → 자격 증명](https://console.cloud.google.com/apis/credentials)**으로 이동합니다.
   - **+ 자격 증명 만들기** → **OAuth 클라이언트 ID**를 클릭합니다.
   - 애플리케이션 유형: **웹 애플리케이션**
   - 이름: `Google Ads 상담사`
   - 승인된 리디렉션 URI: 'http://localhost:8080' 추가(토큰 생성 단계에 필요)
   - **만들기**를 클릭하세요.
   - **클라이언트 ID 복사** → `GOOGLE_ADS_CLIENT_ID`입니다.- **클라이언트 비밀번호 복사** → 이것이 `GOOGLE_ADS_CLIENT_SECRET`입니다.

#### 1A-3단계: 새로 고침 토큰 생성

새로 고침 토큰을 사용하면 에이전트가 사용자 상호 작용 없이 인증할 수 있습니다. 한 번 생성하면 무기한 지속됩니다(취소하지 않는 한).

**옵션 A: Google의 OAuth2 Playground 사용(가장 쉬움)**

1. **[OAuth 2.0 플레이그라운드](https://developers.google.com/oauthplayground/)**로 이동합니다.
2. **기어 아이콘** ⚙️(오른쪽 상단)을 클릭합니다.
   - **자신의 OAuth 자격 증명 사용**을 선택하세요.
   - 1A-2단계의 '클라이언트 ID'와 '클라이언트 비밀번호'를 입력하세요.
   - 설정을 닫습니다
3. 왼쪽 패널에서 **Google Ads API v18**으로 스크롤하고 → `https://www.googleapis.com/auth/adwords`를 확인하세요.
4. **API 승인**을 클릭하세요.
5. Google Ads 계정에 액세스할 수 있는 Google 계정으로 로그인하세요.
6. 요청된 권한을 부여합니다.
7. **토큰 인증 코드 교환**을 클릭하세요.
8. **새로 고침 토큰 복사** → 이것이 `GOOGLE_ADS_REFRESH_TOKEN`입니다.

**옵션 B: google-ads Python 라이브러리 사용**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```그러면 OAuth 동의를 위한 브라우저가 열리고 새로 고침 토큰이 인쇄됩니다.

**옵션 C: 컬 사용**```bash
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
```#### 1A-4단계: 로그인 고객 ID(MCC) 받기

1. **[Google Ads](https://ads.google.com)**로 이동합니다.
2. **관리자 계정**(MCC)에 로그인하세요.
3. 귀하의 **고객 ID**는 오른쪽 상단에 `XXX-XXX-XXXX` 형식으로 표시됩니다.
4. **복사** → 이것이 귀하의 `GOOGLE_ADS_LOGIN_CUSTOMER_ID`입니다.

> 💡 로그인 고객 ID는 MCC를 사용하여 여러 계정을 관리하는 경우에만 필요합니다. 단일 계정을 직접 관리하는 경우 이 항목을 비워 둘 수 있습니다.

#### 1A-5단계: 자격 증명 확인

모든 것이 작동하는지 확인하기 위해 테스트 파일을 만듭니다.```python
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
```계정 리소스 이름이 인쇄되면 Google Ads 사용자 인증 정보가 작동하는 것입니다.

---

### 1B: Cloudinary 자격 증명

Cloudinary는 크기 조정, AI 생성 채우기, 플랫폼별 형식 지정 등 모든 이미지/비디오 처리를 처리합니다.

1. **[Cloudinary 회원가입](https://cloudinary.com/users/register_free)**에 접속하여 무료 계정을 만드세요.
   - 무료 등급에는 월 25크레딧이 포함됩니다(최대 1,000개의 변환에 충분함).
2. 회원가입 후 **[대시보드](https://console.cloudinary.com/pm/getting-started/dashboard)**로 이동합니다.
3. 귀하의 자격 증명이 대시보드에 바로 표시됩니다.
   - **클라우드 이름** → `CLOUDINARY_CLOUD_NAME`
   - **API 키** → `CLOUDINARY_API_KEY`
   - **API 비밀** → `CLOUDINARY_API_SECRET`("공개"를 클릭하여 확인하세요)

> 💡 무료 등급은 개발에 넉넉합니다. 크리에이티브 처리량이 많은 제작의 경우 Plus 플랜($89/월)은 225 크레딧을 제공합니다.

#### Cloudinary가 에이전트에 연결하는 방법

**Cloudinary Creative Tools** 작업(기본 에이전트의 작업 #18)과 **Baymax — Creative Innovate** 하위 에이전트는 모두 이러한 자격 증명을 사용합니다. 이를 통해 다음이 가능해집니다.
- URL에서 이미지/비디오 업로드
- 20개 이상의 플랫폼 사전 설정(Instagram, TikTok, YouTube, 디스플레이 광고 등)에 맞게 크기 조정
- 이미지를 비표준 종횡비로 확장하기 위한 AI 생성 채우기
- 여러 플랫폼에 걸친 일괄 처리

---

### 1C: SearchAPI.io 자격 증명

SearchAPI.io는 Research & Intelligence 하위 에이전트에 실시간 Google 검색 결과, Google 트렌드 데이터, Google Ads 투명성 센터 액세스를 제공합니다.

1. **[SearchAPI.io 회원가입](https://www.searchapi.io/signup)**으로 이동합니다.
   - 무료 등급: 검색 100회/월
2. 회원가입 후 **[Dashboard → API Key](https://www.searchapi.io/dashboard)**로 이동합니다.
3. **API 키 복사** → `SEARCHAPI_API_KEY`

#### SearchAPI가 에이전트에 연결하는 방법

**Nemo — Research & Intelligence**는 세 가지 맞춤 작업을 통해 SearchAPI를 사용합니다.
- **Google 검색 API** — 광고, 자연, 지식 그래프가 포함된 실시간 SERP 결과
- **Google 광고 투명성 센터** - 경쟁업체가 게재 중인 광고 확인
- **Google 트렌드 분석기** — 동향 데이터, 관련 검색어, 지리적 관심도

이러한 작업은 각 작업의 소스 코드에서 `secrets["SEARCHAPI_API_KEY"]`를 통해 API 키를 전달합니다.

---

### 1D: Google AI/Gemini 자격 증명

Baymax — Creative Innovate는 AI 기반 이미지 생성 및 비전 분석을 위해 Google의 Gemini API를 사용합니다.

1. **[Google AI Studio](https://aistudio.google.com)**로 이동합니다.
2. Google 계정으로 로그인
3. 왼쪽 사이드바에서 **API 키 가져오기**를 클릭합니다. (또는 **[API 키](https://aistudio.google.com/apikey)**로 직접 이동합니다.)
4. **API 키 생성**을 클릭하세요.
   - 1A-2단계에서 만든 Google Cloud 프로젝트를 선택하거나 새로 만듭니다.
5. **API 키 복사** → `GOOGLE_AI_API_KEY`

> 💡 무료 등급은 Gemini 2.0 Flash에 대해 15RPM(분당 요청)을 제공합니다. 생산의 경우 종량제 요금이 매우 저렴합니다.

#### Gemini가 에이전트에 연결하는 방법

**Baymax — Creative Innovate** 하위 에이전트는 Gemini를 다음 용도로 사용합니다.
- 소셜 미디어 형식을 위한 AI 이미지 생성/확장
- 기존 크리에이티브 자산의 비전 분석
- 소스 이미지에서 유사 디스플레이 광고 생성

Gemini 작업 파일은 `actions/sub-agents/creative-innovate/02_gemini_vision.py`에 있습니다.

---

### 요약: 모든 자격 증명

1A~1D단계를 완료한 후 `.env` 파일은 다음과 같아야 합니다.```env
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

## 2단계: 주 에이전트 생성

> 이 지침에서는 일반적인 용어를 사용합니다. 특정 에이전트 플랫폼(예: OpenAI 또는 유사)에 맞게 버튼 이름/메뉴를 조정합니다.

### 2.1 — 에이전트 셸 생성

1. 에이전트 플랫폼에서 다음 설정을 사용하여 새 에이전트를 생성합니다.

| 설정 | 가치 |
|---------|---------|
| 이름 | `Google Ads API 에이전트` |
| 모델 | `claude-opus-4-5` (인류학) |
| 액세스 | 비공개 |

2. **설명 설정:**

```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — 시스템 프롬프트 붙여넣기

1. 'prompts/main_agent_system_prompt.md' 파일을 엽니다.
2. **전체 내용**을 복사하세요.
3. 에이전트의 시스템 프롬프트/지침 필드에 붙여넣기
4. 저장

### 2.3 — 내장 도구 활성화

다음 10가지 기본 제공 도구를 활성화하세요(이름은 플랫폼에 따라 다를 수 있음).

- [x] 코드 해석기
- [x] 웹 검색(Google)
- [x] 연구원
- [x] 할 일 / 작업 목록
- [x] 웹 스크레이퍼
- [x] 쿼리 실행기(SQL)
- [x] CSV 리더
- [x] 문자열 일치자
- [x] 표시 파일
- [x] 파일 검색

---

## 3단계: 맞춤 작업 설치(총 28개)

각 사용자 정의 작업은 에이전트 플랫폼의 사용자 정의 작업 빌더에 붙여넣는 Python 파일입니다. 다음을 수행해야 합니다.

1. 액션 생성
2. 소스코드 붙여넣기
3. 자격 증명(비밀) 구성

### 자격 증명 패턴 이해

4가지 자격 증명 패턴이 있습니다. 시작하기 전에 각 작업이 어떤 것을 사용하는지 알아보세요.

| 패턴 | 비밀 수 | 이를 사용한 조치 |
|---------|-------------|----|
| **A**(5개 키 Google Ads) | 5 | 12개 작업 — `LOGIN_CUSTOMER_ID`를 비밀로 포함 |
| **B**(4개 키 Google Ads) | 4 | 13개 작업 — `login_customer_id`를 함수 매개변수로 전달 |
| **C**(3키 Cloudinary) | 3 | 1개 작업 — Cloudinary 크리에이티브 도구 |
| **D** (자격 증명 없음) | 0 | 3가지 작업 — 패키지 설치 프로그램, 세션 관리자, 재구성 문서 |

자세한 내용은 [자격증명 패턴 참조](#credential-patterns-reference)를 참조하세요.

### 작업별 설치

아래의 **모든 작업**에 대해 다음 프로세스를 따르세요.```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### 패턴 A 작업(5가지 핵심 Google Ads) - 12개 작업

각각에 대해 다음 5개의 비밀을 추가하세요.

| 비밀키 | .env의 값 |
|------------|---|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | 개발자 토큰 |
| `GOOGLE_ADS_CLIENT_ID` | OAuth2 클라이언트 ID |
| `GOOGLE_ADS_CLIENT_SECRET` | OAuth2 클라이언트 비밀번호 |
| `GOOGLE_ADS_REFRESH_TOKEN` | 새로 고침 토큰 |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | 귀하의 MCC 고객 ID |

| # | 작업 이름 | 소스 파일 |
|---|-------------|------------|
| 1 | 라벨 관리자 | `actions/main-agent/01_label_manager.py` |
| 2 | 전환추적 관리자 | `actions/main-agent/02_conversion_tracking_manager.py` |
| 12 | 스크립트 관리자 | `actions/main-agent/12_scripts_manager.py` |
| 13 | 실험 관리자 | `actions/main-agent/13_experiments_manager.py` |
| 19 | 쿼리 플래너 및 예산 관리자 | `actions/main-agent/19_query_planner.py` |
| 20 | 추천 관리자 | `actions/main-agent/20_recommendations_manager.py` |
| 23 | 장치 성능 관리자 | `actions/main-agent/23_device_performance_manager.py` |
| 24 | 변경 내역 관리자 | `actions/main-agent/24_change_history_manager.py` |
| 25 | 캠페인 작성자 | `actions/main-agent/25_campaign_creator.py` |
| 26 | 광고 일정 관리자 | `actions/main-agent/26_ad_schedule_manager.py` |
| 27 | 입찰전략 관리자 | `actions/main-agent/27_bidding_strategy_manager.py` |
| 28 | PMax 자산 그룹 관리자 | `actions/main-agent/28_pmax_asset_group_manager.py` |

#### 패턴 B 작업(4가지 핵심 Google Ads) - 13개 작업

각각에 대해 다음 4가지 비밀을 추가하세요.

| 비밀키 | .env의 값 |
|------------|---|
| `개발자_토큰` | 개발자 토큰 |
| `CLIENT_ID` | OAuth2 클라이언트 ID |
| `CLIENT_SECRET` | OAuth2 클라이언트 비밀번호 |
| `새로고침_토큰` | 새로 고침 토큰 |

> ⚠️ 참고: **키 이름**은 패턴 A와 다릅니다(`GOOGLE_ADS_` 접두사 없음). 이는 의도적으로 설계된 것입니다. 이러한 작업은 대신 `login_customer_id`를 함수 매개변수로 허용합니다.

| # | 작업 이름 | 소스 파일 |
|---|-------------|------------|
| 3 | 청중 관리자 | `actions/main-agent/03_audience_manager.py` |
| 4 | 자산관리자 | `actions/main-agent/04_asset_manager.py` |
| 5 | 예산 관리자 | `actions/main-agent/05_budget_manager.py` |
| 6 | RSA 광고 관리자 | `actions/main-agent/06_rsa_ad_manager.py` |
| 7 | 입찰 및 키워드 관리자 | `actions/main-agent/07_bid_keyword_manager.py` |
| 8 | 제외 키워드 관리자 | `actions/main-agent/08_negative_keywords_manager.py` |
| 9 | 캠페인 및 광고그룹 관리자 | `actions/main-agent/09_campaign_adgroup_manager.py` |
| 10 | Google Ads 변형 | `actions/main-agent/10_google_ads_mutate.py` |
| 11 | 계정 접근 검사기 | `actions/main-agent/11_account_access_checker.py` |
| 15 | 사용자 액세스 수준 확인 | `actions/main-agent/15_check_user_access.py` |
| 16 | API 게이트웨이 - 컨텍스트 관리자 | `actions/main-agent/16_api_gateway.py` |
| 21 | 검색어 관리자 | `actions/main-agent/21_search_term_manager.py` |
| 22 | 지역 및 위치 타겟팅 관리자 | `actions/main-agent/22_geo_location_manager.py` |

#### 패턴 C 액션(3키 Cloudinary) — 액션 1개

| 비밀키 | .env의 값 |
|------------|---|
| `CLOUDINARY_CLOUD_NAME` | Cloudinary 클라우드 이름 |
| `CLOUDINARY_API_KEY` | Cloudinary API 키 |
| `CLOUDINARY_API_SECRET` | Cloudinary API 비밀 |

| # | 작업 이름 | 소스 파일 |
|---|-------------|------------|
| 18 | Cloudinary 크리에이티브 도구 | `actions/main-agent/18_cloudinary_creative_tools.py` |

#### 패턴 D 작업(자격 증명 없음) - 3개 작업

코드를 붙여넣기만 하면 됩니다. 비밀은 필요하지 않습니다.

| # | 작업 이름 | 소스 파일 |
|---|-------------|------------|
| 14 | 패키지 설치 프로그램 | `actions/main-agent/14_package_installer.py` |
| 17 | 세션 및 상태 관리자 | `actions/main-agent/17_session_state_manager.py` |

> 😀 **팁:** 플랫폼이 대량 작업 가져오기를 지원하는 경우 'configs/agent_registry.json'을 ID, 이름, 자격 증명 패턴의 정보 소스로 사용하세요.

---

## 4단계: 하위 에이전트 생성(총 6개)

각 하위 에이전트는 주 에이전트가 작업을 위임하는 별도의 에이전트입니다. 각각에는 고유한 시스템 프롬프트, 도구 및 사용자 정의 작업이 있습니다.

### 하위 에이전트 1: 보고 및 분석

| 설정 | 가치 |
|---------|---------|
| 이름 | '심바 — 보고 및 분석' |
| 모델 | `클로드-오푸스-4-5` |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/01_reporting_analytic.md` |

**사용자 정의 작업(8):** `actions/sub-agents/reporting/`에서 설치

| # | 액션 | 소스 파일 | 자격 증명 |
|---|---------|------------|-------------|
| 1 | 성과기자 | `01_performance_reporter.py` | 4키 Google Ads(패턴 B) |
| 2 | 검색어 분석기 | `02_search_terms_analyzer.py` | 4키 Google Ads(패턴 B) |
| 3 | 대화형 키워드 뷰어 | `03_interactive_keyword_viewer.py` | 4키 Google Ads(패턴 B) |
| 4 | 양방향 광고 뷰어 | `04_interactive_ad_viewer.py` | 4키 Google Ads(패턴 B) |
| 5 | 경매 통찰력 기자 | `05_auction_insights_reporter.py` | 4키 Google Ads(패턴 B) |
| 6 | 변경 내역 감사자 | `06_change_history_auditor.py` | 4키 Google Ads(패턴 B) |
| 7 | 실적 최대화(PMax) 향상된 보고 | `07_pmax_enhanced_reporting.py` | 4키 Google Ads(패턴 B) |
| 8 | 패키지 설치 프로그램 | `08_package_installer.py` | 없음(패턴 D) |

**내장 도구(9):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, reporter, google_web_search

> ⚠️ 작업 3 및 4(양방향 키워드/광고 뷰어)는 Google Ads API **v18**을 사용하고 다른 작업은 **v19**를 사용합니다. `google-ads` pip 패키지가 두 가지를 모두 지원하는지 확인하세요.

---

### 하위 에이전트 2: 연구 및 정보

| 설정 | 가치 |
|---------|---------|
| 이름 | `니모 — 연구 및 정보` |
| 모델 | `클로드-오푸스-4-5` |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/02_research_intelligence.md` |

**사용자 정의 작업(4+1):** `actions/sub-agents/research/`에서 설치

| # | 액션 | 소스 파일 | 자격 증명 |
|---|---------|------------|-------------|
| 1 | 키워드 플래너 | `01_keyword_planner.py` | 4키 Google Ads(패턴 B) |
| 2 | 구글 검색 API | `02_google_search_api.py` | 비밀 1개: `SEARCHAPI_API_KEY` |
| 3 | 광고 투명성 센터 | `03_ads_transparency_center.py` | 비밀 1개: `SEARCHAPI_API_KEY` |
| 4 | Google 트렌드 분석기 | `04_google_trends_analyzer.py` | 비밀 1개: `SEARCHAPI_API_KEY` |
| 5 | 패키지 설치 프로그램 | *(주 에이전트에서 재사용)* | 없음(패턴 D) |

**내장 도구(10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, Researcher, google_web_search, web_scraper

---

### 하위 에이전트 3: 최적화

| 설정 | 가치 |
|---------|---------|
| 이름 | `엘사 — 최적화` |
| 모델 | `클로드-오푸스-4-5` |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/03_optimization.md` |

**맞춤 작업:** ⚠️ **아직 없음**

이 하위 에이전트의 시스템 프롬프트는 구축해야 하는 두 가지 사용자 지정 작업을 참조합니다.
- **추천 관리자 - API** — `list`, `apply`, `dismiss`, `get_score`
- **대량 작업 관리자 - API** — `bulk_pause`, `bulk_enable`, `bulk_bid_change`, `bulk_budget_change`, `export`

> 🔧 **할 일:** Google Ads API를 사용하여 이러한 액션을 구축하세요. 매개변수 서명은 시스템 프롬프트 파일에 문서화되어 있습니다. 둘 다 패턴 B(4키 Google Ads) 사용자 인증 정보를 사용합니다.

**내장 도구(10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, Researcher, google_web_search, web_scraper

---

### 하위 에이전트 4: 쇼핑 및 실적 극대화

| 설정 | 가치 |
|---------|---------|
| 이름 | `알라딘 — 쇼핑 및 실적 극대화` |
| 모델 | `클로드-오푸스-4-5` |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/04_shopping_pmax.md` |

**맞춤 작업:** ⚠️ **아직 없음**

이 하위 에이전트의 시스템 프롬프트는 구축해야 하는 하나의 사용자 지정 작업을 참조합니다.
- **쇼핑 및 실적 극대화 관리자 - API** — `list_shopping`, `list_pmax`, `list_asset_groups`, `get_product_performance`, `get_pmax_performance`, `get_pmax_insights`, `pause_asset_group`, `enable_asset_group`

> 🔧 **할 일:** Google Ads API(`google-ads` Python SDK)를 사용하여 이 액션을 구축하세요. 패턴 B 자격 증명을 사용합니다. 주 에이전트의 PMax 자산 그룹 관리자(Action #28)는 이 기능 중 일부를 다루며 시작 템플릿 역할을 할 수 있습니다.**내장 도구(10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, Researcher, google_web_search, web_scraper

---

### 하위 에이전트 5: 크리에이티브

| 설정 | 가치 |
|---------|---------|
| 이름 | `모아나 — 크리에이티브` |
| 모델 | `클로드-오푸스-4-5` |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/05_creative.md` |

**사용자 정의 작업(2):** `actions/sub-agents/creative/`에서 설치

| # | 액션 | 소스 파일 | 자격 증명 |
|---|---------|------------|-------------|
| 1 | 반응형 디스플레이 광고 관리자 | `01_반응형_디스플레이_ads_manager.py` | 4키 Google Ads(패턴 B) |
| 2 | 수요 창출 광고 관리자 | `02_demand_gen_ads_manager.py` | 4키 Google Ads(패턴 B) |

**내장 도구(10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, google_web_search, reporter, web_scraper

---

### 하위 에이전트 6: Baymax — Creative Innovate

| 설정 | 가치 |
|---------|---------|
| 이름 | 'Baymax — Creative Innovate' |
| 모델 | `claude-sonnet-4-5` ⚡ *(더 가벼운 모델 — 의도적)* |
| 액세스 | 채팅 전용 |
| 시스템 프롬프트 | `프롬프트/하위 에이전트/06_creative_innovate.md` |

**사용자 정의 작업(2+1):** `actions/sub-agents/creative-innovate/`에서 설치

| # | 액션 | 소스 파일 | 자격 증명 |
|---|---------|------------|-------------|
| 1 | 구름 도구 | `01_cloudinary_tools.py` | 3키 Cloudinary(패턴 C) |
| 2 | 제미니 비전 | `02_gemini_vision.py` | 비밀번호 1개: `GOOGLE_AI_API_KEY` |
| 3 | 패키지 설치 프로그램 | *(주 에이전트에서 재사용)* | 없음(패턴 D) |

---

## 5단계: 하위 에이전트를 주 에이전트에 연결

6개의 하위 에이전트를 모두 생성한 후, 이를 메인 에이전트에 등록해야 작업을 위임할 수 있습니다.

1. **주요 에이전트** 설정으로 이동합니다.
2. **하위 에이전트** 섹션을 찾습니다.
3. 이름이나 ID를 검색하여 각 하위 에이전트를 추가합니다.

| # | 하위 에이전트 이름 | 에이전트 ID |
|---|---|----------|
| 1 | Simba — 보고 및 분석 | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Nemo — 연구 및 정보 | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 | 엘사 — 최적화 | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 | Aladdin — 쇼핑 및 실적 극대화 | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 | 모아나 — 크리에이티브 | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 | Baymax — 크리에이티브 혁신 | `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 참고: 새 에이전트를 생성하는 경우 에이전트 ID는 **다릅니다**(자동 생성됨). 위의 ID는 원본 빌드에서 가져온 것이며 참조용으로 제공됩니다.

주 에이전트의 시스템 프롬프트에는 작업을 직접 처리할 때와 위임할 때를 알려주는 **하위 에이전트 위임 프로토콜**이 포함되어 있습니다. **세션 및 상태 관리자**(작업 #17)는 핸드오프를 조정합니다.

---

## 6단계: 사용자 액세스 권한 부여

팀 구성원과 에이전트를 공유해야 하는 경우:

1. 메인에이전트 설정 → **공유/접속**으로 이동합니다.
2. **CAN_EDIT** 권한이 있는 사용자 추가
3. 에이전트를 사용하고 수정할 수 있습니다.

---

## 7단계: 검증 및 테스트

전체 시스템이 작동하는지 확인하려면 다음 테스트를 실행하세요.

### 테스트 1: 패키지 설치

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### 테스트 2: 계정 연결```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### 테스트 3: 계정 요약```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### 테스트 4: 읽기 작업```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### 테스트 5: 쓰기 작업(안전)```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### 테스트 6: 하위 에이전트 위임```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### 테스트 7: 흐림```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## 자격 증명 패턴 참조

### 패턴 A: 5가지 핵심 Google Ads

MCC 로그인 고객 ID가 비밀로 저장되는 **12가지 작업**에 사용됩니다.```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### 패턴 B: 4가지 핵심 Google Ads

로그인 고객 ID가 함수 매개변수로 전달되는 **13개 작업**에 사용됩니다.```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ **값**은 패턴 A와 동일합니다. **키 이름**만 다릅니다. 이는 일부 작업이 다른 명명 규칙으로 작성되었기 때문입니다. 기본 자격 증명은 동일합니다.

### 패턴 C: 3키 Cloudinary

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### 패턴 D: 자격 증명 없음

외부 API를 호출하지 않는 작업: 패키지 설치 프로그램, 세션 및 상태 관리자.

---

## 아키텍처 개요

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
```작업 스키마, 매개변수 서명 및 위임 흐름이 포함된 전체 기술 아키텍처는 **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**를 참조하세요.

Cloudflare Buddy 프로덕션 아키텍처(Durable Objects, Vectorize, D1, R2, Agents SDK)는 **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**를 참조하세요.

### 이 저장소를 다른 AI 에이전트와 비교하는 방법

| 기능 | 이 에이전트 | Google Ads 스크립트 | 마이크로소프트 코파일럿 | 당혹감 | 일반 클로드 |
|---------|------------|------|------|------------|---------------|
| 라이브 Google Ads API R/W | 28개 작업 | JS 전용 스크립팅 | 광고 접근 불가 | API 없음 | API 없음 |
| 쓰기 안전(CEP) | 확인/실행/게시 | 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| 다중 제공자 AI | 클로드 + GPT + 쌍둥이 자리 | 해당 없음 | GPT 전용 | 자신의 모델 | 클로드 전용 |
| 하위 대리인 위임 | 전문가 6명 | 해당 없음 | 해당 없음 | 해당 없음 | 해당 없음 |
| 의미기억 | 벡터화(prod) | 없음 | 한정 | 내장 | 대화만 |
| 자체 배포 가능 | 3가지 경로 | 스크립트 편집기 | SaaS 전용 | SaaS 전용 | API 전용 |

---

## 알려진 문제

| 이슈 | 심각도 | 세부정보 | 해결 방법 |
|-------|----------|---------|------------|
| **최적화 하위 에이전트에는 작업이 없습니다** | 🔴 중요 | 시스템 프롬프트에서는 Recommendations Manager 및 Bulk Operations Manager를 설명하지만 두 작업 모두 존재하지 않습니다. | Google Ads API를 사용하여 구축하거나 주 에이전트의 추천 관리자(#20)를 직접 사용 |
| **쇼핑 및 실적 극대화 하위 에이전트에는 작업이 없습니다** | 🔴 중요 | 시스템 프롬프트에 쇼핑 및 실적 극대화 관리자가 설명되어 있지만 조치가 없습니다. | 구축하거나 주 에이전트의 PMax Asset Group Manager(#28)를 출발점으로 사용 |
| **보고의 API 버전 불일치** | 🟡 중형 | 대화형 키워드/광고 뷰어는 v18을 사용하고 다른 보고 작업은 v19를 사용합니다 | `google-ads` pip 패키지가 두 가지를 모두 처리하는지 확인하세요. v18 작업 업그레이드를 고려해보세요 |
| **패턴 A와 B의 명명 불일치** | 🟡 낮음 | 작업 전반에 걸쳐 서로 다른 키 이름으로 저장된 동일한 자격 증명 | 동일한 값을 입력하기만 하면 됩니다. 잘 작동하지만 설정 중에 혼란스러울 뿐입니다 |

---

## 문제 해결

### "일치하는 계정을 찾을 수 없습니다..."

`resolve_customer_id()` 함수는 MCC에 속한 계정을 검색합니다. 다음을 확인하세요.
- 귀하의 'LOGIN_CUSTOMER_ID'는 하위 계정이 아닌 MCC(관리자) 계정입니다.
- 검색 중인 계정이 MCC에 연결되어 있습니다.
- 검색 문자열이 계정을 설명하는 이름의 일부와 일치합니다.

### "google-ads 패키지를 찾을 수 없습니다."

시스템 프롬프트는 모든 대화가 시작될 때 `pip install google-ads>=28.1.0`을 실행하도록 에이전트에 지시합니다. 실패한 경우:
- `code_interpreter`가 활성화되어 있는지 확인하세요.
- 첫 번째 메시지에서 수동으로 설치를 실행해 보세요.

### "OAuth 자격 증명이 만료되었습니다."

새로 고침 토큰은 일반적으로 만료되지 않지만 다음과 같은 경우 취소될 수 있습니다.
- Google 계정 비밀번호를 변경했습니다.
- [Google 보안 설정](https://myaccount.google.com/permissions)에서 앱의 접근 권한을 제거했습니다.
- 토큰이 6개월 이상 사용되지 않았습니다.

**수정:** 1A-3단계의 새로 고침 토큰 생성을 다시 실행하세요.

### "개발자 토큰이 승인되지 않았습니다."

개발자 토큰이 '테스트 계정' 모드인 경우:
- [Google Ads 테스트 계정](https://developers.google.com/google-ads/api/docs/first-call/test-accounts)에서만 작동합니다.
- [Google Ads API 센터](https://ads.google.com/aw/apicenter)에서 기본 액세스를 신청하세요.
- 승인에는 일반적으로 영업일 기준 1~3일이 소요됩니다.

### "비율 제한이 초과되었습니다."

Google Ads API에는 다음과 같은 제한이 있습니다.
- **기본 액세스:** 15,000개 작업/일, 4개 요청/초
- **표준 액세스:** 무제한 작업, 초당 100개 요청

한계에 도달하면 시스템의 필터 우선 아키텍처가 도움이 될 것입니다. `cost_min`, `status` 및 `limit` 매개변수를 사용하여 결과 세트를 줄이세요.

### 하위 에이전트가 응답하지 않음

- 주 에이전트의 하위 에이전트 목록에 하위 에이전트가 연결되어 있는지 확인하세요.
- Session & State Manager 작업(#17)이 설치되어 있는지 확인하세요.
- 하위 에이전트에 자체 자격 증명이 구성되어 있는지 확인하세요(주 에이전트와 공유하지 않음).

---

## 보안

다음 내용은 [`SECURITY.md`](SECURITY.md)를 참조하세요.
- 취약점 보고 프로세스
- CORS, 속도 제한 및 입력 유효성 검사 방식
- 자격증 관리 지침
- 안전 프로토콜 작성(CEP: 확인 → 실행 → 사후 확인)v2.0의 주요 보안 기능:
- **와일드카드 CORS 없음** — 서버 기본값은 localhost입니다. `ALLOWED_ORIGINS`를 통해 구성
- **속도 제한** — IP당 30req/min(`RATE_LIMIT_MAX`를 통해 구성 가능)
- **오류 정리** — 일반 클라이언트 오류, 전체 서버측 로깅
- **GAQL 주입 방지** — 기간 값이 화이트리스트에 추가됨
- **하드코딩된 비밀 없음** — `.env`/환경 변수를 통한 모든 것

---

## 라이선스

MIT 라이센스. 전문은 [`LICENSE`](LICENSE)를 참조하세요.

Google Ads API에는 Google [서비스 약관](https://developers.google.com/google-ads/api/docs/terms)이 적용됩니다. 제3자 서비스(Cloudinary, SearchAPI, Stripe)에는 해당 약관이 적용됩니다.

---

## 기여

전체 가이드는 [`CONTRIBUTING.md`](CONTRIBUTING.md)를 참조하세요. 우선순위 분야:

1. **최적화 하위 에이전트 작업** - 시스템 프롬프트가 존재하며 API 작업이 구축되어야 함
2. **쇼핑 및 실적 극대화 하위 에이전트 작업** — 위와 동일
3. **테스트 범위** — 배포 패키지에 대한 단위 테스트
4. **의미론적 메모리** — Buddy에서 Python으로 벡터화 메모리 포트(pgVector/Pinecone)
5. **스트리밍 응답** — 실시간 도구 실행을 위해 SSE 엔드포인트 추가```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## 관련 프로젝트

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — Claude를 위한 인류 에이전트 기술(분석, 감사, 쓰기, 수학, MCP)
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)** — Claude Code, Claude Desktop, Cursor, OpenAI Agents SDK 및 모든 MCP 클라이언트용 도구 29개가 포함된 Python MCP 서버
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)** — 22개의 MCP 도구, 기술, 명령 및 테마가 포함된 Gemini CLI 확장 프로그램
- **[googleadsagent.ai](https://googleadsagent.ai)** — 의미론적 메모리, 청구 및 모니터링 기능을 갖춘 Cloudflare에 프로덕션 배포(버디)

---

> **실시간 위치:** [googleadsagent.ai](https://googleadsagent.ai)  
> **버전:** 2.0.0  
> **라이센스:** MIT  
> **최종 업데이트:** 2026-03-05