from flask import Flask, jsonify, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

API_KEY = "d72b205804d2ad660924862a76799f33"  # OpenWeatherMapのAPIキー
CITY = "Tokyo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}"

users = {"admin": "password"}  # Simple user store

@app.route("/")
def index():
    if 'username' in session:
        response = requests.get(URL)
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        return render_template("index.html", temperature=temperature, weather=weather)  # HTMLテンプレートを返す
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/weather")
def get_weather():
    if 'username' not in session:
        return redirect(url_for('login'))
    # Add logic to fetch and display weather information
    return "Weather information"

if __name__ == "__main__":
    app.run(debug=True)