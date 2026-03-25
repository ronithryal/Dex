# PM Decision & Tradeoff Log

This log tracks the major product and architectural decisions made during the development of this OS, explicitly highlighting the **tradeoffs** and **product judgment** behind each move. This serves as a primary artifact for Stripe/YC-level engineering and product reviews.

---

## [2026-03-25] - Strategic Pivot: Marginalia SaaS → Dex Local-First AI OS

**Context:** Marginalia was originally a standalone React/Supabase web application for saving articles.

**Decision:** Formally deprecate the Marginalia SaaS app and pivot to a local-first "Personal AI Operating System" architecture built on the Dex engine fork.

**Tradeoffs Considered:**
*   **Approach A: Build the Marginalia SaaS monolith.**
    *   *Pros:* Complete control over UI, easy for non-technical users.
    *   *Cons:* High operational overhead (DB management, auth, hosting), crowded market, lower "engineering depth" signal for high-tier roles.
*   **Approach B: Pivot to Lex/Dex Engine (Local-first).**
    *   *Pros:* High signal for systems thinking, zero-latency local context, composable MCP architecture, defensible "private data" angle.
    *   *Cons:* Higher technical complexity, requires user to manage a local markdown vault.

**Rationale:**
The SaaS approach is a "product-in-search-of-a-problem." By moving into the OS layer (Dex), we are solving the **workflow integration** problem rather than just the **storage** problem. For a Stripe-level role, demonstrating the ability to build a "System of Systems" (MCP, local vault, CLI/Web hybrid) is a significantly stronger signal than building another web-app-on-Supabase.

---

## [2026-03-25] - Decision: Google Workspace API Scope

**Context:** The `google-workspace-mcp` allows access to Gmail, Calendar, Drive, Sheets, Docs, Slides, etc.

**Decision:** Limit initial integration strictly to **Gmail and Calendar** APIs for Phase 1.

**Tradeoffs Considered:**
*   **Approach A: Enable all Workspace APIs.**
    *   *Pros:* Complete access to user data.
    *   *Cons:* High initial setup friction (auth for 7+ APIs), scope creep, potentially overwhelming signal-to-noise ratio.
*   **Approach B: Phased Rollout (Gmail/Calendar Focus).**
    *   *Pros:* Fastest path to the "Morning Briefing" MVP. Focuses on the highest-signal communication channels first.
    *   *Cons:* Temporary loss of document-based context (Drive/Docs).

**Rationale:**
The primary "job-to-be-done" for Phase 1 is high-frequency, daily market intelligence retrieval. Newsletters (Gmail) and Meetings (Calendar) are the highest ROI inputs. By narrowing the scope, we minimize the manual Google Cloud bottleneck while building a solid foundation for the intelligence scanning layer.

---

## [2026-03-25] - Decision: YouTube Intel Strategy (Transcripts vs Metadata)

**Context:** Building the `user-youtube` MCP to extract signals from technical subscriptions.

**Decision:** Prioritize the retrieval of **raw video transcripts** via the search API over channel metadata or generic descriptions.

**Tradeoffs Considered:**
*   **Approach A: Channel/Description Indexing.**
    *   *Pros:* Fast API calls, low token usage.
    *   *Cons:* Low signal density. Descriptions rarely capture the "contrarian take" or technical nuance within the video.
*   **Approach B: Transcript Fetching (Current).**
    *   *Pros:* High semantic density. Allows Dex to perform LLM-summarization on the *actual content* of the talk.
    *   *Cons:* Higher latency, token-intensive, requires transcript-specific API parsing.

**Rationale:**
For a Stripe portfolio project, a "title-fetcher" is a toy. Building a tool that extracts and synthesizes insight from raw technical audio demonstrates superior engineering depth and a clear "contrarian" product filter—identifying the signal within the video that a generic scraper would miss.

---

## [2026-03-25] - Decision: Harmony Strategy (Antigravity IDE + Gemini CLI)

**Context:** Deciding how to balance the use of two different AI development tools that share the same underlying MCP protocol.

**Decision:** Adopt Antigravity as the primary "Agentic IDE" and visual build environment, while exposing all custom MCPs to the Gemini CLI for terminal-based automation and headless execution.

