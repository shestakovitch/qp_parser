import os
import json
import requests
import fake_user_agent
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def main():
    # Загружаем данные для регистрации из файла .env
    load_dotenv()

    TEAM_NAME = os.getenv('TEAM_NAME')
    CAPTAIN_NAME = os.getenv('CAPTAIN_NAME')
    EMAIL = os.getenv('EMAIL')
    PHONE = os.getenv('PHONE')
    NUMBER_OF_PLAYERS = os.getenv('NUMBER_OF_PLAYERS')
    TELEGRAM_NAME = os.getenv('TELEGRAM_NAME')

    # Открываем файл с информацией об играх на которые можно записаться
    with open("available_games.json") as file:
        available_games = json.load(file)

    with open("registered_games.json") as file:
        registered_games = json.load(file)

    for game, link in available_games.items():

        # Если игры нет в словаре с играми на которые уже зарегистрировались - добавляем эту игру в словарь
        if game not in registered_games:
            registered_games[game] = link

            # Подменяем User-Agent
            user = fake_user_agent.user_agent()
            header = {
                'User-Agent': user
            }

            # Словарь с данными для регистрации на игру
            data = {
                "record-from-form": "1",
                "QpRecord[teamName]": "",  # Впишите название команды
                "QpRecord[captainName]": "",  # Впишите имя капитана
                "QpRecord[email]": "",  # Впишите email
                "QpRecord[phone]": "",  # Впишите номер телефона
                "QpRecord[count]": "",  # Впишите количество человек
                "QpRecord[comment]": "",
                "QpRecord[custom_fields_values]": "[{\"name\":\"50d1d4c5-4b3d-4027-b577-01e26b4919f6\",\"type\":\"text\","
                                                  "\"label\":\"ваш+ник+в+telegram\",\"placeholder\":\"\","
                                                  "\"value\":\"@YourTelegram\"}]",  # Впишите телеграм аккаунт
                "QpRecord[first_time]": "0",
                "certificates[]": "",
                "QpRecord[game_id]": link.split("id=")[1],
                "QpRecord[max_people_active]": "1",
                "reservation": "",
                "QpRecord[site_content_id]": ""
            }

        # Передаём ссылку, словарь data и headers в POST запрос
        response = requests.post(link, data=data, headers=header)

        soup = BeautifulSoup(response.text, "lxml")

        # Проверяем ссылку
        try:
            alert = soup.find("div", class_="alert alert-danger").text.strip()
        except AttributeError:
            alert = "no errors"

        # Если код ответа 200 и нет alerta выводим сообщение об успешной регистрации
        if response.status_code == 200 and alert == "no errors":

            # Перезаписываем json с играми на которые уже зарегистрировались
            with open("registered_games.json", "w") as file:
                json.dump(registered_games, file, indent=4, ensure_ascii=False)

            print(f'Вы зарегистрировались на игру {game}\n'
                  f'Ожидайте письмо с подтверждением на email: {data["QpRecord[email]"]}\n')
        else:
            print(f"Ошибка регистрации на игру {game}\n{link}\nKод ошибки: {alert}")
    else:
        print(f"Вы уже зарегистрировались на игру: \n{game}\n")


if __name__ == "__main__":
    main()
