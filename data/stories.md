## stats path 1
* greet
  - utter_greet
* get_covid_update{"location": "uk"}
  - slot{"location": "uk"}
  - action_covid_stats
  - utter_did_that_help
* thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## stats path 2
* get_covid_update{"location": "india"}
  - slot{"location": "india"}
  - action_covid_stats
  - utter_did_that_help
* thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## stats path 3
* greet
  - utter_greet
* get_covid_update{"location": "italy"}
  - slot{"location": "italy"}
  - action_covid_stats
  - utter_did_that_help
* deny
  - utter_ask_again
* get_covid_update{"location": "italy"}
  - slot{"location": "italy"}
  - action_covid_stats
  - utter_did_that_help
* thanks
  - utter_gratitude
* goodbye
  - utter_goodbye

## stats path 4
* greet
  - utter_greet
* get_covid_update{"location": "uk"}
  - slot{"location": "uk"}
  - action_covid_stats
  - utter_did_that_help
* affirm
  - utter_gratitude
* goodbye
  - utter_goodbye

## greet path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

