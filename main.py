import requests

api_key = "1389a9f6a3ac44c1963f33babc19a3ca"

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-07-14&' \
      'sortBy=publishedAt&apiKey=1389a9f6a3ac44c1963f33babc19a3ca'

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
