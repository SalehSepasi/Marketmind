import requests

def get_comments():
    """
    Get comments for a given crypto name
    """

    url = "https://api.coinmarketcap.com/gravity/v3/gravity/time-line-v2"

    payload = {
        "cryptoId": 1,
        "deviceId": "e75870b3-a19a-4751-abb1-c6efc84de52a",
        "languageCode": "en",
        "subType": "normal",
        "type": "Browseby"
    }

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://coinmarketcap.com",
        "Referer": "https://coinmarketcap.com/community/"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=20)
    response.raise_for_status()
    data = response.json()

    posts = data["data"]["list"]
    

    posts_data = []

    for post in posts:
        item = {
            "id": post.get("gravityId"),
            "author": post.get("owner", {}).get("nickname"),
            "text": post.get("textContent", "").strip(),
            "likes": post.get("likeCount", 0),
            "comments": post.get("commentCount", 0)
        }
        posts_data.append(item)

    return posts_data

    
if __name__ == "__main__":
    print("Number of posts:", len(get_comments()))
    print(get_comments())