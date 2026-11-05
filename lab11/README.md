Запуск из папки lab11:

```sh
python main.py
python test_analysis.py
python fetch_profile.py
python profile_sample.py
```

Вариант 1: все задачи указанного пользователя. Пример selected.json получен для ID 5. Для упражнения без сети использованы учебные локальные данные profile_sample.json. Адрес API задаёт профиль GitHub, GET получает данные, таймаут ограничивает ожидание; обработчики сообщают об ошибках HTTP, сети, данных и доступа к файлу.
