import http.client
import json

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	'x-rapidapi-key': "XXXXrapidapi-keyXXXX"
	}

conn.request("GET", "/countries", headers=headers)
res = conn.getresponse()
data = res.read()

# convert json into python dict
data_json = json.loads(data)

num_countries = data_json["results"]

# write countries to a lookup file
with open("data/location.txt", "w") as c:
  for i in range(0,num_countries):
    country = data_json["response"][i]
    c.write(country + "\n")
