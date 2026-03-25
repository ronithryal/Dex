# Leveraging LinkedIn Saved Posts in Dex OS

Your LinkedIn saved posts are a high-signal source of **Lead Intelligence** and **Social Context**. Instead of letting them die in an unvisited LinkedIn folder, Dex converts them into actionable knowledge.

## 📥 Acquisition & Ingest
1. **Export:** Use the [LinkedIn Saves Exporter](https://chromewebstore.google.com/detail/linkedin-saves-exporter/gjodnbfdffddoliaimeoaanjfldemnmn) extension once a day/week.
2. **Download:** Export as a **JSON** file.
3. **Feed Dex:** Drag-and-drop the JSON file into the **`00-Inbox/Drop_Zone/`** folder in your sidebar.
4. **Automation:** Tell Dex "My latest LinkedIn saved posts" (or similar) and mention (@) the file, and it will automatically trigger the `System/ingest/parse_linkedin.py` parser.

## 🏗️ The Transformation (JSON -> Markdown)
Dex follows the **"Dave Killeen Heuristic"** (LLMs dance better with Markdown). Every saved post is converted into a structured `.md` file in `00-Inbox/LinkedIn/` with:
- **Author WikiLinks:** Each author is linked to their own **Person Page** in your vault.
- **Frontmatter:** Metadata like URL, ID, and Ingest Date are preserved for indexing.
- **Full Text:** The raw content is sanitized and formatted for RAG (Retrieval-Augmented Generation).

## 🚀 How to Leverage the Data

### 1. The "Morning Intelligence Brief"
During your `/daily-plan`, Dex scans for new files in the LinkedIn inbox. It will flag:
- **Top-tier Leads:** "You saved three posts from Patrick Collison (Stripe) today. Worth a reach out?"
- **Emerging Trends:** "Multiple saves from 'Enzo Avigo' regarding Claude Cowork. Should we analyze this workflow?"

### 2. Semantic Recall (Chat)
You can query your saved archive directly without scrolling LinkedIn:
- *"What was that contrarian take on stablecoins I saved last week?"*
- *"Show me everything Enzo Avigo has written about AI Agents."*

### 3. CRM Integration
When you visit a Person Page in your vault (e.g., `[[Enzo_Avigo]]`), Dex will automatically show you a list of all posts you’ve saved from them, providing instant context for your next DM or meeting.

---
**Status:** Phase 1c (Active Development)
**Engine:** `parse_linkedin.py`
