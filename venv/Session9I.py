import requests as rq
resposne = rq.get("https://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22")
print(resposne.text)


# https://openweathermap.org/current