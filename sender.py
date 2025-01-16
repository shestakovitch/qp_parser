import os
import requests
from dotenv import load_dotenv

# Читаем переменные окружения
load_dotenv()

def send_message(message):
    """
    Отправляет сообщение об ошибке или успешной регистрации на квиз в телеграм
    """
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    CHAT_ID = os.getenv('CHAT_ID')

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    params = {
        'chat_id': CHAT_ID,
        'text': message
    }

    res = requests.post(url, params=params)
    return res