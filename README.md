# Курсы на Курсере

Скрипт `coursera.py` берет url 20 случайных курсов с [coursera.org](https://www.coursera.org/sitemap~www~courses.xml), проходит по страницам этих курсов, извлекает из них: название курса, язык, дату начала, продолжительность и рейтинг курса. Все эти данные выгружаются в файл `courses_info.xlsx`, создаваемый в каталоге со скриптом, в виде: одна строка - один курс.

# Использование

Скрипт требует установленного Python 3.5, а также зависимостей из `requirements.txt`.

Установка зависимостей:
```sh
$ pip install -r requirements.txt
```
Запуск скрипта:
```sh
$ python coursera.py
```

# Цели проекта

Данный код написан в образовательных целх. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
