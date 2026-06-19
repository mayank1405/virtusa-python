import requests
import datetime
import json
import matplotlib.pyplot as pt
# latitude=28.7417
# longitude=77.1126
# today_date=datetime.date.today()
# past=datetime.date.today() - datetime.timedelta(days=7)
# url=f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={past}&end_date={today_date}&daily=temperature_2m_max,temperature_2m_min"
# response=requests.get(url=url)
# print(response.text)
# a=json.loads(response.text)
# days=a["daily"]["time"]
# temp_max=a["daily"]["temperature_2m_max"]
# temp_min=a["daily"]["temperature_2m_min"]

# pt.plot(days,temp_max, label="MAX_TEMPERATURE")
# pt.plot(days,temp_min, label="MIN_TEMPERATURE")
# pt.xlabel("DAY")
# pt.ylabel("TEMP")
# pt.title("Weather_trends")
# pt.legend()
# pt.xticks(rotation=45, fontsize=8)
# pt.show()

city_name="DELHI"
key="b7345dfbf754f3bd086b3f23ecb99a23"
geourl=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={key}"

response=requests.get(url=geourl)
a=response.json()
name=a[0]["name"]
latitude=a[0]["lat"]
longitude=a[0]["lon"]
print(f"{name}, {latitude}, {longitude}")
print(type(longitude))