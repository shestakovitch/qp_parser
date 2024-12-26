# URL страницы
BASE_URL = "https://beg.quiz-please.com/{}"

# Словарь в котором содержатся статусы игр и их параметры
STATUS_DATA = {
    'available': {'yes_answer': '---------------------------Доступные для записи игры:--------------------------',
                  'no_answer': '----------------------Нет игр на которые можно записаться.---------------------\n',
                  'parameters': ('green', 'active')},
    'end': {'yes_answer': '-------------------Игры на которые можно записаться в резерв:------------------',
            'no_answer': '-----------------Нет игр на которые можно записаться в резерв.-----------------\n',
            'parameters': ('yellow', 'end')},
    'closed': {'yes_answer': '----------------------Игры на которые закрыта регистрация:---------------------',
               'no_answer': '--------------------Нет игр на которые закрыта регистрация.--------------------',
               'parameters': ('pink', 'closed')}
}
