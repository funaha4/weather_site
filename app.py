from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "d72b205804d2ad660924862a76799f33"  # OpenWeatherMapのAPIキー
CITY = "Tokyo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}"


@app.route("/")
def index():
    return render_template("index.html")  # HTMLテンプレートを返す


@app.route("/weather")
def get_weather():
    response = requests.get(URL)
    data = response.json()

    weather_data = {
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
    }
    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)
