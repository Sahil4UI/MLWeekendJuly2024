# API - Application Programming Interface
import urllib.request as url
import json
# Java Script Object Notation
name = input("Ente Name : ")
path=f"https://api.giphy.com/v1/gifs/search?api_key=WgbNwwwSPMc1oOWEJVN72DFTM2gN4dHt&q={name}&limit=25&offset=0&rating=g&lang=en&bundle=messaging_non_clips"
response=url.urlopen(path)
data = json.load(response)
data = data["data"]
for i in range(len(data)):
    url.urlretrieve(data[i]["images"]["original"]["url"],f"myImage{i}.gif")
