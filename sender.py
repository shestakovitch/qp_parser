import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    """
    Отправляет сообщение об ошибке или успешной регистрации на квиз в телеграм
    """
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    params = {
        'chat_id': CHAT_ID,
        'text': message
    }

    res = requests.post(url, params=params)
    return res
