import os
from dotenv import load_dotenv

load_dotenv()

# Загружаем данные для регистрации из файла .env
TEAM_NAME = os.getenv('TEAM_NAME')
CAPTAIN_NAME = os.getenv('CAPTAIN_NAME')
EMAIL = os.getenv('EMAIL')
PHONE = os.getenv('PHONE')
NUMBER_OF_PLAYERS = os.getenv('NUMBER_OF_PLAYERS')
TELEGRAM_NAME = os.getenv('TELEGRAM_NAME')

# Загружаем данные для отправки в telegram
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# URL страницы
BASE_URL = "https://beg.quiz-please.com/{}"

# Словарь в котором содержатся статусы игр и их параметры
STATUS_DATA = {
    'available': {'yes_answer': '---------------------------Доступные для записи игры:--------------------------',
                  'no_answer': '----------------------Нет игр на которые можно записаться.---------------------\n',
                  'parameters': ('green', 'active')},
    'end': {'yes_answer': '-------------------Игры на которые можно записаться в резерв:------------------',
            'no_answer': '-----------------Нет игр на которые можно записаться в резерв.-----------------\n',
            'parameters': ('yellow', 'end')},
    'closed': {'yes_answer': '----------------------Игры на которые закрыта регистрация:---------------------',
               'no_answer': '--------------------Нет игр на которые закрыта регистрация.--------------------',
               'parameters': ('pink', 'closed')}
}
