import requests
import matplotlib.pyplot as pt
import json
import csv
import datetime
import regression
import os

from dotenv import load_dotenv




class Temperature:
    def __init__(self,key):
        self.today=datetime.date.today()
        self.key=key

    
    def temp_details_today(self,latitude=None, longitude=None, city=None):
        if city:
            link=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}&units=metric"
        else:
            link=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.key}&units=metric"
        
        response=requests.get(url=link)
        a=json.loads(response.text)
        desc=a["weather"][0]["main"]
        temp_min=a["main"]["temp_min"]
        temp_max=a["main"]["temp_max"]
        curr_temp=a["main"]["temp"]
        humidity=a["main"]["humidity"]
        division=a["name"]

        data=[
        {"division":division,"date":datetime.date.today(),"desc":desc,"temp":curr_temp,"temp_min":temp_min,"temp_max":temp_max,"humidity":humidity}
        ]
        with open("file1.csv","a", newline="") as csvfile:
            fieldnames=["division","date","desc","temp","temp_min","temp_max","humidity"]
            # writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerows(data)
        
        return data

    def temp_details_past7days(self,latitude,longitude):
        past=self.today - datetime.timedelta(days=7)
        url=f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={past}&end_date={self.today}&daily=temperature_2m_max,temperature_2m_min"
        response=requests.get(url=url)
        a=json.loads(response.text)
        print(a)
        day_list=a["daily"]["time"]
        temp_max=a["daily"]["temperature_2m_max"]
        temp_min=a["daily"]["temperature_2m_min"]

        return (day_list,temp_max,temp_min)

    def plot_graph_7days(self,day_list,temp_max_list,temp_min_list):

    
        pt.plot(day_list,temp_max_list, label="MAX_TEMPERATURE")
        pt.plot(day_list,temp_min_list, label="MIN_TEMPERATURE")
        pt.xlabel("DAY")
        pt.ylabel("TEMP")
        pt.title("Weather_trends")
        pt.legend()
        pt.xticks(rotation=45, fontsize=8)
        pt.show()
    
    def plot_temp_humidity_today(self):
        pass

    def predict_temp(self,temp):

        value=regression.predict(temp)
        return value


key=os.getenv("API_KEY")

obj=Temperature(key)


while True:

    print("Welcome to the weather application")
    print("What would you like to do")



    print("""
    ╔══════════════════════════════════════════════╗
    ║            WEATHER ANALYTICS                 ║
    ╠══════════════════════════════════════════════╣
    ║  1. Today's Weather                          ║
    ║  2. Past 7 Days Weather                      ║
    ║  3. Temperature Trend Graph                  ║
    ║  4. Predict Future Temperature               ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """)

#     print(
        
#         '''
#         1. SHOW TODAYS WEATHER DETAILS
#         2. SHOW PAST 7 DAYS WEATHER DETAILS
#         3. PLOT GRAPH FOR PAST 7 DAYS WEATHER
#         4. PREDICT TEMPERATURE BASED ON PAST DATA 

# '''
#     )
    val=int(input("ENTER YOUR CHOICE"))

    match val:

        case 1:
            print("TYPE 1 TO PROVIDE CITY NAME, TYPE 2 TO PROVIDE COORDINATES")
            choice=int(input("ENTER CHOICE "))
            city_name=None
            if choice == 1:
                city_name=input("ENTER CITY NAME ")
            elif choice == 2:
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            else:
                
                raise Exception("INVALID INPUT")
            
            if city_name:
                x=obj.temp_details_today(city=city_name)
            else:
                x=obj.temp_details_today(latitude=latitude, longitude=longitude)
            print(x)
        
        case 2:

            print("TYPE 1 TO PROVIDE CITY NAME, TYPE 2 TO PROVIDE COORDINATES")
            choice=int(input("ENTER CHOICE "))
            city_name=None
            if choice == 1:
                city_name=input("ENTER CITY NAME ")
            elif choice == 2:
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            else:
                
                raise Exception("INVALID INPUT")
            

            if city_name:
                geourl=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={key}"

                response=requests.get(url=geourl)
                alpha=response.json()
                name=alpha[0]["name"]
                latitude=alpha[0]["lat"]
                longitude=alpha[0]["lon"]
            
            else:
           
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            tup=obj.temp_details_past7days(latitude=latitude, longitude=longitude)
            x=len(tup[0])
            for i in range(x):
                print("day",tup[0][i])
                print("max temperature",tup[1][i])
                print("min temperature",tup[2][i], end="\n\n")

        
        case 3:

            print("TYPE 1 TO PROVIDE CITY NAME, TYPE 2 TO PROVIDE COORDINATES")
            choice=int(input("ENTER CHOICE "))
            city_name=None
            if choice == 1:
                city_name=input("ENTER CITY NAME ")
            elif choice == 2:
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            else:
                
                raise Exception("INVALID INPUT")
            

            if city_name:
                geourl=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={key}"

                response=requests.get(url=geourl)
                alpha=response.json()
                name=alpha[0]["name"]
                latitude=alpha[0]["lat"]
                longitude=alpha[0]["lon"]
            
            else:
           
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            
            tup=obj.temp_details_past7days(latitude=latitude, longitude=longitude)

            obj.plot_graph_7days(tup[0],tup[1],tup[2])
        

        case 4:


            print("TYPE 1 TO PROVIDE CITY NAME, TYPE 2 TO PROVIDE COORDINATES")
            choice=int(input("ENTER CHOICE "))
            city_name=None
            if choice == 1:
                city_name=input("ENTER CITY NAME ")
            elif choice == 2:
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))
            else:
                
                raise Exception("INVALID INPUT")
            

            if city_name:
                geourl=f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={key}"

                response=requests.get(url=geourl)
                alpha=response.json()
                name=alpha[0]["name"]
                latitude=alpha[0]["lat"]
                longitude=alpha[0]["lon"]
            
            else:
           
                latitude=float(input("ENTER LATITUDE "))
                longitude = float(input("ENTER LONGITUDE "))

            tup=obj.temp_details_past7days(latitude=latitude, longitude=longitude)
            print("CHOOSE 1 MAX TEMPERATURE PREDICTION AND 2 FOR MIN TEMPERATURE PREDICTION")
            choice=int(input("enter choice" ))
        
            if choice ==1:
                val=obj.predict_temp(tup[1])
            elif choice ==2:
                val=obj.predict_temp(tup[2])
            else:
                raise Exception("INVALID CHOICE")
            print(val)

        case _:
            print("INVALID CHOICE")
            break


            


        
       




        