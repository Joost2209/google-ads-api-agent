# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

Een AI-aangedreven Google Ads-beheersysteem op bedrijfsniveau met **28 aangepaste tools**, **6 gespecialiseerde sub-agents** en **live lees-/schrijftoegang** tot Google Ads-accounts via de Google Ads API v22.

De productieversie draait op **[googleadsagent.ai](https://googleadsagent.ai)** (Buddy) aan de rand van Cloudflare – met semantisch geheugen, gecodeerde sleutelopslag, geautomatiseerde monitoring en een op krediet gebaseerd factureringssysteem. Deze opslagplaats is de open-source Python-agent die dezelfde mogelijkheden biedt.

---

## Wat is er nieuw in v2.0

- **Verscherping van de beveiliging** — CORS-beperkingen, snelheidsbeperking, opschoning van fouten, preventie van GAQL-injectie
- **Installeerbaar pakket** — `pip install google-ads-agent` (of download van [Releases](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases))
- **MIT-licentie** — juiste open-sourcelicenties
- **Productiearchitectuurdocumenten** — volledige Cloudflare Buddy-referentie in [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md)
- **Beveiligingsbeleid** — [`SECURITY.md`](SECURITY.md) met rapportage van kwetsbaarheden en best practices
- **Bijdragergids** — [`CONTRIBUTING.md`](CONTRIBUTING.md) met prioriteitsgebieden en codestijl
- **Omgevingssjabloon** — [`.env.example`](.env.example) met alle tijdelijke aanduidingen voor referenties

Zie de volledige [CHANGELOG](CHANGELOG.md) voor details.

---


## Inhoudsopgave

- [Snelle start](#snelle-start)
- [Drie implementatiepaden](#drie-implementatiepaden)
  - [Wat Buddy toevoegt (pad C)](#wat-buddy-toevoegt-pad-c)
- [Pad A: Implementeren via de Anthropic API](#pad-a-implementeren-via-de-anthropic-api)
  - [Hoe het werkt](#hoe-het-werkt)
  - [A-1: Verkrijg uw Antropische API-sleutel](#a-1-verkrijg-uw-antropische-api-sleutel)
  - [A-2: Installeren en uitvoeren (Python)](#a-2-installeren-en-uitvoeren-python)
  - [A-3: Gebruik in uw eigen code](#a-3-gebruik-in-uw-eigen-code)
  - [A-7: Bekende valkuilen](#a-7-bekende-valkuilen)
  - [A-8: Het implementatiepakket — Bestandsreferentie](#a-8-het-implementatiepakket-bestandsreferentie)
- [Pad B: Implementeren op een agentplatform (handmatige gebruikersinterface)](#pad-b-implementeren-op-een-agentplatform-handmatige-gebruikersinterface)
- [Vereisten](#vereisten)
- [Stap 1: Verkrijg API-referenties](#stap-1-verkrijg-api-referenties)
  - [1A: Google Ads API-inloggegevens](#1a-google-ads-api-inloggegevens)
  - [1B: Cloudinaire inloggegevens](#1b-cloudinaire-inloggegevens)
  - [1C: SearchAPI.io-referenties](#1c-searchapiio-referenties)
  - [1D: Google AI/Gemini-referenties](#1d-google-aigemini-referenties)
  - [Samenvatting: Alle inloggegevens](#samenvatting-alle-inloggegevens)
- [Stap 2: Creëer de hoofdagent](#stap-2-creeer-de-hoofdagent)
  - [2.1 — Maak de Agent Shell](#21-maak-de-agent-shell)
  - [2.3 — Ingebouwde tools inschakelen](#23-ingebouwde-tools-inschakelen)
- [Stap 3: Aangepaste acties installeren (28 in totaal)](#stap-3-aangepaste-acties-installeren-28-in-totaal)
  - [Referentiepatronen begrijpen](#referentiepatronen-begrijpen)
  - [Actie-voor-actie installatie](#actie-voor-actie-installatie)
- [Stap 4: Subagenten maken (6 in totaal)](#stap-4-subagenten-maken-6-in-totaal)
  - [Subagent 1: Rapportage en analyse](#subagent-1-rapportage-en-analyse)
  - [Subagent 2: Onderzoek en inlichtingen](#subagent-2-onderzoek-en-inlichtingen)
  - [Subagent 3: Optimalisatie](#subagent-3-optimalisatie)
  - [Subagent 4: Winkelen & PMax](#subagent-4-winkelen-pmax)
  - [Subagent 5: Creatief](#subagent-5-creatief)
  - [Subagent 6: Baymax — Creatief innoveren](#subagent-6-baymax-creatief-innoveren)
- [Stap 5: Koppel subagenten aan hoofdagent](#stap-5-koppel-subagenten-aan-hoofdagent)
- [Stap 6: Verleen gebruikerstoegang](#stap-6-verleen-gebruikerstoegang)
- [Stap 7: Validatie en testen](#stap-7-validatie-en-testen)
  - [Test 1: Pakketinstallatie](#test-1-pakketinstallatie)
- [Referentie van referentiepatronen](#referentie-van-referentiepatronen)
  - [Patroon A: Google-advertenties met vijf sleutels](#patroon-a-google-advertenties-met-vijf-sleutels)
  - [Patroon C: Cloudinair met 3 toetsen](#patroon-c-cloudinair-met-3-toetsen)
- [Architectuuroverzicht](#architectuuroverzicht)
  - [Hoe deze opslagplaats zich verhoudt tot andere AI-agenten](#hoe-deze-opslagplaats-zich-verhoudt-tot-andere-ai-agenten)
- [Bekende problemen](#bekende-problemen)
- [Problemen oplossen](#problemen-oplossen)
  - ["Geen account gevonden dat overeenkomt..."](#geen-account-gevonden-dat-overeenkomt)
  - ["google-ads-pakket niet gevonden"](#google-ads-pakket-niet-gevonden)
  - ["OAuth-inloggegevens verlopen"](#oauth-inloggegevens-verlopen)
  - ["Ontwikkelaarstoken niet goedgekeurd"](#ontwikkelaarstoken-niet-goedgekeurd)
  - ["Tarieflimiet overschreden"](#tarieflimiet-overschreden)
  - [Subagent reageert niet](#subagent-reageert-niet)
- [Beveiliging](#beveiliging)
- [Licentie](#licentie)
- [Bijdragen](#bijdragen)
- [Gerelateerde projecten](#gerelateerde-projecten)

---
## Snelle start

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

## Drie implementatiepaden

| Pad | Beste voor | Wat je nodig hebt |
|------|----------|---------------|
| **A: Antropische API (programmatisch)** | Productie-apps, SaaS, automatiseringspijplijnen | Antropische API-sleutel + Python |
| **B: Agentplatform (handmatige gebruikersinterface)** | Snelle prototyping, visuele bouwer voor één gebruiker | Agentplatformaccount |
| **C: Cloudflare-productie (Buddy)** | Full-stack met geheugen, facturering, monitoring | Cloudflare-account |

**Pad A** is wat deze repository kant-en-klaar biedt. Pad C is het productiesysteem op [googleadsagent.ai](https://googleadsagent.ai) — zie [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md) voor de volledige architectuur.

### Wat Buddy toevoegt (pad C)

| Vermogen | Technologie |
|-----------|-----------|
| Persistente status per gebruiker | Duurzame objecten + SQLite |
| Semantisch geheugen | Inbedding vectoriseren |
| Gecodeerde BYOK-opslag | AES-256-GCM |
| Realtime WebSocket | Cloudflare Agents SDK |
| Geautomatiseerde monitoring | Cron-werknemers |
| Facturering op basis van krediet | D1 + Streep |
| AI met meerdere providers | Claude, GPT, Gemini-routering |
| Bestandsexport | R2-objectopslag |

---

## Pad A: Implementeren via de Anthropic API

Dit is de **programmatische implementatie**: geen handmatige gebruikersinterface, geen klikken. Alles loopt via Claude's Messages API met gebruik van tools.

### Hoe het werkt

De actiebestanden in deze opslagplaats zijn oorspronkelijk gebouwd voor een agentplatform. Het `deploy/` pakket past ze aan zodat ze standalone kunnen draaien via de Anthropic API. Dit is wat er onder de motorkap gebeurt als je `python scripts/cli.py` uitvoert:

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

**Wat de adapterlaag (`tool_executor.py`) oplost:**

| Probleem | Wat de actiebestanden doen | Wat de adapter doet |
|---------|-----------------------|--------------------|
| **Geheimen** | Referentie `secrets["KEY"]` als een kale global geïnjecteerd door het agentplatform | Injecteert het dictaat `geheimen` in module `__dict__` vóór `exec_module()` |
| **Pip-installaties** | Voer `subprocess.check_call(["pip", "install", "google-ads"])` uit tijdens het importeren | Monkey-patches subproces om pip-opdrachten over te slaan (deps al in `requirements.txt`) |
| **Parameter komt niet overeen** | 26/28 `run()`-functies hebben expliciete parameters (geen `**kwargs`) | Inspecteert de handtekening van `run()` via `inspect.signature()`, verwijdert alle parameters die Claude verzendt en die niet in de functie |

### A-1: Verkrijg uw Antropische API-sleutel

1. Ga naar **[Anthropic Console](https://console.anthropic.com)**
2. Meld je aan of log in
3. Ga naar **[Instellingen → API-sleutels](https://console.anthropic.com/settings/keys)**
4. Klik op **Sleutel maken**
5. Kopieer de sleutel → dit is uw `ANTHROPIC_API_KEY`

> 💡 De sleutel begint met `sk-ant-api03-...`. Bewaar het veilig: het geeft volledige API-toegang.

**Hoe dit aansluit op het systeem:** Elke aanroep naar Claude's Messages API vereist deze sleutel in de `x-api-key` header. De `anthropic` Python SDK leest het automatisch uit `ANTHROPIC_API_KEY` env var.

### A-2: Installeren en uitvoeren (Python)

**Wat er stap voor stap gebeurt als je dit uitvoert:**

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

**Na stap 6 ziet u:**

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
```Dat is het. De agent is actief en voert echte Google Ads API-aanroepen uit via uw inloggegevens, waarbij Claude bepaalt welke tools moeten worden aangeroepen en hoe de resultaten moeten worden geïnterpreteerd.

### A-3: Gebruik in uw eigen code

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
```### A-4: Implementeren als REST API

De meegeleverde FastAPI-server biedt u HTTP-eindpunten voor elke frontend of integratie:

```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**Eindpunten:**

| Werkwijze | Pad | Beschrijving |
|--------|------|------------|
| `POST` | `/chatten` | Stuur een bericht, ontvang een reactie (maakt automatisch een sessie aan) |
| `POST` | `/sessies` | Maak een nieuwe gesprekssessie aan |
| `KRIJG` | `/sessions/{id}` | Sessie-informatie en aantal berichten ontvangen |
| `VERWIJDEREN` | `/sessions/{id}` | Een sessie verwijderen |
| `KRIJG` | `/gezondheid` | Gezondheidscontrole (referentiestatus) |
| `KRIJG` | `/tools` | Lijst van alle 28 tools en hun bestandsstatus |

**Voorbeeld verzoek:**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**Voorbeeldreactie:**

```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5: Implementeren met Docker```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6: Schaaloverwegingen

| Zorg | Huidige staat | Productie-upgrade |
|---------|--------------|-----------------|
| **Sessies** | In het geheugen opgeslagen dictaat | Wissel naar Redis - voeg de `redis`-service toe in docker-compose, vervang het `sessions` dict door Redis-client |
| **Tarieflimieten** | Antropische API-limieten per laag | Voeg wachtrijverzoeken toe met `selderij` of `asyncio.Semaphore` |
| **Multi-tenant** | Enkele referentieset | Inloggegevens per tenant laden vanuit een geheimenmanager (AWS Secrets Manager, HashiCorp Vault) |
| **Authentificatie** | Geen | Voeg API-sleutel-middleware of OAuth2 toe aan de FastAPI-server |
| **Bewaking** | Basisregistratie | Voeg gestructureerde logging toe + export naar Datadog/CloudWatch |
| **Kostenbeheersing** | Geen | Volg het tokengebruik via `response.usage` en stel budgetwaarschuwingen in |
| **Logica opnieuw proberen** | SDK-standaard (2 nieuwe pogingen) | Stem 'max_retries' af en voeg exponentieel uitstel toe voor Google Ads API-aanroepen |

### A-7: Bekende valkuilen

Dingen die u tijdens de eerste run kunnen doen struikelen:

| Uitgave | Wat gebeurt er | Repareren |
|-------|------------|-----|
| **Google-Ads-import mislukt** | Actiebestanden hebben `google-ads>=28.1.0` nodig, die C-afhankelijkheden heeft | Voer eerst `pip install -r requirements.txt` uit — dit is de reden waarom de adapter inline pip-installaties onderdrukt |
| **`geheimen` KeyError** | Een actie probeert toegang te krijgen tot een referentie die u niet hebt ingesteld in `.env` | Controleer welk referentiepatroon de tool gebruikt (A/B/C/D) en controleer of `.env` deze sleutels heeft |
| **Typefout bij run()** | Claude stuurt een parameter die de functie run() niet accepteert | Het paramfilter zou dit moeten opvangen - als dit niet het geval is, vink dan `python -c "from deployment import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"` |
| **Tarieflimieten** | Basistoegang tot de Google Ads API = 15.000 bewerkingen/dag, 4 vereisten/sec | Gebruik de parameters `cost_min`, `status`, `limit` om resultatensets te verminderen |
| **Eerste laadtijd is langzaam** | Module laden + pip-onderdrukking voegt ~1-2s toe bij eerste gereedschapsoproep | Daaropvolgende oproepen gebruiken modules in de cache — instant |
| **Tokenkosten** | claude-opus-4-5 met 28 gereedschapsdefinities = ~4K tokens per aanvraag alleen voor gereedschappen | Voor kostenoptimalisatie schakelt u over naar `claude-sonnet-4-5-20250929` in de constructor |

### A-8: Het implementatiepakket — Bestandsreferentie

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

## Pad B: Implementeren op een agentplatform (handmatige gebruikersinterface)

Als u de voorkeur geeft aan een visuele bouwer (OpenAI of iets dergelijks), volgt u stap 2 tot en met 7 hieronder. U plakt systeemprompts, actiecode en inloggegevens in de gebruikersinterface van het platform.

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

## Vereisten

Voordat u begint, heeft u het volgende nodig:

| Vereiste | Waarom | Kosten |
|------------|-----|------|
| **Antropische API-sleutel** | Voedt de Claude-agent via de Berichten-API | Betalen per gebruik ([prijzen](https://docs.anthropic.com/en/docs/about-claude/pricing)) |
| **Google Ads-account** | API-toegang om campagnes te beheren | Gratis (advertenties apart uitgeven) |
| **Google Ads-manageraccount (MCC)** | Toegang voor meerdere accounts | Gratis |
| **Google Cloud Platform-project** | OAuth2-inloggegevens voor de Google Ads API | Gratis niveau beschikbaar |
| **Cloudinair account** | Beeld-/videoverwerking voor creatieve middelen | Gratis niveau (25 credits/maand) |
| **SearchAPI.io-account** | Realtime Google-zoekopdracht, trends, advertentietransparantie | Gratis niveau (100 zoekopdrachten/maand) |
| **Google AI Studio-account** | Gemini API voor het genereren van AI-creatie | Gratis niveau beschikbaar |
| **Agentplatformaccount** | Waar u de agent implementeert (bijvoorbeeld OpenAI of iets dergelijks) | Varieert |

---

## Stap 1: Verkrijg API-referenties

U heeft inloggegevens nodig van **4 services**. In deze sectie wordt elke URL doorgenomen met exacte URL's, begeleiding bij schermafbeeldingen en wat u moet kopiëren.

---

### 1A: Google Ads API-inloggegevens

Dit is de meest complexe opstelling. Je hebt **5 waarden** nodig die samenwerken:

| Referentie | Wat het is | Waar het leeft |
|-----------|-----------|----------------|
| `ONTWIKKELAAR_TOKEN` | Uw API-toegangssleutel van Google Ads | Google Ads-gebruikersinterface |
| `CLIENT_ID` | OAuth2 app-ID | Google Cloudconsole |
| `CLIENT_SECRET` | OAuth2-app-geheim | Google Cloudconsole |
| `REFRESH_TOKEN` | OAuth2-token met lange levensduur | Gegenereerd via OAuth-stroom |
| `LOGIN_CUSTOMER_ID` | Uw MCC-account-ID | Google Ads-gebruikersinterface |

#### Stap 1A-1: Haal uw ontwikkelaarstoken op

1. Ga naar **[Google Ads](https://ads.google.com)** en log in met uw manageraccount (MCC)
2. Klik op het pictogram **Extra en instellingen** (sleutel) in de navigatie bovenaan
3. Klik onder **Setup** op **API Center**
   - Als u API Center niet ziet, moet u mogelijk eerst toegang aanvragen
4. Uw **Developer Token** wordt op deze pagina weergegeven
5. **Tokentoegangsniveau:**
   - `Testaccount` — werkt alleen met testaccounts (goed voor ontwikkeling)
   - 'Basistoegang' — tot 15.000 handelingen/dag (vraag dit aan)
   - `Standaardtoegang` — onbeperkt (toepassen na bewijs van gebruik)
6. **Kopieer het token** → dit is uw `GOOGLE_ADS_DEVELOPER_TOKEN`

> ⚠️ Als uw token de status 'In behandeling' heeft, kunt u deze nog steeds gebruiken met testaccounts. Voor productie moet u [basistoegang aanvragen](https://developers.google.com/google-ads/api/docs/access-levels).

#### Stap 1A-2: OAuth2-referenties maken in Google Cloud

1. Ga naar **[Google Cloud Console](https://console.cloud.google.com)**
2. Maak een nieuw project aan (of selecteer een bestaand project):
   - Klik op de vervolgkeuzelijst met projecten bovenaan → **Nieuw project**
   - Naam: `google-ads-agent` (of wat u maar wilt)
   - Klik op **Maken**
3. **Schakel de Google Ads API in:**
   - Ga naar **[API's en services → Bibliotheek](https://console.cloud.google.com/apis/library)**
   - Zoek naar 'Google Ads API'
   - Klik erop → Klik op **Inschakelen**
4. **Configureer het OAuth-toestemmingsscherm:**
   - Ga naar **[API's en services → OAuth-toestemmingsscherm](https://console.cloud.google.com/apis/credentials/consent)**
   - Selecteer **Extern** (tenzij u Google Workspace heeft, en vervolgens Intern)
   - Vul in:
     - App-naam: 'Google Ads-agent'
     - E-mail voor gebruikersondersteuning: uw e-mailadres
     - Contactpersoon ontwikkelaar: uw e-mailadres
   - Klik op **Opslaan en doorgaan**
   - **Bereikingen:** Klik op **Bereiken toevoegen of verwijderen** → zoek naar `Google Ads API` → vink `https://www.googleapis.com/auth/adwords` aan → **Bijwerken** → **Opslaan en doorgaan**
   - **Testgebruikers:** Voeg het e-mailadres van uw Google Ads-account toe → **Opslaan en doorgaan**
   - Klik op **Terug naar dashboard**
5. **OAuth2-client-ID maken:**
   - Ga naar **[API's en services → Inloggegevens](https://console.cloud.google.com/apis/credentials)**
   - Klik op **+ Credentials aanmaken** → **OAuth-client-ID**
   - Applicatietype: **Webapplicatie**
   - Naam: `Google Ads-agent`
   - Geautoriseerde omleidings-URI's: voeg 'http://localhost:8080' toe (nodig voor de stap voor het genereren van tokens)
   - Klik op **Maken**
   - **Kopieer de klant-ID** → dit is uw `GOOGLE_ADS_CLIENT_ID`- **Kopieer het klantgeheim** → dit is uw `GOOGLE_ADS_CLIENT_SECRET`

#### Stap 1A-3: Genereer een vernieuwingstoken

Met het vernieuwingstoken kan de agent verifiëren zonder tussenkomst van de gebruiker. Je genereert het één keer en het duurt voor onbepaalde tijd (tenzij het wordt ingetrokken).

**Optie A: Google's OAuth2 Playground gebruiken (eenvoudigste)**

1. Ga naar **[OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)**
2. Klik op het **tandwielpictogram** ⚙️ (rechtsboven)
   - Vink **Gebruik uw eigen OAuth-inloggegevens** aan
   - Voer uw 'Client-ID' en 'Clientgeheim' uit stap 1A-2 in
   - Sluit de instellingen
3. Scroll in het linkerpaneel naar **Google Ads API v18** → vink `https://www.googleapis.com/auth/adwords` aan
4. Klik op **API's autoriseren**
5. Meld u aan met het Google-account dat toegang heeft tot uw Google Ads-accounts
6. Verleen de gevraagde machtigingen
7. Klik op **Autorisatiecode omwisselen voor tokens**
8. **Kopieer de vernieuwingstoken** → dit is uw `GOOGLE_ADS_REFRESH_TOKEN`

**Optie B: gebruik van de Python-bibliotheek van Google Ads**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```Hiermee wordt een browser geopend voor OAuth-toestemming en wordt het vernieuwingstoken afgedrukt.

**Optie C: Krul gebruiken**```bash
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
```#### Stap 1A-4: Ontvang uw inlogklant-ID (MCC)

1. Ga naar **[Google Ads](https://ads.google.com)**
2. Meld u aan bij uw **Manageraccount** (MCC)
3. Uw **Klant-ID** wordt rechtsboven weergegeven, opgemaakt als `XXX-XXX-XXXX`
4. **Kopieer het** → dit is uw `GOOGLE_ADS_LOGIN_CUSTOMER_ID`

> 💡 De Login Klant-ID is alleen nodig als u een MCC gebruikt om meerdere accounts te beheren. Als u rechtstreeks één account beheert, kunt u dit veld leeg laten.

#### Stap 1A-5: Controleer uw gegevens

Maak een testbestand om te controleren of alles werkt:

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
```Als hierdoor de namen van accountbronnen worden afgedrukt, werken uw Google Ads-inloggegevens.

---

### 1B: Cloudinaire inloggegevens

Cloudinary verzorgt alle beeld-/videoverwerking: formaat wijzigen, AI-generatieve vulling, platformspecifieke opmaak.

1. Ga naar **[Cloudinary Sign Up](https://cloudinary.com/users/register_free)** en maak een gratis account aan
   - Gratis niveau bevat 25 credits/maand (genoeg voor ~1.000 transformaties)
2. Ga na het aanmelden naar **[Dashboard](https://console.cloudinary.com/pm/getting-started/dashboard)**
3. Uw inloggegevens worden direct op het dashboard weergegeven:
   - **Cloudnaam** → `CLOUDINARY_CLOUD_NAME`
   - **API-sleutel** → `CLOUDINARY_API_KEY`
   - **API-geheim** → `CLOUDINARY_API_SECRET` (klik op "Onthullen" om het te zien)

> 💡 De gratis laag is genereus voor ontwikkeling. Voor productie met zware creatieve verwerking geeft het Plus-abonnement ($89/maand) 225 credits.

#### Hoe Cloudinary verbinding maakt met de agent

De actie **Cloudinary Creative Tools** (actie #18 op de hoofdagent) en de subagent **Baymax — Creative Innovate** gebruiken beide deze inloggegevens. Ze maken het volgende mogelijk:
- Afbeeldingen/video's uploaden van URL's
- Formaat wijzigen voor meer dan 20 platformvoorinstellingen (Instagram, TikTok, YouTube, display-advertenties, enz.)
- AI generatieve vulling voor het uitbreiden van afbeeldingen naar niet-standaard beeldverhoudingen
- Batchverwerking op meerdere platforms

---

### 1C: SearchAPI.io-referenties

SearchAPI.io biedt realtime Google-zoekresultaten, Google Trends-gegevens en Google Ads Transparency Center-toegang voor de Research & Intelligence-subagent.

1. Ga naar **[SearchAPI.io aanmelden](https://www.searchapi.io/signup)**
   - Gratis niveau: 100 zoekopdrachten/maand
2. Ga na het aanmelden naar **[Dashboard → API Key](https://www.searchapi.io/dashboard)**
3. **Kopieer uw API-sleutel** → `SEARCHAPI_API_KEY`

#### Hoe SearchAPI verbinding maakt met de agent

De **Nemo — Research & Intelligence** gebruikt SearchAPI via drie aangepaste acties:
- **Google Search API** — realtime SERP-resultaten met advertenties, organisch, kennisgrafiek
- **Google Ads Transparency Center**: bekijk welke advertenties concurrenten weergeven
- **Google Trends Analyzer** — trendgegevens, gerelateerde zoekopdrachten, geografische interesse

Deze acties geven de API-sleutel door via `secrets["SEARCHAPI_API_KEY"]` in de broncode van elke actie.

---

### 1D: Google AI/Gemini-referenties

De Baymax – Creative Innovate maakt gebruik van de Gemini API van Google voor het genereren van afbeeldingen en visieanalyse op basis van AI.

1. Ga naar **[Google AI Studio](https://aistudio.google.com)**
2. Meld u aan met uw Google-account
3. Klik op **Get API Key** in de linkerzijbalk (of ga rechtstreeks naar **[API Keys](https://aistudio.google.com/apikey)**)
4. Klik op **API-sleutel maken**
   - Selecteer het Google Cloud-project dat u in stap 1A-2 heeft gemaakt (of maak een nieuw project)
5. **Kopieer de API-sleutel** → `GOOGLE_AI_API_KEY`

> 💡 De gratis laag biedt 15 RPM (verzoeken per minuut) voor Gemini 2.0 Flash. Voor productie is het pay-as-you-go-tarief zeer betaalbaar.

#### Hoe Gemini verbinding maakt met de agent

De subagent **Baymax — Creative Innovate** gebruikt Gemini voor:
- AI-beeldgeneratie/-extensie voor sociale-mediaformaten
- Visieanalyse van bestaand creatief vermogen
- Varianten van display-advertenties genereren op basis van bronafbeeldingen

Het Gemini-actiebestand bevindt zich op `actions/sub-agents/creative-innovate/02_gemini_vision.py`.

---

### Samenvatting: Alle inloggegevens

Na het voltooien van de stappen 1A tot en met 1D zou uw `.env`-bestand er als volgt uit moeten zien:

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

## Stap 2: Creëer de hoofdagent

> Deze instructies gebruiken algemene terminologie. Pas knopnamen/menu's aan voor uw specifieke agentplatform (bijvoorbeeld OpenAI of iets dergelijks).

### 2.1 — Maak de Agent Shell

1. Maak op uw agentplatform een nieuwe agent met deze instellingen:

| Instelling | Waarde |
|---------|-------|
| Naam | `Google Ads API-agent` |
| Model | `claude-opus-4-5` (Antropisch) |
| Toegang | Privé |

2. **Stel de beschrijving in:**

```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — Plak de systeemprompt

1. Open het bestand: `prompts/main_agent_system_prompt.md`
2. Kopieer de **volledige inhoud**
3. Plak het in het systeemprompt-/instructieveld van uw agent
4. Opslaan

### 2.3 — Ingebouwde tools inschakelen

Schakel deze 10 ingebouwde tools in (namen kunnen per platform verschillen):

- [x] Code-interpreter
- [x] Zoeken op internet (Google)
- [x] Onderzoeker
- [x] Todo / Takenlijst
- [x] Webschraper
- [x] Query-uitvoerder (SQL)
- [x] CSV-lezer
- [x] Tekenreeksmatcher
- [x] Bestand weergeven
- [x] Bestand zoeken

---

## Stap 3: Aangepaste acties installeren (28 in totaal)

Elke aangepaste actie is een Python-bestand dat in de aangepaste actiebouwer van uw agentplatform wordt geplakt. Je moet:

1. Maak de actie
2. Plak de broncode
3. Configureer de inloggegevens (geheimen)

### Referentiepatronen begrijpen

Er zijn 4 identificatiepatronen. Weet welke elke actie gebruikt voordat je begint:

| Patroon | # geheimen | Acties die er gebruik van maken |
|---------|-------------|----------------|
| **A** (Google-advertenties met 5 toetsen) | 5 | 12 acties — inclusief `LOGIN_CUSTOMER_ID` als geheim |
| **B** (Google-advertenties met 4 toetsen) | 4 | 13 acties — geeft `login_customer_id` door als een functieparam |
| **C** (Cloudinair met 3 toetsen) | 3 | 1 actie — Cloudinaire creatieve tools |
| **D** (Geen inloggegevens) | 0 | 3 acties: pakketinstallatieprogramma, sessiebeheer, reconstructiedocument |

Zie [Credential Patterns Reference](#credential-patterns-reference) voor volledige details.

### Actie-voor-actie installatie

Voor **elke actie** hieronder volgt u dit proces:

```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### Patroon A-acties (Google-advertenties met 5 toetsen) — 12 acties

Voeg voor elk deze 5 geheimen toe:

| Geheime sleutel | Waarde uit .env |
|-----------|---------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Uw ontwikkelaarstoken |
| `GOOGLE_ADS_CLIENT_ID` | Uw OAuth2-client-ID |
| `GOOGLE_ADS_CLIENT_SECRET` | Uw OAuth2-clientgeheim |
| `GOOGLE_ADS_REFRESH_TOKEN` | Uw vernieuwingstoken |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Uw MCC-klant-ID |

| # | Actienaam | Bronbestand |
|---|-------------|------------|
| 1 | Labelmanager | `actions/main-agent/01_label_manager.py` |
| 2 | Beheerder voor het bijhouden van conversies | `actions/main-agent/02_conversion_tracking_manager.py` |
| 12 | Scriptbeheer | `actions/main-agent/12_scripts_manager.py` |
| 13 | Experimentenmanager | `actions/main-agent/13_experiments_manager.py` |
| 19 | Queryplanner & Budgetmanager | `actions/main-agent/19_query_planner.py` |
| 20 | Aanbevelingenmanager | `actions/main-agent/20_recommendations_manager.py` |
| 23 | Apparaatprestatiebeheer | `actions/main-agent/23_device_performance_manager.py` |
| 24 | Beheerder van wijzigingsgeschiedenis | `actions/main-agent/24_change_history_manager.py` |
| 25 | Campagnemaker | `actions/main-agent/25_campaign_creator.py` |
| 26 | Advertentieplanningsmanager | `actions/main-agent/26_ad_schedule_manager.py` |
| 27 | Biedstrategiebeheerder | `actions/main-agent/27_bidding_strategy_manager.py` |
| 28 | PMax Asset Groepsmanager | `actions/main-agent/28_pmax_asset_group_manager.py` |

#### Patroon B-acties (Google-advertenties met 4 toetsen) — 13 acties

Voeg voor elk deze 4 geheimen toe:

| Geheime sleutel | Waarde uit .env |
|-----------|---------------|
| `ONTWIKKELAAR_TOKEN` | Uw ontwikkelaarstoken |
| `CLIENT_ID` | Uw OAuth2-client-ID |
| `CLIENT_SECRET` | Uw OAuth2-clientgeheim |
| `REFRESH_TOKEN` | Uw vernieuwingstoken |

> ⚠️ Opmerking: de **sleutelnamen** verschillen van Patroon A (geen `GOOGLE_ADS_` voorvoegsel). Dit is zo ontworpen: deze acties accepteren in plaats daarvan 'login_customer_id' als functieparameter.

| # | Actienaam | Bronbestand |
|---|-------------|------------|
| 3 | Doelgroepmanager | `actions/main-agent/03_audience_manager.py` |
| 4 | Vermogensbeheerder | `actions/main-agent/04_asset_manager.py` |
| 5 | Budgetbeheerder | `actions/main-agent/05_budget_manager.py` |
| 6 | RSA Ad Manager | `actions/main-agent/06_rsa_ad_manager.py` |
| 7 | Bied- en trefwoordmanager | `actions/main-agent/07_bid_keyword_manager.py` |
| 8 | Beheerder van uitsluitingszoekwoorden | `actions/main-agent/08_negative_keywords_manager.py` |
| 9 | Campagne- en advertentiegroepmanager | `actions/main-agent/09_campaign_adgroup_manager.py` |
| 10 | Google-advertenties muteren | `actions/main-agent/10_google_ads_mutate.py` |
| 11 | Accounttoegangscontrole | `actions/main-agent/11_account_access_checker.py` |
| 15 | Controleer gebruikerstoegangsniveaus | `actions/main-agent/15_check_user_access.py` |
| 16 | API-gateway - Contextbeheer | `actions/main-agent/16_api_gateway.py` |
| 21 | Zoektermmanager | `actions/main-agent/21_search_term_manager.py` |
| 22 | Beheerder voor geografische en locatietargeting | `actions/main-agent/22_geo_location_manager.py` |

#### Patroon C-actie (Cloudinair met 3 toetsen) — 1 actie

| Geheime sleutel | Waarde uit .env |
|-----------|---------------|
| `CLOUDINARY_CLOUD_NAME` | Uw Cloudinary-cloudnaam |
| `CLOUDINARY_API_KEY` | Uw Cloudinary API-sleutel |
| `CLOUDINARY_API_SECRET` | Uw Cloudinary API-geheim |

| # | Actienaam | Bronbestand |
|---|-------------|------------|
| 18 | Cloudinaire creatieve tools | `actions/main-agent/18_cloudinary_creative_tools.py` |

#### Patroon D-acties (geen inloggegevens) — 3 acties

Plak gewoon de code - geen geheimen nodig.

| # | Actienaam | Bronbestand |
|---|-------------|------------|
| 14 | Pakketinstallatieprogramma | `actions/main-agent/14_package_installer.py` |
| 17 | Sessie- en staatsmanager | `actions/main-agent/17_session_state_manager.py` |

> 📌 **Tip:** Als uw platform bulkimportacties ondersteunt, gebruik dan `configs/agent_registry.json` als de bron van waarheid voor ID's, namen en referentiepatronen.

---

## Stap 4: Subagenten maken (6 in totaal)

Elke subagent is een afzonderlijke agent waaraan de hoofdagent taken delegeert. Ze hebben elk hun eigen systeemprompt, tools en aangepaste acties.

### Subagent 1: Rapportage en analyse

| Instelling | Waarde |
|---------|-------|
| Naam | `Simba — Rapportage en analyse` |
| Model | `claude-opus-4-5` |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/01_reporting_analysis.md` |

**Aangepaste acties (8):** Installeren vanuit `actions/sub-agents/reporting/`

| # | Actie | Bronbestand | Referenties |
|---|--------|-----------|------------|
| 1 | Prestatieverslaggever | `01_performance_reporter.py` | Google-advertenties met 4 toetsen (patroon B) |
| 2 | Zoektermenanalyser | `02_search_terms_analyzer.py` | Google-advertenties met 4 toetsen (patroon B) |
| 3 | Interactieve zoekwoordviewer | `03_interactive_keyword_viewer.py` | Google-advertenties met 4 toetsen (patroon B) |
| 4 | Interactieve advertentieviewer | `04_interactieve_ad_viewer.py` | Google-advertenties met 4 toetsen (patroon B) |
| 5 | Verslaggever van veilinginzichten | `05_auction_insights_reporter.py` | Google-advertenties met 4 toetsen (patroon B) |
| 6 | Auditor van wijzigingsgeschiedenis | `06_change_history_auditor.py` | Google-advertenties met 4 toetsen (patroon B) |
| 7 | PMax Verbeterde rapportage | `07_pmax_enhanced_reporting.py` | Google-advertenties met 4 toetsen (patroon B) |
| 8 | Pakketinstallatieprogramma | `08_package_installer.py` | Geen (patroon D) |

**Ingebouwde tools (9):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, researcher, google_web_search

> ⚠️ Acties 3 en 4 (interactieve zoekwoorden/advertentieviewers) gebruiken de Google Ads API **v18**, terwijl de andere **v19** gebruiken. Controleer of het pip-pakket 'google-ads' beide ondersteunt.

---

### Subagent 2: Onderzoek en inlichtingen

| Instelling | Waarde |
|---------|-------|
| Naam | `Nemo — Onderzoek en inlichtingen` |
| Model | `claude-opus-4-5` |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/02_research_intelligence.md` |

**Aangepaste acties (4+1):** Installeren vanuit `actions/sub-agents/research/`

| # | Actie | Bronbestand | Referenties |
|---|--------|-----------|------------|
| 1 | Zoekwoordplanner | `01_keyword_planner.py` | Google-advertenties met 4 toetsen (patroon B) |
| 2 | Google Zoeken-API | `02_google_search_api.py` | 1 geheim: `SEARCHAPI_API_KEY` |
| 3 | Centrum voor transparantie van advertenties | `03_ads_transparency_center.py` | 1 geheim: `SEARCHAPI_API_KEY` |
| 4 | Google Trends-analyzer | `04_google_trends_analyzer.py` | 1 geheim: `SEARCHAPI_API_KEY` |
| 5 | Pakketinstallatieprogramma | *(hergebruik van hoofdagent)* | Geen (patroon D) |

**Ingebouwde tools (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, researcher, google_web_search, web_scraper

---

### Subagent 3: Optimalisatie

| Instelling | Waarde |
|---------|-------|
| Naam | `Elsa — Optimalisatie` |
| Model | `claude-opus-4-5` |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/03_optimization.md` |

**Aangepaste acties:** ⚠️ **Er bestaat nog geen**

De systeemprompt van deze subagent verwijst naar twee aangepaste acties die moeten worden gebouwd:
- **Aanbevelingenbeheer - API** — `list`, `apply`, `dismiss`, `get_score`
- **Bulk Operations Manager - API** — `bulk_pause`, `bulk_enable`, `bulk_bid_change`, `bulk_budget_change`, `export`

> 🔧 **TODO:** Bouw deze acties met behulp van de Google Ads API. De parameterhandtekeningen worden gedocumenteerd in het systeempromptbestand. Beide zouden Patroon B-inloggegevens (4-sleutel Google Ads) gebruiken.

**Ingebouwde tools (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, researcher, google_web_search, web_scraper

---

### Subagent 4: Winkelen & PMax

| Instelling | Waarde |
|---------|-------|
| Naam | `Aladdin — Winkelen en PMax` |
| Model | `claude-opus-4-5` |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/04_shopping_pmax.md` |

**Aangepaste acties:** ⚠️ **Er bestaat nog geen**

De systeemprompt van deze subagent verwijst naar één aangepaste actie die moet worden gebouwd:
- **Shopping & PMax Manager - API** — `list_shopping`, `list_pmax`, `list_asset_groups`, `get_product_performance`, `get_pmax_performance`, `get_pmax_insights`, `pause_asset_group`, `enable_asset_group`

> 🔧 **TODO:** Bouw deze actie met behulp van de Google Ads API (`google-ads` Python SDK). Zou Patroon B-referenties gebruiken. De PMax Asset Group Manager van de hoofdagent (actie nr. 28) dekt een deel van deze functionaliteit en kan als startsjabloon dienen.**Ingebouwde tools (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, researcher, google_web_search, web_scraper

---

### Subagent 5: Creatief

| Instelling | Waarde |
|---------|-------|
| Naam | `Moana — Creatief` |
| Model | `claude-opus-4-5` |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/05_creative.md` |

**Aangepaste acties (2):** Installeren vanuit `actions/sub-agents/creative/`

| # | Actie | Bronbestand | Referenties |
|---|--------|-----------|------------|
| 1 | Beheerder van responsieve display-advertenties | `01_responsive_display_ads_manager.py` | Google-advertenties met 4 toetsen (patroon B) |
| 2 | Beheerder van vraaggenererende advertenties | `02_demand_gen_ads_manager.py` | Google-advertenties met 4 toetsen (patroon B) |

**Ingebouwde tools (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, google_web_search, researcher, web_scraper

---

### Subagent 6: Baymax — Creatief innoveren

| Instelling | Waarde |
|---------|-------|
| Naam | `Baymax — Creatief innoveren` |
| Model | `claude-sonnet-4-5` ⚡ *(lichter model - opzettelijk)* |
| Toegang | CHAT_ONLY |
| Systeemprompt | `prompts/sub-agents/06_creative_innovate.md` |

**Aangepaste acties (2+1):** Installeren vanuit `actions/sub-agents/creative-innovate/`

| # | Actie | Bronbestand | Referenties |
|---|--------|-----------|------------|
| 1 | Cloudinaire tools | `01_cloudinary_tools.py` | 3-toets cloudinair (patroon C) |
| 2 | Tweelingvisie | `02_gemini_vision.py` | 1 geheim: `GOOGLE_AI_API_KEY` |
| 3 | Pakketinstallatieprogramma | *(hergebruik van hoofdagent)* | Geen (patroon D) |

---

## Stap 5: Koppel subagenten aan hoofdagent

Nadat u alle zes de subagenten heeft aangemaakt, moet u ze registreren bij de hoofdagent, zodat deze taken kan delegeren.

1. Ga naar de **Hoofdagent**-instellingen
2. Zoek het gedeelte **Subagenten**
3. Voeg elke subagent toe door te zoeken naar de naam of ID:

| # | Naam subagent | Agent-ID |
|---|----------------|----------|
| 1 | Simba — Rapportage en analyse | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Nemo — Onderzoek en inlichtingen | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 | Elsa — Optimalisatie | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 | Aladdin — Winkelen en PMax | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 | Moana — Creatief | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 | Baymax — Creatief innoveren | `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 Opmerking: Agent-ID's zullen **anders** zijn als u nieuwe agenten maakt (ze worden automatisch gegenereerd). De bovenstaande ID's zijn afkomstig van de originele build en dienen ter referentie.

De systeemprompt van de hoofdagent bevat het **Sub-Agent Delegation Protocol** dat hem vertelt wanneer hij taken direct moet afhandelen of moet delegeren. De **Sessie- en Staatsmanager** (Actie #17) coördineert de overdracht.

---

## Stap 6: Verleen gebruikerstoegang

Als u de agent met teamleden wilt delen:

1. Ga naar Hoofdagentinstellingen → **Delen/Toegang**
2. Voeg gebruikers toe met toestemming **CAN_EDIT**
3. Ze kunnen de agent gebruiken en aanpassen

---

## Stap 7: Validatie en testen

Voer deze tests uit om te controleren of het volledige systeem werkt:

### Test 1: Pakketinstallatie

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### Test 2: Accountverbinding```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### Test 3: Rekeningoverzicht```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### Test 4: Leesbewerking```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### Test 5: Schrijfbewerking (veilig)```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### Test 6: Delegatie van subagenten```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### Test 7: Cloudinair```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## Referentie van referentiepatronen

### Patroon A: Google-advertenties met vijf sleutels

Gebruikt door **12 acties** waarbij de MCC Login-klant-ID als geheim wordt opgeslagen.```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### Patroon B: Google-advertenties met vier sleutels

Gebruikt door **13 acties** waarbij Login Klant-ID wordt doorgegeven als functieparameter.```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ De **waarden** zijn identiek aan Patroon A. Alleen de **sleutelnamen** verschillen. Dit komt omdat sommige acties met verschillende naamgevingsconventies zijn geschreven. De onderliggende referenties zijn hetzelfde.

### Patroon C: Cloudinair met 3 toetsen

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### Patroon D: Geen inloggegevens

Acties die geen externe API's aanroepen: Package Installer, Session & State Manager.

---

## Architectuuroverzicht

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
```Voor de volledige technische architectuur met actieschema's, parameterhandtekeningen en delegatiestroom, zie **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

Voor de Cloudflare Buddy-productiearchitectuur (Durable Objects, Vectorize, D1, R2, Agents SDK), zie **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**.

### Hoe deze opslagplaats zich verhoudt tot andere AI-agenten

| Kenmerk | Deze makelaar | Google Ads-scripts | Microsoft Copiloot | Verbijstering | Generieke Claude |
|--------|-----------|------------------|-----------------|-----------|-------------|
| Live Google Ads API R/W | 28 acties | Alleen JS-scripting | Geen toegang tot advertenties | Geen API | Geen API |
| Schrijfveiligheid (CEP) | Bevestigen/Uitvoeren/Posten | Geen | N.v.t. | N.v.t. | N.v.t. |
| AI met meerdere providers | Claude + GPT + Tweelingen | N.v.t. | Alleen GPT | Eigen modellen | Alleen Claude |
| Delegatie van subagenten | 6 specialisten | N.v.t. | N.v.t. | N.v.t. | N.v.t. |
| Semantisch geheugen | Vectoriseren (prod) | Geen | Beperkt | Ingebouwd | Alleen gesprek |
| Zelf inzetbaar | 3 paden | Scripteditor | Alleen SaaS | Alleen SaaS | Alleen API |

---

## Bekende problemen

| Uitgave | Ernst | Details | Oplossing |
|-------|----------|---------|-----------|
| **Optimalisatie-subagent heeft geen acties** | 🔴Kritisch | Systeemprompt beschrijft Recommendations Manager & Bulk Operations Manager, maar geen van beide acties bestaat | Bouw ze met behulp van de Google Ads API, of gebruik rechtstreeks de Recommendations Manager (#20) van de hoofdagent |
| **Shopping & PMax-subagent heeft geen acties** | 🔴Kritisch | Systeemprompt beschrijft Shopping & PMax Manager, maar er is geen actie | Bouw het, of gebruik de PMax Asset Group Manager (#28) van de hoofdagent als uitgangspunt |
| **API-versie komt niet overeen in rapportage** | 🟡 Middel | Interactieve zoekwoorden/advertentieviewers gebruiken v18, andere rapportageacties gebruiken v19 | Controleer of het pip-pakket van `google-ads` beide verwerkt; overweeg een upgrade van v18-acties |
| **Inconsistentie in de naamgeving van patroon A versus B** | 🟡 Laag | Dezelfde inloggegevens opgeslagen onder verschillende sleutelnamen voor acties | Voer gewoon dezelfde waarden in — werkt prima, alleen verwarrend tijdens de installatie |

---

## Problemen oplossen

### "Geen account gevonden dat overeenkomt..."

De functie `resolve_customer_id()` zoekt naar accounts onder uw MCC. Zorg ervoor dat:
- Uw `LOGIN_CUSTOMER_ID` is het MCC-account (Manager), geen kinderaccount
- Het account dat u zoekt is gekoppeld aan uw MCC
- De zoekreeks komt overeen met een deel van de beschrijvende naam van het account

### "google-ads-pakket niet gevonden"

De systeemprompt instrueert de agent om `pip install google-ads>=28.1.0` uit te voeren aan het begin van elk gesprek. Als het mislukt:
- Zorg ervoor dat `code_interpreter` is ingeschakeld
- Probeer de installatie handmatig uit te voeren in het eerste bericht

### "OAuth-inloggegevens verlopen"

Vernieuwingstokens verlopen doorgaans niet, maar kunnen wel worden ingetrokken als:
- U heeft het wachtwoord van uw Google-account gewijzigd
- Je hebt de toegang tot de app verwijderd in [Google Beveiligingsinstellingen](https://myaccount.google.com/permissions)
- Het token is al meer dan 6 maanden niet gebruikt

**Opgelost:** Voer het genereren van vernieuwingstokens uit stap 1A-3 opnieuw uit.

### "Ontwikkelaarstoken niet goedgekeurd"

Als uw ontwikkelaarstoken zich in de modus 'Testaccount' bevindt:
- Het werkt alleen met [Google Ads-testaccounts](https://developers.google.com/google-ads/api/docs/first-call/test-accounts)
- Vraag basistoegang aan bij [Google Ads API Center](https://ads.google.com/aw/apicenter)
- Goedkeuring duurt doorgaans 1-3 werkdagen

### "Tarieflimiet overschreden"

De Google Ads API heeft deze limieten:
- **Basistoegang:** 15.000 bewerkingen/dag, 4 verzoeken/seconde
- **Standaardtoegang:** Onbeperkte bewerkingen, 100 verzoeken/seconde

Als de limieten worden bereikt, zou de Filter-First Architectuur van het systeem moeten helpen: gebruik de parameters `cost_min`, `status` en `limit` om de resultatensets te beperken.

### Subagent reageert niet

- Controleer of de subagent is gekoppeld in de lijst met subagenten van de hoofdagent
- Controleer of de actie Session & State Manager (#17) is geïnstalleerd
- Zorg ervoor dat de subagent zijn eigen inloggegevens heeft geconfigureerd (deze worden niet gedeeld met de hoofdagent)

---

## Beveiliging

Zie [`SECURITY.md`](SECURITY.md) voor:
- Kwetsbaarheidsrapportageproces
- CORS, snelheidsbeperking en invoervalidatiepraktijken
- Richtlijnen voor referentiebeheer
- Veiligheidsprotocol schrijven (CEP: Bevestigen → Uitvoeren → Nacontrole)Belangrijkste beveiligingsfuncties in v2.0:
- **Geen wildcard CORS** — server is standaard ingesteld op localhost; configureren via `ALLOWED_ORIGINS`
- **Snelheidslimiet** — 30 req/min per IP (configureerbaar via `RATE_LIMIT_MAX`)
- **Foutopschoning** — algemene clientfouten, volledige logboekregistratie aan de serverzijde
- **GAQL-injectiepreventie** — menstruatiewaarden op de witte lijst gezet
- **Geen hardgecodeerde geheimen** — alles via `.env` / omgevingsvariabelen

---

## Licentie

MIT-licentie. Zie [`LICENTIE`](LICENTIE) voor de volledige tekst.

De Google Ads API is onderworpen aan de [Servicevoorwaarden] van Google (https://developers.google.com/google-ads/api/docs/terms). Diensten van derden (Cloudinary, SearchAPI, Stripe) zijn onderworpen aan hun respectieve voorwaarden.

---

## Bijdragen

Zie [`CONTRIBUTING.md`](CONTRIBUTING.md) voor de volledige handleiding. Prioritaire gebieden:

1. **Optimalisatie-subagentacties**: er bestaat een systeemprompt, er moeten API-acties worden gebouwd
2. **Shopping- en PMax-subagentacties** — hetzelfde als hierboven
3. **Testdekking**: eenheidstests voor het implementatiepakket
4. **Semantisch geheugen** — vectoriseer geheugen van Buddy naar Python (pgvector/Pinecone)
5. **Streamingreacties**: voeg SSE-eindpunt toe voor real-time uitvoering van tools```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## Gerelateerde projecten

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — Antropische agentvaardigheden voor Claude (analyse, audit, schrijven, wiskunde, MCP)
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)** — Python MCP-server met 29 tools voor Claude Code, Claude Desktop, Cursor, OpenAI Agents SDK en elke MCP-client
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)** — Gemini CLI-extensie met 22 MCP-tools, vaardigheden, opdrachten en thema's
- **[googleadsagent.ai](https://googleadsagent.ai)** — Productie-implementatie (Buddy) op Cloudflare met semantisch geheugen, facturering en monitoring

---

> **Live op:** [googleadsagent.ai](https://googleadsagent.ai)  
> **Versie:** 2.0.0  
> **Licentie:** MIT  
> **Laatst bijgewerkt:** 05-03-2026