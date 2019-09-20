<h1>Элементарный телеграм бот.</h1>
[![Build Status](https://travis-ci.org/ilyaagusev/elementary_bot.svg?branch=master)](https://travis-ci.org/ilyaagusev/elementary_bot)

Настоящий телеграм бот написан для обучения программированию на языке Python и имеет адрес @pre_elementary_bot

<h2>Установка</h2>
Убедитесь, что директория в которую вы распковали архив, имеет доступ к интернет и содержит следующие файлы:

Название файла  | Содержание файла
----------------|----------------------
bot.py          | Основная функция бота
handlers.py     | Функции обработки событий
README.md       | Данный файл
settings.py     | Настройки прокси и ключ к боту
starter.py      | Функция обработки команды Start
requirements.txt| Файл с зависимостями

В файле `settings.py` необходимо передать в словарь PROXY адрес прокси, логин и пароль, в переменную API_KEY ключ к боту.

```python
PROXY = {
    'proxy_url': 'адрес_прокси',
    'urllib3_proxy_kwargs': {'username': 'логин', 'password': 'пароль'},
    }

API_KEY = 'ваш_ключ'

```
<h2>Требования</h2>

Использование бота требует установленного Python версии 3.6.8 и библиотеки python-telegram-bot.

<h2>Запуск</h2>

Запуск бота осуществляется через консоль командой: 

    
    python bot.py

