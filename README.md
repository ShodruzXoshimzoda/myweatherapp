Flask - myweatherapp

Это простое веб-приложение на Flask, которое позволяет пользователю вводить название города и получать:

- текущую погоду (температура, описание, иконка, местное время);
- прогноз на ближайшие 5 дней (в 12:00 каждого дня).

Данные берутся с OpenWeatherMap API.

---

 Запуск проекта
1. Клонируйте репозиторий (если нужно):
git clone https://github.com/ShodruzXoshimzoda/myweatherapp.git
cd myweatherapp

2.Создайте виртуальное окружение (рекомендуется):
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows

3.Установите зависимости:
pip install -r requirements.txt

4.Получите API-ключ
https://openweathermap.org/

5.Запустите приложение:
python3 app.py  # Linux
python app.py   # Windows
