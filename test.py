import requests

link="https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=1dd2848490a84d188a177541edabfabd"

f=requests.get(link).json()
Articles=f["articles"]
print(f)
for i in Articles:
    print(i["title"])
    print(i["description"])
    print(i["url"])
    print(type(i["url"]))


