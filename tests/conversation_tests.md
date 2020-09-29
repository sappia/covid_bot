#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## stats path 1
* greet: hello
  - utter_greet
* get_covid_update: give me the coronavirus stats for Russia
  - action_covid_stats
  - utter_did_that_help
* thanks: thanks a lot
  - utter_gratitude
* goodbye: bye
  - utter_goodbye

## stats path 2
* get_covid_update: I want to know the coronavirus cases and deaths in France
  - action_covid_stats
  - utter_did_that_help
* thanks: Thank you
  - utter_gratitude
* goodbye: see you later
  - utter_goodbye

## stats path 3
* greet: hi
  - utter_greet
* get_covid_update: china coronavirus stats please
  - action_covid_stats
  - utter_did_that_help
* deny: no
  - utter_ask_again
* get_covid_update: give me the covid statistics for China
  - action_covid_stats
  - utter_did_that_help
* thanks: Thanks for that
  - utter_gratitude
* goodbye: goodbye
  - utter_goodbye

## greet path
* greet: hey
  - utter_greet

## say goodbye
* goodbye: bye
  - utter_goodbye
