import requests as rq
import json

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c9a032e908b8406d99bb5d1135692460"
# Fetch JSON Response from Server
response = rq.get(url)

"""
print(response.text) # Printing of JSON Textual Data
print(type(response.text))

print()

# Let us convert JSON Data into Python Dictionary
newsData = json.loads(response.text)
print(newsData)
print(type(newsData))

print()
print("======JSON Parsing======")
print()

print("totalResults: ",newsData["totalResults"])
print("artcles[0]: ",newsData["articles"][0])

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(newsData["articles"][0]["author"])
print(newsData["articles"][0]["title"])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(newsData["articles"][1]["author"])
print(newsData["articles"][1]["title"])
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

"""
newsData = json.loads(response.text)
for i in range(0, 10):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(newsData["articles"][i]["author"])
    print(newsData["articles"][i]["title"])
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")