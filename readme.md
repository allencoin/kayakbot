# About

This is a Twitter bot that will check weather conditions in the Triangle, NC area once a day and tweet if it's a good day for kayaking. 

https://twitter.com/BotKayak

Right now, it's just pulling in local weather data for Raleigh. 

This bot currently (or will) ingest data from **Open Weather API** and the **United States Geologic Survey API**. 

## TODO:

- Expand to Durham and Orange counties
- Pull in water level data using the US Geologic Survey's API to get information about river conditions
- Include information about river conditions, or just recommend to stick to lakes. 
- If it's a bad day for kayaking, look ahead to tomorrow and tweet if tomorrow's conditions are favorable
- Maybe explore generating an image to include with the tweet that has additional information

## DON'T:

- Go chasing waterfalls

## Tutorial

If you want to clone this and set it up on your own: 

1. Add a file called `constants.py` and add the following: 

```
WEATHER_API_KEY = "YOUR TOKEN HERE"
TWITTER_API_KEY = "YOUR TOKEN HERE"
TWITTER_API_SECRET = "YOUR TOKEN HERE"
TWITTER_ACCESS_TOKEN = "YOUR TOKEN HERE"
TWITTER_TOKEN_SECRET = "YOUR TOKEN HERE"
```

2. Get your Weather API from https://openweathermap.org/api
3. Get your Twitter API key by applying for a Twitter Developer account at https://developer.twitter.com then follow the [API documentation](https://developer.twitter.com/en/docs/getting-started)
4. Change `city_id` and `city_lat`/`city_lon` in `weather.py` for your local area. 
5. Deploy to Python Anywhere https://www.pythonanywhere.com/
6. ???
7. Profit! 