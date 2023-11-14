from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        # You could render "City Not Found" instead like we do below
        return render_template('city-not-found.html')

    weather_data = get_current_weather(city)

    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    temp_f = float(weather_data['main']['temp'])
    feels_like_f = float(weather_data['main']['feels_like'])

    # Convert from Fahrenheit to Celsius
    temp_c = (temp_f - 32) / 1.8
    feels_like_c = (feels_like_f - 32) / 1.8

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{temp_c:.1f}",
        feels_like=f"{feels_like_c:.1f}"
    )


@app.route('/health')
def health_check():
    return 'OK'


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)