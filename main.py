import requests
from send_email import send_email

topic = "tesla"

api_key = "1389a9f6a3ac44c1963f33babc19a3ca"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2023-07-16&sortBy=publishedAt&"
       "apiKey=1389a9f6a3ac44c1963f33babc19a3ca")

request = requests.get(url)

content = request.json()

body = "Subject: Today's News" + "\n"

for article in content["articles"][:20]:
    if (article["description"] is not None) and (article["title"] is not None):
        body = body + article["title"] + "\n"\
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
