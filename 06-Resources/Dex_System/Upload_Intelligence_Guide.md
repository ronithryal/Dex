# Intelligence Ingest Guide (The Drop Zone)

Dex functions as an **Intelligence Processing Platform**. Any raw signal you capture—LinkedIn saves, YouTube transcripts, or JSON exports—is transformed into structured Markdown for daily briefings and semantic recall.

## 📥 The Drop Zone Architecture
The folder **`00-Inbox/Drop_Zone/`** is the universal landing pad. Instead of managing complex API integrations for every service, you simply drop raw data here.

### 1. LinkedIn Saved Posts (Core Example)
- **Acquire:** Use the [LinkedIn Saves Exporter](https://chromewebstore.google.com/detail/linkedin-saves-exporter/gjodnbfdffddoliaimeoaanjfldemnmn) extension.
- **Drop:** Drag the exported `.json` into the `Drop_Zone/`.
- **Command:** `/ingest` or mention the file (`Ingest @linkedin-saved-posts.json`).
- **Result:** Dex converts thousands of rows into clean Markdown in `00-Inbox/LinkedIn/`.

### 2. General JSON / Markdown Uploads
If you have data from other platforms (Substack, X, Research databases) in JSON or MD format:
- **Drop:** Place them in the `Drop_Zone/`.
- **Trigger:** Use `/ingest` to process and archive them.
- **Workflow:** Dex will identify the source and apply the **"Dave Killeen Markdown Heuristic"** to optimize the content for RAG.

### 3. YouTube Signal Capture
You can teach the OS which channels to track for your daily briefings:
- **Command:** `/ingest add @Handle to favorite channels`.
- **Action:** Dex will resolve the handle to a Channel ID and add it to your `user-profile.yaml` tracking list.

## 🏗️ The Transformation (Raw -> Markdown)
Dex follows the rule: **"LLMs dance better with Markdown."** 
- **WikiLinks:** Authors and companies are automatically linked to their respective **Person** or **Company** pages.
- **Frontmatter:** Every note includes metadata (URL, ingest date, source) for RAG indexing.
- **Archiving:** Once processed, raw files are timestamped and moved to `07-Archives/` to keep your vault clean.

## 🚀 Leveraging Your Intelligence
- **`/daily-plan`**: Scans your ingested vault for the day's top signals.
- **`/chat`**: Queries your entire personal intelligence graph.
- **`[[Person_Pages]]`**: Instant context on everyone you've saved content from.

---
**Status:** Phase 1d (Generalized Ingest Active)
**Command:** `/ingest`
