import json
import os
import re
import shutil
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text[:50]

def archive_json(json_path, archive_dir):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_path = os.path.join(archive_dir, f"linkedin-export-{timestamp}.json")
    shutil.copy2(json_path, archive_path)
    print(f"Archived raw JSON to: {archive_path}")

def parse_linkedin_json(json_path, output_dir, archive_dir):
    # First, preserve the raw data forever as per client request
    archive_json(json_path, archive_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Use today's date for ingest since source dates are often missing in exports
    ingest_date = datetime.now().strftime("%Y-%m-%d")

    count = 0
    for item in data:
        author = item.get("author", "Unknown Author")
        title = item.get("title", "No Title")
        url = item.get("url", "")
        activity_id = item.get("id", "")

        # Clean up title for filename
        clean_title = slugify(title)
        clean_author = slugify(author)
        
        filename = f"{ingest_date} - {clean_author} - {clean_title}.md"
        file_path = os.path.join(output_dir, filename)

        # Build Markdown content (Dave Killeen heuristic: LLMs dance better with MD)
        md_content = f"""---
author: [[{author}]]
source: LinkedIn
url: {url}
activity_id: {activity_id}
ingest_date: {ingest_date}
tags: #inbox #linkedin #intel
---

# {author} | LinkedIn Saved Post

{title}

---
[View on LinkedIn]({url})
"""

        # Robust surrogate handling for social media emojis/symbols
        # This safely encodes the content while handling lone surrogates found in LinkedIn exports
        safe_content = md_content.encode('utf-8', 'surrogatepass').decode('utf-8', 'ignore')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(safe_content)
        count += 1

    print(f"Successfully processed {count} LinkedIn posts into {output_dir}")

if __name__ == "__main__":
    # Primary Source: The Dex Drop Zone
    VAULT_BASE = "/Users/ronith/Marginalia/dex"
    DROP_ZONE = os.path.join(VAULT_BASE, "00-Inbox/Drop_Zone")
    VAULT_DEST = os.path.join(VAULT_BASE, "00-Inbox/LinkedIn")
    VAULT_ARCHIVE = os.path.join(VAULT_BASE, "07-Archives/LinkedIn_Saves")

    # Look for files matching the LinkedIn pattern in the Drop Zone first
    found_file = False
    if os.path.exists(DROP_ZONE):
        for f in os.listdir(DROP_ZONE):
            if f.endswith(".json") and "linkedin" in f.lower():
                JSON_SOURCE = os.path.join(DROP_ZONE, f)
                print(f"Detected LinkedIn export in Drop Zone: {f}")
                parse_linkedin_json(JSON_SOURCE, VAULT_DEST, VAULT_ARCHIVE)
                found_file = True
                break # Just process the first one for now

    if not found_file:
        # Fallback to Downloads if the Drop Zone is empty or missing
        JSON_SOURCE = "/Users/ronith/Downloads/linkedin-saved-posts (1).json"
        if os.path.exists(JSON_SOURCE):
            parse_linkedin_json(JSON_SOURCE, VAULT_DEST, VAULT_ARCHIVE)
        else:
            print(f"No LinkedIn exports found in Drop Zone or Downloads.")
