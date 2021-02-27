import requests, json
import constants

api_key = constants.WEATHER_API_KEY

base_url = "https://api.openweathermap.org/data/2.5/onecall?"

# This is just doing Wake County right now but needs to be expanded
city_id = "4497286"
city_lat = "35.7900"
city_lon = "-78.6500"

complete_url = base_url + "lat=" + city_lat + "&lon=" + city_lon + "&appid=" + api_key + "&units=imperial&lang=us"

print(complete_url)

response = requests.get(complete_url) 

if response.status_code == 200:
	data = response.json()

	daily_data = data["daily"]

	weather_today = daily_data[0]

	# high temp
	high_today = int(weather_today["temp"]["max"])

	# feels like high?
	feels_like_today = int(weather_today["feels_like"]["day"])

	# get weather conditions
	conditions_today = weather_today["weather"]

	# get chance of rain
	chance_of_rain_today = weather_today["pop"]

	#get uvi today
	uvi_today = weather_today["uvi"]

	#get wind speed
	wind_today = int(weather_today["wind_speed"])

else:
	print("HTTP Error")
	there_was_an_error = 1

for s in conditions_today:
	conditions_today_int = int(s["id"])

# Is it good weather for kayaking? 
# Is the high temperature within a certain range
# and are conditions above 800 
# and is there a low chance of rain

is_it_a_good_day_to_kayak = 0

what_kind_of_day_is_it = ""

if conditions_today_int >= 800 and 54 <= high_today <= 93 and chance_of_rain_today < 15 and wind_today <= 16:
	is_it_a_good_day_to_kayak = 1
	what_kind_of_day_is_it = "It's a good day to kayak! "
else:
	print("Today is not a good day to kayak.")
	what_kind_of_day_is_it = "It's not a very good day to kayak :( "

import random

enthusiastic_words = ["a FANTASTIC", "an AMAZING", "a WONDERFUL", "a GORGEOUS", "a STUPENDOUS", "an AWESOME"]

if 800 <= conditions_today_int <= 802 and 65 <= high_today <= 85 and chance_of_rain_today < 5 and wind_today <= 10:
	is_it_a_fantastic_day_to_kayak = 1
	what_kind_of_day_is_it = "It's " + random.choice(enthusiastic_words) + " day to kayak!!! "



for s in conditions_today:
	if s["id"] == 800:
		conditions_statement = "sunny"
	elif s["id"] == 801:
		conditions_statement = "a little cloudy"
	elif s["id"] == 802:
		conditions_statement = "partly cloudy"
	elif s["id"] == 803:
		conditions_statement = "cloudy"
	elif s["id"] == 803:
		conditions_statement = "overcast"
	else:
		conditions_statement = "not ideal conditions"

high_today_statement = str(high_today) + "°. "

# describe the high temperature
if high_today <= 45:
	high_today_statement = str(high_today) + "°. It's cold! "

if 46 <= high_today <= 55:
	high_today_statement = str(high_today) + "°. Chilly. "

if 56 <= high_today <= 65:
	high_today_statement = str(high_today) + "°. Wear layers. "

if 66 <= high_today <= 68:
	high_today_statement = str(high_today) + "°. It's nice! "

if high_today == 69:
	high_today_statement = str(high_today) + "°. Nice... "

if 70 <= high_today <= 75:
	high_today_statement = str(high_today) + "°. It's nice! "

if 76 <= high_today <= 85:
	high_today_statement = str(high_today) + "°. It's warm! "

if high_today > 86:
	high_today_statement = str(high_today) + "°. Well it's a hot one... "


# Describe the wind
if wind_today <= 5:
	wind_today_statement = "There's low wind @ " + str(wind_today) + "mph. "
if 6 <= wind_today <= 9:
	wind_today_statement = "There's some wind @ " + str(wind_today) + "mph. "
if 10 <= wind_today <= 12:
	wind_today_statement = "It's a little windy @ " + str(wind_today) + "mph. "
if 13 <= wind_today <= 16:
	wind_today_statement = "It's windy @ " + str(wind_today) + "mph. "
if wind_today >= 17: 
	wind_today_statement = "It's too windy!!!"


chance_of_rain_statement = str(chance_of_rain_today) + "% chance of rain"

uv_statement = "Wear sunscreen! The UV index will be " + str(uvi_today) + ". "

feels_like_statement = "It'll feel like " + str(feels_like_today) + "°. "

weather_statement = what_kind_of_day_is_it + "In Raleigh it'll be " + conditions_statement + " with a " + chance_of_rain_statement + " and a high of " + high_today_statement + feels_like_statement + uv_statement + wind_today_statement

# print(weather_statement)
