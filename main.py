import logging

from scraper import fetch_page
from game_info import get_game_status, available_games
from config import BASE_URL, STATUS_DATA
from logger import setup_logging
import registration

logger = logging.getLogger(__name__)


def main():
    setup_logging()
    try:
        url = BASE_URL.format('schedule')
        logger.info("Загрузка расписания: %s", url)
        soup = fetch_page(url)

        city = soup.find('option', attrs={'selected': True}).text.strip()
        logger.info("Город: %s", city)
        #print(f"\n{'-' * 79}\nГород: {city}\n")

        for status in STATUS_DATA:
            get_game_status(soup, status)

        if available_games:
            logger.info("Найдено игр для записи: %d", len(available_games))
            header = f"\n{'-' * 79}\nИгры на которые можно записаться (также сохранены в файл available_games.json):\n"
            #print(header)
            logger.info(header.strip())
            for k, v in available_games.items():
                entry = f"{k}:\n{v}\n"
                #print(entry)
                logger.info("Игра для записи:\n%s\nСсылка: %s", k, v)
        else:
            msg = "К сожалению нет игр на которые можно записаться"
            logger.info(msg)
            #print(f"\n{msg}")
    except Exception as e:
        logger.exception("Ошибка при обработке расписания")
        #print(f"Ошибка: {e}")
    #print(f"\n{'-' * 79}")


if __name__ == "__main__":
    main()
    registration.main()
