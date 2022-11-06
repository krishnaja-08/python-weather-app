import requests
city=input("Enter the city name:")
API_KEY="Get your key from https://openweathermap.org"
url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+API_KEY 
info=requests.get(url)
res=info.json()
if(info.status_code == 200):
  temperature=res["main"]["temp"]-273.16
  weather=res["weather"][0]
  print("City name : "+city)
  print("Temperature : "+ str(round(temperature,2)) + "°C")
  print("Weather : "+weather["main"])
  print("Description : "+weather["description"])
else:
  print("Invalid city name!")