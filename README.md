# Парсер игр Квиз, плиз!


## Installation

Cloning a repository:

```git clone https://github.com/shestakovitch/qp_parser.git```

Creating virtual environment:

```python3 -m venv venv```


Activating the virtual environment:

```source venv/bin/activate```

Installing the required packages from requirements.txt﻿:

```pip3 install -r requirements.txt```

## Description

In config.py you should change BASE_URL. For example, if you are in Moscow it will be "https://msk.quiz-please.com/{}", сheck your link at https://quizplease.com/
To check for available games, run main.py.
In registration.py, you should fill in the information about your team: team name, captain name, email, phone, number of teammates, and Telegram account.
To register for all available games, run registration.py.
