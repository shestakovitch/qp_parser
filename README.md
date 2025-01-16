# Квиз, плиз! games parser


## Installation

Cloning a repository:

```git clone https://github.com/shestakovitch/qp_parser.git```

Creating a virtual environment:

```python3 -m venv venv```


Activating the virtual environment:

```source venv/bin/activate```

Installing the required packages from requirements.txt﻿:

```pip3 install -r requirements.txt```

## Description

You should rename .env.example file to .env, and fill in the information about your team: team name, captain name, email, phone, number of teammates, and Telegram account.

You should create a new bot in @BotFather:

https://core.telegram.org/bots/features#creating-a-new-bot

Insert API Token into BOT_TOKEN in the .env file.

Find this bot @username_to_id_bot in Telegram, select the chat or channel you want to receive game registration or error messages and it will give you a Chat id. Paste this Chat id into CHAT_ID in the .env file

In config.py you should change BASE_URL. For example, if you are in Moscow it will be "https://msk.quiz-please.com/{}", сheck your link at https://quizplease.com/.


When you run main.py:

1. It checks the games and prints them by category to the terminal (available games, games for which you can register as a reserve, games for which registration is closed)
2. Games for which registration is not closed are saved to the file available_games.json and passed on to registration.py
3. If the game is not in the registered_games.json file, you will be registered for it. If registered_games.json is empty you will be registered for all available games in the city you specified in BASE_URL


