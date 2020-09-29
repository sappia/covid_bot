import http.client
import json
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	'x-rapidapi-key': "XXXXrapidapi-keyXXXX"
	}

class ApiAction(Action):
	def name(self):
		return "action_covid_stats"

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		print(loc)
		conn.request("GET", "/statistics?country="+loc, headers=headers)
		res = conn.getresponse()
		data = res.read()

		# convert json into python dict
		data_json = json.loads(data)

		# number of new cases
		cases = data_json["response"][0]["cases"]["new"]

		# number of new deaths
		deaths = data_json["response"][0]["deaths"]["new"]

		out_message = "Number of latest cases in {} is {} and latest deaths is {}.".format(loc, cases, deaths)

		dispatcher.utter_message(out_message)

		return [SlotSet('location', loc)]
