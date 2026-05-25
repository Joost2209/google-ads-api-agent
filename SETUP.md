# SETUP — Google Ads API Agent for vehgroshop.be

## State

- Repo: `https://github.com/Joost2209/google-ads-api-agent`
- Python 3.12 installed
- Dependencies installed (`pip install -r requirements.txt`)
- `.env` exists (from `.env.example`) — **placeholders, needs real values**

## Unlock (become build mode)

To switch from read-only to execute mode, use this prompt:
```
je mag nu van plan naar build om dingen uit te voeren
```

---

## Step 1: Fill credentials in `.env`

Edit `.env` in the repo root. Replace all `YOUR_*_HERE` placeholders:

| Variable | Required? | Source |
|---|---|---|
| `ANTHROPIC_API_KEY` | YES | https://console.anthropic.com → API Keys |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | YES | Google Ads UI → API Center |
| `GOOGLE_ADS_CLIENT_ID` | YES | Google Cloud Console → Credentials (OAuth2) |
| `GOOGLE_ADS_CLIENT_SECRET` | YES | Google Cloud Console → Credentials (OAuth2) |
| `GOOGLE_ADS_REFRESH_TOKEN` | YES | OAuth2 Playground with `https://www.googleapis.com/auth/adwords` scope |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | YES | Google Ads UI → MCC account ID (digits only, no dashes) |
| `CLOUDINARY_CLOUD_NAME` | Optional | https://cloudinary.com → Dashboard |
| `CLOUDINARY_API_KEY` | Optional | Cloudinary Dashboard |
| `CLOUDINARY_API_SECRET` | Optional | Cloudinary Dashboard |
| `SEARCHAPI_API_KEY` | Optional | https://searchapi.io → Dashboard |
| `GOOGLE_AI_API_KEY` | Optional | https://aistudio.google.com → Get API Key |

Credentials for the Google Ads project linked to `itvehgro@gmail.com` should be available in the Google Cloud Console under that account.

---

## Step 2: Validate

```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/validate.py
```

All 26 checks should pass green. If Anthropic API or Google Ads checks fail red, the keys in `.env` are invalid/placeholder.

---

## Step 3: Start the agent

### Interactive CLI (terminal chat)
```powershell
$env:PYTHONIOENCODING='utf-8'; python scripts/cli.py
```

### REST API server (for frontend/api usage)
```powershell
uvicorn deploy.server:app --host 0.0.0.0 --port 8000
```

---

## Step 4 (optional): GitHub collaborators

Add collaborator `itvehgro@gmail.com` to the GitHub repo:
```powershell
gh auth login
gh api repos/Joost2209/google-ads-api-agent/collaborators/itvehgro@gmail.com -f permission=push -X PUT
```

Or manually via: https://github.com/Joost2209/google-ads-api-agent/settings/access

---

## Architecture

- **28 tools** in `actions/main-agent/` (numbered 01-28.py)
- **6 sub-agents** in `actions/sub-agents/` with their own tools
- **Orchestrator** in `deploy/orchestrator.py` — Claude <-> tool loop
- **Server** in `deploy/server.py` — FastAPI REST API
- **Config** in `configs/agent_registry.json` — agent/tool metadata
- **Prompts** in `prompts/` — system prompts for main agent + sub-agents

## Language

The agent (Claude) works in Dutch. Communicate with it in Dutch, it responds in Dutch. Campaigns, ads, keywords — all can be in Dutch via the Google Ads API.

Some minor hardcoded English defaults exist (keyword planner language_id=1000, geo locale=en) — these can be changed to Dutch values later, but are not blockers.
