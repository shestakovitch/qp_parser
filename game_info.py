import json
import logging

from config import BASE_URL, STATUS_DATA
import urllib.parse

logger = logging.getLogger(__name__)

available_games = {}


def get_game_info(soup, color, status):
    """
    Находит и выводит информацию об играх с указанными параметрами.
    """
    games = soup.find_all('div', class_=f'h3 h3-{color} h3-mb10 block-date-with-language-game game-{status}')
    logger.info("Найдено игр со статусом '%s': %d", status, len(games))

    for game in games:
        print("\n")

        game_date = game.text.strip()
        game_name = game.find_next('div', class_='h2 h2-game-card h2-left').text.strip()
        game_number = game.find_next('div', class_='h2 h2-game-card').text.strip()
        bar_name = game.find_next('div', class_='schedule-block-info-bar').text.strip()
        address_div = soup.find('div', class_='techtext techtext-halfwhite')
        for a in address_div.find_all('a'):
            a.extract()
        bar_address = address_div.get_text(strip=True)
        google_maps_link = f"https://www.google.com/maps/search/?q={urllib.parse.quote(bar_address)}"

        game_time = game.find_next('div', class_='schedule-info').find_next('div', class_='schedule-info').find_next(
            'div', class_='techtext').text.strip()

        link_path = game.find_next('a', class_='schedule-block-head w-inline-block')['href']
        link = BASE_URL.format(link_path.lstrip('/'))

        game_info = f"{game_date} {game_time}\n{game_name} {game_number}\n{bar_name}\n{google_maps_link}"
        print(game_info)
        logger.info("Игра (%s):\n%s", status, game_info)

        if status in ('active', 'end'):
            available_games[f"{game_date} {game_time}\n{game_name} {game_number}\n{bar_name}\n{google_maps_link}"] = link

    print(f"\n{'-' * 79}")

    with open("available_games.json", "w", encoding='utf-8') as f:
        json.dump(available_games, f, indent=4, ensure_ascii=False)
    logger.info("Сохранено %d игр в available_games.json", len(available_games))


def get_game_status(soup, status):
    """
    Проверяет наличие игр с указанным статусом и вызывает обработку.
    """
    if soup.select_one(f'div.schedule-block.{status}'):
        print(STATUS_DATA[status]['yes_answer'])
        logger.info(STATUS_DATA[status]['yes_answer'])
        get_game_info(soup, *STATUS_DATA[status]['parameters'])
    else:
        print(STATUS_DATA[status]['no_answer'])
        logger.info(STATUS_DATA[status]['no_answer'].strip())
