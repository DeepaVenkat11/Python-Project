import requests

#Using this datas we can finf out a temperature of a city
class City():
    def __init__(self,city,lat,lon,units="metric") :
        self.city = city
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=b70b58deeb323f2f77a7448d3e919365")
        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_max = response_json["main"]["temp_max"]
        self.temp_min = response_json["main"]["temp_min"]
     
    def temp_print(self):
        print(f"The current temperature of {self.city} is {self.temp}° C\n")

my_city = City("Jummu Kashmir",33.2778,75.3412)
my_city.temp_print()

#33.2778° N, 75.3412° E