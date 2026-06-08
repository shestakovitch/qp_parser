import logging

import requests
from bs4 import BeautifulSoup
import fake_user_agent

logger = logging.getLogger(__name__)


def fetch_page(url):
    """
    Отправляет GET-запрос по указанному URL и возвращает объект BeautifulSoup.
    """

    user = fake_user_agent.user_agent()
    headers = {
        'User-Agent': user
    }
    logger.debug("GET %s (User-Agent: %s)", url, user)

    try:
        response = requests.get(url, headers=headers, timeout=5)
        logger.debug("Ответ %s: статус %d", url, response.status_code)

        if response.status_code == 200:
            logger.info("Страница загружена: %s", url)
            return BeautifulSoup(response.text, "lxml")

        logger.error("Не удалось загрузить страницу %s, статус: %d", url, response.status_code)
        raise Exception(f"Не удалось загрузить страницу. Статус: {response.status_code}")

    except requests.exceptions.Timeout:
        logger.error("Таймаут при загрузке %s", url)
        raise Exception("Страница недоступна. Превышено время ожидания (5 секунд).")
    except (requests.exceptions.ConnectionError, requests.exceptions.RequestException) as e:
        logger.error("Ошибка соединения при загрузке %s: %s", url, e)
        raise Exception(f"Страница недоступна. Ошибка соединения: {str(e)}")
