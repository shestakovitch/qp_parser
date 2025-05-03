import requests
from bs4 import BeautifulSoup
import fake_user_agent


def fetch_page(url):
    """
    Отправляет GET-запрос по указанному URL и возвращает объект BeautifulSoup.
    """

    # Подменяем User-Agent на фейковый и передаём в response в виде headers
    user = fake_user_agent.user_agent()
    headers = {
        'User-Agent': user
    }

    try:
        # Добавляем таймаут в 5 секунд
        response = requests.get(url, headers=headers, timeout=5)

        # Если код ответа 200 - записываем результат response в HTML файл и передаём для дальнейшего парсинга
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        else:
            raise Exception(f"Не удалось загрузить страницу. Статус: {response.status_code}")

    except requests.exceptions.Timeout:
        raise Exception("Страница недоступна. Превышено время ожидания (5 секунд).")
    except (requests.exceptions.ConnectionError, requests.exceptions.RequestException) as e:
        raise Exception(f"Страница недоступна. Ошибка соединения: {str(e)}")
