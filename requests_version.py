import requests
import os
import json

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)
data = response.json()

folder = "posts_requests"
os.makedirs(folder, exist_ok=True)

for item in data:
    file_path = os.path.join(folder, f"post_{item['id']}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(item, f, indent=4, ensure_ascii=False)

print("Done (requests)")