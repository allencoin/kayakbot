# Here, if it's good weather to kayak and depending on how the river conditions are, I'll compose a tweet and tweet it
import tweepy
import constants
import weather

# if weather.is_it_a_good_day_to_kayak == 1:
# 	print("Let's tweet!")
# else:
# 	print("It's not a good day to kayak. No tweet for you!")

consumer_key = constants.TWITTER_API_KEY
consumer_secret = constants.TWITTER_API_SECRET
access_key = constants.TWITTER_ACCESS_TOKEN
access_token = constants.TWITTER_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_token)

api = tweepy.API(auth)

api.update_status(weather.weather_statement)