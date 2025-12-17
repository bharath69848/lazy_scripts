import requests
import webbrowser

url = "https://leetcode.com/graphql/"

payload = {
    "query": """
    query getDailyLink {
      activeDailyCodingChallengeQuestion {
        link
      }
    }
    """
}

headers = {
    "Content-Type": "application/json"
}

res = requests.post(url, json=payload, headers=headers)
data = res.json()

link = "https://leetcode.com" + data["data"]["activeDailyCodingChallengeQuestion"]["link"]
webbrowser.get("google-chrome").open(link)
