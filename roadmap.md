## Full Roadmap: Dex Setup → Portfolio → Stripe Demo

***

### Phase 0: Foundation (Day 1) [COMPLETE]

- [x] **Fork `davekilleen/dex`** to your GitHub first — before touching anything locally
- [x] `git clone https://github.com/ronithryal/dex.git` locally
- [x] Open the cloned fork in Antigravity
- [x] Run `/setup` with your role definition:
   - **Role:** Product Manager / Founder / Builder
   - **Focus areas/pillars:** Portfolio/GitHub presence, Stripe application, DeFi/on-chain analytics, AI-native product development, Learning/career growth (GT Physics, YC prep)
   - **Working style:** Solo, async, build fast, ship publicly
   - **Communication:** Direct, bullet points, no fluff
- [x] Everything from step 4 onward — your vault structure, user profile, skills, MCPs — is on YOUR GitHub from day one

**GitHub portfolio structure:**
```
yourusername/dex               ← your fork (vault data gitignored, skills/MCPs public)
yourusername/dex-web           ← Next.js web UI on top of Dex (savewithmarginalia)
yourusername/mcp-youtube       ← standalone, starrable
yourusername/mcp-x             ← X/Twitter intel
yourusername/mcp-dune          ← crossover with your existing DeFi work
yourusername/mcp-stripe        ← Stripe demo artifact
yourusername/mcp-phantombuster ← LinkedIn intel
```

***

### Phase 1: Core Intel Layer (Week 1)

This is the layer Dave built that is **not** in the public repo — you're replicating and improving it. Every MCP you build here is a standalone public repo on your GitHub.

**1a. Newsletters [ACTIVE]**
- [x] Run `/google-workspace-setup` — connects Gmail (google-workspace-mcp registered)
- [ ] Dex's `daily-plan` Step 5.8 already queries Gmail for newsletters and extracts market signals with a "why this matters / contrarian angle" framing
- [ ] You get your newsletters feeding into your briefing immediately, no custom code needed
- Cost: $0

**1b. YouTube Intel [ACTIVE]**
- [x] Build an MCP server that fetches new videos from subscribed channels, summarizes them, and flags what's new, novel, and contrarian
- [x] Name it `user-youtube` — registered in `.mcp.json`
- [ ] Output goes to `06-Resources/Intel/YouTube_YYYY-MM-DD.md`
- [ ] `daily-plan` trigger: checks if today's intel file exists — if not, triggers the MCP
- [ ] Publish as standalone repo: `yourusername/mcp-youtube`
- Cost: $0 — YouTube Data API free quota

**1c. LinkedIn Intel [COMPLETE - SIGNAL SCALE]**
- [x] **Signal Capture:** Created `System/ingest/parse_linkedin.py` for high-volume transformation.
- [x] **Ingest:** Processed 3,477 items into `00-Inbox/LinkedIn/` (Vault Markdown).
- [ ] **Phantom Buster Upgrade:** Use Phantom Buster to scrape LinkedIn messages and connection requests, exports as CSV/webhook.
- [ ] **CRM Indexing:** Dex cross-references new connections against your contacts in `05-Areas/People/` to flag who's worth responding to (fintech/YC/Stripe focus).
- [ ] Publish ingest script as: `yourusername/mcp-phantombuster`

**1d. X/Twitter Intel**
- [ ] Pull your X timeline, bookmarks, and mentions into a daily digest using the X API free tier (tweepy)
- [ ] Build a `user-x` MCP that:
  - Fetches bookmarks saved since last run
  - Fetches timeline from accounts you follow, filtered by engagement threshold
  - Flags "strong signal" posts (DeFi, fintech, YC focus)
- [ ] **Drop Zone Pivot:** Maintain manual JSON export support for resilience against API changes.
- [ ] Publish as standalone repo: `yourusername/mcp-x`

**1e. The cron job layer**
- [ ] Setup background automations (`.scripts/` + macOS Launch Agents) that pre-populate intel files overnight.
- [ ] Nightly cron fires YouTube, LinkedIn, X, and other fetchers — `/daily-plan` in the morning just assembles, doesn't fetch.

**Full intel source map after Phase 1:**

| Source | Tool | How it gets into Dex |
|---|---|---|
| Newsletters | Gmail via Google Workspace MCP (built-in) | Gmail query in `/daily-plan` Step 5.8 |
| YouTube (~100 channels) | YouTube Data API → `user-youtube` MCP | `06-Resources/Intel/YouTube_YYYY-MM-DD.md` |
| LinkedIn messages | Phantom Buster → custom ingest script | Vault markdown, cross-ref against `People/` |
| X/Twitter | X API free tier → `user-x` MCP | `06-Resources/Intel/X_YYYY-MM-DD.md` |
| Meetings | Granola MCP (built-in) | Auto-syncs 30 min post-meeting |
| Calendar | Apple Calendar MCP (built-in) | Live read during `/daily-plan` |

***

### Phase 2: Stripe Demo Layer (Week 2–3)

Everything in this phase is explicitly portfolio-facing and Stripe-relevant.

**2a. `user-stripe` MCP**
- [ ] Check Smithery.ai for community Stripe MCPs to customize.
- [ ] Surfaces into your daily briefing: payment volume trends, dispute rates, failed charges, revenue signals.
- [ ] "Eating your own dog food" — you're reasoning about Stripe data inside your AI operating system.
- [ ] Publish as standalone repo: `yourusername/mcp-stripe`.

**2b. `user-dune` MCP**
- [ ] Connect your existing Dune Analytics dashboards (Morpho Blue work) into Dex.
- [ ] DeFi signals in the morning briefing: protocol TVL, liquidation risks, yield changes.
- [ ] Directly relevant to Stripe's stablecoin/crypto push.
- [ ] Publish as standalone repo: `yourusername/mcp-dune`.

**2c. `dex-web` — the web UI layer**
- [ ] A Next.js/Supabase app that reads your Dex vault and surfaces it visually (savewithmarginalia).
- [ ] Daily briefing as a web dashboard — not just terminal output.
- [ ] Built with Lovable for speed, Supabase for sync.
- [ ] Deploy it, put the URL in your Stripe application.

***

### Phase 3: Marginalia → Dex (Parallel, not blocking)

Marginalia is deprecated. Archive the repo with a postmortem README. Extract its value and fold into Dex:

| Marginalia Feature | What It Becomes in Dex |
|---|---|
| Article reader + tagging | **`/save-article`** skill: Scrapling fetches URL → clean markdown → auto-tagged by pillar → saved to `06-Resources/Reading/` |
| Semantic search | Already in Dex as QMD (`/enable-semantic-search`) |
| Chat with your notes | This IS Dex's core loop — your Marginalia chat UI becomes the `dex-web` frontend |
| Knowledge graph | Dex's Obsidian integration + wiki-link auto-linker |
| Newsletter ingestion | Folded into Gmail MCP |
| Supabase backend | Becomes the sync layer for `dex-web` — multi-device, shareable briefings |

**The one Marginalia concept worth building as a new Dex skill:**
**`/save-article`** — URL in, tagged markdown out, auto-queued into reading list, surfaced in daily plan. Ship it as a standalone skill and submit it as a PR to Dave's upstream repo.

***

### The Through-Line for Stripe

Every phase tells the same story: *"I built an AI-native operating system that reasons about financial data, and I built it the way I'd build a product at Stripe — incrementally, with composable MCP infrastructure, eating my own dog food on Stripe's own APIs, and shipping everything publicly."*

The `dex-web` URL + your GitHub org with 5-6 active MCP repos + the Dex fork with visible commit history = a stronger Stripe application than any resume line.
