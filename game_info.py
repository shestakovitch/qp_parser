from config import BASE_URL, STATUS_DATA
import json

available_games = {}


def get_game_info(soup, color, status):
    """
    Извлекает и сохраняет информацию об играх с заданным цветом и статусом.
    """
    game_blocks = soup.find_all('div', class_=f'h3 h3-{color} h3-mb10 block-date-with-language-game game-{status}')
    for block in game_blocks:
        print("\n")

        game_date = block.text.strip()
        top_block = block.find_next('div', class_='schedule-block-top')
        link = BASE_URL.rstrip('/') + top_block.find('a', class_='schedule-block-head w-inline-block')['href']

        game_name = block.find_next('div', class_='h2 h2-game-card h2-left').text.strip()
        game_number = block.find_next('div', class_='h2 h2-game-card').text.strip()

        game_time = block.find_next('div', class_='schedule-info')\
                         .find_next('div', class_='schedule-info')\
                         .find_next('div', class_='techtext').text.strip()

        info = f"{game_date} {game_time}\n{game_name} {game_number}"
        print(info)

        if status in ('active', 'end'):
            available_games[info] = link

    print(f"\n{'-'*79}")

    with open("available_games.json", "w", encoding="utf-8") as f:
        json.dump(available_games, f, indent=4, ensure_ascii=False)


def get_game_status(soup, status):
    """
    Проверяет наличие игр с заданным статусом и вызывает парсер.
    """
    if soup.find('div', class_=f'schedule-block {status}'):
        print(STATUS_DATA[status]['yes_answer'])
        get_game_info(soup, *STATUS_DATA[status]['parameters'])
    else:
        print(STATUS_DATA[status]['no_answer'])
