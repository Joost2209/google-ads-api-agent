# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

Система управления Google Рекламой корпоративного уровня на базе искусственного интеллекта с **28 специальными инструментами**, **6 специализированными субагентами** и **оперативным доступом для чтения и записи** к аккаунтам Google Рекламы через Google Ads API v22.

Рабочая версия работает по адресу **[googleadsagent.ai](https://googleadsagent.ai)** (Buddy) на периферии Cloudflare — с семантической памятью, зашифрованным хранилищем ключей, автоматическим мониторингом и системой выставления счетов на основе кредитов. Этот репозиторий представляет собой агент Python с открытым исходным кодом, обладающий теми же возможностями.

---

## Что нового в версии 2.0

- **Усиление безопасности** — ограничения CORS, ограничение скорости, очистка ошибок, предотвращение внедрения GAQL.
- **Устанавливаемый пакет** — `pip install google-ads-agent` (или загрузите его из [Releases](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases))
- **Лицензия MIT** — правильное лицензирование открытого исходного кода.
- **Документация по производственной архитектуре** — полный справочник по Cloudflare Buddy в [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md).
- **Политика безопасности** — [`SECURITY.md`](SECURITY.md) с отчетами об уязвимостях и передовыми практиками.
- **Руководство для участников** — [`CONTRIBUTING.md`](CONTRIBUTING.md) с приоритетными областями и стилем кода.
- **Шаблон среды** — [`.env.example`](.env.example) со всеми заполнителями учетных данных.

Подробности смотрите в полном тексте [CHANGELOG](CHANGELOG.md).

---


## Содержание

- [Быстрый старт](#быстрыи-старт)
- [Три пути развертывания](#три-пути-развертывания)
  - [Что добавляет приятель (Путь C)](#что-добавляет-приятель-путь-c)
- [Путь А: развертывание через Anthropic API](#путь-а-развертывание-через-anthropic-api)
  - [Как это работает](#как-это-работает)
  - [A-1: получите ключ Anthropic API](#a-1-получите-ключ-anthropic-api)
  - [A-2: Установка и запуск (Python)](#a-2-установка-и-запуск-python)
  - [A-3: Использование в собственном коде](#a-3-использование-в-собственном-коде)
  - [A-7: Известные ошибки](#a-7-известные-ошибки)
  - [A-8: Пакет развертывания — ссылка на файл](#a-8-пакет-развертывания-ссылка-на-фаил)
- [Путь B: развертывание на платформе агента (пользовательский интерфейс вручную)](#путь-b-развертывание-на-платформе-агента-пользовательскии-интерфеис-вручную)
- [Предварительные условия](#предварительные-условия)
- [Шаг 1. Получите учетные данные API](#шаг-1-получите-учетные-данные-api)
  - [1A: Учетные данные API Google Рекламы](#1a-учетные-данные-api-google-рекламы)
  - [1B: Облачные учетные данные](#1b-облачные-учетные-данные)
  - [1С:SearchAPI.io Учетные данные](#1сsearchapiio-учетные-данные)
  - [1D: учетные данные Google AI/Gemini](#1d-учетные-данные-google-aigemini)
  - [Сводка: все учетные данные](#сводка-все-учетные-данные)
- [Шаг 2: Создайте главного агента](#шаг-2-создаите-главного-агента)
  - [2.1 — Создание оболочки агента](#21-создание-оболочки-агента)
  - [2.3 — Включить встроенные инструменты](#23-включить-встроенные-инструменты)
- [Шаг 3. Установите дополнительные действия (всего 28)](#шаг-3-установите-дополнительные-деиствия-всего-28)
  - [Понимание шаблонов учетных данных](#понимание-шаблонов-учетных-данных)
  - [Пошаговая установка](#пошаговая-установка)
- [Шаг 4: Создайте субагентов (всего 6)](#шаг-4-создаите-субагентов-всего-6)
  - [Субагент 1: отчетность и анализ](#субагент-1-отчетность-и-анализ)
  - [Субагент 2: Исследования и разведка](#субагент-2-исследования-и-разведка)
  - [Субагент 3: Оптимизация](#субагент-3-оптимизация)
  - [Субагент 4: Покупки и максимальная эффективность](#субагент-4-покупки-и-максимальная-эффективность)
  - [Субагент 5: Креатив](#субагент-5-креатив)
  - [Субагент 6: Бэймакс — Креативные инновации](#субагент-6-бэимакс-креативные-инновации)
- [Шаг 5: Свяжите субагенты с основным агентом](#шаг-5-свяжите-субагенты-с-основным-агентом)
- [Шаг 6. Предоставьте пользователю доступ](#шаг-6-предоставьте-пользователю-доступ)
- [Шаг 7: Проверка и тестирование](#шаг-7-проверка-и-тестирование)
  - [Тест 1: Установка пакета](#тест-1-установка-пакета)
- [Справочник по шаблонам учетных данных](#справочник-по-шаблонам-учетных-данных)
  - [Модель А: 5 ключей Google Реклама](#модель-а-5-ключеи-google-реклама)
  - [Шаблон C: 3-кнопочный Cloudinary](#шаблон-c-3-кнопочныи-cloudinary)
- [Обзор архитектуры](#обзор-архитектуры)
  - [Чем этот репозиторий отличается от других агентов ИИ](#чем-этот-репозитории-отличается-от-других-агентов-ии)
- [Известные проблемы](#известные-проблемы)
- [Устранение неполадок](#устранение-неполадок)
  - ["Не найдено ни одной подходящей учетной записи..."](#не-наидено-ни-однои-подходящеи-учетнои-записи)
  - ["пакет google-ads не найден"](#пакет-google-ads-не-наиден)
  - [«Срок действия учетных данных OAuth истек»](#срок-деиствия-учетных-данных-oauth-истек)
  - [«Токен разработчика не одобрен»](#токен-разработчика-не-одобрен)
  - ["Превышен лимит скорости"](#превышен-лимит-скорости)
  - [Субагент не отвечает](#субагент-не-отвечает)
- [Безопасность](#безопасность)
- [Лицензия](#лицензия)
- [Вклад](#вклад)
- [Похожие проекты](#похожие-проекты)

---
## Быстрый старт

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

## Три пути развертывания

| Путь | Лучшее для | Что вам нужно |
|------|----------|---------------|
| **A: Антропный API (программный)** | Производственные приложения, SaaS, конвейеры автоматизации | Антропный ключ API + Python |
| **B: Платформа агента (пользовательский интерфейс вручную)** | Быстрое прототипирование, однопользовательский, визуальный конструктор | Учетная запись агентской платформы |
| **C: Производство Cloudflare (Приятель)** | Полный стек с памятью, биллингом, мониторингом | Аккаунт Cloudflare |

**Путь A** — это то, что этот репозиторий предоставляет «из коробки». Путь C — это производственная система по адресу [googleadsagent.ai](https://googleadsagent.ai). Полную архитектуру см. в [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md).

### Что добавляет приятель (Путь C)

| Возможность | Технология |
|-----------|-----------|
| Постоянное состояние для каждого пользователя | Прочные объекты + SQLite |
| Семантическая память | Векторизовать вложения |
| Зашифрованное хранилище BYOK | AES-256-GCM |
| WebSocket в реальном времени | SDK для агентов Cloudflare |
| Автоматизированный мониторинг | Крон Рабочие |
| Кредитный биллинг | D1 + Полоса |
| Мультипровайдерный ИИ | Клод, GPT, маршрутизация Gemini |
| Экспорт файлов | Объектное хранилище R2 |

---

## Путь А: развертывание через Anthropic API

Это **программное развертывание** — без ручного пользовательского интерфейса и щелчков мышью. Все работает через API сообщений Клода с использованием инструментов.

### Как это работает

Файлы действий в этом репозитории изначально были созданы для платформы агента. Пакет `deploy/` адаптирует их для автономной работы через Anthropic API. Вот что происходит «под капотом», когда вы запускаете `python scripts/cli.py`:

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

**Что решает уровень адаптера (`tool_executor.py`):**

| Проблема | Что делают файлы действий | Что делает адаптер |
|---------|------------------------|----------------------|
| **Секреты** | Ссылка на `secrets["KEY"]` как на глобальный объект, внедренный платформой агента | Вставляет `secrets` dict в модуль `__dict__` перед `exec_module()` |
| **Установки Pip** | Запустите `subprocess.check_call(["pip", "install", "google-ads"])` во время импорта | Подпроцесс Monkey-patches для пропуска команд pip (deps уже есть в `requirements.txt`) |
| **Несоответствие параметров** | 26/28 Функции `run()` имеют явные параметры (без `**kwargs`) | Проверяет подпись `run()` через `inspect.signature()`, удаляет любые параметры, отправляемые Клодом, которых нет в функции |

### A-1: получите ключ Anthropic API

1. Перейдите в **[Anthropic Console](https://console.anthropic.com)**.
2. Зарегистрируйтесь или войдите в систему
3. Перейдите в **[Настройки → Ключи API](https://console.anthropic.com/settings/keys)**.
4. Нажмите **Создать ключ**.
5. Скопируйте ключ → это ваш `ANTHROPIC_API_KEY`

> 💡 Ключ начинается с `sk-ant-api03-...`. Храните его в надежном месте — он предоставляет полный доступ к API.

**Как это связано с системой:** Для каждого вызова API сообщений Клода требуется этот ключ в заголовке `x-api-key`. `антропный` Python SDK автоматически считывает его из `ANTHROPIC_API_KEY` env var.

### A-2: Установка и запуск (Python)

**Что происходит шаг за шагом, когда вы запускаете это:**

```bash
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

**После шага 6 вы увидите:**

```
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
```Вот и все. Агент работает, совершая реальные вызовы API Google Рекламы с использованием ваших учетных данных, а Клод определяет, какие инструменты вызывать и как интерпретировать результаты.

### A-3: Использование в собственном коде

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
```### A-4: Развертывание как REST API

Включенный сервер FastAPI предоставляет вам конечные точки HTTP для любого интерфейса или интеграции:

```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**Конечные точки:**

| Метод | Путь | Описание |
|--------|------|-------------|
| `ПОСТ` | `/чат` | Отправьте сообщение, получите ответ (сессия создается автоматически) |
| `ПОСТ` | `/сессии` | Создать новый сеанс беседы |
| `ПОЛУЧИТЬ` | `/sessions/{id}` | Получить информацию о сеансе и количество сообщений |
| `УДАЛИТЬ` | `/sessions/{id}` | Удалить сеанс |
| `ПОЛУЧИТЬ` | `/здоровье` | Проверка здоровья (статус учетных данных) |
| `ПОЛУЧИТЬ` | `/инструменты` | Список всех 28 инструментов и статус их файлов |

**Пример запроса:**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**Пример ответа:**

```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5: Развертывание с помощью Docker```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6: Рекомендации по масштабированию

| Концерн | Текущее состояние | Модернизация производства |
|---------|--------------|-------------------|
| **Сеансы** | Диктовка в памяти | Переключитесь на Redis — добавьте сервис redis в docker-compose, замените dict `sessions` на клиент Redis |
| **Ограничения ставок** | Ограничения антропного API на уровень | Добавьте очередь запросов с помощью celery или asyncio.Semaphore |
| **Мультиарендатор** | Единый набор учетных данных | Загрузка учетных данных для каждого клиента из диспетчера секретов (AWS Secrets Manager, HashiCorp Vault) |
| **Аутентификация** | Нет | Добавьте промежуточное программное обеспечение ключа API или OAuth2 на сервер FastAPI |
| **Мониторинг** | Базовое ведение журнала | Добавить структурированное журналирование + экспорт в Datadog/CloudWatch |
| **Контроль затрат** | Нет | Отслеживайте использование токенов через «response.usage» и устанавливайте оповещения о бюджете |
| **Логика повтора** | SDK по умолчанию (2 попытки) | Настройте max_retries и добавьте экспоненциальную задержку для вызовов API Google Рекламы |

### A-7: Известные ошибки

Вещи, которые могут сбить вас с толку при первом запуске:

| Выпуск | Что происходит | Исправить |
|-------|-------------|-----|
| **не удалось импортировать Google-рекламу** | Файлам действий требуется `google-ads>=28.1.0`, который имеет зависимости C | Сначала запустите `pip install -r require.txt` — именно поэтому адаптер подавляет встроенную установку pip |
| **`secrets` KeyError** | Действие пытается получить доступ к учетным данным, которые вы не указали в `.env` | Проверьте, какой шаблон учетных данных использует инструмент (A/B/C/D), и убедитесь, что в `.env` есть эти ключи |
| **Ошибка типа при запуске()** | Клод отправляет параметр, который функция run() не принимает | Фильтр параметров должен это уловить — если это не так, проверьте `python -c "из развертывания import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"` |
| **Ограничения ставок** | Базовый доступ к Google Ads API = 15 тыс. операций в день, 4 запроса в секунду | Используйте параметры Cost_min, Status, Limit для сокращения наборов результатов |
| **Первая загрузка медленная** | Загрузка модуля + подавление пипов добавляет ~1-2 секунды при первом вызове инструмента | Последующие вызовы используют кэшированные модули — мгновенно |
| **Стоимость токенов** | claude-opus-4-5 с 28 определениями инструментов = ~4 000 токенов на запрос только для инструментов | Для оптимизации затрат переключитесь на claude-sonnet-4-5-20250929 в конструкторе |

### A-8: Пакет развертывания — ссылка на файл

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

## Путь B: развертывание на платформе агента (пользовательский интерфейс вручную)

Если вы предпочитаете визуальный конструктор (OpenAI или аналогичный), выполните шаги 2–7 ниже. Вы вставите системные подсказки, код действия и учетные данные в пользовательский интерфейс платформы.

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

## Предварительные условия

Прежде чем начать, вам понадобится:

| Требование | Почему | Стоимость |
|-------------|-----|------|
| **Антропный ключ API** | Обеспечивает работу агента Claude через API сообщений | Плата за использование ([цены](https://docs.anthropic.com/en/docs/about-claude/pricing)) |
| **Аккаунт Google Рекламы** | Доступ к API для управления кампаниями | Бесплатно (реклама расходуется отдельно) |
| **Аккаунт Google Ads Manager (MCC)** | Доступ к нескольким аккаунтам | Бесплатно |
| **Проект Google Cloud Platform** | Учетные данные OAuth2 для Google Ads API | Доступен бесплатный уровень |
| **Облачный аккаунт** | Обработка изображений/видео для творческих ресурсов | Уровень бесплатного пользования (25 кредитов в месяц) |
| **Учетная запись SearchAPI.io** | Поиск в Google в режиме реального времени, тенденции, прозрачность рекламы | Уровень бесплатного пользования (100 поисков в месяц) |
| **Аккаунт Google AI Studio** | Gemini API для создания креативов с помощью ИИ | Доступен бесплатный уровень |
| **Аккаунт агентской платформы** | Где вы развертываете агент (например, OpenAI или аналогичный) | Варьируется |

---

## Шаг 1. Получите учетные данные API

Вам нужны учетные данные от **4 сервисов**. В этом разделе описывается каждый из них с точными URL-адресами, инструкциями по созданию снимков экрана и указанием того, что копировать.

---

### 1A: Учетные данные API Google Рекламы

Это самая сложная установка. Вам нужно **5 значений**, которые работают вместе:

| Полномочия | Что это такое | Где он живет |
|------------|-----------|----------------|
| `DEVELOPER_TOKEN` | Ваш ключ доступа к API от Google Рекламы | Интерфейс Google Рекламы |
| `CLIENT_ID` | Идентификатор приложения OAuth2 | Облачная консоль Google |
| `CLIENT_SECRET` | Секрет приложения OAuth2 | Облачная консоль Google |
| `REFRESH_TOKEN` | Долговечный токен OAuth2 | Создано через поток OAuth |
| `LOGIN_CUSTOMER_ID` | Идентификатор вашего аккаунта MCC | Интерфейс Google Рекламы |

#### Шаг 1A–1. Получите токен разработчика

1. Перейдите на сайт **[Google Реклама](https://ads.google.com)** и войдите в свой управляющий аккаунт (MCC).
2. Нажмите значок **Инструменты и настройки** (гаечный ключ) в верхней части навигации.
3. В разделе **Настройка** нажмите **Центр API**.
   - Если вы не видите Центр API, возможно, вам придется сначала запросить доступ.
4. Ваш **Токен разработчика** отображается на этой странице.
5. **Уровень доступа к токену:**
   - `Тестовый аккаунт` — работает только с тестовыми аккаунтами (подходит для разработки)
   - «Базовый доступ» — до 15 000 операций/день (для этого подайте заявку)
   - «Стандартный доступ» — без ограничений (применяется после подтверждения использования)
6. **Скопируйте токен** → это ваш `GOOGLE_ADS_DEVELOPER_TOKEN`.

> ⚠️ Если ваш токен имеет статус «Ожидание», вы все равно можете использовать его с тестовыми учетными записями. Для рабочей версии вам необходимо [подать заявку на базовый доступ](https://developers.google.com/google-ads/api/docs/access-levels).

#### Шаг 1A-2. Создайте учетные данные OAuth2 в Google Cloud

1. Перейдите в **[Google Cloud Console](https://console.cloud.google.com)**.
2. Создайте новый проект (или выберите существующий):
   – Нажмите раскрывающийся список проектов вверху → **Новый проект**.
   – Имя: `google-ads-agent` (или любое другое, которое вы предпочитаете).
   – Нажмите **Создать**.
3. **Включите Google Реклама API:**
   – Перейдите в раздел **[API и службы → Библиотека](https://console.cloud.google.com/apis/library)**.
   – Найдите `API Google Рекламы`.
   - Нажмите на него → Нажмите **Включить**.
4. **Настройте экран согласия OAuth:**
   – Перейдите в раздел **[API и службы → Экран согласия OAuth](https://console.cloud.google.com/apis/credentials/consent)**.
   – Выберите **Внешний** (если у вас нет Google Workspace, затем Внутренний).
   - Заполните:
     – Название приложения: «Агент Google Рекламы».
     - Адрес электронной почты службы поддержки пользователей: ваш адрес электронной почты.
     - Контактное лицо разработчика: ваш адрес электронной почты.
   – Нажмите **Сохранить и продолжить**.
   - **Области действия.** Нажмите **Добавить или удалить области** → найдите `Google Реклама API` → проверьте `https://www.googleapis.com/auth/adwords` → **Обновить** → **Сохранить и продолжить**
   – **Тестовые пользователи:** добавьте адрес электронной почты своего аккаунта Google Рекламы → **Сохранить и продолжить**
   – Нажмите **Вернуться на панель управления**.
5. **Создайте идентификатор клиента OAuth2:**
   – Перейдите в раздел **[API и службы → Учетные данные](https://console.cloud.google.com/apis/credentials)**.
   – Нажмите **+ Создать учетные данные** → **Идентификатор клиента OAuth**.
   - Тип приложения: **Веб-приложение**.
   – Имя: `Агент Google Рекламы`
   – Авторизованные URI перенаправления: добавьте `http://localhost:8080` (необходим для этапа создания токена).
   – Нажмите **Создать**.
   - **Скопируйте идентификатор клиента** → это ваш `GOOGLE_ADS_CLIENT_ID`- **Скопируйте секрет клиента** → это ваш `GOOGLE_ADS_CLIENT_SECRET`

#### Шаг 1A–3. Создайте токен обновления

Токен обновления позволяет агенту проходить проверку подлинности без взаимодействия с пользователем. Вы создаете его один раз, и он действует неопределенное время (если не отозван).

**Вариант А: использование Google OAuth2 Playground (самый простой)**

1. Перейдите на страницу **[Площадка OAuth 2.0](https://developers.google.com/oauthplayground/)**.
2. Нажмите **значок шестеренки** ⚙️ (вверху справа).
   – Установите флажок **Использовать собственные учетные данные OAuth**.
   – Введите свой «Идентификатор клиента» и «Секрет клиента», полученные на шаге 1A–2.
   - Закройте настройки
3. На левой панели прокрутите до **Google Ads API v18** → установите флажок https://www.googleapis.com/auth/adwords`.
4. Нажмите **Авторизовать API**.
5. Войдите в систему, используя учетную запись Google, которая имеет доступ к вашим учетным записям Google Рекламы.
6. Предоставьте запрошенные разрешения
7. Нажмите **Обменять код авторизации на токены**.
8. **Скопируйте токен обновления** → это ваш `GOOGLE_ADS_REFRESH_TOKEN`

**Вариант Б. Использование библиотеки Python для Google Рекламы**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```При этом открывается браузер для получения согласия OAuth и печатается токен обновления.

**Вариант C: Использование завитка**```bash
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
```#### Шаг 1A–4. Получите идентификатор клиента для входа (MCC)

1. Перейдите на страницу **[Google Реклама](https://ads.google.com)**.
2. Войдите в свой **Управляющий аккаунт** (MCC).
3. Ваш **Идентификатор клиента** отображается в правом верхнем углу в формате «XXX-XXX-XXXX».
4. **Скопируйте** → это ваш `GOOGLE_ADS_LOGIN_CUSTOMER_ID`

> 💡 Идентификатор клиента для входа необходим только в том случае, если вы используете MCC для управления несколькими учетными записями. Если вы напрямую управляете одной учетной записью, вы можете оставить это поле пустым.

#### Шаг 1A-5. Проверьте свои учетные данные

Создайте тестовый файл, чтобы убедиться, что все работает:

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
```Если при этом печатаются имена ресурсов учетной записи, ваши учетные данные Google Рекламы работают.

---

### 1B: Облачные учетные данные

Cloudinary берет на себя всю обработку изображений и видео — изменение размера, генеративную заливку с помощью искусственного интеллекта, форматирование для конкретной платформы.

1. Перейдите на страницу **[Регистрация Cloudinary](https://cloudinary.com/users/register_free)** и создайте бесплатную учетную запись.
   - Уровень бесплатного пользования включает 25 кредитов в месяц (достаточно для ~ 1000 преобразований)
2. После регистрации перейдите на **[Панель управления](https://console.cloudinary.com/pm/getting-started/dashboard)**.
3. Ваши учетные данные отображаются прямо на панели управления:
   - **Имя облака** → `CLOUDINARY_CLOUD_NAME`
   - **Ключ API** → `CLOUDINARY_API_KEY`
   - **Секрет API** → `CLOUDINARY_API_SECRET` (нажмите «Показать», чтобы увидеть его)

> 💡 Бесплатный уровень щедр на развитие. Для производства с тяжелой творческой обработкой план Plus (89 долларов США в месяц) дает 225 кредитов.

#### Как Cloudinary подключается к агенту

Действие **Cloudinary Creative Tools** (действие № 18 на главном агенте) и субагент **Baymax — Creative Innovate** используют эти учетные данные. Они позволяют:
- Загрузка изображений/видео с URL-адресов.
- Изменение размера для более чем 20 пресетов платформ (Instagram, TikTok, YouTube, медийная реклама и т. д.)
- Генеративная заливка AI для расширения изображений до нестандартных соотношений сторон.
- Пакетная обработка на нескольких платформах.

---

### 1С:SearchAPI.io Учетные данные

SearchAPI.io предоставляет результаты поиска Google в режиме реального времени, данные Google Trends и доступ к Центру прозрачности Google Рекламы для субагента Research & Intelligence.

1. Перейдите на страницу **[Регистрация SearchAPI.io](https://www.searchapi.io/signup)**.
   - Уровень бесплатного пользования: 100 поисков в месяц.
2. После регистрации перейдите в **[Панель управления → Ключ API](https://www.searchapi.io/dashboard)**.
3. **Скопируйте ключ API** → `SEARCHAPI_API_KEY`

#### Как SearchAPI подключается к агенту

**Nemo — Research & Intelligence** использует SearchAPI посредством трёх настраиваемых действий:
- **Google Search API** — результаты поисковой выдачи в реальном времени с рекламой, органическими данными и графиком знаний.
- **Центр прозрачности Google Рекламы** — узнайте, какую рекламу показывают конкуренты.
- **Анализатор Google Trends** — данные о тенденциях, связанных запросах, географических интересах.

Эти действия передают ключ API через `secrets["SEARCHAPI_API_KEY"]` в исходном коде каждого действия.

---

### 1D: учетные данные Google AI/Gemini

Baymax — Creative Innovate использует API Gemini от Google для генерации изображений и анализа изображения с помощью искусственного интеллекта.

1. Перейдите в **[Google AI Studio](https://aistudio.google.com)**.
2. Войдите в свою учетную запись Google.
3. Нажмите **Получить ключ API** на левой боковой панели (или перейдите непосредственно к **[Ключи API](https://aistudio.google.com/apikey)**).
4. Нажмите **Создать ключ API**.
   – Выберите проект Google Cloud, созданный на шаге 1A–2 (или создайте новый).
5. **Скопируйте ключ API** → `GOOGLE_AI_API_KEY`

> 💡 Уровень бесплатного пользования обеспечивает 15 об/мин (запросов в минуту) для Gemini 2.0 Flash. Для производства ставка оплаты по мере использования очень доступна.

#### Как Gemini подключается к агенту

Субагент **Baymax — Creative Innovate** использует Gemini для:
- Генерация/расширение изображений AI для форматов социальных сетей
- Анализ видения существующих творческих активов.
– Создание вариантов медийных объявлений на основе исходных изображений.

Файл действий Gemini находится по адресу `actions/sub-agents/creative-innovate/02_gemini_vision.py`.

---

### Сводка: все учетные данные

После выполнения шагов 1A–1D ваш файл `.env` должен выглядеть так:

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

## Шаг 2: Создайте главного агента

> В этих инструкциях используется общая терминология. Адаптируйте названия кнопок/меню для вашей конкретной агентской платформы (например, OpenAI или аналогичной).

### 2.1 — Создание оболочки агента

1. На вашей агентской платформе создайте нового агента со следующими настройками:

| Настройка | Значение |
|---------|-------|
| Имя | `Агент API Google Рекламы` |
| Модель | `claude-opus-4-5` (Антропный) |
| Доступ | Частное |

2. **Установите описание:**

```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — Вставьте системную подсказку

1. Откройте файл: `prompts/main_agent_system_prompt.md`
2. Скопируйте **все содержимое**
3. Вставьте в поле системной подсказки/инструкций вашего агента.
4. Сохранить

### 2.3 — Включить встроенные инструменты

Включите эти 10 встроенных инструментов (названия могут различаться в зависимости от платформы):

- [x] Интерпретатор кода
- [x] Веб-поиск (Google)
- [x] Исследователь
- [x] Todo/Список задач
- [x] Веб-скребок
- [x] Исполнитель запросов (SQL)
- [x] Чтение CSV
- [x] Сопоставление строк
- [x] Показать файл
- [x] Поиск файлов

---

## Шаг 3. Установите дополнительные действия (всего 28)

Каждое настраиваемое действие представляет собой файл Python, который вставляется в конструктор настраиваемых действий вашей платформы агента. Вам нужно будет:

1. Создайте действие
2. Вставьте исходный код
3. Настройте учетные данные (секреты)

### Понимание шаблонов учетных данных

Существует 4 шаблона учетных данных. Прежде чем начать, узнайте, какой из них используется в каждом действии:

| Узор | Количество секретов | Действия с его использованием |
|---------|-------------|-----------------|
| **A** (5 ключей Google Реклама) | 5 | 12 действий — включая `LOGIN_CUSTOMER_ID` в качестве секрета |
| **B** (4-клавишная реклама Google) | 4 | 13 действий — передает `login_customer_id` как параметр функции |
| **C** (3-клавишный Cloudinary) | 3 | 1 действие — Cloudinary Creative Tools |
| **D** (Нет учетных данных) | 0 | 3 действия — Установщик пакетов, Менеджер сеансов, Документ реконструкции |

Подробную информацию см. в [Справочнике по шаблонам учетных данных](#credential-patterns-reference).

### Пошаговая установка

Для **каждого действия** ниже выполните следующую процедуру:

```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### Действия по шаблону A (5-ключевая реклама Google) — 12 действий

Для каждого добавьте эти 5 секретов:

| Секретный ключ | Значение из .env |
|------------|----------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Ваш токен разработчика |
| `GOOGLE_ADS_CLIENT_ID` | Ваш идентификатор клиента OAuth2 |
| `GOOGLE_ADS_CLIENT_SECRET` | Секрет вашего клиента OAuth2 |
| `GOOGLE_ADS_REFRESH_TOKEN` | Ваш токен обновления |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Ваш идентификатор клиента MCC |

| # | Название действия | Исходный файл |
|---|-------------|------------|
| 1 | Менеджер этикеток | `действия/main-agent/01_label_manager.py` |
| 2 | Менеджер отслеживания конверсий | `actions/main-agent/02_conversion_tracking_manager.py` |
| 12 | Менеджер скриптов | `actions/main-agent/12_scripts_manager.py` |
| 13 | Менеджер экспериментов | `actions/main-agent/13_experiments_manager.py` |
| 19 | Планировщик запросов и менеджер бюджета | `actions/main-agent/19_query_planner.py` |
| 20 | Менеджер по рекомендациям | `actions/main-agent/20_recommendations_manager.py` |
| 23 | Диспетчер производительности устройств | `actions/main-agent/23_device_ Performance_manager.py` |
| 24 | Менеджер истории изменений | `actions/main-agent/24_change_history_manager.py` |
| 25 | Создатель кампании | `actions/main-agent/25_campaign_creator.py` |
| 26 | Менеджер расписания объявлений | `actions/main-agent/26_ad_schedule_manager.py` |
| 27 | Менеджер по стратегии торгов | `actions/main-agent/27_bidding_strategy_manager.py` |
| 28 | Менеджер группы активов PMax | `actions/main-agent/28_pmax_asset_group_manager.py` |

#### Действия по шаблону B (4-клавишная реклама Google) — 13 действий

Для каждого добавьте эти 4 секрета:

| Секретный ключ | Значение из .env |
|------------|----------------|
| `DEVELOPER_TOKEN` | Ваш токен разработчика |
| `CLIENT_ID` | Ваш идентификатор клиента OAuth2 |
| `CLIENT_SECRET` | Секрет вашего клиента OAuth2 |
| `REFRESH_TOKEN` | Ваш токен обновления |

> ⚠️ Примечание. **названия клавиш** отличаются от шаблона A (без префикса `GOOGLE_ADS_`). Это сделано специально — вместо этого эти действия принимают `login_customer_id` в качестве параметра функции.

| # | Название действия | Исходный файл |
|---|-------------|------------|
| 3 | Менеджер аудитории | `действия/main-agent/03_audience_manager.py` |
| 4 | Менеджер активов | `действия/main-agent/04_asset_manager.py` |
| 5 | Бюджетный менеджер | `действия/main-agent/05_budget_manager.py` |
| 6 | Менеджер рекламы RSA | `actions/main-agent/06_rsa_ad_manager.py` |
| 7 | Менеджер ставок и ключевых слов | `actions/main-agent/07_bid_keyword_manager.py` |
| 8 | Менеджер минус-слов | `actions/main-agent/08_negative_keywords_manager.py` |
| 9 | Менеджер кампаний и групп объявлений | `actions/main-agent/09_campaign_adgroup_manager.py` |
| 10 | Изменение Google Рекламы | `actions/main-agent/10_google_ads_mutate.py` |
| 11 | Проверка доступа к учетной записи | `actions/main-agent/11_account_access_checker.py` |
| 15 | Проверьте уровни доступа пользователей | `actions/main-agent/15_check_user_access.py` |
| 16 | API-шлюз — Контекстный менеджер | `действия/main-agent/16_api_gateway.py` |
| 21 | Менеджер поисковых запросов | `actions/main-agent/21_search_term_manager.py` |
| 22 | Менеджер геотаргетинга и геотаргетинга | `actions/main-agent/22_geo_location_manager.py` |

#### Действие шаблона C (3-клавишный Cloudinary) — 1 действие

| Секретный ключ | Значение из .env |
|------------|----------------|
| `CLOUDINARY_CLOUD_NAME` | Имя вашего облака Cloudinary |
| `CLOUDINARY_API_KEY` | Ваш ключ Cloudinary API |
| `CLOUDINARY_API_SECRET` | Ваш секрет Cloudinary API |

| # | Название действия | Исходный файл |
|---|-------------|------------|
| 18 | Cloudinary инструменты для творчества | `actions/main-agent/18_cloudinary_creative_tools.py` |

#### Действия шаблона D (без учетных данных) — 3 действия

Просто вставьте код — никаких секретов не нужно.

| # | Название действия | Исходный файл |
|---|-------------|------------|
| 14 | Установщик пакетов | `actions/main-agent/14_package_installer.py` |
| 17 | Менеджер сеансов и состояний | `actions/main-agent/17_session_state_manager.py` |

> 📌 **Совет.** Если ваша платформа поддерживает массовый импорт действий, используйте `configs/agent_registry.json` в качестве источника достоверных данных для идентификаторов, имен и шаблонов учетных данных.

---

## Шаг 4: Создайте субагентов (всего 6)

Каждый субагент — это отдельный агент, которому главный агент делегирует задачи. У каждого из них есть своя собственная системная подсказка, инструменты и настраиваемые действия.

### Субагент 1: отчетность и анализ

| Настройка | Значение |
|---------|-------|
| Имя | `Симба — Отчетность и анализ` |
| Модель | `Клод-опус-4-5` |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `prompts/sub-agents/01_reporting_anaанализ.md` |

**Пользовательские действия (8):** Установка из `actions/sub-agents/reporting/`

| # | Действие | Исходный файл | Полномочия |
|---|--------|-----------|-------------|
| 1 | Репортер производительности | `01_ Performance_reporter.py` | 4-ключевая реклама Google (шаблон Б) |
| 2 | Анализатор поисковых запросов | `02_search_terms_analyzer.py` | 4-ключевая реклама Google (шаблон Б) |
| 3 | Интерактивный просмотрщик ключевых слов | `03_interactive_keyword_viewer.py` | 4-ключевая реклама Google (шаблон Б) |
| 4 | Интерактивный просмотрщик рекламы | `04_interactive_ad_viewer.py` | 4-ключевая реклама Google (шаблон Б) |
| 5 | Репортер аукционной информации | `05_auction_insights_reporter.py` | 4-ключевая реклама Google (шаблон Б) |
| 6 | Аудитор истории изменений | `06_change_history_auditor.py` | 4-ключевая реклама Google (шаблон Б) |
| 7 | Расширенные отчеты PMax | `07_pmax_enhanced_reporting.py` | 4-ключевая реклама Google (шаблон Б) |
| 8 | Установщик пакетов | `08_package_installer.py` | Нет (Шаблон D) |

**Встроенные инструменты (9):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, Browser_use, Researcher, google_web_search

> ⚠️ Действия 3 и 4 (Интерактивные средства просмотра ключевых слов/рекламы) используют Google Ads API **v18**, а остальные используют **v19**. Убедитесь, что пакет pip `google-ads` поддерживает оба варианта.

---

### Субагент 2: Исследования и разведка

| Настройка | Значение |
|---------|-------|
| Имя | `Немо — Исследования и разведка` |
| Модель | `Клод-опус-4-5` |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `подсказки/субагенты/02_research_intelligence.md` |

**Пользовательские действия (4+1):** Установка из `actions/sub-agents/research/`

| # | Действие | Исходный файл | Полномочия |
|---|--------|-----------|-------------|
| 1 | Планировщик ключевых слов | `01_keyword_planner.py` | 4-ключевая реклама Google (шаблон Б) |
| 2 | API поиска Google | `02_google_search_api.py` | 1 секрет: `SEARCHAPI_API_KEY` |
| 3 | Центр прозрачности рекламы | `03_ads_transparency_center.py` | 1 секрет: `SEARCHAPI_API_KEY` |
| 4 | Анализатор тенденций Google | `04_google_trends_analyzer.py` | 1 секрет: `SEARCHAPI_API_KEY` |
| 5 | Установщик пакетов | *(повторное использование из основного агента)* | Нет (Шаблон D) |

**Встроенные инструменты (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, Browser_use, Researcher, google_web_search, web_scraper

---

### Субагент 3: Оптимизация

| Настройка | Значение |
|---------|-------|
| Имя | `Эльза — Оптимизация` |
| Модель | `Клод-опус-4-5` |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `подсказки/субагенты/03_optimization.md` |

**Пользовательские действия:** ⚠️ **ЕЩЁ НЕ СУЩЕСТВУЕТ**

Системное приглашение этого субагента ссылается на два дополнительных действия, которые необходимо создать:
- **Менеджер рекомендаций - API** — `list`, `apply`, `dismiss`, `get_score`
- **Менеджер массовых операций - API** — `bulk_pause`, `bulk_enable`, `bulk_bid_change`, `bulk_budget_change`, `export`

> 🔧 **ЗАДАЧА:** Создайте эти действия с помощью API Google Рекламы. Сигнатуры параметров документированы в файле системных подсказок. Оба будут использовать учетные данные шаблона B (4-ключевая реклама Google).

**Встроенные инструменты (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, Browser_use, Researcher, google_web_search, web_scraper

---

### Субагент 4: Покупки и максимальная эффективность

| Настройка | Значение |
|---------|-------|
| Имя | `Аладдин — Шоппинг и PMax` |
| Модель | `Клод-опус-4-5` |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `подсказки/субагенты/04_shopping_pmax.md` |

**Пользовательские действия:** ⚠️ **ЕЩЁ НЕ СУЩЕСТВУЕТ**

Системное приглашение этого субагента ссылается на одно настраиваемое действие, которое необходимо создать:
- **Shopping & PMax Manager – API** — `list_shopping`, `list_pmax`, `list_asset_groups`, `get_product_ Performance`, `get_pmax_ Performance`, `get_pmax_insights`, `pause_asset_group`, `enable_asset_group`

> 🔧 **ЗАДАЧА:** Создайте это действие с помощью Google Ads API (Google-ads` Python SDK). Буду использовать учетные данные шаблона B. Диспетчер групп активов PMax основного агента (действие № 28) охватывает некоторые из этих функций и может служить стартовым шаблоном.**Встроенные инструменты (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, Browser_use, Researcher, google_web_search, web_scraper

---

### Субагент 5: Креатив

| Настройка | Значение |
|---------|-------|
| Имя | `Моана — Креатив` |
| Модель | `Клод-опус-4-5` |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `подсказки/субагенты/05_creative.md` |

**Пользовательские действия (2):** Установка из `actions/sub-agents/creative/`

| # | Действие | Исходный файл | Полномочия |
|---|--------|-----------|-------------|
| 1 | Менеджер адаптивной медийной рекламы | `01_Response_display_ads_manager.py` | 4-ключевая реклама Google (шаблон Б) |
| 2 | Менеджер по формированию спроса | `02_demand_gen_ads_manager.py` | 4-ключевая реклама Google (шаблон Б) |

**Встроенные инструменты (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, Browser_use, google_web_search, исследователь, web_scraper

---

### Субагент 6: Бэймакс — Креативные инновации

| Настройка | Значение |
|---------|-------|
| Имя | `Бэймакс — Креативные инновации` |
| Модель | `claude-sonnet-4-5` ⚡ *(более легкая модель — намеренно)* |
| Доступ | ТОЛЬКО ЧАТ |
| Системная подсказка | `подсказки/субагенты/06_creative_innovate.md` |

**Пользовательские действия (2+1):** Установка из `actions/sub-agents/creative-innovate/`

| # | Действие | Исходный файл | Полномочия |
|---|--------|-----------|-------------|
| 1 | Облачные инструменты | `01_cloudinary_tools.py` | 3-клавишный Cloudinary (схема C) |
| 2 | Близнецы Видение | `02_gemini_vision.py` | 1 секрет: `GOOGLE_AI_API_KEY` |
| 3 | Установщик пакетов | *(повторное использование из основного агента)* | Нет (Шаблон D) |

---

## Шаг 5: Свяжите субагенты с основным агентом

После создания всех 6 субагентов вам необходимо зарегистрировать их в главном агенте, чтобы он мог делегировать задачи.

1. Зайдите в настройки **Главного агента**.
2. Найдите раздел **Субагенты**.
3. Добавьте каждого субагента, выполнив поиск по его имени или идентификатору:

| # | Имя субагента | Идентификатор агента |
|---|----------------|----------|
| 1 | Симба — Отчетность и анализ | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Немо — Исследования и разведка | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 | Эльза — Оптимизация | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 | Аладдин — Шопинг и PМакс | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 | Моана — Креатив | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 | Бэймакс — Креативные инновации | `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 Примечание. Идентификаторы агентов будут **другими**, если вы создаете новых агентов (они генерируются автоматически). Приведенные выше идентификаторы взяты из исходной сборки и предоставлены для справки.

Системное приглашение главного агента включает **Протокол делегирования субагента**, который сообщает ему, когда обрабатывать задачи напрямую, а когда делегировать. **Менеджер сеансов и состояний** (Действие № 17) координирует передачу обслуживания.

---

## Шаг 6. Предоставьте пользователю доступ

Если вам нужно поделиться агентом с членами команды:

1. Зайдите в настройки Главного Агента → **Общий доступ/Доступ**.
2. Добавьте пользователей с разрешением **CAN_EDIT**.
3. Они смогут использовать и модифицировать агент.

---

## Шаг 7: Проверка и тестирование

Запустите эти тесты, чтобы убедиться, что вся система работает:

### Тест 1: Установка пакета

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### Тест 2: подключение учетной записи```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### Тест 3: Сводная информация об аккаунте```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### Тест 4: операция чтения```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### Тест 5: Операция записи (безопасно)```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### Тест 6: Делегирование субагента```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### Тест 7: Cloudinary```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## Справочник по шаблонам учетных данных

### Модель А: 5 ключей Google Реклама

Используется **12 действиями**, где идентификатор клиента для входа в MCC хранится в секрете.```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### Модель Б: 4-ключевая реклама Google

Используется **13 действиями**, где идентификатор клиента для входа передается в качестве параметра функции.```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ **значения** идентичны шаблону A. Отличаются только **названия клавиш**. Это связано с тем, что некоторые действия были написаны с использованием других соглашений об именах. Базовые учетные данные те же.

### Шаблон C: 3-кнопочный Cloudinary

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### Шаблон D: нет учетных данных

Действия, которые не вызывают внешние API: установщик пакетов, диспетчер сеансов и состояний.

---

## Обзор архитектуры

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
```Полную техническую архитектуру со схемами действий, подписями параметров и потоком делегирования см. в **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

Информацию о производственной архитектуре Cloudflare Buddy (Durable Objects, Vectorize, D1, R2, Agents SDK) см. в **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**.

### Чем этот репозиторий отличается от других агентов ИИ

| Особенность | Этот агент | Скрипты Google Рекламы | Microsoft второй пилот | Растерянность | Дженерик Клод |
|---------|-----------|-------------------|-------------------|------------|---------------|
| Живой API Google Рекламы для чтения и записи | 28 действий | Скрипты только на JS | Нет доступа к рекламе | Нет API | Нет API |
| Безопасность записи (CEP) | Подтвердить/Выполнить/Опубликовать | Нет | Н/Д | Н/Д | Н/Д |
| Мультипровайдерный ИИ | Клод + GPT + Близнецы | Н/Д | только GPT | Собственные модели | Только Клод |
| Делегирование субагента | 6 специалистов | Н/Д | Н/Д | Н/Д | Н/Д |
| Семантическая память | Векторизация (прод) | Нет | Ограниченная | Встроенный | Только разговор |
| Саморазвертывающийся | 3 пути | Редактор сценариев | Только SaaS | Только SaaS | только API |

---

## Известные проблемы

| Выпуск | Серьезность | Подробности | Обходной путь |
|-------|----------|---------|------------|
| **Субагент оптимизации не выполняет никаких действий** | 🔴 Критический | Системное приглашение описывает Диспетчер рекомендаций и Диспетчер массовых операций, но ни одно из действий не существует | Создайте их с помощью Google Ads API или напрямую используйте Менеджер рекомендаций основного агента (#20) |
| **Субагент Shopping & PMax не выполняет никаких действий** | 🔴 Критический | Системное приглашение описывает Shopping & PMax Manager, но никаких действий не существует | Создайте его или используйте диспетчер групп активов PMax основного агента (#28) в качестве отправной точки |
| **Несоответствие версии API в отчетах** | 🟡 Средний | Интерактивные средства просмотра ключевых слов и рекламы используют версию 18, другие действия по созданию отчетов используют версию 19 | Убедитесь, что пакет pip `google-ads` обрабатывает оба варианта; рассмотреть возможность обновления действий v18 |
| **Несоответствие именования шаблонов A и B** | 🟡 Низкий | Одни и те же учетные данные хранятся под разными именами ключей для разных действий | Просто введите те же значения — работает нормально, только запутывает при настройке |

---

## Устранение неполадок

### "Не найдено ни одной подходящей учетной записи..."

Функция `resolve_customer_id()` ищет учетные записи в вашем MCC. Убедитесь:
– Ваш `LOGIN_CUSTOMER_ID` — это учетная запись MCC (управляющего), а не дочерняя учетная запись.
– Аккаунт, который вы ищете, связан с вашим MCC.
– Строка поиска соответствует части описательного имени учетной записи.

### "пакет google-ads не найден"

Системная подсказка инструктирует агента запускать `pip install google-ads>=28.1.0` в начале каждого разговора. Если это не удается:
- Убедитесь, что `code_interpreter` включен.
- Попробуйте запустить установку вручную в первом сообщении

### «Срок действия учетных данных OAuth истек»

Токены обновления обычно не имеют срока действия, но их можно отозвать, если:
- Вы изменили пароль своей учетной записи Google.
– Вы удалили доступ к приложению в [Настройках безопасности Google](https://myaccount.google.com/permissions).
- Токен не использовался более 6 месяцев.

**Исправление.** Повторно запустите создание токена обновления, начиная с шага 1A–3.

### «Токен разработчика не одобрен»

Если ваш токен разработчика находится в режиме «Тестовая учетная запись»:
– Работает только с [тестовыми аккаунтами Google Рекламы](https://developers.google.com/google-ads/api/docs/first-call/test-accounts).
– Подайте заявку на базовый доступ в [Центре API Google Рекламы](https://ads.google.com/aw/apicenter).
- Одобрение обычно занимает 1-3 рабочих дня.

### "Превышен лимит скорости"

API Google Рекламы имеет следующие ограничения:
- **Базовый доступ:** 15 000 операций в день, 4 запроса в секунду.
- **Стандартный доступ:** Неограниченное количество операций, 100 запросов в секунду.

При превышении лимитов должна помочь системная архитектура Filter-First — используйте параметры Cost_min, Status и Limit, чтобы сократить наборы результатов.

### Субагент не отвечает

- Убедитесь, что субагент связан в списке субагентов основного агента.
- Убедитесь, что действие диспетчера сеансов и состояний (# 17) установлено.
- Убедитесь, что у субагента настроены собственные учетные данные (они не используются совместно с основным агентом).

---

## Безопасность

См. [`SECURITY.md`](SECURITY.md) для:
- Процесс сообщения об уязвимостях
- CORS, ограничение скорости и методы проверки входных данных.
- Рекомендации по управлению учетными данными
- Написать протокол безопасности (CEP: Подтвердить → Выполнить → Пост-проверка)Ключевые функции безопасности в версии 2.0:
- **Нет подстановочного знака CORS** — по умолчанию используется локальный хост; настроить через `ALLOWED_ORIGINS`
- **Ограничение скорости** — 30 запросов/мин на один IP (настраивается через `RATE_LIMIT_MAX`)
- **Очистка ошибок** — общие ошибки клиента, полное журналирование на стороне сервера.
- **Предотвращение внедрения GAQL** — значения периода внесены в белый список.
- **Нет жестко запрограммированных секретов** — все через `.env`/переменные среды

---

## Лицензия

Лицензия МТИ. Полный текст см. в [`LICENSE`](LICENSE).

API Google Рекламы регулируется [Условиями обслуживания] Google(https://developers.google.com/google-ads/api/docs/terms). Сторонние сервисы (Cloudinary, SearchAPI, Stripe) регулируются соответствующими условиями.

---

## Вклад

Полное руководство см. в [`CONTRIBUTING.md`](CONTRIBUTING.md). Приоритетные направления:

1. **Действия субагента оптимизации** — системное приглашение существует, необходимо создать действия API
2. **Действия субагента «Покупки и максимальная эффективность»** — то же, что указано выше.
3. **Тестовое покрытие** — модульные тесты для пакета развертывания.
4. **Семантическая память** — перенос векторизации памяти из Buddy в Python (pgvector/Pinecone).
5. **Потоковая передача ответов** — добавьте конечную точку SSE для выполнения инструмента в реальном времени.```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## Похожие проекты

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — антропные навыки агента для Клода (анализ, аудит, письмо, математика, MCP)
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)** — сервер Python MCP с 29 инструментами для Claude Code, Claude Desktop, Cursor, OpenAI Agents SDK и любого клиента MCP.
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)** — расширение Gemini CLI с 22 инструментами MCP, навыками, командами и темами.
- **[googleadsagent.ai](https://googleadsagent.ai)** — производственное развертывание (Buddy) на Cloudflare с семантической памятью, выставлением счетов и мониторингом.

---

> **Прямая трансляция по адресу:** [googleadsagent.ai](https://googleadsagent.ai)  
> **Версия:** 2.0.0  
> **Лицензия:** MIT  
> **Последнее обновление:** 5 марта 2026 г.