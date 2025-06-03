import os
from dotenv import load_dotenv



from flask import Flask, render_template, request
import requests
from datetime import datetime, timedelta

load_dotenv()
app = Flask(__name__)
  # <-- вставь сюда свой API-ключ
API_KEY = os.getenv('API_KEY')
@app.route('/', methods=['GET', 'POST'])
def index():
    current_weather = None
    forecast_list = []
    city_time = None

    if request.method == 'POST':
        city = request.form['city']
        
        # Текущая погода
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            timezone_offset = weather_data['timezone']
            local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)

            current_weather = {
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
                'time': local_time.strftime('%Y-%m-%d %H:%M:%S')
            }

            # Прогноз на 5 дней
            forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=ru'
            forecast_response = requests.get(forecast_url)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()['list']

                # Получаем прогноз на каждый следующий день в 12:00
                for forecast in forecast_data:
                    if "12:00:00" in forecast['dt_txt']:
                        forecast_time = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
                        forecast_list.append({
                            'date': forecast_time.strftime('%d.%m.%Y'),
                            'temperature': forecast['main']['temp'],
                            'description': forecast['weather'][0]['description'],
                            'icon': forecast['weather'][0]['icon']
                        })

        else:
            current_weather = {'error': 'Город не найден'}

    return render_template('index.html', weather=current_weather, forecast=forecast_list)

if __name__ == '__main__':
    app.run(debug=True)
