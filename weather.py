import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=09a603f4f54413c362fedf1a41187277")

        except:
            print("Whoops! No internet!")

        self.response_json = response.json()

        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        print(f"In {self.name}, it is currently {self.temp} C°")
        print(f"Today's high: {self.temp_max} C°" )
        print(f"Today's low: {self.temp_min} C°" )


my_city = City("Dhaka", 23.777176, 	90.399452)
my_city.temp_print()

vacation_city = City("Minneapolis", 44.9778, -93.2650)
vacation_city.temp_print()