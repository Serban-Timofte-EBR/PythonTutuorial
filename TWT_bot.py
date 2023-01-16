import tweepy
import time

#First 4 variables are have to be replace according to your dev account on Tweeter as strings

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "farming"
numberOfTweets = 4

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(400)

#Follow back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Like post which contains search string
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