**Tradeoffs Considered:**
*   **Approach A: Standardize solely on Antigravity.**
    *   *Pros:* Single configuration path, reduced mental overhead.
    *   *Cons:* Loss of terminal flexibility; harder to pipe agent output into other Unix tools (e.g., jq, grep).
*   **Approach B: Use both harmoniously (Current).**
    *   *Pros:* Combines the deep-coding strengths of a visual IDE with the speed and automation power of a CLI. Future-proofs the MCPs for CI/CD.
    *   *Cons:* Minor configuration redundancy (must register servers in both the IDE's MCP Store and the CLI's `~/.mcp.json`).

**Rationale:**
By standardizing at the **MCP Layer**, we ensure that our "Intelligence OS" is tool-agnostic. For an engineering portfolio, this demonstrates advanced systems thinking: building a modular service layer that provides a consistent interface to multiple clients, regardless of whether the UI is a web editor or a terminal.

---

## [2026-03-25] - Decision: LinkedIn Ingest Strategy (Manual Extension)

**Context:** Deciding how to ingest social and lead intelligence from LinkedIn while avoiding platform bans and scraping liabilities.

**Decision:** Use a **Manual Extension Ingest** model (via the *LinkedIn Saves Exporter* extension) where the user periodically exports saved posts as JSON and dumps them into the Dex vault for automated processing into Markdown.

**Tradeoffs Considered:**
*   **Approach A: Automated PhantomBuster Scraping (Headless).**
   *   *Pros:* Zero user friction after setup.
   *   *Cons:* High ban risk for the user's primary account, requires third-party API subscription, high maintenance cost due to LinkedIn UI changes.
*   **Approach B: Manual Extension + Markdown Parser (Current).**
   *   *Pros:* Zero ban risk (mimics human browser behavior), high fidelity data (saves and full text), no API costs.
   *   *Cons:* High friction—user must "turn the key" manually by running the export.

**Rationale:**
For a "Private OS," reliability and safety are paramount. By relying on a browser extension for the **acquisition** layer and custom parsing for the **intelligence** layer, we bypass the scraping cat-and-mouse game. This also creates a clear daily rhythm: the user "feeds" the OS their latest signals, and the OS returns the "Briefing."

**Data Representation Choice:** 🛡️ JSON vs. Markdown
We will convert all raw JSON exports into structured **Markdown** files inside the vault. As per the "Dave Killeen" heuristic: **"LLMs dance better with Markdown."** Markdown preserves semantic relationships (headers, bullets, links) in a way that RAG systems can index and reason over far more naturally than raw JSON blobs.

**Future**
Implenation of PhantomBuster and automation of the manual extension ingest process. This will be done by building a custom MCP that can interact with the PhantomBuster API. This will be done in a way that is safe for the user's account and does not violate any terms of service. 

---

## [2026-03-25] - Milestone: Build Skill 001 (LinkedIn Intelligence)

**Decision:** Formally classify the "LinkedIn Saved Posts Detection & Parsing" workflow as the system's first user-built **Agentic Skill**.

**Context:** The user implemented a two-part intelligence bridge:
1. **Trigger Logic:** A behavioral rule in `CLAUDE.md` that detects the presence of LinkedIn exports.
2. **Execution Logic:** A Python parser (`parse_linkedin.py`) that implements the "Dave Killeen Markdown Heuristic."

**Rationale:**
This represents the transition from "Writing Scripts" to "Building an Operating System." By teaching the AI to recognize a signal (JSON upload) and respond with a specific set of tools (Transformation + Indexing), the user has built a core component of the Dex OS Intelligence Layer.

---

## [2026-03-25] - Decision: The "Drop Zone" Pivot

**Context:** Identifying that the Antigravity IDE (and most chat interfaces) creates friction for non-text file attachments (JSON, PDF), which are critical for intelligence ingestion.

**Decision:** Pivot to a **"Drop Zone" Ingest Architecture** using the vault folder `00-Inbox/Drop_Zone/` as the primary landing pad for all raw intelligence exports.

**Tradeoffs Considered:**
*   **Approach A: Rely on Chat Attachments.**
    *   *Pros:* Low friction conceptually.
    *   *Cons:* Frequently blocked by UI sandboxing in IDEs; unreliable path resolution.
*   **Approach B: Physical Ingest Folder (Drop Zone).**
   *   *Pros:* Zero UI friction; permanent record of raw ingest; easier for agent tools to scan and process.
   *   *Cons:* Requires one extra step for the user to drag a file into the sidebar.

