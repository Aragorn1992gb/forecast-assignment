# forecast-assignment
use openweathermap.org apis to retrieve last 5-days weather for a given location

# API
GET
http://127.0.0.1:5000/
Query param: "location" in which you specify the city/address, example: "Lecce, LE"

Example Response:
{
    "city": {
        "coord": {
            "lat": 40.357,
            "lon": 18.1718
        },
        "country": "IT",
        "id": 3174953,
        "name": "Lecce",
        "population": 83303,
        "sunrise": 1679719398,
        "sunset": 1679763804,
        "timezone": 3600
    },
    "cnt": 40,
    "cod": "200",
    "list": [
        {
            "clouds": {
                "all": 0
            },
            "dt": 1679767200,
            "dt_txt": "2023-03-25 18:00:00",
            "main": {
                "feels_like": 289.42,
                "grnd_level": 1007,
                "humidity": 63,
                "pressure": 1012,
                "sea_level": 1012,
                "temp": 290.03,
                "temp_kf": 2.57,
                "temp_max": 290.03,
                "temp_min": 287.46
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 240,
                "gust": 2.42,
                "speed": 1.91
            }
        },
        {
            "clouds": {
                "all": 0
            },
            "dt": 1679778000,
            "dt_txt": "2023-03-25 21:00:00",
            "main": {
                "feels_like": 288.36,
                "grnd_level": 1008,
                "humidity": 68,
                "pressure": 1013,
                "sea_level": 1013,
                "temp": 288.95,
                "temp_kf": 2.16,
                "temp_max": 288.95,
                "temp_min": 286.79
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 245,
                "gust": 3.76,
                "speed": 2.81
            }
        },
        {
            "clouds": {
                "all": 2
            },
            "dt": 1679788800,
            "dt_txt": "2023-03-26 00:00:00",
            "main": {
                "feels_like": 286.97,
                "grnd_level": 1007,
                "humidity": 72,
                "pressure": 1013,
                "sea_level": 1013,
                "temp": 287.59,
                "temp_kf": 1.22,
                "temp_max": 287.59,
                "temp_min": 286.37
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 317,
                "gust": 4.09,
                "speed": 3.33
            }
        },
        {
            "clouds": {
                "all": 7
            },
            "dt": 1679799600,
            "dt_txt": "2023-03-26 03:00:00",
            "main": {
                "feels_like": 285.14,
                "grnd_level": 1007,
                "humidity": 82,
                "pressure": 1013,
                "sea_level": 1013,
                "temp": 285.69,
                "temp_kf": 0,
                "temp_max": 285.69,
                "temp_min": 285.69
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 324,
                "gust": 4.83,
                "speed": 3.63
            }
        },
        {
            "clouds": {
                "all": 9
            },
            "dt": 1679810400,
            "dt_txt": "2023-03-26 06:00:00",
            "main": {
                "feels_like": 286.38,
                "grnd_level": 1008,
                "humidity": 84,
                "pressure": 1014,
                "sea_level": 1014,
                "temp": 286.77,
                "temp_kf": 0,
                "temp_max": 286.77,
                "temp_min": 286.77
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 329,
                "gust": 4.96,
                "speed": 2.81
            }
        },
        {
            "clouds": {
                "all": 29
            },
            "dt": 1679821200,
            "dt_txt": "2023-03-26 09:00:00",
            "main": {
                "feels_like": 289.61,
                "grnd_level": 1008,
                "humidity": 67,
                "pressure": 1014,
                "sea_level": 1014,
                "temp": 290.11,
                "temp_kf": 0,
                "temp_max": 290.11,
                "temp_min": 290.11
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03d",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 339,
                "gust": 2.37,
                "speed": 2.44
            }
        },
        {
            "clouds": {
                "all": 38
            },
            "dt": 1679832000,
            "dt_txt": "2023-03-26 12:00:00",
            "main": {
                "feels_like": 290.87,
                "grnd_level": 1007,
                "humidity": 59,
                "pressure": 1013,
                "sea_level": 1013,
                "temp": 291.44,
                "temp_kf": 0,
                "temp_max": 291.44,
                "temp_min": 291.44
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03d",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 231,
                "gust": 2.79,
                "speed": 0.86
            }
        },
        {
            "clouds": {
                "all": 91
            },
            "dt": 1679842800,
            "dt_txt": "2023-03-26 15:00:00",
            "main": {
                "feels_like": 290.69,
                "grnd_level": 1005,
                "humidity": 50,
                "pressure": 1011,
                "sea_level": 1011,
                "temp": 291.49,
                "temp_kf": 0,
                "temp_max": 291.49,
                "temp_min": 291.49
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 214,
                "gust": 5.11,
                "speed": 3.16
            }
        },
        {
            "clouds": {
                "all": 79
            },
            "dt": 1679853600,
            "dt_txt": "2023-03-26 18:00:00",
            "main": {
                "feels_like": 286.45,
                "grnd_level": 1004,
                "humidity": 65,
                "pressure": 1010,
                "sea_level": 1010,
                "temp": 287.28,
                "temp_kf": 0,
                "temp_max": 287.28,
                "temp_min": 287.28
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 197,
                "gust": 6.35,
                "speed": 4.25
            }
        },
        {
            "clouds": {
                "all": 24
            },
            "dt": 1679864400,
            "dt_txt": "2023-03-26 21:00:00",
            "main": {
                "feels_like": 285.59,
                "grnd_level": 1003,
                "humidity": 65,
                "pressure": 1009,
                "sea_level": 1009,
                "temp": 286.5,
                "temp_kf": 0,
                "temp_max": 286.5,
                "temp_min": 286.5
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 185,
                "gust": 6.74,
                "speed": 4.33
            }
        },
        {
            "clouds": {
                "all": 18
            },
            "dt": 1679875200,
            "dt_txt": "2023-03-27 00:00:00",
            "main": {
                "feels_like": 285.5,
                "grnd_level": 1001,
                "humidity": 73,
                "pressure": 1007,
                "sea_level": 1007,
                "temp": 286.23,
                "temp_kf": 0,
                "temp_max": 286.23,
                "temp_min": 286.23
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 167,
                "gust": 7.68,
                "speed": 4.87
            }
        },
        {
            "clouds": {
                "all": 18
            },
            "dt": 1679886000,
            "dt_txt": "2023-03-27 03:00:00",
            "main": {
                "feels_like": 285.3,
                "grnd_level": 999,
                "humidity": 84,
                "pressure": 1005,
                "sea_level": 1005,
                "temp": 285.79,
                "temp_kf": 0,
                "temp_max": 285.79,
                "temp_min": 285.79
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 184,
                "gust": 9.2,
                "speed": 4.93
            }
        },
        {
            "clouds": {
                "all": 10
            },
            "dt": 1679896800,
            "dt_txt": "2023-03-27 06:00:00",
            "main": {
                "feels_like": 287.07,
                "grnd_level": 998,
                "humidity": 77,
                "pressure": 1004,
                "sea_level": 1004,
                "temp": 287.56,
                "temp_kf": 0,
                "temp_max": 287.56,
                "temp_min": 287.56
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 212,
                "gust": 11.17,
                "speed": 6.5
            }
        },
        {
            "clouds": {
                "all": 0
            },
            "dt": 1679907600,
            "dt_txt": "2023-03-27 09:00:00",
            "main": {
                "feels_like": 289.38,
                "grnd_level": 998,
                "humidity": 51,
                "pressure": 1004,
                "sea_level": 1004,
                "temp": 290.28,
                "temp_kf": 0,
                "temp_max": 290.28,
                "temp_min": 290.28
            },
            "pop": 0.04,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 245,
                "gust": 13.42,
                "speed": 9.93
            }
        },
        {
            "clouds": {
                "all": 2
            },
            "dt": 1679918400,
            "dt_txt": "2023-03-27 12:00:00",
            "main": {
                "feels_like": 289.31,
                "grnd_level": 998,
                "humidity": 48,
                "pressure": 1004,
                "sea_level": 1004,
                "temp": 290.29,
                "temp_kf": 0,
                "temp_max": 290.29,
                "temp_min": 290.29
            },
            "pop": 0.19,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 285,
                "gust": 15.21,
                "speed": 11.79
            }
        },
        {
            "clouds": {
                "all": 71
            },
            "dt": 1679929200,
            "dt_txt": "2023-03-27 15:00:00",
            "main": {
                "feels_like": 286.6,
                "grnd_level": 1000,
                "humidity": 57,
                "pressure": 1006,
                "sea_level": 1006,
                "temp": 287.61,
                "temp_kf": 0,
                "temp_max": 287.61,
                "temp_min": 287.61
            },
            "pop": 0.32,
            "rain": {
                "3h": 0.15
            },
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "light rain",
                    "icon": "10d",
                    "id": 500,
                    "main": "Rain"
                }
            ],
            "wind": {
                "deg": 308,
                "gust": 17.03,
                "speed": 12.26
            }
        },
        {
            "clouds": {
                "all": 68
            },
            "dt": 1679940000,
            "dt_txt": "2023-03-27 18:00:00",
            "main": {
                "feels_like": 284.92,
                "grnd_level": 1002,
                "humidity": 61,
                "pressure": 1008,
                "sea_level": 1008,
                "temp": 285.99,
                "temp_kf": 0,
                "temp_max": 285.99,
                "temp_min": 285.99
            },
            "pop": 0.05,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 311,
                "gust": 15.37,
                "speed": 10.36
            }
        },
        {
            "clouds": {
                "all": 0
            },
            "dt": 1679950800,
            "dt_txt": "2023-03-27 21:00:00",
            "main": {
                "feels_like": 284.39,
                "grnd_level": 1005,
                "humidity": 65,
                "pressure": 1011,
                "sea_level": 1011,
                "temp": 285.41,
                "temp_kf": 0,
                "temp_max": 285.41,
                "temp_min": 285.41
            },
            "pop": 0.2,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 312,
                "gust": 13.12,
                "speed": 8.54
            }
        },
        {
            "clouds": {
                "all": 28
            },
            "dt": 1679961600,
            "dt_txt": "2023-03-28 00:00:00",
            "main": {
                "feels_like": 283.99,
                "grnd_level": 1006,
                "humidity": 66,
                "pressure": 1012,
                "sea_level": 1012,
                "temp": 285.02,
                "temp_kf": 0,
                "temp_max": 285.02,
                "temp_min": 285.02
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03n",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 306,
                "gust": 13.22,
                "speed": 8.41
            }
        },
        {
            "clouds": {
                "all": 74
            },
            "dt": 1679972400,
            "dt_txt": "2023-03-28 03:00:00",
            "main": {
                "feels_like": 283.21,
                "grnd_level": 1007,
                "humidity": 55,
                "pressure": 1013,
                "sea_level": 1013,
                "temp": 284.58,
                "temp_kf": 0,
                "temp_max": 284.58,
                "temp_min": 284.58
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04n",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 351,
                "gust": 9.93,
                "speed": 6.73
            }
        },
        {
            "clouds": {
                "all": 81
            },
            "dt": 1679983200,
            "dt_txt": "2023-03-28 06:00:00",
            "main": {
                "feels_like": 283.04,
                "grnd_level": 1009,
                "humidity": 61,
                "pressure": 1015,
                "sea_level": 1015,
                "temp": 284.28,
                "temp_kf": 0,
                "temp_max": 284.28,
                "temp_min": 284.28
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "broken clouds",
                    "icon": "04d",
                    "id": 803,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 332,
                "gust": 8.42,
                "speed": 5.42
            }
        },
        {
            "clouds": {
                "all": 100
            },
            "dt": 1679994000,
            "dt_txt": "2023-03-28 09:00:00",
            "main": {
                "feels_like": 282.23,
                "grnd_level": 1013,
                "humidity": 54,
                "pressure": 1019,
                "sea_level": 1019,
                "temp": 283.71,
                "temp_kf": 0,
                "temp_max": 283.71,
                "temp_min": 283.71
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 340,
                "gust": 11.4,
                "speed": 9.24
            }
        },
        {
            "clouds": {
                "all": 94
            },
            "dt": 1680004800,
            "dt_txt": "2023-03-28 12:00:00",
            "main": {
                "feels_like": 283.96,
                "grnd_level": 1015,
                "humidity": 40,
                "pressure": 1021,
                "sea_level": 1021,
                "temp": 285.61,
                "temp_kf": 0,
                "temp_max": 285.61,
                "temp_min": 285.61
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 347,
                "gust": 13.33,
                "speed": 12.05
            }
        },
        {
            "clouds": {
                "all": 14
            },
            "dt": 1680015600,
            "dt_txt": "2023-03-28 15:00:00",
            "main": {
                "feels_like": 283.08,
                "grnd_level": 1017,
                "humidity": 38,
                "pressure": 1023,
                "sea_level": 1023,
                "temp": 284.86,
                "temp_kf": 0,
                "temp_max": 284.86,
                "temp_min": 284.86
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 344,
                "gust": 14.64,
                "speed": 11.15
            }
        },
        {
            "clouds": {
                "all": 8
            },
            "dt": 1680026400,
            "dt_txt": "2023-03-28 18:00:00",
            "main": {
                "feels_like": 281.75,
                "grnd_level": 1019,
                "humidity": 39,
                "pressure": 1025,
                "sea_level": 1025,
                "temp": 283.63,
                "temp_kf": 0,
                "temp_max": 283.63,
                "temp_min": 283.63
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 345,
                "gust": 14.76,
                "speed": 10.44
            }
        },
        {
            "clouds": {
                "all": 7
            },
            "dt": 1680037200,
            "dt_txt": "2023-03-28 21:00:00",
            "main": {
                "feels_like": 278.88,
                "grnd_level": 1021,
                "humidity": 41,
                "pressure": 1027,
                "sea_level": 1027,
                "temp": 282.85,
                "temp_kf": 0,
                "temp_max": 282.85,
                "temp_min": 282.85
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 355,
                "gust": 14.25,
                "speed": 10.39
            }
        },
        {
            "clouds": {
                "all": 30
            },
            "dt": 1680048000,
            "dt_txt": "2023-03-29 00:00:00",
            "main": {
                "feels_like": 276.92,
                "grnd_level": 1022,
                "humidity": 38,
                "pressure": 1029,
                "sea_level": 1029,
                "temp": 281.28,
                "temp_kf": 0,
                "temp_max": 281.28,
                "temp_min": 281.28
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03n",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 9,
                "gust": 13.18,
                "speed": 9.85
            }
        },
        {
            "clouds": {
                "all": 13
            },
            "dt": 1680058800,
            "dt_txt": "2023-03-29 03:00:00",
            "main": {
                "feels_like": 276.62,
                "grnd_level": 1023,
                "humidity": 39,
                "pressure": 1029,
                "sea_level": 1029,
                "temp": 280.65,
                "temp_kf": 0,
                "temp_max": 280.65,
                "temp_min": 280.65
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 4,
                "gust": 11.43,
                "speed": 7.83
            }
        },
        {
            "clouds": {
                "all": 7
            },
            "dt": 1680069600,
            "dt_txt": "2023-03-29 06:00:00",
            "main": {
                "feels_like": 278.09,
                "grnd_level": 1024,
                "humidity": 43,
                "pressure": 1030,
                "sea_level": 1030,
                "temp": 281.56,
                "temp_kf": 0,
                "temp_max": 281.56,
                "temp_min": 281.56
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 7,
                "gust": 9.09,
                "speed": 6.87
            }
        },
        {
            "clouds": {
                "all": 16
            },
            "dt": 1680080400,
            "dt_txt": "2023-03-29 09:00:00",
            "main": {
                "feels_like": 281.74,
                "grnd_level": 1025,
                "humidity": 37,
                "pressure": 1031,
                "sea_level": 1031,
                "temp": 283.67,
                "temp_kf": 0,
                "temp_max": 283.67,
                "temp_min": 283.67
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 12,
                "gust": 6.29,
                "speed": 5.9
            }
        },
        {
            "clouds": {
                "all": 8
            },
            "dt": 1680091200,
            "dt_txt": "2023-03-29 12:00:00",
            "main": {
                "feels_like": 282.86,
                "grnd_level": 1024,
                "humidity": 36,
                "pressure": 1030,
                "sea_level": 1030,
                "temp": 284.71,
                "temp_kf": 0,
                "temp_max": 284.71,
                "temp_min": 284.71
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01d",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 13,
                "gust": 4.64,
                "speed": 4.7
            }
        },
        {
            "clouds": {
                "all": 13
            },
            "dt": 1680102000,
            "dt_txt": "2023-03-29 15:00:00",
            "main": {
                "feels_like": 282.37,
                "grnd_level": 1023,
                "humidity": 37,
                "pressure": 1029,
                "sea_level": 1029,
                "temp": 284.24,
                "temp_kf": 0,
                "temp_max": 284.24,
                "temp_min": 284.24
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 37,
                "gust": 3.03,
                "speed": 3.53
            }
        },
        {
            "clouds": {
                "all": 19
            },
            "dt": 1680112800,
            "dt_txt": "2023-03-29 18:00:00",
            "main": {
                "feels_like": 280.04,
                "grnd_level": 1023,
                "humidity": 47,
                "pressure": 1029,
                "sea_level": 1029,
                "temp": 281.47,
                "temp_kf": 0,
                "temp_max": 281.47,
                "temp_min": 281.47
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02n",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 106,
                "gust": 2.63,
                "speed": 2.43
            }
        },
        {
            "clouds": {
                "all": 3
            },
            "dt": 1680123600,
            "dt_txt": "2023-03-29 21:00:00",
            "main": {
                "feels_like": 279.32,
                "grnd_level": 1023,
                "humidity": 49,
                "pressure": 1029,
                "sea_level": 1029,
                "temp": 281.1,
                "temp_kf": 0,
                "temp_max": 281.1,
                "temp_min": 281.1
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "clear sky",
                    "icon": "01n",
                    "id": 800,
                    "main": "Clear"
                }
            ],
            "wind": {
                "deg": 175,
                "gust": 3.1,
                "speed": 2.82
            }
        },
        {
            "clouds": {
                "all": 36
            },
            "dt": 1680134400,
            "dt_txt": "2023-03-30 00:00:00",
            "main": {
                "feels_like": 279.4,
                "grnd_level": 1022,
                "humidity": 55,
                "pressure": 1028,
                "sea_level": 1028,
                "temp": 281.39,
                "temp_kf": 0,
                "temp_max": 281.39,
                "temp_min": 281.39
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "scattered clouds",
                    "icon": "03n",
                    "id": 802,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 175,
                "gust": 3.77,
                "speed": 3.25
            }
        },
        {
            "clouds": {
                "all": 97
            },
            "dt": 1680145200,
            "dt_txt": "2023-03-30 03:00:00",
            "main": {
                "feels_like": 280.02,
                "grnd_level": 1021,
                "humidity": 68,
                "pressure": 1027,
                "sea_level": 1027,
                "temp": 282.09,
                "temp_kf": 0,
                "temp_max": 282.09,
                "temp_min": 282.09
            },
            "pop": 0,
            "sys": {
                "pod": "n"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04n",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 178,
                "gust": 4.75,
                "speed": 3.66
            }
        },
        {
            "clouds": {
                "all": 98
            },
            "dt": 1680156000,
            "dt_txt": "2023-03-30 06:00:00",
            "main": {
                "feels_like": 283.19,
                "grnd_level": 1020,
                "humidity": 74,
                "pressure": 1026,
                "sea_level": 1026,
                "temp": 284.11,
                "temp_kf": 0,
                "temp_max": 284.11,
                "temp_min": 284.11
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 185,
                "gust": 6.01,
                "speed": 3.74
            }
        },
        {
            "clouds": {
                "all": 100
            },
            "dt": 1680166800,
            "dt_txt": "2023-03-30 09:00:00",
            "main": {
                "feels_like": 286.72,
                "grnd_level": 1020,
                "humidity": 62,
                "pressure": 1026,
                "sea_level": 1026,
                "temp": 287.6,
                "temp_kf": 0,
                "temp_max": 287.6,
                "temp_min": 287.6
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 205,
                "gust": 5.48,
                "speed": 4.46
            }
        },
        {
            "clouds": {
                "all": 99
            },
            "dt": 1680177600,
            "dt_txt": "2023-03-30 12:00:00",
            "main": {
                "feels_like": 289.1,
                "grnd_level": 1018,
                "humidity": 56,
                "pressure": 1024,
                "sea_level": 1024,
                "temp": 289.91,
                "temp_kf": 0,
                "temp_max": 289.91,
                "temp_min": 289.91
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "overcast clouds",
                    "icon": "04d",
                    "id": 804,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 190,
                "gust": 5.06,
                "speed": 4.7
            }
        },
        {
            "clouds": {
                "all": 17
            },
            "dt": 1680188400,
            "dt_txt": "2023-03-30 15:00:00",
            "main": {
                "feels_like": 288.7,
                "grnd_level": 1016,
                "humidity": 56,
                "pressure": 1022,
                "sea_level": 1022,
                "temp": 289.54,
                "temp_kf": 0,
                "temp_max": 289.54,
                "temp_min": 289.54
            },
            "pop": 0,
            "sys": {
                "pod": "d"
            },
            "visibility": 10000,
            "weather": [
                {
                    "description": "few clouds",
                    "icon": "02d",
                    "id": 801,
                    "main": "Clouds"
                }
            ],
            "wind": {
                "deg": 183,
                "gust": 5.88,
                "speed": 5.5
            }
        }
    ],
    "message": 0
}
