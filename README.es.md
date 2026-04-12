# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

Un sistema de administración de Google Ads de nivel empresarial impulsado por inteligencia artificial con **28 herramientas personalizadas**, **6 subagentes especializados** y **acceso de lectura/escritura en vivo** a cuentas de Google Ads a través de la API de Google Ads v22.

La versión de producción se ejecuta en **[googleadsagent.ai](https://googleadsagent.ai)** (Buddy) en el borde de Cloudflare, con memoria semántica, almacenamiento de claves cifradas, monitoreo automatizado y un sistema de facturación basado en créditos. Este repositorio es el agente Python de código abierto que impulsa las mismas capacidades.

---

## Novedades de la versión 2.0

- **Reforzamiento de la seguridad**: restricciones CORS, limitación de velocidad, desinfección de errores, prevención de inyección GAQL
- **Paquete instalable** — `pip install google-ads-agent` (o descárgalo desde [Versiones](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases))
- **Licencia MIT**: licencia adecuada de código abierto
- **Documentos de arquitectura de producción**: referencia completa de Cloudflare Buddy en [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md)
- **Política de seguridad** — [`SECURITY.md`](SECURITY.md) con informes de vulnerabilidad y mejores prácticas
- **Guía para contribuyentes** — [`CONTRIBUTING.md`](CONTRIBUTING.md) con áreas prioritarias y estilo de código
- **Plantilla de entorno** — [`.env.example`](.env.example) con todos los marcadores de posición de credenciales

Consulte el [CHANGELOG](CHANGELOG.md) completo para obtener más detalles.

---


## Tabla de contenidos

- [Inicio rápido](#inicio-rapido)
- [Tres rutas de implementación](#tres-rutas-de-implementacion)
  - [Lo que Buddy agrega (Ruta C)](#lo-que-buddy-agrega-ruta-c)
- [Ruta A: Implementación a través de la API Anthropic](#ruta-a-implementacion-a-traves-de-la-api-anthropic)
  - [Cómo funciona](#como-funciona)
  - [A-1: Obtenga su clave API de Anthropic](#a-1-obtenga-su-clave-api-de-anthropic)
  - [A-2: Instalar y ejecutar (Python)](#a-2-instalar-y-ejecutar-python)
  - [A-3: Úselo en su propio código](#a-3-uselo-en-su-propio-codigo)
  - [A-7: Errores conocidos](#a-7-errores-conocidos)
  - [A-8: El paquete de implementación: referencia del archivo](#a-8-el-paquete-de-implementacion-referencia-del-archivo)
- [Ruta B: Implementación en una plataforma de agente (IU manual)](#ruta-b-implementacion-en-una-plataforma-de-agente-iu-manual)
- [Requisitos previos](#requisitos-previos)
- [Paso 1: Obtener las credenciales API](#paso-1-obtener-las-credenciales-api)
  - [1A: Credenciales de la API de Google Ads](#1a-credenciales-de-la-api-de-google-ads)
  - [1B: Credenciales nubosas](#1b-credenciales-nubosas)
  - [1C: Credenciales de SearchAPI.io](#1c-credenciales-de-searchapiio)
  - [1D: Credenciales de Google AI/Gemini](#1d-credenciales-de-google-aigemini)
  - [Resumen: todas las credenciales](#resumen-todas-las-credenciales)
- [Paso 2: Crear el agente principal](#paso-2-crear-el-agente-principal)
  - [2.1 — Crear el Shell del agente](#21-crear-el-shell-del-agente)
  - [2.3 — Habilitar herramientas integradas](#23-habilitar-herramientas-integradas)
- [Paso 3: Instalar acciones personalizadas (28 en total)](#paso-3-instalar-acciones-personalizadas-28-en-total)
  - [Comprensión de los patrones de credenciales](#comprension-de-los-patrones-de-credenciales)
  - [Instalación acción por acción](#instalacion-accion-por-accion)
- [Paso 4: Crear subagentes (6 en total)](#paso-4-crear-subagentes-6-en-total)
  - [Subagente 1: Informes y análisis](#subagente-1-informes-y-analisis)
  - [Subagente 2: Investigación e Inteligencia](#subagente-2-investigacion-e-inteligencia)
  - [Subagente 3: Optimización](#subagente-3-optimizacion)
  - [Subagente 4: Compras y PMax](#subagente-4-compras-y-pmax)
  - [Subagente 5: Creativo](#subagente-5-creativo)
  - [Subagente 6: Baymax — Innovación creativa](#subagente-6-baymax-innovacion-creativa)
- [Paso 5: Vincular subagentes al agente principal](#paso-5-vincular-subagentes-al-agente-principal)
- [Paso 6: Conceder acceso al usuario](#paso-6-conceder-acceso-al-usuario)
- [Paso 7: Validación y prueba](#paso-7-validacion-y-prueba)
  - [Prueba 1: instalación del paquete](#prueba-1-instalacion-del-paquete)
- [Referencia de patrones de credenciales](#referencia-de-patrones-de-credenciales)
  - [Patrón A: Google Ads de cinco claves](#patron-a-google-ads-de-cinco-claves)
  - [Patrón C: Cloudinary de 3 teclas](#patron-c-cloudinary-de-3-teclas)
- [Descripción general de la arquitectura](#descripcion-general-de-la-arquitectura)
  - [Cómo se compara este repositorio con otros agentes de IA](#como-se-compara-este-repositorio-con-otros-agentes-de-ia)
- [Problemas conocidos](#problemas-conocidos)
- [Solución de problemas](#solucion-de-problemas)
  - ["No se encontró ninguna cuenta que coincida..."](#no-se-encontro-ninguna-cuenta-que-coincida)
  - ["paquete de anuncios de Google no encontrado"](#paquete-de-anuncios-de-google-no-encontrado)
  - ["Las credenciales de OAuth caducaron"](#las-credenciales-de-oauth-caducaron)
  - ["Token de desarrollador no aprobado"](#token-de-desarrollador-no-aprobado)
  - ["Límite de tarifa excedido"](#limite-de-tarifa-excedido)
  - [El subagente no responde](#el-subagente-no-responde)
- [Seguridad](#seguridad)
- [Licencia](#licencia)
- [Contribuyendo](#contribuyendo)
- [Proyectos relacionados](#proyectos-relacionados)

---
## Inicio rápido

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

## Tres rutas de implementación

| Camino | Mejor para | Lo que necesitas |
|------|----------|---------------|
| **A: API antrópica (programática)** | Aplicaciones de producción, SaaS, procesos de automatización | Clave API antrópica + Python |
| **B: Plataforma del agente (UI manual)** | Creación rápida de prototipos, constructor visual para un solo usuario | Cuenta de plataforma de agente |
| **C: Producción de Cloudflare (amigo)** | Full-stack con memoria, facturación, monitoreo | Cuenta de Cloudflare |

**Ruta A** es lo que este repositorio proporciona de forma inmediata. La ruta C es el sistema de producción en [googleadsagent.ai](https://googleadsagent.ai); consulte [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md) para conocer la arquitectura completa.

### Lo que Buddy agrega (Ruta C)

| Capacidad | Tecnología |
|-----------|-----------|
| Estado persistente por usuario | Objetos duraderos + SQLite |
| Memoria semántica | Vectorizar incrustaciones |
| Almacenamiento BYOK cifrado | AES-256-GCM |
| WebSocket en tiempo real | SDK de agentes de Cloudflare |
| Monitoreo automatizado | Trabajadores cron |
| Facturación basada en crédito | D1 + Raya |
| IA multiproveedor | Claude, GPT, enrutamiento Géminis |
| Exportaciones de archivos | Almacenamiento de objetos R2 |

---

## Ruta A: Implementación a través de la API Anthropic

Esta es la **implementación programática**: sin interfaz de usuario manual ni clics. Todo se ejecuta a través de la API de mensajes de Claude con el uso de herramientas.

### Cómo funciona

Los archivos de acciones de este repositorio se crearon originalmente para una plataforma de agente. El paquete `deploy/` los adapta para ejecutarse de forma independiente a través de la API Anthropic. Esto es lo que sucede internamente cuando ejecutas `python scripts/cli.py`:

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

**Qué resuelve la capa adaptadora (`tool_executor.py`):**

| Problema | Qué hacen los archivos de acción | Qué hace el adaptador |
|---------|------------------------|----------------------|
| **Secretos** | Referencia `secretos["KEY"]` como un global simple inyectado por la plataforma del agente | Inyecta `secrets` dict en el módulo `__dict__` antes de `exec_module()` |
| **Instalaciones de tuberías** | Ejecute `subprocess.check_call(["pip", "install", "google-ads"])` en el momento de la importación | Subproceso Monkey-patches para omitir comandos pip (los departamentos ya están en `requirements.txt`) |
| **No coinciden los parámetros** | 26/28 las funciones `run()` tienen parámetros explícitos (sin `**kwargs`) | Inspecciona la firma `run()` mediante `inspect.signature()`, descarta cualquier parámetro que envíe Claude y que no esté en la función |

### A-1: Obtenga su clave API de Anthropic

1. Vaya a **[Consola Anthropic](https://console.anthropic.com)**
2. Regístrate o inicia sesión
3. Vaya a **[Configuración → Claves API](https://console.anthropic.com/settings/keys)**
4. Haga clic en **Crear clave**
5. Copie la clave → esta es su `ANTHROPIC_API_KEY`

> 💡 La clave comienza con `sk-ant-api03-...`. Guárdelo de forma segura: otorga acceso completo a la API.

**Cómo se relaciona esto con el sistema:** Cada llamada a la API de mensajes de Claude requiere esta clave en el encabezado `x-api-key`. El SDK de Python `anthropic` lo lee automáticamente desde la var env `ANTHROPIC_API_KEY`.

### A-2: Instalar y ejecutar (Python)

**Qué sucede, paso a paso, cuando ejecutas esto:**

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

**Después del paso 6, verás:**

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
```Eso es todo. El agente se está ejecutando y realiza llamadas reales a la API de Google Ads a través de sus credenciales, con Claude organizando a qué herramientas llamar y cómo interpretar los resultados.

### A-3: Úselo en su propio código

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
```### A-4: Implementar como API REST

El servidor FastAPI incluido le brinda puntos finales HTTP para cualquier interfaz o integración:

```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**Puntos finales:**

| Método | Camino | Descripción |
|--------|------|-------------|
| `POST` | `/chat` | Enviar un mensaje, obtener una respuesta (sesión de creación automática) |
| `POST` | `/ sesiones` | Crear una nueva sesión de conversación |
| `OBTENER` | `/sesiones/{id}` | Obtenga información de la sesión y recuento de mensajes |
| `BORRAR` | `/sesiones/{id}` | Eliminar una sesión |
| `OBTENER` | `/salud` | Comprobación de estado (estado de la credencial) |
| `OBTENER` | `/herramientas` | Enumere las 28 herramientas y su estado de archivo |

**Solicitud de ejemplo:**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**Respuesta de ejemplo:**

```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5: Implementar con Docker```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6: Consideraciones de escala

| Preocupación | Estado actual | Actualización de producción |
|---------|--------------|-------------------|
| **Sesiones** | Diccionado en memoria | Cambie a Redis: agregue el servicio `redis` en docker-compose, reemplace el diccionario `sessions` con el cliente Redis |
| **Límites de tarifas** | Límites de API antrópica por nivel | Agregue cola de solicitudes con `apio` o `asyncio.Semaphore` |
| **Multiinquilino** | Conjunto de credenciales único | Cargar credenciales por inquilino desde un administrador de secretos (AWS Secrets Manager, HashiCorp Vault) |
| **Autenticación** | Ninguno | Agregue middleware de clave API u OAuth2 al servidor FastAPI |
| **Monitoreo** | Registro básico | Agregar registro estructurado + exportar a Datadog/CloudWatch |
| **Control de costes** | Ninguno | Realice un seguimiento del uso de tokens a través de `response.usage` y establezca alertas de presupuesto |
| **Lógica de reintento** | Valor predeterminado del SDK (2 reintentos) | Ajuste `max_retries` y agregue un retroceso exponencial para las llamadas a la API de Google Ads |

### A-7: Errores conocidos

Cosas que podrían hacerte tropezar en la primera carrera:

| Problema | Qué pasa | Arreglar |
|-------|-------------|-----|
| **La importación de Google Ads falla** | Los archivos de acción necesitan `google-ads>=28.1.0` que tiene dependencias de C | Primero ejecute `pip install -r requisitos.txt`; esta es la razón por la que el adaptador suprime las instalaciones de pip en línea |
| **Error clave `secretos`** | Una acción intenta acceder a una credencial que no configuró en `.env` | Verifique qué patrón de credenciales utiliza la herramienta (A/B/C/D) y verifique que `.env` tenga esas claves |
| **Error de tipo al ejecutar()** | Claude envía un parámetro que la función run() no acepta | El filtro de parámetros debería detectar esto; si no es así, marque `python -c "desde implementar import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"` |
| **Límites de tarifas** | Acceso básico a la API de Google Ads = 15.000 operaciones/día, 4 solicitudes/seg. Utilice los parámetros `cost_min`, `status`, `limit` para reducir los conjuntos de resultados |
| **La primera carga es lenta** | La carga del módulo + supresión de pips agrega ~1-2 segundos en la primera llamada a la herramienta | Las llamadas posteriores utilizan módulos almacenados en caché: instantáneo |
| **Costos simbólicos** | claude-opus-4-5 con 28 definiciones de herramientas = ~4K tokens por solicitud solo para herramientas | Para optimizar costos, cambie a `claude-sonnet-4-5-20250929` en el constructor |

### A-8: El paquete de implementación: referencia del archivo

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

## Ruta B: Implementación en una plataforma de agente (IU manual)

Si prefiere un constructor visual (OpenAI o similar), siga los pasos 2 a 7 a continuación. Pegará las indicaciones del sistema, el código de acción y las credenciales en la interfaz de usuario de la plataforma.

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

## Requisitos previos

Antes de comenzar, necesitará:

| Requisito | Por qué | Costo |
|-------------|-----|------|
| **Clave API antrópica** | Alimenta al agente Claude a través de la API de mensajes | Pago por uso ([precios](https://docs.anthropic.com/en/docs/about-claude/pricing)) |
| **Cuenta de Google Ads** | Acceso API para gestionar campañas | Gratis (los anuncios se gastan por separado) |
| **Cuenta de Google Ads Manager (MCC)** | Acceso multicuenta | Gratis |
| **Proyecto Google Cloud Platform** | Credenciales OAuth2 para la API de Google Ads | Nivel gratuito disponible |
| **Cuenta Cloudinary** | Procesamiento de imágenes/vídeo para recursos creativos | Nivel gratuito (25 créditos/mes) |
| **Cuenta SearchAPI.io** | Búsqueda en Google en tiempo real, Tendencias, Transparencia de anuncios | Nivel gratuito (100 búsquedas/mes) |
| **Cuenta de Google AI Studio** | API Gemini para la generación creativa de IA | Nivel gratuito disponible |
| **Cuenta de plataforma de agente** | Dónde implementa el agente (por ejemplo, OpenAI o similar) | Varía |

---

## Paso 1: Obtener las credenciales API

Necesita credenciales de **4 servicios**. Esta sección recorre cada uno con las URL exactas, orientación sobre capturas de pantalla y qué copiar.

---

### 1A: Credenciales de la API de Google Ads

Esta es la configuración más compleja. Necesitas **5 valores** que funcionen juntos:

| Credencial | Qué es | Dónde vive |
|------------|-----------|----------------|
| `DESARROLLADOR_TOKEN` | Tu clave de acceso API de Google Ads | Interfaz de usuario de Google Ads |
| `ID_CLIENTE` | Identificador de aplicación OAuth2 | Consola de Google Cloud |
| `CLIENTE_SECRETO` | Secreto de la aplicación OAuth2 | Consola de Google Cloud |
| `REFRESH_TOKEN` | Token OAuth2 de larga duración | Generado a través del flujo OAuth |
| `LOGIN_CUSTOMER_ID` | Su ID de cuenta de MCC | Interfaz de usuario de Google Ads |

#### Paso 1A-1: Obtenga su token de desarrollador

1. Vaya a **[Google Ads](https://ads.google.com)** e inicie sesión con su cuenta de administrador (MCC).
2. Haga clic en el icono **Herramientas y configuración** (llave inglesa) en la navegación superior.
3. En **Configuración**, haga clic en **Centro API**
   - Si no ve el Centro API, es posible que primero deba solicitar acceso
4. Su **Token de desarrollador** se muestra en esta página
5. **Nivel de acceso al token:**
   - `Cuenta de prueba`: funciona solo con cuentas de prueba (bueno para el desarrollo)
   - `Acceso Básico` — hasta 15.000 operaciones/día (solicite esto)
   - `Acceso estándar`: ilimitado (se aplica después de demostrar el uso)
6. **Copia el token** → este es tu `GOOGLE_ADS_DEVELOPER_TOKEN`

> ⚠️ Si tu token muestra el estado "Pendiente", aún puedes usarlo con cuentas de prueba. Para la producción, debe [solicitar acceso básico](https://developers.google.com/google-ads/api/docs/access-levels).

#### Paso 1A-2: Crear credenciales OAuth2 en Google Cloud

1. Vaya a **[Google Cloud Console](https://console.cloud.google.com)**
2. Cree un nuevo proyecto (o seleccione uno existente):
   - Haga clic en el menú desplegable del proyecto en la parte superior → **Nuevo proyecto**
   - Nombre: `google-ads-agent` (o el que prefieras)
   - Haga clic en **Crear**
3. **Habilite la API de Google Ads:**
   - Vaya a **[API y servicios → Biblioteca](https://console.cloud.google.com/apis/library)**
   - Busque "API de anuncios de Google"
   - Haga clic en él → Haga clic en **Activar**
4. **Configure la pantalla de consentimiento de OAuth:**
   - Vaya a **[API y servicios → Pantalla de consentimiento de OAuth](https://console.cloud.google.com/apis/credentials/consent)**
   - Seleccione **Externo** (a menos que tenga Google Workspace, luego Interno)
   - Complete:
     - Nombre de la aplicación: "Agente de Google Ads"
     - Correo electrónico de atención al usuario: tu correo electrónico
     - Contacto del desarrollador: tu correo electrónico
   - Haga clic en **Guardar y continuar**
   - **Ámbitos:** Haga clic en **Agregar o quitar ámbitos** → busque `Google Ads API` → marque `https://www.googleapis.com/auth/adwords` → **Actualizar** → **Guardar y continuar**
   - **Usuarios de prueba:** Agregue el correo electrónico de su cuenta de Google Ads → **Guardar y continuar**
   - Haga clic en **Volver al panel**
5. **Crear ID de cliente OAuth2:**
   - Vaya a **[API y servicios → Credenciales](https://console.cloud.google.com/apis/credentials)**
   - Haga clic en **+ Crear credenciales** → **ID de cliente OAuth**
   - Tipo de aplicación: **Aplicación web**
   - Nombre: "Agente de Google Ads"
   - URI de redireccionamiento autorizado: agregue `http://localhost:8080` (necesario para el paso de generación del token)
   - Haga clic en **Crear**
   - **Copia el ID del cliente** → este es tu `GOOGLE_ADS_CLIENT_ID`- **Copia el secreto del cliente** → este es tu `GOOGLE_ADS_CLIENT_SECRET`

#### Paso 1A-3: generar un token de actualización

El token de actualización permite al agente autenticarse sin interacción del usuario. Lo generas una vez y dura indefinidamente (a menos que sea revocado).

**Opción A: Usar OAuth2 Playground de Google (más fácil)**

1. Vaya a **[OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)**
2. Haz clic en el **ícono de ajustes** ⚙️ (arriba a la derecha)
   - Marque **Utilice sus propias credenciales de OAuth**
   - Ingrese su "ID de cliente" y "Secreto de cliente" del Paso 1A-2
   - Cerrar la configuración
3. En el panel izquierdo, desplácese hasta **Google Ads API v18** → marque `https://www.googleapis.com/auth/adwords`
4. Haga clic en **Autorizar API**
5. Inicia sesión con la cuenta de Google que tiene acceso a tus cuentas de Google Ads.
6. Conceder los permisos solicitados
7. Haga clic en **Código de autorización de intercambio por tokens**
8. **Copia el token de actualización** → este es tu `GOOGLE_ADS_REFRESH_TOKEN`

**Opción B: uso de la biblioteca Python de Google-Ads**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```Esto abre un navegador para el consentimiento de OAuth e imprime el token de actualización.

**Opción C: Usar curl**```bash
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
```#### Paso 1A-4: Obtenga su ID de cliente de inicio de sesión (MCC)

1. Vaya a **[Google Ads](https://ads.google.com)**
2. Inicie sesión en su **Cuenta de administrador** (MCC)
3. Su **ID de cliente** se muestra en la parte superior derecha, con el formato `XXX-XXX-XXXX`.
4. **Cópielo** → este es su `GOOGLE_ADS_LOGIN_CUSTOMER_ID`

> 💡 El ID de cliente de inicio de sesión solo es necesario si estás utilizando un MCC para administrar varias cuentas. Si administra una sola cuenta directamente, puede dejar esto en blanco.

#### Paso 1A-5: Verifique sus credenciales

Cree un archivo de prueba para verificar que todo funciona:

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
```Si esto imprime los nombres de los recursos de la cuenta, sus credenciales de Google Ads están funcionando.

---

### 1B: Credenciales nubosas

Cloudinary maneja todo el procesamiento de imágenes/vídeo: cambio de tamaño, relleno generativo de IA y formato específico de la plataforma.

1. Vaya a **[Registro en Cloudinary](https://cloudinary.com/users/register_free)** y cree una cuenta gratuita
   - El nivel gratuito incluye 25 créditos/mes (suficiente para ~1000 transformaciones)
2. Después de registrarse, vaya a **[Dashboard](https://console.cloudinary.com/pm/getting-started/dashboard)**
3. Sus credenciales se muestran directamente en el panel:
   - **Nombre de la nube** → `CLOUDINARY_CLOUD_NAME`
   - **Clave API** → `CLOUDINARY_API_KEY`
   - **API Secret** → `CLOUDINARY_API_SECRET` (haga clic en "Revelar" para verlo)

> 💡 El nivel gratuito es generoso para el desarrollo. Para producción con mucho procesamiento creativo, el plan Plus ($89/mes) ofrece 225 créditos.

#### Cómo se conecta Cloudinary con el agente

La acción **Cloudinary Creative Tools** (Acción n.º 18 en el agente principal) y el subagente **Baymax — Creative Innovate** utilizan estas credenciales. Permiten:
- Carga de imágenes/vídeos desde URL
- Cambio de tamaño para más de 20 ajustes preestablecidos de plataforma (Instagram, TikTok, YouTube, anuncios gráficos, etc.)
- Relleno generativo de IA para ampliar imágenes a relaciones de aspecto no estándar
- Procesamiento por lotes en múltiples plataformas

---

### 1C: Credenciales de SearchAPI.io

SearchAPI.io proporciona resultados de búsqueda de Google en tiempo real, datos de Google Trends y acceso al Centro de transparencia de Google Ads para el subagente de Investigación e Inteligencia.

1. Vaya a **[Registro en SearchAPI.io](https://www.searchapi.io/signup)**
   - Nivel gratuito: 100 búsquedas/mes
2. Después de registrarse, vaya a **[Panel → Clave API](https://www.searchapi.io/dashboard)**
3. **Copia tu clave API** → `SEARCHAPI_API_KEY`

#### Cómo se conecta SearchAPI con el agente

**Nemo — Investigación e Inteligencia** utiliza SearchAPI a través de tres acciones personalizadas:
- **API de búsqueda de Google**: resultados SERP en tiempo real con anuncios, gráficos orgánicos y de conocimiento
- **Centro de transparencia de Google Ads**: vea qué anuncios publican los competidores
- **Google Trends Analyzer**: datos de tendencias, consultas relacionadas, interés geográfico

Estas acciones pasan la clave API a través de `secrets["SEARCHAPI_API_KEY"]` en el código fuente de cada acción.

---

### 1D: Credenciales de Google AI/Gemini

Baymax - Creative Innovate utiliza la API Gemini de Google para la generación de imágenes y el análisis de visión con tecnología de inteligencia artificial.

1. Vaya a **[Google AI Studio](https://aistudio.google.com)**
2. Inicia sesión con tu cuenta de Google
3. Haga clic en **Obtener clave API** en la barra lateral izquierda (o vaya directamente a **[Claves API](https://aistudio.google.com/apikey)**)
4. Haga clic en **Crear clave API**
   - Seleccione el proyecto de Google Cloud que creó en el Paso 1A-2 (o cree uno nuevo)
5. **Copia la clave API** → `GOOGLE_AI_API_KEY`

> 💡 El nivel gratuito proporciona 15 RPM (solicitudes por minuto) para Gemini 2.0 Flash. Para la producción, la tarifa de pago por uso es muy asequible.

#### Cómo se conecta Gemini con el agente

El subagente **Baymax — Creative Innovate** utiliza Gemini para:
- Generación/extensión de imágenes de IA para formatos de redes sociales.
- Análisis de visión de activos creativos existentes.
- Generar variaciones de anuncios gráficos a partir de imágenes de origen.

El archivo de acción de Gemini se encuentra en `actions/sub-agents/creative-innovate/02_gemini_vision.py`.

---

### Resumen: todas las credenciales

Después de completar los pasos 1A a 1D, su archivo `.env` debería verse así:

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

## Paso 2: Crear el agente principal

> Estas instrucciones utilizan terminología genérica. Adapte los nombres/menús de los botones para su plataforma de agente específica (por ejemplo, OpenAI o similar).

### 2.1 — Crear el Shell del agente

1. En su plataforma de agente, cree un nuevo agente con esta configuración:

| Configuración | Valor |
|---------|-------|
| Nombre | `Agente API de Google Ads` |
| Modelo | `claude-opus-4-5` (Antrópico) |
| Acceso | Privado |

2. **Establezca la descripción:**

```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — Pegar el mensaje del sistema

1. Abra el archivo: `prompts/main_agent_system_prompt.md`
2. Copie el **contenido completo**
3. Pegue en el campo de instrucciones/indicaciones del sistema de su agente.
4. Guardar

### 2.3 — Habilitar herramientas integradas

Habilite estas 10 herramientas integradas (los nombres pueden variar según la plataforma):

- [x] Intérprete de código
- [x] Búsqueda web (Google)
- [x] Investigador
- [x] Todo / Lista de tareas
- [x] Raspador web
- [x] Ejecutor de consultas (SQL)
- [x] Lector CSV
- [x] Comparador de cadenas
- [x] Mostrar archivo
- [x] Búsqueda de archivos

---

## Paso 3: Instalar acciones personalizadas (28 en total)

Cada acción personalizada es un archivo Python que se pega en el generador de acciones personalizadas de su plataforma de agente. Necesitarás:

1. Crea la acción
2. Pega el código fuente
3. Configurar las credenciales (secretos)

### Comprensión de los patrones de credenciales

Hay 4 patrones de credenciales. Sepa cuál utiliza cada acción antes de comenzar:

| Patrón | # de secretos | Acciones al usarlo |
|---------|-------------|-----------------|
| **A** (Google Ads de cinco teclas) | 5 | 12 acciones: incluye `LOGIN_CUSTOMER_ID` como secreto |
| **B** (Google Ads de 4 teclas) | 4 | 13 acciones: pasa `login_customer_id` como parámetro de función |
| **C** (Nubinario de 3 teclas) | 3 | 1 acción — Herramientas creativas de Cloudinary |
| **D** (Sin credenciales) | 0 | 3 acciones: instalador de paquetes, administrador de sesiones, documento de reconstrucción |

Consulte [Referencia de patrones de credenciales](#credential-patterns-reference) para obtener detalles completos.

### Instalación acción por acción

Para **cada acción** a continuación, siga este proceso:

```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### Acciones del patrón A (Google Ads de 5 teclas): 12 acciones

Para cada uno, agrega estos 5 secretos:

| Clave secreta | Valor de .env |
|------------|----------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Tu token de desarrollador |
| `GOOGLE_ADS_CLIENT_ID` | Su ID de cliente OAuth2 |
| `GOOGLE_ADS_CLIENT_SECRET` | Su secreto de cliente OAuth2 |
| `GOOGLE_ADS_REFRESH_TOKEN` | Tu token de actualización |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Su ID de cliente de MCC |

| # | Nombre de la acción | Archivo fuente |
|---|-------------|------------|
| 1 | Administrador de etiquetas | `acciones/main-agent/01_label_manager.py` |
| 2 | Administrador de seguimiento de conversiones | `acciones/main-agent/02_conversion_tracking_manager.py` |
| 12 | Administrador de guiones | `acciones/main-agent/12_scripts_manager.py` |
| 13 | Gerente de Experimentos | `acciones/main-agent/13_experiments_manager.py` |
| 19 | Planificador de consultas y administrador de presupuesto | `acciones/main-agent/19_query_planner.py` |
| 20 | Gerente de Recomendaciones | `acciones/main-agent/20_recommendations_manager.py` |
| 23 | Administrador de rendimiento del dispositivo | `acciones/main-agent/23_device_rendimiento_manager.py` |
| 24 | Administrador de historial de cambios | `acciones/main-agent/24_change_history_manager.py` |
| 25 | Creador de campañas | `acciones/main-agent/25_campaign_creator.py` |
| 26 | Administrador de programación de anuncios | `acciones/main-agent/26_ad_schedule_manager.py` |
| 27 | Gerente de Estrategia de Ofertas | `acciones/main-agent/27_bidding_strategy_manager.py` |
| 28 | Gerente del Grupo de Activos PMax | `acciones/main-agent/28_pmax_asset_group_manager.py` |

#### Acciones del patrón B (Google Ads de 4 teclas): 13 acciones

Para cada uno, agrega estos 4 secretos:

| Clave secreta | Valor de .env |
|------------|----------------|
| `DESARROLLADOR_TOKEN` | Tu token de desarrollador |
| `ID_CLIENTE` | Su ID de cliente OAuth2 |
| `CLIENTE_SECRETO` | Su secreto de cliente OAuth2 |
| `REFRESH_TOKEN` | Tu token de actualización |

> ⚠️ Nota: Los **nombres de clave** son diferentes del Patrón A (sin prefijo `GOOGLE_ADS_`). Esto es por diseño: estas acciones aceptan `login_customer_id` como parámetro de función.

| # | Nombre de la acción | Archivo fuente |
|---|-------------|------------|
| 3 | Gerente de audiencia | `acciones/main-agent/03_audience_manager.py` |
| 4 | Gerente de Activos | `acciones/main-agent/04_asset_manager.py` |
| 5 | Gerente de Presupuesto | `acciones/main-agent/05_budget_manager.py` |
| 6 | Administrador de anuncios RSA | `acciones/main-agent/06_rsa_ad_manager.py` |
| 7 | Administrador de ofertas y palabras clave | `acciones/main-agent/07_bid_keyword_manager.py` |
| 8 | Administrador de palabras clave negativas | `acciones/main-agent/08_negative_keywords_manager.py` |
| 9 | Administrador de campañas y grupos de anuncios | `acciones/main-agent/09_campaign_adgroup_manager.py` |
| 10 | Mutación de anuncios de Google | `acciones/main-agent/10_google_ads_mutate.py` |
| 11 | Comprobador de acceso a cuenta | `acciones/main-agent/11_account_access_checker.py` |
| 15 | Verificar niveles de acceso de usuarios | `acciones/main-agent/15_check_user_access.py` |
| 16 | Puerta de enlace API: administrador de contexto | `acciones/main-agent/16_api_gateway.py` |
| 21 | Administrador de términos de búsqueda | `acciones/main-agent/21_search_term_manager.py` |
| 22 | Gerente de orientación geográfica y geográfica | `acciones/main-agent/22_geo_location_manager.py` |

#### Acción del patrón C (Cloudinary de 3 teclas) — 1 acción

| Clave secreta | Valor de .env |
|------------|----------------|
| `NOMBRE_NUBE_NUBE` | El nombre de tu nube Cloudinary |
| `CLOUDINARY_API_KEY` | Su clave API de Cloudinary |
| `CLOUDINARY_API_SECRET` | Su secreto API de Cloudinary |

| # | Nombre de la acción | Archivo fuente |
|---|-------------|------------|
| 18 | Herramientas creativas de Cloudinary | `acciones/main-agent/18_cloudinary_creative_tools.py` |

#### Acciones del patrón D (sin credenciales): 3 acciones

Simplemente pegue el código, no se necesitan secretos.

| # | Nombre de la acción | Archivo fuente |
|---|-------------|------------|
| 14 | Instalador de paquetes | `acciones/main-agent/14_package_installer.py` |
| 17 | Gerente de sesión y estado | `acciones/main-agent/17_session_state_manager.py` |

> 📌 **Consejo:** Si su plataforma admite la importación masiva de acciones, utilice `configs/agent_registry.json` como fuente de verdad para ID, nombres y patrones de credenciales.

---

## Paso 4: Crear subagentes (6 en total)

Cada subagente es un agente independiente en el que el agente principal delega tareas. Cada uno tiene su propio sistema, herramientas y acciones personalizadas.

### Subagente 1: Informes y análisis

| Configuración | Valor |
|---------|-------|
| Nombre | `Simba — Informes y análisis` |
| Modelo | `claude-opus-4-5` |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/01_reporting_analysis.md` |

**Acciones personalizadas (8):** Instalar desde `acciones/subagentes/informes/`

| # | Acción | Archivo fuente | Credenciales |
|---|--------|-----------|-------------|
| 1 | Reportero de desempeño | `01_rendimiento_reporter.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 2 | Analizador de términos de búsqueda | `02_search_terms_analyzer.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 3 | Visor interactivo de palabras clave | `03_interactive_keyword_viewer.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 4 | Visor de anuncios interactivo | `04_interactive_ad_viewer.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 5 | Reportero de estadísticas de subastas | `05_auction_insights_reporter.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 6 | Auditor de historial de cambios | `06_change_history_auditor.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 7 | Informes mejorados de PMax | `07_pmax_enhanced_reporting.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 8 | Instalador de paquetes | `08_package_installer.py` | Ninguno (Patrón D) |

**Herramientas integradas (9):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, investigador, google_web_search

> ⚠️ Las acciones 3 y 4 (palabras clave interactivas/visores de anuncios) usan la API de Google Ads **v18** mientras que las demás usan **v19**. Verifique que el paquete pip `google-ads` admita ambos.

---

### Subagente 2: Investigación e Inteligencia

| Configuración | Valor |
|---------|-------|
| Nombre | `Nemo — Investigación e Inteligencia` |
| Modelo | `claude-opus-4-5` |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/02_research_intelligence.md` |

**Acciones personalizadas (4+1):** Instalar desde `acciones/sub-agentes/research/`

| # | Acción | Archivo fuente | Credenciales |
|---|--------|-----------|-------------|
| 1 | Planificador de palabras clave | `01_keyword_planner.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 2 | API de búsqueda de Google | `02_google_search_api.py` | 1 secreto: `SEARCHAPI_API_KEY` |
| 3 | Centro de transparencia de anuncios | `03_ads_transparency_center.py` | 1 secreto: `SEARCHAPI_API_KEY` |
| 4 | Analizador de tendencias de Google | `04_google_trends_analyzer.py` | 1 secreto: `SEARCHAPI_API_KEY` |
| 5 | Instalador de paquetes | *(reutilización del agente principal)* | Ninguno (Patrón D) |

**Herramientas integradas (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, investigador, google_web_search, web_scraper

---

### Subagente 3: Optimización

| Configuración | Valor |
|---------|-------|
| Nombre | `Elsa — Optimización` |
| Modelo | `claude-opus-4-5` |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/03_optimización.md` |

**Acciones personalizadas:** ⚠️ **NO EXISTE AÚN**

El mensaje del sistema de este subagente hace referencia a dos acciones personalizadas que deben crearse:
- **Administrador de recomendaciones - API** — `lista`, `aplicar`, `descartar`, `get_score`
- **Administrador de operaciones masivas - API** — `bulk_pause`, `bulk_enable`, `bulk_bid_change`, `bulk_budget_change`, `export`

> 🔧 **TODO:** Cree estas acciones utilizando la API de Google Ads. Las firmas de los parámetros están documentadas en el archivo de aviso del sistema. Ambos usarían credenciales del Patrón B (Google Ads de 4 teclas).

**Herramientas integradas (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, investigador, google_web_search, web_scraper

---

### Subagente 4: Compras y PMax

| Configuración | Valor |
|---------|-------|
| Nombre | `Aladdin — Compras y PMax` |
| Modelo | `claude-opus-4-5` |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/04_shopping_pmax.md` |

**Acciones personalizadas:** ⚠️ **NO EXISTE AÚN**

El mensaje del sistema de este subagente hace referencia a una acción personalizada que debe crearse:
- **Compras y PMax Manager - API** — `list_shopping`, `list_pmax`, `list_asset_groups`, `get_product_rendimiento`, `get_pmax_rendimiento`, `get_pmax_insights`, `pause_asset_group`, `enable_asset_group`

> 🔧 **TODO:** Cree esta acción utilizando la API de Google Ads (`google-ads` Python SDK). Usaría credenciales del Patrón B. El PMax Asset Group Manager del agente principal (Acción n.º 28) cubre parte de esta funcionalidad y puede servir como plantilla inicial.**Herramientas integradas (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, investigador, google_web_search, web_scraper

---

### Subagente 5: Creativo

| Configuración | Valor |
|---------|-------|
| Nombre | `Moana — Creativo` |
| Modelo | `claude-opus-4-5` |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/05_creative.md` |

**Acciones personalizadas (2):** Instalar desde `acciones/sub-agentes/creativo/`

| # | Acción | Archivo fuente | Credenciales |
|---|--------|-----------|-------------|
| 1 | Administrador de anuncios de display responsivos | `01_responsive_display_ads_manager.py` | Anuncios de Google de 4 teclas (Patrón B) |
| 2 | Gerente de anuncios de generación de demanda | `02_demand_gen_ads_manager.py` | Anuncios de Google de 4 teclas (Patrón B) |

**Herramientas integradas (10):** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, google_web_search, investigador, web_scraper

---

### Subagente 6: Baymax — Innovación creativa

| Configuración | Valor |
|---------|-------|
| Nombre | `Baymax — Innovación creativa` |
| Modelo | `claude-sonnet-4-5` ⚡ *(modelo más ligero - intencional)* |
| Acceso | CHAT_ONLY |
| Aviso del sistema | `prompts/sub-agentes/06_creative_innovate.md` |

**Acciones personalizadas (2+1):** Instalar desde `actions/sub-agents/creative-innovate/`

| # | Acción | Archivo fuente | Credenciales |
|---|--------|-----------|-------------|
| 1 | Herramientas nubosas | `01_cloudinary_tools.py` | Cloudinary de 3 teclas (Patrón C) |
| 2 | Visión de Géminis | `02_gemini_vision.py` | 1 secreto: `GOOGLE_AI_API_KEY` |
| 3 | Instalador de paquetes | *(reutilización del agente principal)* | Ninguno (Patrón D) |

---

## Paso 5: Vincular subagentes al agente principal

Después de crear los 6 subagentes, debe registrarlos con el agente principal para que pueda delegar tareas.

1. Vaya a la configuración del **Agente principal**
2. Busque la sección **Subagentes**
3. Agregue cada subagente buscando su nombre o ID:

| # | Nombre del subagente | ID del agente |
|---|----------|----------|
| 1 | Simba — Informes y análisis | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Nemo — Investigación e inteligencia | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 | Elsa — Optimización | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 | Aladdin — Compras y PMax | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 | Moana — Creativa | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 | Baymax — Innovación creativa | `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 Nota: Los ID de los agentes serán **diferentes** si estás creando nuevos agentes (se generan automáticamente). Los ID anteriores pertenecen a la compilación original y se proporcionan como referencia.

El mensaje del sistema del agente principal incluye el **Protocolo de delegación de subagente** que le indica cuándo manejar las tareas directamente o delegar. El **Responsable de sesión y estado** (Acción n.° 17) coordina los traspasos.

---

## Paso 6: Conceder acceso al usuario

Si necesita compartir el agente con miembros del equipo:

1. Vaya a Configuración del agente principal → **Compartir/Acceder**
2. Agregue usuarios con permiso **CAN_EDIT**
3. Podrán utilizar y modificar el agente.

---

## Paso 7: Validación y prueba

Ejecute estas pruebas para verificar que todo el sistema esté funcionando:

### Prueba 1: instalación del paquete

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### Prueba 2: Conexión de cuenta```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### Prueba 3: Resumen de cuenta```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### Prueba 4: operación de lectura```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### Prueba 5: operación de escritura (segura)```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### Prueba 6: Delegación de subagente```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### Prueba 7: Nubosidad```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## Referencia de patrones de credenciales

### Patrón A: Google Ads de cinco claves

Usado por **12 acciones** donde el ID de cliente de inicio de sesión de MCC se almacena como secreto.```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### Patrón B: Google Ads de cuatro teclas

Utilizado por **13 acciones** donde el ID de cliente de inicio de sesión se pasa como parámetro de función.```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ Los **valores** son idénticos al Patrón A. Solo difieren los **nombres clave**. Esto se debe a que algunas acciones se escribieron con diferentes convenciones de nomenclatura. Las credenciales subyacentes son las mismas.

### Patrón C: Cloudinary de 3 teclas

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### Patrón D: Sin credenciales

Acciones que no llaman a API externas: instalador de paquetes, administrador de sesión y estado.

---

## Descripción general de la arquitectura

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
```Para conocer la arquitectura técnica completa con esquemas de acción, firmas de parámetros y flujo de delegación, consulte **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

Para conocer la arquitectura de producción de Cloudflare Buddy (Durable Objects, Vectorize, D1, R2, Agents SDK), consulte **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**.

### Cómo se compara este repositorio con otros agentes de IA

| Característica | Este agente | Secuencias de comandos de anuncios de Google | Copiloto de Microsoft | Perplejidad | Claude genérico |
|---------|-----------|-------------------|-------------------|------------|---------------|
| API de Google Ads en vivo R/W | 28 acciones | secuencias de comandos sólo JS | Sin acceso a anuncios | Sin API | Sin API |
| Seguridad de escritura (CEP) | Confirmar/Ejecutar/Publicar | Ninguno | N/A | N/A | N/A |
| IA multiproveedor | Claude + GPT + Géminis | N/A | Sólo GPT | Modelos propios | Sólo Claudio |
| Delegación de subagentes | 6 especialistas | N/A | N/A | N/A | N/A |
| Memoria semántica | Vectorizar (producir) | Ninguno | Limitado | Incorporado | Sólo conversación |
| Autodesplegable | 3 caminos | Editor de guiones | Sólo SaaS | Sólo SaaS | Sólo API |

---

## Problemas conocidos

| Problema | Gravedad | Detalles | Solución alternativa |
|-------|----------|---------|------------|
| **El subagente de optimización no tiene acciones** | 🔴 Crítico | El mensaje del sistema describe el Administrador de recomendaciones y el Administrador de operaciones masivas, pero no existe ninguna acción | Constrúyalos utilizando la API de Google Ads o utilice directamente el Administrador de recomendaciones del agente principal (n.º 20) |
| **El subagente de Shopping y PMax no tiene acciones** | 🔴 Crítico | El mensaje del sistema describe Shopping & PMax Manager, pero no existe ninguna acción | Constrúyalo o utilice PMax Asset Group Manager (#28) del agente principal como punto de partida |
| **La versión de API no coincide en Informes** | 🟡 Medio | Los espectadores interactivos de palabras clave/anuncios utilizan la versión 18, otras acciones de informes utilizan la versión 19 | Verifique que el paquete pip `google-ads` maneje ambos; considere actualizar las acciones v18 |
| **Inconsistencia de nomenclatura entre el patrón A y B** | 🟡 Bajo | Mismas credenciales almacenadas con diferentes nombres de clave en todas las acciones | Simplemente ingrese los mismos valores; funciona bien, solo confunde durante la configuración |

---

## Solución de problemas

### "No se encontró ninguna cuenta que coincida..."

La función `resolve_customer_id()` busca cuentas en su MCC. Asegúrate de:
- Su `LOGIN_CUSTOMER_ID` es la cuenta de MCC (Administrador), no una cuenta infantil
- La cuenta que estás buscando está vinculada a tu MCC
- La cadena de búsqueda coincide con parte del nombre descriptivo de la cuenta.

### "paquete de anuncios de Google no encontrado"

El mensaje del sistema indica al agente que ejecute `pip install google-ads>=28.1.0` al comienzo de cada conversación. Si está fallando:
- Asegúrate de que `code_interpreter` esté habilitado
- Intente ejecutar la instalación manualmente en el primer mensaje.

### "Las credenciales de OAuth caducaron"

Los tokens de actualización generalmente no caducan, pero pueden revocarse si:
- Cambiaste la contraseña de tu cuenta de Google.
- Eliminaste el acceso a la aplicación en [Configuración de seguridad de Google](https://myaccount.google.com/permissions)
- El token no se ha utilizado en más de 6 meses.

**Solución:** Vuelva a ejecutar la generación del token de actualización desde el Paso 1A-3.

### "Token de desarrollador no aprobado"

Si su token de desarrollador está en modo "Cuenta de prueba":
- Solo funciona con [cuentas de prueba de Google Ads](https://developers.google.com/google-ads/api/docs/first-call/test-accounts)
- Solicite acceso básico en el [Centro API de Google Ads](https://ads.google.com/aw/apicenter)
- La aprobación suele tardar entre 1 y 3 días laborables.

### "Límite de tarifa excedido"

La API de Google Ads tiene estos límites:
- **Acceso Básico:** 15.000 operaciones/día, 4 solicitudes/segundo
- **Acceso estándar:** Operaciones ilimitadas, 100 solicitudes/segundo

Si se alcanzan los límites, la arquitectura Filter-First del sistema debería ayudar: utilice los parámetros `cost_min`, `status` y `limit` para reducir los conjuntos de resultados.

### El subagente no responde

- Verificar que el subagente esté vinculado en la lista de subagentes del agente principal
- Verifique que la acción Administrador de sesión y estado (#17) esté instalada
- Asegúrese de que el subagente tenga sus propias credenciales configuradas (no las comparte con el agente principal)

---

## Seguridad

Consulte [`SECURITY.md`](SECURITY.md) para:
- Proceso de informes de vulnerabilidad
- CORS, limitación de velocidad y prácticas de validación de entradas.
- Pautas de gestión de credenciales.
- Escribir protocolo de seguridad (CEP: Confirmar → Ejecutar → Post-verificación)Funciones de seguridad clave en v2.0:
- **Cors sin comodín**: el valor predeterminado del servidor es localhost; configurar a través de `ALLOWED_ORIGINS`
- **Limitación de velocidad**: 30 solicitudes/min por IP (configurable mediante `RATE_LIMIT_MAX`)
- **Saneamiento de errores**: errores genéricos del cliente, registro completo del lado del servidor
- **Prevención de inyección GAQL**: valores del período incluidos en la lista blanca
- **Sin secretos codificados**: todo a través de `.env`/variables de entorno

---

## Licencia

Licencia MIT. Consulte [`LICENCIA`](LICENCIA) para obtener el texto completo.

La API de Google Ads está sujeta a las [Condiciones de servicio] de Google (https://developers.google.com/google-ads/api/docs/terms). Los servicios de terceros (Cloudinary, SearchAPI, Stripe) están sujetos a sus respectivos términos.

---

## Contribuyendo

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) para obtener la guía completa. Áreas prioritarias:

1. **Acciones de subagente de optimización**: el mensaje del sistema existe, necesita acciones de API creadas
2. **Acciones del subagente de Shopping y PMax**: igual que arriba
3. **Cobertura de prueba**: pruebas unitarias para el paquete de implementación
4. **Memoria semántica** — puerto Vectoriza la memoria de Buddy a Python (pgvector/Pinecone)
5. **Transmisión de respuestas**: agregue un punto final SSE para la ejecución de herramientas en tiempo real```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## Proyectos relacionados

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — Habilidades de agente antrópico para Claude (análisis, auditoría, redacción, matemáticas, MCP)
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)**: servidor Python MCP con 29 herramientas para Claude Code, Claude Desktop, Cursor, OpenAI Agents SDK y cualquier cliente MCP
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)**: extensión CLI de Gemini con 22 herramientas, habilidades, comandos y temas de MCP
- **[googleadsagent.ai](https://googleadsagent.ai)** — Implementación de producción (Buddy) en Cloudflare con memoria semántica, facturación y monitoreo

---

> **En vivo en:** [googleadsagent.ai](https://googleadsagent.ai)  
> **Versión:** 2.0.0  
> **Licencia:** MIT  
> **Última actualización:** 2026-03-05