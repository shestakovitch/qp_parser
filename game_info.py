from config import BASE_URL, STATUS_DATA
import json

available_links = {}  # Словарь для хранения игр на которые можно записаться и ссылок на них


def get_game_info(soup, color, status):
    """
    Находит и выводит информацию об играх с указанными параметрами.
    """
    h3_elements = soup.find_all('div', class_=f'h3 h3-{color} h3-mb10 block-date-with-language-game game-{status}')
    for h3 in h3_elements:
        print("\n")

        # Находим дату игры
        game_date = h3.text.strip()
        schedule_block_top = h3.find_next('div', class_='schedule-block-top')

        # Находим ссылку на игру
        link = BASE_URL.format('')[:-1] + schedule_block_top.find('a', class_='schedule-block-head w-inline-block')[
            'href']

        # Находим название игры
        game_name = h3.find_next('div', class_='h2 h2-game-card h2-left').text.strip()

        # Находим номер игры
        game_number = h3.find_next('div', class_='h2 h2-game-card').text.strip()

        # Выводим информацию об игре
        print(f"{game_date}\n{game_name}{game_number}")

        # Если статус игры active или end, то добавляем ссылки в список available_links
        if status in ('active', 'end'):
            available_links[f"{game_date} {game_name} {game_number}"] = link

    print(f"\n{'-'*79}")

    # Записываем информацию об играх в json файл
    with open("available_games.json", "w") as file:
        json.dump(available_links, file, indent=4, ensure_ascii=False)

def get_game_status(soup, status):
    """
    Проверяет наличие игр с указанным статусом и вызывает обработку.
    """
    if soup.find('div', class_=f'schedule-block {status}'):
        print(STATUS_DATA[status]['yes_answer'])
        get_game_info(soup, *STATUS_DATA[status]['parameters'])
    else:
        print(STATUS_DATA[status]['no_answer'])
