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

In config.py you should change BASE_URL. For example, if you are in Moscow it will be "https://msk.quiz-please.com/{}", сheck your link at https://quizplease.com/.

Run main.py to check for available games. Information about available games will be saved in the file available_games.json.

In registration.py, you should fill in the information about your team: team name, captain name, email, phone, number of teammates, and Telegram account.

To register for games you must first run main.py, then registration.py.

Registration.py compares registered_games.json and available_games.json. If registered_games.json is empty you will be registered for all available games in the city you specified in BASE_URL.

