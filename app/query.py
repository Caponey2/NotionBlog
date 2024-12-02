import requests 
from dotenv import load_dotenv
from datetime import datetime, timezone
import os


load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_pages():
    url=f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 100}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    import json
    with open('db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    
    return results

#get_pages()



pages = get_pages()
for page in pages:
    page_id = page["id"]
    props = page["properties"]
    url = page["url"]
    title = props["Name"]["title"][0]["text"]["content"]
    #published = props["Published"]["date"]["start"]
    #published = datetime.fromisoformat(published)
    print(title)