**Rationale:**
In an "Agentic Operating System," the vault is the source of truth. By using the **Drop Zone**, we move the ingestion process away from the transient chat window and into the permanent filesystem. This allows the AI Agent to proactively scan for new signals without waiting for a user to manage "attachments."

---

## [2026-03-25] - Milestone: Stage 1 Activation (Intelligence Layer Live)

**Context:** Finalizing the ingestion pipeline for the Dex OS Intelligence Layer.

**Accomplishments:**
- **LinkedIn Archive Processed:** 3,477 items transformed from raw JSON to structured Markdown in `00-Inbox/LinkedIn/`.
- **System Ignition:** Successfully registered and activated `google-workspace-mcp` (Gmail/Calendar) and `user-youtube` (Transcripts) in the Antigravity `mcp_config.json`.
- **Daily Plan V1:** Generated the first automated Intelligence Briefing (`00-Inbox/Daily_Plans/2026-03-25.md`) by synthesizing cross-platform signals.

**Rationale:**
This milestone marks the completion of the "Passive Ingest" phase. The OS now has active "eyes" (Gmail/YouTube) and a "memory" (LinkedIn Archive). We have moved from a static storage vault to a dynamic intelligence engine that proactive summarizes user inputs.

---

## [2026-03-25] - Decision: Formalizing Skill 001 (/ingest-linkedin)

**Context:** Transitioning the LinkedIn parser from a "background behavior" to a first-class command/trigger system.

**Decision:** Formally register the command `/ingest-linkedin` and implement a "tag-sensing" trigger where mentioning a Drop Zone file automatically invokes the intelligence ingest skill.

**Rationale:**
To build a system that feels like an "OS," users need consistent interface patterns. Just as `/daily-plan` synthesizes intelligence, `/ingest-linkedin` captures it. By allowing the user to simply tag a file (e.g., "Ingest @linkedin-saved-posts.json"), we create a "Physical Ingest" metaphor that maps to how people naturally interact with files in a workspace.

---

## [2026-03-25] - Decision: Universal Ingest Architecture (/ingest)

**Context:** Expanding from a LinkedIn-only parser to a multi-source intelligence engine (YouTube, X, PDF, generic JSON).

**Decision:** Generalized `/ingest-linkedin` into a universal `/ingest` command. Replaced source-specific guides with a unified `Upload_Intelligence_Guide.md`.

**Rationale:**
A "Skill Per Platform" approach (e.g., `/ingest-linkedin`, `/ingest-twitter`) doesn't scale for the user. By centralizing all ingestion under `/ingest`, we reinforce the **"Drop Zone"** as the single entry point for all intelligence. This allows the command to grow intelligently—detecting the data type and applying the appropriate "Dave Killeen Markdown Heuristic" automatically.


---

## [2026-03-25] - Decision: Intelligence Archival (/daily-plan)

**Context:** The `/daily-plan` skill generates high-value intelligence briefs from social/email signals.

**Decision:** Require that all `/daily-plan` outputs are automatically saved to `00-Inbox/Daily_Plans/YYYY-MM-DD.md`.

**Rationale:**
By forcing the agent to write the briefing to the vault, we create a version-controlled history of the user's daily intelligence. This enables the Agent to perform "Multi-Day Synthesis" (e.g., "What have been the top 3 trends in the last 7 days?") without re-reading thousands of raw source files. The vault becomes the summarized memory.

---

## [2026-03-25] - Decision: Social Ingest Strategy (Path A: The Drop Zone)

**Context:** Determining the best way to ingest X (Twitter) bookmarks and posts without the volatility and cost of the X API v2.

**Decision:** Adopt **"Path A: The Drop Zone"** for all social intelligence (X, LinkedIn). Users perform period exports (JSON) and Dex processes them locally.

**Rationale:**
The X API is a "moving target" with high costs and restrictive scopes. By standardizing on **Manual Export -> Local Parsing**, we ensure the Dex OS remains:
1. **Private/Local-First**: Data never leaves the machine.
2. **Resilient**: We are not broken by API removals or platform policy shifts.
3. **Low Friction**: The same `/ingest` command handles all platforms identically.
Tracking follows is done via `user-profile.yaml` to create intent, while the Drop Zone provides the actual data.

**Future**