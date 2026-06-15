import requests

def wiki_search(query):

    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")

    headers = {
        "User-Agent": "AI-Voice-Assistant/1.0"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data.get("extract", "No information found.")