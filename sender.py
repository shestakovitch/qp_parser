import logging

import requests
from config import BOT_TOKEN, CHAT_ID

logger = logging.getLogger(__name__)


def send_message(message):
    """
    Отправляет сообщение об ошибке или успешной регистрации на квиз в телеграм
    """
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

    params = {
        'chat_id': CHAT_ID,
        'text': message
    }

    logger.debug("Отправка сообщения в Telegram (chat_id: %s)", CHAT_ID)
    res = requests.post(url, params=params)

    if res.status_code == 200:
        logger.info("Сообщение отправлено в Telegram")
    else:
        logger.error("Не удалось отправить сообщение в Telegram, статус: %d", res.status_code)

    return res
