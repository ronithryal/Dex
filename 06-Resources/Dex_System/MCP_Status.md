# Dex OS — MCP System Status

This document tracks the active "Intelligence Bridges" connected to your vault.

## 🟢 YouTube Intelligence (user-youtube)
- **Repo:** `/Users/ronith/Marginalia/mcp-youtube/` (Standalone Portfolio Repo)
- **Status:** ACTIVE
- **Connection:** YouTube Data API (v3)
- **Capabilities:** Fetch latest transcripts, Summarize videos, Summarize channel sentiment.
- **Workflow:** Automatically triggers during `/daily-plan` if new videos are detected.

## 🟢 LinkedIn Ingest (Skill 001)
- **Logic:** `System/ingest/parse_linkedin.py`
- **Status:** ACTIVE
- **Capabilities:** Transforms Drop Zone JSON exports into Markdown archives.
- **Workflow:** Explicit trigger via `/ingest` or manual file drop.

## 🟡 X/Twitter Intelligence (user-x)
- **Status:** PENDING (Phase 1d)
- **Strategy:** Drop Zone Ingest (Manual-First) with `scrapling` fallback.

## 🟡 DeFi Intelligence (user-dune)
- **Status:** PLANNED (Phase 2b)
- **Connection:** Dune Analytics API.

---
**Last Ignition:** 2026-03-25 16:21
**Engine:** FastMCP (Python)
