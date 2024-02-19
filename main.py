import requests
import csv
import pandas as pd
import datetime
import time

def get_weather_from_one(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather_from_all(api_key, coordinates):
    data_list = {"coord.lon" : [], "coord.lat" : [], "weather.id" : [], "weather.main" : [], 
                 "weather.description" : [], "weather.icon" : [], "base" : [], "main.temp" : [], 
                 "main.feels_like" : [], "main.pressure" : [], "main.humidity" : [], 
                 "main.temp_min" : [], "main.temp_max" : [], "main.sea_level" : [], 
                 "main.grnd_level" : [], "visibility" : [], "wind.speed" : [], "wind.deg" : [], 
                 "wind.gust" : [], "clouds.all" : [], "rain.1h" : [], "rain.3h" : [], "snow.1h" : [], 
                 "snow.3h" : [], "dt" : [], "sys.type" : [], "sys.id" : [], "sys.message" : [], 
                 "sys.country" : [], "sys.sunrise" : [], "sys.sunset" : [], "timezone" : [], 
                 "id" : [], "name" : [], "cod" : []}

    for i, coordinate in enumerate(coordinates):
        # if (i > 100):
        #     break
        one_point_data = get_weather_from_one(api_key, coordinate[3], coordinate[2])

        try:
            coord_lon = one_point_data["coord"]["lon"]
        except KeyError:
            coord_lon = "nan"

        try:
            coord_lat = one_point_data["coord"]["lat"]
        except KeyError:
            coord_lat = "nan"

        try:
            weather_id = one_point_data["weather"][0]["id"]
        except KeyError:
            weather_id = "nan"

        try:
            weather_main = one_point_data["weather"][0]["main"]
        except KeyError:
            weather_main = "nan"

        try:
            weather_description = one_point_data["weather"][0]["description"]
        except KeyError:
            weather_description = "nan"

        try:
            weather_icon = one_point_data["weather"][0]["icon"]
        except KeyError:
            weather_icon = "nan"

        try:
            base = one_point_data["base"]
        except KeyError:
            base = "nan"

        try:
            main_temp = one_point_data["main"]["temp"]
        except KeyError:
            main_temp = "nan"

        try:
            main_feels__like = one_point_data["main"]["feels_like"]
        except KeyError:
            main_feels__like = "nan"

        try:
            main_pressure = one_point_data["main"]["pressure"]
        except KeyError:
            main_pressure = "nan"

        try:
            main_humidity = one_point_data["main"]["humidity"]
        except KeyError:
            main_humidity = "nan"

        try:
            main_temp__min = one_point_data["main"]["temp_min"]
        except KeyError:
            main_temp__min = "nan"

        try:
            main_temp__max = one_point_data["main"]["temp_max"]
        except KeyError:
            main_temp__max = "nan"

        try:
            main_sea__level = one_point_data["main"]["sea_level"]
        except KeyError:
            main_sea__level = "nan"

        try:
            main_grnd__level = one_point_data["main"]["grnd_level"]
        except KeyError:
            main_grnd__level = "nan"

        try:
            visibility = one_point_data["visibility"]
        except KeyError:
            visibility = "nan"

        try:
            wind_speed = one_point_data["wind"]["speed"]
        except KeyError:
            wind_speed = "nan"

        try:
            wind_deg = one_point_data["wind"]["deg"]
        except KeyError:
            wind_deg = "nan"

        try:
            wind_gust = one_point_data["wind"]["gust"]
        except KeyError:
            wind_gust = "nan"

        try:
            clouds_all = one_point_data["clouds"]["all"]
        except KeyError:
            clouds_all = "nan"

        try:
            rain_1h = one_point_data["rain"]["1h"]
        except KeyError:
            rain_1h = "nan"

        try:
            rain_3h = one_point_data["rain"]["3h"]
        except KeyError:
            rain_3h = "nan"

        try:
            snow_1h = one_point_data["snow"]["1h"]
        except KeyError:
            snow_1h = "nan"

        try:
            snow_3h = one_point_data["snow"]["3h"]
        except KeyError:
            snow_3h = "nan"

        try:
            dt = one_point_data["dt"]
        except KeyError:
            dt = "nan"

        try:
            sys_type = one_point_data["sys"]["type"]
        except KeyError:
            sys_type = "nan"

        try:
            sys_id = one_point_data["sys"]["id"]
        except KeyError:
            sys_id = "nan"

        try:
            sys_message = one_point_data["sys"]["message"]
        except KeyError:
            sys_message = "nan"

        try:
            sys_country = one_point_data["sys"]["country"]
        except KeyError:
            sys_country = "nan"

        try:
            sys_sunrise = one_point_data["sys"]["sunrise"]
        except KeyError:
            sys_sunrise = "nan"

        try:
            sys_sunset = one_point_data["sys"]["sunset"]
        except KeyError:
            sys_sunset = "nan"

        try:
            timezone = one_point_data["timezone"]
        except KeyError:
            timezone = "nan"

        try:
            id_ = one_point_data["id"]
        except KeyError:
            id_ = "nan"

        try:
            name = one_point_data["name"]
        except KeyError:
            name = "nan"

        try:
            cod = one_point_data["cod"]
        except KeyError:
            cod = "nan"


        data_list["coord.lon"].append(coord_lon)
        data_list["coord.lat"].append(coord_lat)
        data_list["weather.id"].append(weather_id)
        data_list["weather.main"].append(weather_main)
        data_list["weather.description"].append(weather_description)
        data_list["weather.icon"].append(weather_icon)
        data_list["base"].append(base)
        data_list["main.temp"].append(main_temp)
        data_list["main.feels_like"].append(main_feels__like)
        data_list["main.pressure"].append(main_pressure)
        data_list["main.humidity"].append(main_humidity)
        data_list["main.temp_min"].append(main_temp__min)
        data_list["main.temp_max"].append(main_temp__max)
        data_list["main.sea_level"].append(main_sea__level)
        data_list["main.grnd_level"].append(main_grnd__level)
        data_list["visibility"].append(visibility)
        data_list["wind.speed"].append(wind_speed)
        data_list["wind.deg"].append(wind_deg)
        data_list["wind.gust"].append(wind_gust)
        data_list["clouds.all"].append(clouds_all)
        data_list["rain.1h"].append(rain_1h)
        data_list["rain.3h"].append(rain_3h)
        data_list["snow.1h"].append(snow_1h)
        data_list["snow.3h"].append(snow_3h)
        data_list["dt"].append(dt)
        data_list["sys.type"].append(sys_type)
        data_list["sys.id"].append(sys_id)
        data_list["sys.message"].append(sys_message)
        data_list["sys.country"].append(sys_country)
        data_list["sys.sunrise"].append(sys_sunrise)
        data_list["sys.sunset"].append(sys_sunset)
        data_list["timezone"].append(timezone)
        data_list["id"].append(id_)
        data_list["name"].append(name)
        data_list["cod"].append(cod)

        print(i)

        time.sleep(1)

    return data_list

# def save_to_csv(weather_data, filename):
#     df = pd.DataFrame({
#         'City': [weather_data['name']],
#         'Temperature (Celsius)': [weather_data['main']['temp']],
#         'Humidity (%)': [weather_data['main']['humidity']],
#         'Description': [weather_data['weather'][0]['description']]
#     })
#     df.to_csv(filename, index=False)

def get_cord_as_list(filename):
    data_list = []
    with open(filename, 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            data_list.append(row)

    return data_list

def main():
    api_key = ''
    coordinates = get_cord_as_list("All_cites_WGS84.csv")

    # filename = 'weather_data.csv'

    weather_data = get_weather_from_all(api_key, coordinates[1:])

    df = pd.DataFrame(weather_data)

    df.to_csv(f"./data/weather_air_{datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.csv", encoding='utf-8')

    # print(weather_data)

    # if weather_data['cod'] == 200:
    #     save_to_csv(weather_data, filename)
    #     print(f"Weather data for {city} saved successfully to {filename}.")
    # else:
    #     print("City not found. Please try again.")

if __name__ == "__main__":
    main()
