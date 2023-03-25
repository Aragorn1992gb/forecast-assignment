from flask import Flask, request

import os

import requests
import urllib.parse

app = Flask(__name__)

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')


@app.route('/')
def forecast():
    address = request.args.get('location')
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()
    url_openweathermap = f"https://api.openweathermap.org/data/2.5/forecast?lat={response[0]['lat']}1&lon={response[0]['lon']}&appid={OPENWEATHERMAP_API_KEY}"
    openweathermap_response = requests.get(url_openweathermap).json()

    return openweathermap_response

if __name__ == "__main__":
    app.run(debug=True)