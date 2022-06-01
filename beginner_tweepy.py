# Importing Tweepy
import tweepy

# Credentials
api_key = "INSERT API KEY"
api_secret = "INSERT API KEY SECRET"
bearer_token = r"INSERT BEARER TOKEN"
access_token = "INSERT ACCESS TOKEN"
access_token_secret = "INSERT ACCESS TOKEN SECRET"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Tweeting
client.create_tweet(text="Hello World")

# Liking
client.like("Tweet id here as integer")

# Retweeting
client.retweet("Tweet id here as integer")

# Replying
client.create_tweet(in_reply_to_tweet_id="Tweet id here as integer", text="Hello user")

# Printing Home Timeline
for tweet in api.home_timeline():
    print(tweet.text)

# Printing User Timeline
person = client.get_user(username="Account name").data.id

for tweet in client.get_users_tweets(person).data:
    print(tweet.text)
