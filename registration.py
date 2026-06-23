import json
import logging

import requests
import fake_user_agent
from bs4 import BeautifulSoup
from game_info import available_games
from config import TEAM_NAME, CAPTAIN_NAME, EMAIL, PHONE, NUMBER_OF_PLAYERS, TELEGRAM_NAME
from sender import send_message
from logger import setup_logging

logger = logging.getLogger(__name__)


def main():
    if not available_games:
        logger.info("Нет доступных игр")
        return

    with open("registered_games.json") as file:
        registered_games = json.load(file)

    logger.info("Начало регистрации, доступно игр: %d", len(available_games))

    for game, link in available_games.items():

        if game not in registered_games:
            registered_games[game] = link

            user = fake_user_agent.user_agent()
            header = {
                'User-Agent': user
            }

            data = {
                "record-from-form": "1",
                "QpRecord[teamName]": TEAM_NAME,
                "QpRecord[captainName]": CAPTAIN_NAME,
                "QpRecord[email]": EMAIL,
                "QpRecord[phone]": PHONE,
                "QpRecord[count]": NUMBER_OF_PLAYERS,
                "QpRecord[comment]": "",
                "QpRecord[custom_fields_values]": "[{\"name\":\"50d1d4c5-4b3d-4027-b577-01e26b4919f6\",\"type\":\"text\","
                                                  "\"label\":\"ваш+ник+в+telegram\",\"placeholder\":\"\","
                                                  f'"\"value\": "{TELEGRAM_NAME}"}}]',
                "QpRecord[first_time]": "0",
                "certificates[]": "",
                "QpRecord[game_id]": link.split("id=")[1],
                "QpRecord[max_people_active]": "1",
                "reservation": "",
                "QpRecord[site_content_id]": "",
                "QpRecord[is_agreed_to_mailing]": "1"
            }

            logger.info("Регистрация на игру: %s", link)
            response = requests.post(link, data=data, headers=header)
            logger.debug("Ответ регистрации: статус %d", response.status_code)

            soup = BeautifulSoup(response.text, "lxml")

            try:
                alert = soup.find("div", class_="alert alert-danger").text.strip()
            except AttributeError:
                alert = "no errors"

            if response.status_code == 200 and alert == "no errors":
                with open("registered_games.json", "w") as file:
                    json.dump(registered_games, file, indent=4, ensure_ascii=False)

                success_msg = (
                    f'Вы зарегистрировались на игру {game}\n'
                    f'Ожидайте письмо с подтверждением на email: {data["QpRecord[email]"]}\n'
                )
                #print(success_msg)
                logger.info(success_msg.strip())

                send_message(f'Вы зарегистрировались на игру:\n{game}')
            else:
                error_msg = f"Ошибка регистрации на игру {game}\n{link}\nKод ошибки: {alert}"
                #print(error_msg)
                logger.error(error_msg)
        else:
            already_msg = f"Вы уже зарегистрировались на игру: \n{game}\n"
            #print(already_msg)
            logger.info(already_msg.strip())

    #print(f"\n{'-' * 79}")


if __name__ == "__main__":
    setup_logging()
    main()
