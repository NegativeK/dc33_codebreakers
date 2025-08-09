"""
curl 'https://code-two.replit.app/api/challenge/submit' \
  -X POST \
  -H 'Content-Type: application/json' \
  -H 'Cookie: connect.sid=s%3AYKDcyaksSHOxvIiiFBsjB.mfZAacFprreQ2nooxaMUmVm1XkyGFqoFugwDEhrGMOc' \
  --data-raw '{"code": "undergroundnet.ru"}'
"""

import itertools
import requests
import time

FAILED_REQUEST = {"success": False, "message": "Invalid code"}

GUESSES = [
    """
ГЛАВНАЯ ФОРУМ ИНСТРУМЕНТЫ МАРКЕТ КОНТАКТЫ
ДОБРО ПОЖАЛОВАТЬ В ПОДПОЛЬЕ

Закрытое сообщество для изучения информационной безопасности. Здесь вы найдете инструменты, обучающие материалы и единомышленников. Соблюдайте правила и будьте осторожны.
СТАТИСТИКА ФОРУМА
Пользователей: 1,337
Тем: 42,069
Сообщений: 133,742
Онлайн: 89
ПОСЛЕДНЯЯ АКТИВНОСТЬ
Neo_1999 опубликовал новую тему в "Взлом" 2 мин
Morpheus_Code загрузил новый инструмент 15 мин
Trinity_Hack обновила профиль 1 час
ДОСТУП К СИСТЕМЕ
Система активна
Защищенное соединение
Анонимный доступ

Для доступа к закрытым разделам войдите в систему.
СООБЩЕНИЯ
Agent_Smith
Система обнаружила новую уязвимость...
23:42
CodeBreaker
Кто-то пытается взломать матрицу...
23:15

ВНИМАНИЕ: Этот сайт предназначен только для образовательных целей

Администрация не несет ответственности за действия пользователей

© 2024 UNDERGROUNDNET.RU - Все права защищены
""",
    """
АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяМАТРИЦАСИСТЕМАЗИОНМОРФЕУСНЕОТРИНИТИ                                                                                                                        Вызов выполнен
Вы успешно расшифровали матрицу Добро пожаловать в истину 
Сессия истекла
Перезагрузите страницу и войдите снова
Неверный код
Введенный вами код неверен Продолжайте поиск в матрице                             Ошибка
Пожалуйста введите код Скопировано
Ссылка  скопирована в буфер обмена
Доступ разрешен
Ваша секретная ссылка  раскрыта
Скопировать ссылку
Открыть ссылку
Попробовать снова
Введите секретный код
Расшифруйте паттерн чтобы открыть скрытую ссылку
Введите код здесь
Проверка
Отправить код
Доступ разрешен
Добро пожаловать в систему
Ошибка входа
Попробуйте еще раз
Ошибка
Введите имя пользователя и пароль
АКТИВЕНПОЛЬЗОВАТЕЛЕЙ
ГЛАВНАЯ
ФОРУМ
ИНСТРУМЕНТЫ
МАРКЕТ
КОНТАКТЫ
ДОБРО ПОЖАЛОВАТЬ В ПОДПОЛЬЕ
Закрытое сообщество для изучения информационной безопасности
Здесь вы найдете инструменты обучающие материалы и единомышленников
Соблюдайте правила и будьте осторожны
СТАТИСТИКА ФОРУМА
Пользователей
Тем
Сообщений
Онлайн
ПОСЛЕДНЯЯ АКТИВНОСТЬ
опубликовал новую тему в Взлом мин
загрузил новый инструмент мин
обновила профиль час
ДОСТУП К СИСТЕМЕ
Система активна
Защищенное соединение
Анонимный доступ  Для доступа к закрытым разделам войдите в системуИмя
пользователя
Пароль
ПОДКЛЮЧЕНИЕ
ВОЙТИ
Отмена
ВОЙТИ В СИСТЕМУ
СООБЩЕНИЯ
Система обнаружила новую уязвимость
Ктото пытается взломать матрицу
ВНИМАНИЕ Этот сайт предназначен только для образовательных целейАдминистрация не несет ответственности за действия пользователей
Все права защищены
""",
    """
ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
MATRIX
SYSTEMA
SION
ZION
MORPHEUS
NEO
TRINITY
Challenge completed
You have successfully decrypted the matrix
Welcome to the truth
Session expired
Reload the page and log in again
Invalid code
The code you entered is incorrect
Continue searching in the matrix
Error
Please enter the code
Copied
Link copied to clipboard
Access allowed
Your secret link has been revealed
Copy link
Open link
Try again
Enter the secret code
Decipher the pattern to reveal the hidden link
Enter the code here
Verification
Submit code
Access allowed
Welcome to the system
Login error
Try again
Error
Enter your username and password 
ACTIVE
USERS HOME FORUM TOOLS MARKET CONTACTS WELCOME WELCOME UNDERGROUND
A closed community for studying information security
Here you will find tools, training materials and like-minded people
Follow the rules and be careful
FORUM
STATISTICS
Users
Topics
Messages
Online
LATEST ACTIVITY
posted a new topic in Hacking
min uploaded a new tool min updated profile hour SYSTEM ACCESS
The system is active
Secure connection
Anonymous access
To access closed sections, log in
Username Password CONNECTION LOGIN Cancel
LOGIN MESSAGES
The system has detected a new vulnerability
Someone is trying to hack the matrix
ATTENTION This site is for educational purposes only
The administration is not responsible for the actions of users All rights reserved
""",
]


def clean_string(contents: str) -> set[str]:
    processed = contents.split("\n")
    tiered = [line.split(" ") for line in processed]

    flattened = (elm for items in tiered for elm in items)
    stripped = (line.strip(".:,") for line in flattened)
    lowered = (line.lower() for line in stripped)
    line = (line for line in lowered if line != "")

    result = set(line)

    return result


def main():
    # guesses = clean_string(GUESSES[1])
    words = [
        "m4trix",
        "sy5tem",
        "z1on",
        "m0rpheus",
        "n3o",
        "tr1nity",
    ]
    pairs = itertools.product(words, words)
    guesses = (pair[0] + pair[1] for pair in pairs)

    for guess in guesses:
        cookies = {
            "connect.sid": "s%3AYKDcyaksSHOxvIiiFBsjB.mfZAacFprreQ2nooxaMUmVm1XkyGFqoFugwDEhrGMOc",
        }

        req = requests.post(
            "https://code-two.replit.app/api/challenge/submit",
            cookies=cookies,
            data={"code": guess},
        )

        json_response = req.json()
        print(f"{guess=}\n{json_response}")

        if req.status_code != 400:
            print("Holy crap, success?")
            break

        if json_response != FAILED_REQUEST:
            print("Unexpected failure response")
            print(FAILED_REQUEST)
            breakpoint()
            break

        time.sleep(0.2)


if __name__ == "__main__":
    main()
