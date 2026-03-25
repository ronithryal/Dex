## Full Roadmap: Dex Setup → Portfolio → Stripe Demo

### Phase 0: Foundation (Day 1)

1. **Fork `davekilleen/dex`** to your GitHub right now — everything you build goes on YOUR fork from day one. Name it something that signals the portfolio angle (e.g., `yourusername/dex` or `yourusername/os` for "personal operating system")
2. Clone your fork locally, open it in Antigravity, run `/setup`
3. Commit structure for portfolio visibility:
   - Your skills → `.claude/skills/your-skill-name/`
   - Your MCPs → standalone repos (`mcp-youtube`, `mcp-dune`, etc.) submoduled in or linked
   - Web UI → separate repo (`dex-web`)

***

### Phase 1: Core Intel Layer (Week 1)

This is the layer Dave built that's **not** in the public repo — you're replicating and improving it.

**1a. Newsletters (easiest, highest ROI — do this first)**
- Run `/google-workspace-setup` — this IS in the public repo, connects Gmail
- Dex's `daily-plan` Step 5.8 already queries Gmail for newsletters and extracts market signals with a "why this matters / contrarian angle" framing
- You get 120 newsletter digests feeding into your briefing immediately, no custom code

**1b. YouTube Intel (first custom MCP to build)**
- Dave's approach: point Antigravity at YouTube Data API docs, say "build me an MCP server that fetches the transacripts of new videos from my subscribed channels, summarizes them, and flags what's new, novel, and contrarian"
- Name it `user-youtube` in your `.mcp.json` so Dex updates never overwrite it
- Output goes to `06-Resources/Intel/YouTube_YYYY-MM-DD.md`
- `daily-plan` Step 5 checks if today's intel file exists — if not, triggers the MCP to generate it
- Publish the MCP as a standalone repo: `yourusername/mcp-youtube` — this becomes a starrable, shareable GitHub artifact

**1c. LinkedIn Saved Posts Parser [COMPLETE]**
- **Daily JSON Ingest:** Established the **Drop Zone** (`00-Inbox/Drop_Zone/`) as the landing pad for LinkedIn JSON exports.
- **Skill 001:** Created `System/ingest/parse_linkedin.py` to transform 3,000+ saves into structured Markdown (the "Dave Killeen Heuristic").
- **Success:** Processed 3,477 items into `00-Inbox/LinkedIn/` with automated author WikiLinking.

**1d. X/Twitter Intel (Drop Zone Pivot)**
- **Ingest Strategy:** Parallel to LinkedIn, use the **Drop Zone** for X Bookmark exports to avoid API cost and platform bans.
- **Task:** Build `System/ingest/parse_x.py` to process X Bookmark JSON into the same Markdown ecosystem.
- **Contextual 'Follows':** Add handles to `System/user-profile.yaml` via `/ingest follow @Handle`. Dex will use these to flag high-signal posts during the ingest process.
- **Scrapling Fallback:** Experiment with the `scrapling` MCP for ad-hoc profile scans when a manual export isn't available.
- Cost: $0 — Zero API dependency.

**1e. The cron job layer**
- Dave runs background automations (`.scripts/` + macOS Launch Agents) that pre-populate intel files overnight so they're ready when he opens Claude
- Same pattern, your version: a nightly cron that fires the YouTube MCP, LinkedIn ingestion script, and any other data fetchers — so `/daily-plan` in the morning just assembles, doesn't fetch

**Full intel source map:**

| Source | Tool | How it gets into Dex |
|---|---|---|
| YouTube (~100 channels) | YouTube Data API → `user-youtube` MCP | `06-Resources/Intel/YouTube_YYYY-MM-DD.md` |
| X/Twitter | X API (tweepy) → `user-x` MCP | `06-Resources/Intel/X_YYYY-MM-DD.md` |
| LinkedIn messages | Daily JSON export / upload | Vault markdown, cross-ref against People/ |
| 120 newsletters | Gmail via Google Workspace MCP (built-in) | Gmail query in `/daily-plan` Step 5.8 |
| DeFi/on-chain signals | Dune Analytics → `user-dune` MCP (you build this) | `06-Resources/Intel/Crypto_YYYY-MM-DD.md` |
| Meetings | Granola MCP (built-in) | Auto-syncs 30 min post-meeting |
| Calendar | Apple Calendar MCP (built-in) | Live read during `/daily-plan` |

***

### Phase 2: Stripe Demo Layer (Week 2–3)

Everything in this phase is explicitly portfolio-facing and Stripe-relevant.

**2a. `user-stripe` MCP**
- Build an MCP against Stripe's API (they already publish an official one — check Smithery.ai first, then customize)
- Surfaces into your daily briefing: payment volume trends, dispute rates, failed charges, revenue signals
- "Eating your own dog food" — you're reasoning about Stripe data inside your operating system
- Standalone repo: `yourusername/mcp-stripe`

**2b. `user-dune` MCP**
- Connect your existing Dune Analytics dashboards (Morpho Blue work) into Dex
- DeFi signals in the morning briefing: protocol TVL, liquidation risks, yield changes
- This is the crossover that makes your profile unique — most PMs don't have on-chain analytics in their daily operating system
- Directly relevant to Stripe's stablecoin/crypto push

**2c. `dex-web` — the web UI layer**
- A Next.js/Supabase app that reads your Dex vault and surfaces it visually
- Daily briefing as a web dashboard (not just terminal output)
- This is the PM + builder demo: you took a CLI-first tool and productized it for non-technical users
- Built with Lovable for speed, Supabase for sync (also your Marginalia Supabase schema is reusable here — see Phase 3)
- Deploy it, put the URL in your Stripe application

***

### Phase 3: The Engine → Cockpit Sync (Parallel)
*Connecting the local vault to the `savewithmarginalia` web UI.*

| Dex Concept | What It Becomes in the Cockpit |
|---|---|
| **Social Parsers** | `/ingest` skill: Transforms raw Drop Zone JSON into structured Markdown. |
| **Daily Plans** | `30-briefings/` folder: Synced to Supabase for mobile viewing as "Morning Intel". |
| **Person Pages** | `05-Areas/People/` WikiLinks: Visualized in the UI as CRM-style contact profiles. |
| **Search Tuning** | Hybrid Search (pgvector + Markdown): Standardized across terminal and web. |
| **Skill Triggers** | UI Buttons: Direct invocation of Dex/Claude Python MCP server routines. |

**The one Cog worth building as a new Dex skill:**
A **`/save-article`** skill — Scrapling fetches URL → clean markdown → auto-tagged → saved to `06-Resources/Reading/`. This embeds the entire "Article Keeper" job-to-be-done natively in your OS core.

***

### Phase 4: Advanced Automations (Nice-to-Have)

**4a. LinkedIn Scraping (Full Automation)**
- Dave uses **Phantom Buster** to scrape LinkedIn messages and connection requests, exports as CSV/webhook.
- A lightweight cron script or custom MCP ingests that export into a vault markdown file.
- Re-introduces automated signal discovery for professional networking once the core engine is stable.

---

### GitHub Portfolio Structure

```
yourusername/dex              ← your fork (vault data gitignored, skills/MCPs public)
yourusername/dex-web          ← Next.js web UI on top of Dex
yourusername/mcp-youtube      ← standalone, starrable
yourusername/mcp-x            ← standalone, starrable
yourusername/mcp-dune         ← crossover with your existing DeFi work
yourusername/mcp-stripe       ← Stripe demo artifact
yourusername/mcp-phantombuster ← LinkedIn scraping (Phase 4)
```
