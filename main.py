import requests
from send_email import send_email

api_key = "1389a9f6a3ac44c1963f33babc19a3ca"

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-07-14&' \
      'sortBy=publishedAt&apiKey=1389a9f6a3ac44c1963f33babc19a3ca'

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"].bold() + "\n" + article["description"] + 2*"\n"

message = f"""\
Subject: News Regarding Tesla 

{body}
"""
message = message.encode("utf-8")
send_email(message)

