#!/usr/bin/python3.7
# Here, if it's good weather to kayak and depending on how the river conditions are, I'll compose a tweet and tweet it
import tweepy
import constants
import weather

consumer_key = constants.TWITTER_API_KEY
consumer_secret = constants.TWITTER_API_SECRET
access_key = constants.TWITTER_ACCESS_TOKEN
access_token = constants.TWITTER_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_token)

api = tweepy.API(auth)

# # Just tweet every day for now
# api.update_status(weather.weather_statement)

if weather.is_it_a_good_day_to_kayak == 1:
	api.update_status(weather.weather_statement)
else:
	print("It's not a good day to kayak")
	# api.update_status("Today is not a good day to kayak :(")
	exit()

# api.update_status("Hello world! I am a helpful bot by @Allen_Coin that will let you know if there's good kayaking weather in the Triangle, NC area.")

# test_tweet = "I'm just seeing if I can tweet from @pythonanywhere... The high today is " + str(weather.high_today) + "°. The weather today is " + str(weather.conditions_statement) + ".\r\nYours truly, \r\n🛶🤖"

# # print(test_tweet)

# api.update_status(test_tweet)