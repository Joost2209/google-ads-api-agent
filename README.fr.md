# Google Ads API Agent

[![Release](https://img.shields.io/github/v/release/itallstartedwithaidea/google-ads-api-agent)](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [한국어](README.ko.md)

Un système de gestion Google Ads de niveau entreprise, alimenté par l'IA, avec **28 outils personnalisés**, **6 sous-agents spécialisés** et un **accès en lecture/écriture en direct** aux comptes Google Ads via l'API Google Ads v22.

La version de production s'exécute sur **[googleadsagent.ai](https://googleadsagent.ai)** (Buddy) à la périphérie de Cloudflare — avec une mémoire sémantique, un stockage de clés cryptées, une surveillance automatisée et un système de facturation basé sur le crédit. Ce dépôt est l'agent Python open source qui alimente les mêmes fonctionnalités.

---

## Quoi de neuf dans la version 2.0

- **Renforcement de la sécurité** — Restrictions CORS, limitation du débit, désinfection des erreurs, prévention des injections GAQL
- **Pack installable** — `pip install google-ads-agent` (ou téléchargez-le depuis [Releases](https://github.com/itallstartedwithaidea/google-ads-api-agent/releases))
- **Licence MIT** — licence open source appropriée
- **Documents sur l'architecture de production** — référence complète de Cloudflare Buddy dans [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md)
- **Politique de sécurité** — [`SECURITY.md`](SECURITY.md) avec rapports de vulnérabilité et meilleures pratiques
- **Guide du contributeur** — [`CONTRIBUTING.md`](CONTRIBUTING.md) avec zones prioritaires et style de code
- **Modèle d'environnement** — [`.env.example`](.env.example) avec tous les espaces réservés pour les informations d'identification

Consultez le [CHANGELOG](CHANGELOG.md) complet pour plus de détails.

---


## Table des matières

- [Démarrage rapide](#demarrage-rapide)
- [Trois chemins de déploiement](#trois-chemins-de-deploiement)
  - [Ce que Buddy ajoute (Chemin C)](#ce-que-buddy-ajoute-chemin-c)
- [Chemin A : Déployer via l'API Anthropic](#chemin-a-deployer-via-lapi-anthropic)
  - [Comment ça marche](#comment-ca-marche)
  - [A-1 : Obtenez votre clé API Anthropic](#a-1-obtenez-votre-cle-api-anthropic)
  - [A-2 : Installer et exécuter (Python)](#a-2-installer-et-executer-python)
  - [A-3 : Utiliser dans votre propre code](#a-3-utiliser-dans-votre-propre-code)
  - [A-7 : les pièges connus](#a-7-les-pieges-connus)
  - [A-8 : Le package de déploiement – Référence du fichier](#a-8-le-package-de-deploiement-reference-du-fichier)
- [Chemin B : Déployer sur une plate-forme d'agent (interface utilisateur manuelle)](#chemin-b-deployer-sur-une-plate-forme-dagent-interface-utilisateur-manuelle)
- [Prérequis](#prerequis)
- [Étape 1 : Obtenir les informations d'identification de l'API](#etape-1-obtenir-les-informations-didentification-de-lapi)
  - [1A : identifiants de l'API Google Ads](#1a-identifiants-de-lapi-google-ads)
  - [1B : Identifiants Cloudinary](#1b-identifiants-cloudinary)
  - [1C : informations d'identification SearchAPI.io](#1c-informations-didentification-searchapiio)
  - [1D : informations d'identification Google IA/Gemini](#1d-informations-didentification-google-iagemini)
  - [Résumé : Tous les identifiants](#resume-tous-les-identifiants)
- [Étape 2 : Créer l'agent principal](#etape-2-creer-lagent-principal)
  - [2.1 — Créer le shell de l'agent](#21-creer-le-shell-de-lagent)
  - [2.3 — Activer les outils intégrés](#23-activer-les-outils-integres)
- [Étape 3 : Installer des actions personnalisées (28 au total)](#etape-3-installer-des-actions-personnalisees-28-au-total)
  - [Comprendre les modèles d'informations d'identification](#comprendre-les-modeles-dinformations-didentification)
  - [Installation action par action](#installation-action-par-action)
- [Étape 4 : Créer des sous-agents (6 au total)](#etape-4-creer-des-sous-agents-6-au-total)
  - [Sous-agent 1 : Reporting et analyse](#sous-agent-1-reporting-et-analyse)
  - [Sous-agent 2 : Recherche et renseignement](#sous-agent-2-recherche-et-renseignement)
  - [Sous-agent 3 : Optimisation](#sous-agent-3-optimisation)
  - [Sous-agent 4 : Shopping et PMax](#sous-agent-4-shopping-et-pmax)
  - [Sous-agent 5 : Créatif](#sous-agent-5-creatif)
  - [Sous-agent 6 : Baymax – Innovation créative](#sous-agent-6-baymax-innovation-creative)
- [Étape 5 : Lier les sous-agents à l'agent principal](#etape-5-lier-les-sous-agents-a-lagent-principal)
- [Étape 6 : Accorder l'accès aux utilisateurs](#etape-6-accorder-lacces-aux-utilisateurs)
- [Étape 7 : Validation et tests](#etape-7-validation-et-tests)
  - [Test 1 : Installation du package](#test-1-installation-du-package)
- [Référence des modèles d'informations d'identification](#reference-des-modeles-dinformations-didentification)
  - [Modèle A : annonces Google à 5 clés](#modele-a-annonces-google-a-5-cles)
  - [Modèle C : Cloudinaire à 3 clés](#modele-c-cloudinaire-a-3-cles)
- [Présentation de l'architecture](#presentation-de-larchitecture)
  - [Comment ce dépôt se compare aux autres agents IA](#comment-ce-depot-se-compare-aux-autres-agents-ia)
- [Problèmes connus](#problemes-connus)
- [Dépannage](#depannage)
  - ["Aucun compte correspondant trouvé..."](#aucun-compte-correspondant-trouve)
  - ["Package Google Ads introuvable"](#package-google-ads-introuvable)
  - ["Les identifiants OAuth ont expiré"](#les-identifiants-oauth-ont-expire)
  - ["Jeton de développeur non approuvé"](#jeton-de-developpeur-non-approuve)
  - ["Limite de débit dépassée"](#limite-de-debit-depassee)
  - [Le sous-agent ne répond pas](#le-sous-agent-ne-repond-pas)
- [Sécurité](#securite)
- [Licence](#licence)
- [Contribuer](#contribuer)
- [Projets connexes](#projets-connexes)

---
## Démarrage rapide

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

## Trois chemins de déploiement

| Chemin | Idéal pour | Ce dont vous avez besoin |
|------|----------|--------------------|
| **A : API anthropique (programmatique)** | Applications de production, SaaS, pipelines d'automatisation | Clé API anthropique + Python |
| **B : Plate-forme d'agent (interface utilisateur manuelle)** | Prototypage rapide, utilisateur unique, constructeur visuel | Compte de plateforme d'agent |
| **C : Cloudflare Production (copain)** | Full-stack avec mémoire, facturation, surveillance | Compte Cloudflare |

**Le chemin A** est ce que ce dépôt fournit immédiatement. Le chemin C est le système de production sur [googleadsagent.ai](https://googleadsagent.ai) — voir [`docs/BUDDY_ARCHITECTURE.md`](docs/BUDDY_ARCHITECTURE.md) pour l'architecture complète.

### Ce que Buddy ajoute (Chemin C)

| Capacité | Technologie |
|-----------|---------------|
| État persistant par utilisateur | Objets durables + SQLite |
| Mémoire sémantique | Vectoriser les intégrations |
| Stockage BYOK crypté | AES-256-GCM |
| WebSocket en temps réel | SDK des agents Cloudflare |
| Surveillance automatisée | Travailleurs Cron |
| Facturation basée sur le crédit | D1 + Rayure |
| IA multi-fournisseurs | Claude, GPT, routage Gémeaux |
| Exportations de fichiers | Stockage d'objets R2 |

---

## Chemin A : Déployer via l'API Anthropic

Il s'agit du **déploiement programmatique** : pas d'interface utilisateur manuelle, pas de clic. Tout passe par l'API Messages de Claude avec utilisation d'outils.

### Comment ça marche

Les fichiers d'action de ce dépôt ont été initialement créés pour une plate-forme d'agent. Le package `deploy/` les adapte pour qu'ils s'exécutent de manière autonome via l'API Anthropic. Voici ce qui se passe sous le capot lorsque vous exécutez « python scripts/cli.py » :

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

**Ce que la couche adaptateur (`tool_executor.py`) résout :**

| Problème | Que font les fichiers d'action | Que fait l'adaptateur |
|---------|--------------|----------------------|
| **Secrets** | Référencez `secrets["KEY"]` en tant que simple global injecté par la plateforme d'agent | Injecte le dict `secrets` dans le module `__dict__` avant `exec_module()` |
| **Installations Pip** | Exécutez `subprocess.check_call(["pip", "install", "google-ads"])` au moment de l'importation | Sous-processus Monkey-patches pour ignorer les commandes pip (deps déjà dans `requirements.txt`) |
| **Incompatibilité de paramètres** | 26/28 Les fonctions `run()` ont des paramètres explicites (pas de `**kwargs`) | Inspecte la signature `run()` via `inspect.signature()`, supprime tous les paramètres envoyés par Claude qui ne sont pas dans la fonction |

### A-1 : Obtenez votre clé API Anthropic

1. Accédez à **[Anthropic Console](https://console.anthropic.com)**
2. Inscrivez-vous ou connectez-vous
3. Accédez à **[Paramètres → Clés API](https://console.anthropic.com/settings/keys)**
4. Cliquez sur **Créer une clé**
5. Copiez la clé → ceci est votre `ANTHROPIC_API_KEY`

> 💡 La clé commence par `sk-ant-api03-...`. Stockez-le en toute sécurité : il accorde un accès complet à l'API.

**Comment cela est lié au système :** Chaque appel à l'API Messages de Claude nécessite cette clé dans l'en-tête `x-api-key`. Le SDK Python `anthropic` le lit automatiquement à partir de la variable d'environnement `ANTHROPIC_API_KEY`.

### A-2 : Installer et exécuter (Python)

**Que se passe-t-il, étape par étape, lorsque vous exécutez ceci :**

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

**Après l'étape 6, vous verrez :**

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
```C'est ça. L'agent est en cours d'exécution et effectue de véritables appels d'API Google Ads via vos informations d'identification, Claude orchestrant les outils à appeler et la manière d'interpréter les résultats.

### A-3 : Utiliser dans votre propre code

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
```### A-4 : Déployer en tant qu'API REST

Le serveur FastAPI inclus vous donne des points de terminaison HTTP pour toute interface ou intégration :

```bash
# Start the server
uvicorn deploy.server:app --host 0.0.0.0 --port 8000

# Or with Docker
docker compose up
```

**Points de terminaison :**

| Méthode | Chemin | Descriptif |
|--------|------|-------------|
| `POST` | `/chat` | Envoyer un message, obtenir une réponse (session de création automatique) |
| `POST` | `/sessions` | Créer une nouvelle session de conversation |
| `OBTENIR` | `/sessions/{id}` | Obtenez des informations sur la session et le nombre de messages |
| `SUPPRIMER` | `/sessions/{id}` | Supprimer une session |
| `OBTENIR` | `/santé` | Bilan de santé (statut des informations d'identification) |
| `OBTENIR` | `/outils` | Répertoriez les 28 outils et leur statut de fichier |

**Exemple de demande :**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "List all campaigns for Acme Corp", "session_id": "optional-session-id"}'
```

**Exemple de réponse :**

```json
{
  "response": "Here are the active campaigns for Acme Corp (ID: 123-456-7890):\n\n1. Brand Search — $1,234.56 spend, 89 conversions...",
  "session_id": "abc-123-def",
  "tool_calls_made": 2
}
```### A-5 : Déployer avec Docker```bash
# Build and run
docker compose up -d

# Scale to multiple instances
docker compose up -d --scale agent=3

# Run the CLI interactively
docker compose run cli

# Run validation
docker compose run validate
```### A-6 : Considérations relatives à la mise à l'échelle

| Préoccupation | État actuel | Mise à niveau de la production |
|---------|--------------|-------------------|
| **Séances** | Dict en mémoire | Passer à Redis — ajoutez le service `redis` dans docker-compose, remplacez le dict `sessions` par le client Redis |
| **Limites de taux** | Limites de l'API Anthropic par niveau | Ajouter une file d'attente de requêtes avec `celery` ou `asyncio.Semaphore` |
| **Multi-locataire** | Ensemble d'informations d'identification unique | Charger les informations d'identification par locataire à partir d'un gestionnaire de secrets (AWS Secrets Manager, HashiCorp Vault) |
| **Authentification** | Aucun | Ajouter un middleware de clé API ou OAuth2 au serveur FastAPI |
| **Surveillance** | Journalisation de base | Ajouter une journalisation structurée + exportation vers Datadog/CloudWatch |
| **Contrôle des coûts** | Aucun | Suivez l'utilisation des jetons via «response.usage» et définissez des alertes budgétaires |
| **Logique de nouvelle tentative** | SDK par défaut (2 tentatives) | Ajustez « max_retries » et ajoutez un intervalle exponentiel pour les appels d'API Google Ads |

### A-7 : les pièges connus

Choses qui pourraient vous faire trébucher dès la première course :

| Problème | Que se passe-t-il | Corriger |
|-------|-------------|-----|
| **L'importation de Google Ads échoue** | Les fichiers d'action nécessitent `google-ads>=28.1.0` qui a des dépendances C | Exécutez d'abord `pip install -r Requirements.txt` — c'est pourquoi l'adaptateur supprime les installations pip en ligne |
| **`secrets` KeyError** | Une action tente d'accéder à un identifiant que vous n'avez pas défini dans `.env` | Vérifiez quel modèle d'informations d'identification l'outil utilise (A/B/C/D) et vérifiez que `.env` possède ces clés |
| **TypeError à l'exécution()** | Claude envoie un paramètre que la fonction run() n'accepte pas | Le filtre de paramètres devrait détecter cela — si ce n'est pas le cas, cochez `python -c "from déployer import ToolExecutor; print(ToolExecutor().get_run_signature('tool_name'))"` |
| **Limites de taux** | Accès de base à l'API Google Ads = 15 000 opérations/jour, 4 requêtes/s | Utilisez les paramètres `cost_min`, `status`, `limit` pour réduire les jeux de résultats |
| **Le premier chargement est lent** | Le chargement du module + la suppression des pips ajoutent environ 1 à 2 secondes au premier appel d'outil | Les appels suivants utilisent des modules mis en cache — instantané |
| **Coûts des jetons** | claude-opus-4-5 avec 28 définitions d'outils = ~ 4 000 jetons par requête uniquement pour les outils | Pour optimiser les coûts, passez à `claude-sonnet-4-5-20250929` dans le constructeur |

### A-8 : Le package de déploiement – Référence du fichier

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

## Chemin B : Déployer sur une plate-forme d'agent (interface utilisateur manuelle)

Si vous préférez un générateur visuel (OpenAI ou similaire), suivez les étapes 2 à 7 ci-dessous. Vous collerez les invites système, le code d'action et les informations d'identification dans l'interface utilisateur de la plateforme.

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

## Prérequis

Avant de commencer, vous aurez besoin de :

| Exigence | Pourquoi | Coût |
|-------------|-----|------|
| **Clé API anthropique** | Alimente l'agent Claude via l'API Messages | Paiement à l'utilisation ([tarification](https://docs.anthropic.com/en/docs/about-claude/pricing)) |
| **Compte Google Ads** | Accès API pour gérer les campagnes | Gratuit (les annonces sont dépensées séparément) |
| **Compte Google Ads Manager (MCC)** | Accès multi-comptes | Gratuit |
| **Projet Google Cloud Platform** | Identifiants OAuth2 pour l'API Google Ads | Niveau gratuit disponible |
| **Compte cloudinaire** | Traitement d'images/vidéo pour les ressources créatives | Niveau gratuit (25 crédits/mois) |
| **Compte SearchAPI.io** | Recherche Google en temps réel, tendances, transparence des annonces | Niveau gratuit (100 recherches/mois) |
| **Compte Google AI Studio** | API Gemini pour la génération de créations IA | Niveau gratuit disponible |
| **Compte de plateforme d'agent** | Où vous déployez l'agent (par exemple, OpenAI ou similaire) | Varie |

---

## Étape 1 : Obtenir les informations d'identification de l'API

Vous avez besoin des informations d'identification de **4 services**. Cette section présente chacun d'eux avec les URL exactes, des conseils sur les captures d'écran et ce qu'il faut copier.

---

### 1A : identifiants de l'API Google Ads

C'est la configuration la plus complexe. Vous avez besoin de **5 valeurs** qui fonctionnent ensemble :

| Informations d'identification | Qu'est-ce que c'est | Où il vit |
|------------|-----------|----------------|
| `DEVELOPER_TOKEN` | Votre clé d'accès API de Google Ads | Interface utilisateur de Google Ads |
| `ID_CLIENT` | Identifiant de l'application OAuth2 | Google Cloud Console |
| `CLIENT_SECRET` | Secret de l'application OAuth2 | Google Cloud Console |
| `REFRESH_TOKEN` | Jeton OAuth2 de longue durée | Généré via le flux OAuth |
| `LOGIN_CUSTOMER_ID` | Votre identifiant de compte CM | Interface utilisateur de Google Ads |

#### Étape 1A-1 : Obtenez votre jeton de développeur

1. Accédez à **[Google Ads](https://ads.google.com)** et connectez-vous avec votre compte Manager (MCC).
2. Cliquez sur l'icône **Outils et paramètres** (clé) dans la navigation supérieure.
3. Sous **Configuration**, cliquez sur **Centre API**.
   - Si vous ne voyez pas API Center, vous devrez peut-être d'abord demander l'accès.
4. Votre **Jeton de développeur** est affiché sur cette page
5. **Niveau d'accès au jeton :**
   - `Test Account` — fonctionne uniquement avec les comptes de test (bon pour le développement)
   - « Accès de base » — jusqu'à 15 000 opérations/jour (en faire la demande)
   - « Accès standard » – illimité (à appliquer après avoir prouvé son utilisation)
6. **Copiez le jeton** → ceci est votre `GOOGLE_ADS_DEVELOPER_TOKEN`

> ⚠️ Si votre token affiche le statut « En attente », vous pouvez toujours l'utiliser avec des comptes de test. Pour la production, vous devez [demander un accès de base](https://developers.google.com/google-ads/api/docs/access-levels).

#### Étape 1A-2 : Créer des informations d'identification OAuth2 dans Google Cloud

1. Accédez à **[Google Cloud Console](https://console.cloud.google.com)**
2. Créez un nouveau projet (ou sélectionnez-en un existant) :
   - Cliquez sur le menu déroulant du projet en haut → **Nouveau projet**
   - Nom : `google-ads-agent` (ou celui que vous préférez)
   - Cliquez sur **Créer**
3. **Activez l'API Google Ads :**
   - Accédez à **[API et services → Bibliothèque](https://console.cloud.google.com/apis/library)**
   - Recherchez « API Google Ads »
   - Cliquez dessus → Cliquez sur **Activer**
4. **Configurez l'écran de consentement OAuth :**
   - Accédez à **[API et services → écran de consentement OAuth](https://console.cloud.google.com/apis/credentials/consent)**
   - Sélectionnez **Externe** (sauf si vous disposez de Google Workspace, puis Interne)
   - Remplissez :
     - Nom de l'application : "Agent Google Ads"
     - Email d'assistance utilisateur : votre email
     - Contact développeur : votre email
   - Cliquez sur **Enregistrer et continuer**
   - **Étendues :** cliquez sur **Ajouter ou supprimer des étendues** → recherchez "API Google Ads" → cochez "https://www.googleapis.com/auth/adwords` → **Mettre à jour** → **Enregistrer et continuer**
   - **Utilisateurs test :** Ajoutez l'adresse e-mail de votre compte Google Ads → **Enregistrez et continuez**
   - Cliquez sur **Retour au tableau de bord**
5. **Créez un identifiant client OAuth2 :**
   - Accédez à **[API et services → Identifiants](https://console.cloud.google.com/apis/credentials)**
   - Cliquez sur **+ Créer des informations d'identification** → **ID client OAuth**
   - Type d'application : **Application Web**
   - Nom : "Agent Google Ads"
   - URI de redirection autorisés : Ajouter `http://localhost:8080` (nécessaire pour l'étape de génération du token)
   - Cliquez sur **Créer**
   - **Copiez l'ID client** → il s'agit de votre `GOOGLE_ADS_CLIENT_ID`- **Copiez le secret client** → ceci est votre `GOOGLE_ADS_CLIENT_SECRET`

#### Étape 1A-3 : Générer un jeton d'actualisation

Le jeton d'actualisation permet à l'agent de s'authentifier sans interaction de l'utilisateur. Vous le générez une fois et il dure indéfiniment (sauf révocation).

**Option A : Utiliser OAuth2 Playground de Google (le plus simple)**

1. Accédez à **[OAuth 2.0 Playground](https://developers.google.com/oauthplayground/)**
2. Cliquez sur l'**icône d'engrenage** ⚙️ (en haut à droite)
   - Cochez **Utilisez vos propres informations d'identification OAuth**
   - Entrez votre « ID client » et votre « Secret client » de l'étape 1A-2
   - Fermez les paramètres
3. Dans le panneau de gauche, faites défiler jusqu'à **API Google Ads v18** → cochez « https://www.googleapis.com/auth/adwords ».
4. Cliquez sur **Autoriser les API**
5. Connectez-vous avec le compte Google qui a accès à vos comptes Google Ads
6. Accordez les autorisations demandées
7. Cliquez sur **Échanger le code d'autorisation contre les jetons**
8. **Copiez le jeton d'actualisation** → ceci est votre `GOOGLE_ADS_REFRESH_TOKEN`

**Option B : Utilisation de la bibliothèque Python google-ads**```bash
pip install google-ads

# Run the built-in auth helper
python -m google_ads.auth.generate_user_credentials \
  --client_id=YOUR_CLIENT_ID \
  --client_secret=YOUR_CLIENT_SECRET
```Cela ouvre un navigateur pour le consentement OAuth et imprime le jeton d'actualisation.

**Option C : Utiliser curl**```bash
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
```#### Étape 1A-4 : Obtenez votre identifiant client de connexion (MCC)

1. Accédez à **[Google Ads](https://ads.google.com)**
2. Connectez-vous à votre **Compte Manager** (MCC)
3. Votre **ID client** s'affiche en haut à droite, au format « XXX-XXX-XXXX »
4. **Copiez-le** → ceci est votre `GOOGLE_ADS_LOGIN_CUSTOMER_ID`

> 💡 L'ID client de connexion n'est nécessaire que si vous utilisez un MCC pour gérer plusieurs comptes. Si vous gérez directement un seul compte, vous pouvez laisser ce champ vide.

#### Étape 1A-5 : Vérifiez vos informations d'identification

Créez un fichier de test pour vérifier que tout fonctionne :

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
```Si cela imprime les noms des ressources du compte, vos informations d'identification Google Ads fonctionnent.

---

### 1B : Identifiants Cloudinary

Cloudinary gère tous les traitements d'image/vidéo : redimensionnement, remplissage génératif de l'IA, formatage spécifique à la plate-forme.

1. Accédez à **[Inscription Cloudinary](https://cloudinary.com/users/register_free)** et créez un compte gratuit
   - Le niveau gratuit comprend 25 crédits/mois (assez pour environ 1 000 transformations)
2. Après vous être inscrit, accédez à **[Dashboard](https://console.cloudinary.com/pm/getting-started/dashboard)**
3. Vos identifiants s'affichent directement sur le tableau de bord :
   - **Nom du cloud** → `CLOUDINARY_CLOUD_NAME`
   - **Clé API** → `CLOUDINARY_API_KEY`
   - **API Secret** → `CLOUDINARY_API_SECRET` (cliquez sur "Révéler" pour le voir)

> 💡 Le niveau gratuit est généreux pour le développement. Pour la production avec un traitement créatif important, le plan Plus (89 $/mois) offre 225 crédits.

#### Comment Cloudinary se connecte à l'agent

L'action **Cloudinary Creative Tools** (action n° 18 sur l'agent principal) et le sous-agent **Baymax — Creative Innovate** utilisent tous deux ces informations d'identification. Ils permettent :
- Téléchargement d'images/vidéos à partir d'URL
- Redimensionnement pour plus de 20 préréglages de plateformes (Instagram, TikTok, YouTube, annonces display, etc.)
- Remplissage génératif AI pour étendre les images à des formats d'image non standard
- Traitement par lots sur plusieurs plateformes

---

### 1C : informations d'identification SearchAPI.io

SearchAPI.io fournit des résultats de recherche Google en temps réel, des données Google Trends et un accès au centre de transparence Google Ads pour le sous-agent Research & Intelligence.

1. Accédez à **[Inscription SearchAPI.io](https://www.searchapi.io/signup)**
   - Niveau gratuit : 100 recherches/mois
2. Après votre inscription, accédez à **[Tableau de bord → Clé API](https://www.searchapi.io/dashboard)**
3. **Copiez votre clé API** → `SEARCHAPI_API_KEY`

#### Comment SearchAPI se connecte à l'agent

**Nemo — Research & Intelligence** utilise SearchAPI via trois actions personnalisées :
- **API de recherche Google** — résultats SERP en temps réel avec publicités, organiques et graphique de connaissances
- **Centre de transparence Google Ads** : découvrez les annonces diffusées par les concurrents.
- **Google Trends Analyser** — données de tendance, requêtes associées, intérêt géographique

Ces actions transmettent la clé API via `secrets["SEARCHAPI_API_KEY"]` dans le code source de chaque action.

---

### 1D : informations d'identification Google IA/Gemini

Le Baymax — Creative Innovate utilise l'API Gemini de Google pour la génération d'images et l'analyse de la vision basées sur l'IA.

1. Accédez à **[Google AI Studio](https://aistudio.google.com)**
2. Connectez-vous avec votre compte Google
3. Cliquez sur **Obtenir la clé API** dans la barre latérale gauche (ou accédez directement à **[Clés API](https://aistudio.google.com/apikey)**).
4. Cliquez sur **Créer une clé API**
   - Sélectionnez le projet Google Cloud que vous avez créé à l'étape 1A-2 (ou créez-en un nouveau).
5. **Copiez la clé API** → `GOOGLE_AI_API_KEY`

> 💡 Le niveau gratuit offre 15 RPM (requêtes par minute) pour Gemini 2.0 Flash. Pour la production, le tarif par répartition est très abordable.

#### Comment Gemini se connecte à l'agent

Le sous-agent **Baymax — Creative Innovate** utilise Gemini pour :
- Génération/extension d'images IA pour les formats de médias sociaux
- Analyse de la vision des actifs créatifs existants
- Génération de variantes d'annonces graphiques à partir des images sources

Le fichier d'action Gemini se trouve dans `actions/sub-agents/creative-innovate/02_gemini_vision.py`.

---

### Résumé : Tous les identifiants

Après avoir terminé les étapes 1A à 1D, votre fichier « .env » devrait ressembler à :

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

## Étape 2 : Créer l'agent principal

> Ces instructions utilisent une terminologie générique. Adaptez les noms/menus des boutons pour votre plate-forme d'agent spécifique (par exemple, OpenAI ou similaire).

### 2.1 — Créer le shell de l'agent

1. Sur votre plateforme d'agent, créez un nouvel agent avec ces paramètres :

| Paramètre | Valeur |
|---------|-------|
| Nom | `Agent API Google Ads` |
| Modèle | `claude-opus-4-5` (Anthropique) |
| Accès | Privé |

2. **Définissez la description :**

```
Google Ads strategist with LIVE API access and CONTEXT. Now with FULL CAMPAIGN
support: Create campaigns, ad groups, keywords, manage bidding strategies, PMax,
ad schedules, and location targeting. Features automatic data offloading, memory
checkpoints, and creative assets via Cloudinary.
```### 2.2 — Collez l'invite système

1. Ouvrez le fichier : `prompts/main_agent_system_prompt.md`
2. Copiez le **contenu entier**
3. Collez dans le champ d'invite/instructions système de votre agent
4. Enregistrer

### 2.3 — Activer les outils intégrés

Activez ces 10 outils intégrés (les noms peuvent varier selon la plate-forme) :

- [x] Interpréteur de code
- [x] Recherche sur le Web (Google)
- [x] Chercheur
- [x] Todo / Liste des tâches
- [x] Grattoir Web
- [x] Exécuteur de requêtes (SQL)
- [x] Lecteur CSV
- [x] Matcheur de chaînes
- [x] Afficher le fichier
- [x] Recherche de fichiers

---

## Étape 3 : Installer des actions personnalisées (28 au total)

Chaque action personnalisée est un fichier Python qui est collé dans le générateur d'actions personnalisées de votre plateforme d'agent. Vous devrez :

1. Créez l'action
2. Collez le code source
3. Configurez les informations d'identification (secrets)

### Comprendre les modèles d'informations d'identification

Il existe 4 modèles de titres de compétences. Sachez lequel chaque action utilise avant de commencer :

| Modèle | Nombre de secrets | Actions qui l'utilisent |
|---------|-------------|-----------------|
| **A** (annonces Google à 5 clés) | 5 | 12 actions — inclut `LOGIN_CUSTOMER_ID` comme secret |
| **B** (Google Ads à 4 clés) | 4 | 13 actions — transmet `login_customer_id` comme paramètre de fonction |
| **C** (Cloudinaire à 3 touches) | 3 | 1 action — Outils créatifs Cloudinary |
| **D** (Aucune information d'identification) | 0 | 3 actions — Installateur de package, gestionnaire de session, document de reconstruction |

Voir [Référence des modèles d'informations d'identification](#credential-patterns-reference) pour plus de détails.

### Installation action par action

Pour **chaque action** ci-dessous, suivez ce processus :

```
1. Create New Custom Action on your platform
2. Set the Name (from table below)
3. Set the Integration type (google_ads, default, or none)
4. Paste the source code from the file path listed
5. Add credential secrets matching the pattern letter
6. Save and verify
```#### Actions du modèle A (Google Ads à 5 clés) – 12 actions

Pour chacun, ajoutez ces 5 secrets :

| Clé secrète | Valeur de .env |
|------------|----------------|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | Votre jeton de développeur |
| `GOOGLE_ADS_CLIENT_ID` | Votre identifiant client OAuth2 |
| `GOOGLE_ADS_CLIENT_SECRET` | Votre secret client OAuth2 |
| `GOOGLE_ADS_REFRESH_TOKEN` | Votre jeton de rafraîchissement |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | Votre numéro client MCC |

| # | Nom de l'action | Fichier source |
|---|-------------|------------|
| 1 | Gestionnaire d'étiquettes | `actions/main-agent/01_label_manager.py` |
| 2 | Gestionnaire de suivi des conversions | `actions/main-agent/02_conversion_tracking_manager.py` |
| 12 | Gestionnaire de scripts | `actions/main-agent/12_scripts_manager.py` |
| 13 | Responsable des expériences | `actions/main-agent/13_experiments_manager.py` |
| 19 | Planificateur de requêtes et gestionnaire de budget | `actions/main-agent/19_query_planner.py` |
| 20 | Gestionnaire de recommandations | `actions/main-agent/20_recommendations_manager.py` |
| 23 | Gestionnaire des performances des appareils | `actions/main-agent/23_device_performance_manager.py` |
| 24 | Gestionnaire de l'historique des modifications | `actions/main-agent/24_change_history_manager.py` |
| 25 | Créateur de campagne | `actions/main-agent/25_campaign_creator.py` |
| 26 | Gestionnaire de calendrier de publicité | `actions/main-agent/26_ad_schedule_manager.py` |
| 27 | Responsable de la stratégie d'enchères | `actions/main-agent/27_bidding_strategy_manager.py` |
| 28 | Gestionnaire de groupe d'actifs PMax | `actions/main-agent/28_pmax_asset_group_manager.py` |

#### Actions du modèle B (Google Ads à 4 clés) – 13 actions

Pour chacun, ajoutez ces 4 secrets :

| Clé secrète | Valeur de .env |
|------------|----------------|
| `DEVELOPER_TOKEN` | Votre jeton de développeur |
| `ID_CLIENT` | Votre identifiant client OAuth2 |
| `CLIENT_SECRET` | Votre secret client OAuth2 |
| `REFRESH_TOKEN` | Votre jeton de rafraîchissement |

> ⚠️ Remarque : les **noms de clés** sont différents du modèle A (pas de préfixe `GOOGLE_ADS_`). C'est intentionnel — ces actions acceptent à la place `login_customer_id` comme paramètre de fonction.

| # | Nom de l'action | Fichier source |
|---|-------------|------------|
| 3 | Gestionnaire d'audience | `actions/main-agent/03_audience_manager.py` |
| 4 | Gestionnaire d'actifs | `actions/main-agent/04_asset_manager.py` |
| 5 | Gestionnaire budgétaire | `actions/main-agent/05_budget_manager.py` |
| 6 | Gestionnaire de publicités RSA | `actions/main-agent/06_rsa_ad_manager.py` |
| 7 | Gestionnaire d'enchères et de mots clés | `actions/main-agent/07_bid_keyword_manager.py` |
| 8 | Gestionnaire de mots clés négatifs | `actions/main-agent/08_negative_keywords_manager.py` |
| 9 | Gestionnaire de campagnes et de groupes d'annonces | `actions/main-agent/09_campaign_adgroup_manager.py` |
| 10 | Mutation de Google Ads | `actions/main-agent/10_google_ads_mutate.py` |
| 11 | Vérificateur d'accès au compte | `actions/main-agent/11_account_access_checker.py` |
| 15 | Vérifier les niveaux d'accès des utilisateurs | `actions/main-agent/15_check_user_access.py` |
| 16 | API Gateway - Gestionnaire de contexte | `actions/main-agent/16_api_gateway.py` |
| 21 | Gestionnaire de termes de recherche | `actions/main-agent/21_search_term_manager.py` |
| 22 | Gestionnaire de ciblage géographique et géographique | `actions/main-agent/22_geo_location_manager.py` |

#### Action du modèle C (Cloudinary à 3 touches) — 1 action

| Clé secrète | Valeur de .env |
|------------|----------------|
| `CLOUDINARY_CLOUD_NAME` | Votre nom de cloud Cloudinary |
| `CLOUDINARY_API_KEY` | Votre clé API Cloudinary |
| `CLOUDINARY_API_SECRET` | Votre secret API Cloudinary |

| # | Nom de l'action | Fichier source |
|---|-------------|------------|
| 18 | Outils créatifs cloudinaires | `actions/main-agent/18_cloudinary_creative_tools.py` |

#### Actions du modèle D (sans informations d'identification) — 3 actions

Collez simplement le code – aucun secret n’est nécessaire.

| # | Nom de l'action | Fichier source |
|---|-------------|------------|
| 14 | Programme d'installation du package | `actions/main-agent/14_package_installer.py` |
| 17 | Gestionnaire de session et d'état | `actions/main-agent/17_session_state_manager.py` |

> 📌 **Conseil :** Si votre plate-forme prend en charge l'importation d'actions en masse, utilisez `configs/agent_registry.json` comme source de vérité pour les identifiants, les noms et les modèles d'informations d'identification.

---

## Étape 4 : Créer des sous-agents (6 au total)

Chaque sous-agent est un agent distinct auquel l'agent principal délègue des tâches. Ils ont chacun leur propre invite système, leurs outils et leurs actions personnalisées.

### Sous-agent 1 : Reporting et analyse

| Paramètre | Valeur |
|---------|-------|
| Nom | `Simba — Rapports et analyses` |
| Modèle | `claude-opus-4-5` |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/01_reporting_analysis.md` |

**Actions personnalisées (8) :** Installation à partir de `actions/sous-agents/reporting/`

| # | Actions | Fichier source | Informations d'identification |
|---|--------|-----------|-------------|
| 1 | Journaliste des performances | `01_performance_reporter.py` | Annonces Google à 4 clés (modèle B) |
| 2 | Analyseur de termes de recherche | `02_search_terms_analyzer.py` | Annonces Google à 4 clés (modèle B) |
| 3 | Visionneuse interactive de mots clés | `03_interactive_keyword_viewer.py` | Annonces Google à 4 clés (modèle B) |
| 4 | Visionneuse de publicités interactive | `04_interactive_ad_viewer.py` | Annonces Google à 4 clés (modèle B) |
| 5 | Journaliste sur les informations sur les enchères | `05_auction_insights_reporter.py` | Annonces Google à 4 clés (modèle B) |
| 6 | Auditeur de l'historique des modifications | `06_change_history_auditor.py` | Annonces Google à 4 clés (modèle B) |
| 7 | Rapports améliorés PMax | `07_pmax_enhanced_reporting.py` | Annonces Google à 4 clés (modèle B) |
| 8 | Programme d'installation du package | `08_package_installer.py` | Aucun (modèle D) |

**Outils intégrés (9) :** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, chercheur, google_web_search

> ⚠️ Les actions 3 et 4 (observateurs de mots clés/annonces interactifs) utilisent l'API Google Ads **v18** tandis que les autres utilisent **v19**. Vérifiez que le package pip « google-ads » prend en charge les deux.

---

### Sous-agent 2 : Recherche et renseignement

| Paramètre | Valeur |
|---------|-------|
| Nom | `Nemo — Recherche et renseignement` |
| Modèle | `claude-opus-4-5` |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/02_research_intelligence.md` |

**Actions personnalisées (4+1) :** Installation à partir de `actions/sous-agents/research/`

| # | Actions | Fichier source | Informations d'identification |
|---|--------|-----------|-------------|
| 1 | Planificateur de mots clés | `01_keyword_planner.py` | Annonces Google à 4 clés (modèle B) |
| 2 | API de recherche Google | `02_google_search_api.py` | 1 secret : `SEARCHAPI_API_KEY` |
| 3 | Centre de transparence des annonces | `03_ads_transparency_center.py` | 1 secret : `SEARCHAPI_API_KEY` |
| 4 | Analyseur de tendances Google | `04_google_trends_analyzer.py` | 1 secret : `SEARCHAPI_API_KEY` |
| 5 | Programme d'installation du package | *(réutilisation depuis l'agent principal)* | Aucun (modèle D) |

**Outils intégrés (10) :** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, chercheur, google_web_search, web_scraper

---

### Sous-agent 3 : Optimisation

| Paramètre | Valeur |
|---------|-------|
| Nom | `Elsa — Optimisation` |
| Modèle | `claude-opus-4-5` |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/03_optimization.md` |

**Actions personnalisées :** ⚠️ **AUCUNE N'EXISTE ENCORE**

L'invite système de ce sous-agent fait référence à deux actions personnalisées qui doivent être créées :
- **Recommendations Manager - API** — `list`, `apply`, `dismiss`, `get_score`
- **Bulk Operations Manager - API** — `bulk_pause`, `bulk_enable`, `bulk_bid_change`, `bulk_budget_change`, `export`

> 🔧 **À FAIRE :** Créez ces actions à l'aide de l'API Google Ads. Les signatures des paramètres sont documentées dans le fichier d'invite système. Les deux utiliseraient les informations d’identification du modèle B (Google Ads à 4 clés).

**Outils intégrés (10) :** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, chercheur, google_web_search, web_scraper

---

### Sous-agent 4 : Shopping et PMax

| Paramètre | Valeur |
|---------|-------|
| Nom | `Aladdin — Shopping et PMax` |
| Modèle | `claude-opus-4-5` |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/04_shopping_pmax.md` |

**Actions personnalisées :** ⚠️ **AUCUNE N'EXISTE ENCORE**

L'invite système de ce sous-agent fait référence à une action personnalisée qui doit être créée :
- **Shopping & PMax Manager - API** — `list_shopping`, `list_pmax`, `list_asset_groups`, `get_product_performance`, `get_pmax_performance`, `get_pmax_insights`, `pause_asset_group`, `enable_asset_group`

> 🔧 **À FAIRE :** Créez cette action à l'aide de l'API Google Ads (SDK Python `google-ads`). Utiliserait les informations d’identification du modèle B. Le gestionnaire de groupe d'actifs PMax de l'agent principal (action n° 28) couvre certaines de ces fonctionnalités et peut servir de modèle de départ.**Outils intégrés (10) :** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, chercheur, google_web_search, web_scraper

---

### Sous-agent 5 : Créatif

| Paramètre | Valeur |
|---------|-------|
| Nom | `Moana — Créatif` |
| Modèle | `claude-opus-4-5` |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/05_creative.md` |

**Actions personnalisées (2) :** Installation à partir de `actions/sub-agents/creative/`

| # | Actions | Fichier source | Informations d'identification |
|---|--------|-----------|-------------|
| 1 | Gestionnaire d'annonces display responsives | `01_responsive_display_ads_manager.py` | Annonces Google à 4 clés (modèle B) |
| 2 | Gestionnaire d'annonces de génération de demande | `02_demand_gen_ads_manager.py` | Annonces Google à 4 clés (modèle B) |

**Outils intégrés (10) :** code_interpreter, query_executor, csv_reader, string_matcher, display_file, file_search, browser_use, google_web_search, chercheur, web_scraper

---

### Sous-agent 6 : Baymax – Innovation créative

| Paramètre | Valeur |
|---------|-------|
| Nom | `Baymax — Innovation créative` |
| Modèle | `claude-sonnet-4-5` ⚡ *(modèle plus léger — intentionnel)* |
| Accès | CHAT_ONLY |
| Invite système | `invites/sous-agents/06_creative_innovate.md` |

**Actions personnalisées (2+1) :** Installation à partir de `actions/sous-agents/creative-innovate/`

| # | Actions | Fichier source | Informations d'identification |
|---|--------|-----------|-------------|
| 1 | Outils cloudinaires | `01_cloudinary_tools.py` | Cloudinary à 3 touches (modèle C) |
| 2 | Vision Gémeaux | `02_gemini_vision.py` | 1 secret : `GOOGLE_AI_API_KEY` |
| 3 | Programme d'installation du package | *(réutilisation depuis l'agent principal)* | Aucun (modèle D) |

---

## Étape 5 : Lier les sous-agents à l'agent principal

Après avoir créé les 6 sous-agents, vous devez les enregistrer auprès de l'agent principal afin qu'il puisse déléguer des tâches.

1. Accédez aux paramètres **Agent principal**
2. Recherchez la section **Sous-agents**
3. Ajoutez chaque sous-agent en recherchant son nom ou son ID :

| # | Nom du sous-agent | ID d'agent |
|---|----------------|----------|
| 1 | Simba — Rapports et analyses | `8b9991fd-7750-417e-a2c2-69527d64388b` |
| 2 | Nemo — Recherche et renseignement | `47885bdc-0390-44a4-ab58-9046c1182691` |
| 3 | Elsa — Optimisation | `c08c6cde-b9a6-4aa4-b7a2-3b6ed5720cbb` |
| 4 | Aladdin — Shopping et PMax | `b57147ce-fa6e-47ec-b92b-39bc8d16d7a7` |
| 5 | Moana — Créatif | `9aeb9afc-bd87-4df7-955a-1b928b23aa0e` |
| 6 | Baymax — Innovation créative | `9b971c1c-0204-4496-869e-7a3620718242` |

> 💡 Remarque : les ID d'agent seront **différents** si vous créez de nouveaux agents (ils sont générés automatiquement). Les identifiants ci-dessus proviennent de la version originale et sont fournis à titre de référence.

L'invite système de l'agent principal inclut le **Protocole de délégation de sous-agent** qui lui indique quand gérer les tâches directement ou par délégation. Le **Session & State Manager** (Action n° 17) coordonne les transferts.

---

## Étape 6 : Accorder l'accès aux utilisateurs

Si vous devez partager l'agent avec les membres de l'équipe :

1. Accédez aux paramètres de l'agent principal → **Partage/Accès**
2. Ajoutez des utilisateurs avec l'autorisation **CAN_EDIT**
3. Ils pourront utiliser et modifier l'agent

---

## Étape 7 : Validation et tests

Exécutez ces tests afin de vérifier que le système complet fonctionne :

### Test 1 : Installation du package

```
You: "Install the google-ads package"
Expected: Agent runs code_interpreter to pip install google-ads>=28.1.0
```### Test 2 : Connexion au compte```
You: "Test my Google Ads connection"
Expected: Agent uses Account Access Checker → test_connection
         Shows list of accessible accounts
```### Test 3 : Récapitulatif du compte```
You: "Show me an account summary for [YOUR ACCOUNT NAME]"
Expected: Agent uses Query Planner → get_account_summary
         Shows total spend, conversions, entity counts
```### Test 4 : Opération de lecture```
You: "List the top 5 campaigns by spend for [YOUR ACCOUNT NAME]"
Expected: Agent uses Campaign Manager → list_campaigns with cost filter
         Shows campaigns in a table with dollar amounts
```### Test 5 : Opération d'écriture (sûr)```
You: "Create a test label called 'Agent Test' with color blue"
Expected: Agent uses Label Manager → create_label
         Shows preview, asks for CONFIRM before creating
```### Test 6 : Délégation de sous-agents```
You: "Give me a full performance report for all campaigns in [ACCOUNT] for the last 30 days"
Expected: Agent delegates to Reporting sub-agent
         Returns summarized findings, not a data dump
```### Test 7 : Cloudinaire```
You: "Upload this image and resize it for Instagram: [IMAGE_URL]"
Expected: Agent uses Cloudinary Creative Tools or delegates to Baymax — Creative Innovate
         Returns resized image URLs
```---

## Référence des modèles d'informations d'identification

### Modèle A : annonces Google à 5 clés

Utilisé par **12 actions** où l'ID client de connexion MCC est stocké en tant que secret.```
GOOGLE_ADS_DEVELOPER_TOKEN  → Developer token from Google Ads API Center
GOOGLE_ADS_CLIENT_ID        → OAuth2 client ID from Google Cloud Console
GOOGLE_ADS_CLIENT_SECRET    → OAuth2 client secret from Google Cloud Console
GOOGLE_ADS_REFRESH_TOKEN    → OAuth2 refresh token (generated once)
GOOGLE_ADS_LOGIN_CUSTOMER_ID → MCC account ID (XXX-XXX-XXXX format)
```### Modèle B : annonces Google à 4 clés

Utilisé par **13 actions** où l'ID client de connexion est transmis en tant que paramètre de fonction.```
DEVELOPER_TOKEN  → Same developer token, different key name
CLIENT_ID        → Same OAuth2 client ID, different key name
CLIENT_SECRET    → Same OAuth2 client secret, different key name
REFRESH_TOKEN    → Same refresh token, different key name
```> ⚠️ Les **valeurs** sont identiques au modèle A. Seuls les **noms de clés** diffèrent. Cela est dû au fait que certaines actions ont été écrites avec des conventions de dénomination différentes. Les informations d'identification sous-jacentes sont les mêmes.

### Modèle C : Cloudinaire à 3 clés

```
CLOUDINARY_CLOUD_NAME  → From Cloudinary Dashboard
CLOUDINARY_API_KEY     → From Cloudinary Dashboard
CLOUDINARY_API_SECRET  → From Cloudinary Dashboard (click Reveal)
```### Modèle D : Aucune information d'identification

Actions qui n'appellent pas d'API externes : Package Installer, Session & State Manager.

---

## Présentation de l'architecture

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
```Pour l'architecture technique complète avec les schémas d'action, les signatures de paramètres et le flux de délégation, voir **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**.

Pour l'architecture de production Cloudflare Buddy (Durable Objects, Vectorize, D1, R2, Agents SDK), voir **[docs/BUDDY_ARCHITECTURE.md](docs/BUDDY_ARCHITECTURE.md)**.

### Comment ce dépôt se compare aux autres agents IA

| Fonctionnalité | Cet agent | Scripts Google Ads | Copilote Microsoft | Perplexité | Générique Claude |
|---------|-----------|---------|-------------------|------------|---------------|
| API Google Ads en direct R/W | 28 actions | Scripts JS uniquement | Aucun accès aux annonces | Aucune API | Aucune API |
| Sécurité d'écriture (CEP) | Confirmer/Exécuter/Publier | Aucun | N/A | N/A | N/A |
| IA multi-fournisseurs | Claude + GPT + Gémeaux | N/A | GPT uniquement | Propres modèles | Claude seulement |
| Délégation de sous-agent | 6 spécialistes | N/A | N/A | N/A | N/A |
| Mémoire sémantique | Vectoriser (prod) | Aucun | Limité | Intégré | Conversation uniquement |
| Auto-déployable | 3 chemins | Éditeur de scripts | SaaS uniquement | SaaS uniquement | API uniquement |

---

## Problèmes connus

| Problème | Gravité | Détails | Solution de contournement |
|-------|----------|---------|------------|
| **Le sous-agent d'optimisation n'a aucune action** | 🔴 Critique | L'invite système décrit Recommendations Manager et Bulk Operations Manager, mais aucune des deux actions n'existe | Créez-les à l'aide de l'API Google Ads ou utilisez directement le gestionnaire de recommandations de l'agent principal (#20) |
| **Le sous-agent Shopping & PMax n'a aucune action** | 🔴 Critique | L'invite système décrit Shopping & PMax Manager, mais aucune action n'existe | Construisez-le ou utilisez le gestionnaire de groupe d'actifs PMax de l'agent principal (#28) comme point de départ |
| **Incompatibilité de version d'API dans Reporting** | 🟡 Moyen | Les visualiseurs de mots clés/annonces interactifs utilisent la version 18, les autres actions de création de rapports utilisent la version 19 | Vérifiez que le package pip « google-ads » gère les deux ; envisagez de mettre à niveau les actions v18 |
| **Incohérence de dénomination des modèles A et B** | 🟡 Faible | Mêmes informations d'identification stockées sous différents noms de clé pour toutes les actions | Entrez simplement les mêmes valeurs - fonctionne bien, mais prête à confusion lors de l'installation |

---

## Dépannage

### "Aucun compte correspondant trouvé..."

La fonction `resolve_customer_id()` recherche les comptes sous votre MCC. Assurez-vous :
- Votre `LOGIN_CUSTOMER_ID` est le compte MCC (Manager), pas un compte enfant
- Le compte que vous recherchez est associé à votre Centre multicompte.
- La chaîne de recherche correspond à une partie du nom descriptif du compte

### "Package Google Ads introuvable"

L'invite système demande à l'agent d'exécuter « pip install google-ads>=28.1.0 » au début de chaque conversation. En cas d'échec :
- Assurez-vous que `code_interpreter` est activé
- Essayez d'exécuter l'installation manuellement dans le premier message

### "Les identifiants OAuth ont expiré"

Les jetons d'actualisation n'expirent généralement pas, mais ils peuvent être révoqués si :
- Vous avez modifié le mot de passe de votre compte Google
- Vous avez supprimé l'accès à l'application dans [Paramètres de sécurité Google](https://myaccount.google.com/permissions)
- Le token n'a pas été utilisé depuis plus de 6 mois

**Correction :** Réexécutez la génération du jeton d'actualisation à partir de l'étape 1A-3.

### "Jeton de développeur non approuvé"

Si votre token de développeur est en mode « Compte test » :
- Cela ne fonctionne qu'avec les [comptes de test Google Ads](https://developers.google.com/google-ads/api/docs/first-call/test-accounts)
- Demandez un accès de base au [Centre API Google Ads](https://ads.google.com/aw/apicenter)
- L'approbation prend généralement 1 à 3 jours ouvrables

### "Limite de débit dépassée"

L'API Google Ads présente les limites suivantes :
- **Accès de base :** 15 000 opérations/jour, 4 requêtes/seconde
- **Accès standard :** Opérations illimitées, 100 requêtes/seconde

Si vous atteignez les limites, l'architecture Filter-First du système devrait vous aider : utilisez les paramètres `cost_min`, `status` et `limit` pour réduire les ensembles de résultats.

### Le sous-agent ne répond pas

- Vérifiez que le sous-agent est lié dans la liste des sous-agents de l'agent principal
- Vérifiez que l'action Session & State Manager (#17) est installée
- Assurez-vous que le sous-agent dispose de ses propres informations d'identification configurées (elles ne sont pas partagées avec l'agent principal).

---

## Sécurité

Voir [`SECURITY.md`](SECURITY.md) pour :
- Processus de reporting des vulnérabilités
- Pratiques CORS, limitation de débit et validation des entrées
- Directives de gestion des informations d'identification
- Rédiger le protocole de sécurité (CEP : Confirmer → Exécuter → Post-vérification)Principales fonctionnalités de sécurité de la version 2.0 :
- **Pas de CORS générique** — le serveur est par défaut localhost ; configurer via `ALLOWED_ORIGINS`
- **Limitation de débit** — 30 req/min par IP (configurable via `RATE_LIMIT_MAX`)
- **Désinfection des erreurs** — erreurs client génériques, journalisation complète côté serveur
- **Prévention des injections GAQL** — valeurs de période sur liste blanche
- **Aucun secret codé en dur** — tout via `.env`/variables d'environnement

---

## Licence

Licence MIT. Voir [`LICENSE`](LICENSE) pour le texte intégral.

L'API Google Ads est soumise aux [Conditions d'utilisation] de Google(https://developers.google.com/google-ads/api/docs/terms). Les services tiers (Cloudinary, SearchAPI, Stripe) sont soumis à leurs conditions respectives.

---

## Contribuer

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) pour le guide complet. Domaines prioritaires :

1. **Actions de sous-agent d'optimisation** : une invite système existe, nécessite la création d'actions API
2. **Actions des sous-agents Shopping et PMax** — comme ci-dessus
3. **Couverture des tests** — tests unitaires pour le package de déploiement
4. **Mémoire sémantique** — port Vectoriser la mémoire de Buddy vers Python (pgvector/Pinecone)
5. **Réponses en streaming** — ajoutez un point de terminaison SSE pour l'exécution d'outils en temps réel```bash
# Quick contributor setup
git clone https://github.com/itallstartedwithaidea/google-ads-api-agent.git
cd google-ads-api-agent
python -m venv venv && source venv/bin/activate
pip install -e ".[all]"
cp .env.example .env
python scripts/validate.py
```---

## Projets connexes

- **[google-ads-skills](https://github.com/itallstartedwithaidea/google-ads-skills)** — Compétences d'agent anthropique pour Claude (analyse, audit, rédaction, mathématiques, MCP)
- **[google-ads-mcp](https://github.com/itallstartedwithaidea/google-ads-mcp)** — Serveur Python MCP avec 29 outils pour Claude Code, Claude Desktop, Cursor, OpenAI Agents SDK et tout client MCP
- **[google-ads-gemini-extension](https://github.com/itallstartedwithaidea/google-ads-gemini-extension)** — Extension Gemini CLI avec 22 outils, compétences, commandes et thèmes MCP
- **[googleadsagent.ai](https://googleadsagent.ai)** — Déploiement en production (Buddy) sur Cloudflare avec mémoire sémantique, facturation et surveillance

---

> **En direct sur :** [googleadsagent.ai](https://googleadsagent.ai)  
> **Version :** 2.0.0  
> **Licence :** MIT  
> **Dernière mise à jour :** 2026-03-05