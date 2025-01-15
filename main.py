from scraper import fetch_page
from game_info import get_game_status, available_links
from config import BASE_URL, STATUS_DATA
import registration


def main():
    try:
        # Загрузка страницы
        url = BASE_URL.format('schedule')
        soup = fetch_page(url)

        # Вывод названия города
        print(f"\n{'-' * 79}\nГород: {soup.find('option', attrs={'selected': True}).text.strip()}\n")

        # Обработка статусов игр
        for status in STATUS_DATA:
            get_game_status(soup, status)

        # Вывод ссылок на игры если они есть
        if available_links:
            print(f"\n{'-' * 79}\nИгры на которые можно записаться (также сохранены в файл available_games.json):\n")
            for k, v in available_links.items():
                print(f"{k}:\n{v}\n")
        else:
            print("\nК сожалению нет игр на которые можно записаться")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
    registration.main()
