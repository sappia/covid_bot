# Covidbot

## Overview
This is a covid stats bot built using [RASA](https://rasa.com/) and [Rapid API](https://rapidapi.com/). This bot provides the latest covid cases and deaths for the country asked for.

The covid stats for a country are obtained by sending a request to [COVID-19](https://rapidapi.com/api-sports/api/covid-193), an API available on [RapidAPI](https://rapidapi.com/).

The aim of this project was to use RASA to create a simple bot and learn some of the core features of RASA like stories, domains, intents, actions, entities, slots and lookups.

## Contents
This project consists of training data, configuration files and action python file required to build the bot. Below are the files in the project and their purpose:
  * __config.yml__ contains the model configuration i.e. language, pipeline and policies
  * __domain.yml__ contains the domain of the assistant (bot) which includes actions, entities, slots, intents, responses
  * __endpoints.yml__ contains the webhook configuration for the custom actions
  * __actions.py__ contains the implementation of a custom action_covid_stats which gets the stats from Rapid API
  * __data/nlu.md__ contains training examples for each intent to train the NLU model
  * __data/stories.md__ contains training stories which are conversations to train the RASA Core dialogue system
  * __data/location.txt__ contains list of country names from COVID-19 Rapid API used as lookup by Rasa bot
  * __get_countries.py__ gets list of country names from COVID-19 Rapid API and writes to data/location.txt

## Installation
This bot was built using Python 3.7.3 and Rasa 1.10.3 versions. I recommend using the latest version of Rasa available [here in Rasa docs](https://rasa.com/docs/rasa/user-guide/installation/) and the Python version recommended by Rasa.

## Usage
To use this bot, follow the below steps:
1. Change the Rapid API key to your own key in actions.py and get_countries.py

2. Train the Rasa model:
```
rasa train
```
3. Test the Rasa model after training:
```
rasa train
```
4. In one terminal window, run the actions.py file
```
rasa run actions
```
5. In another terminal window, run the shell to interact with your bot
```
rasa shell
```

To have a conversation with the bot, see sample story paths in tests/conversation_tests.md



