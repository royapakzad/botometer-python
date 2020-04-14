import tweepy
import csv
from tweepy import OAuthHandler
import time
import botometer
import json
import pandas

# Botometer API key authentication
mashape_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Consumer keys and access tokens, used for OAuth
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# extract twitter user A's followers 
users = tweepy.Cursor(api.followers, screen_name="RoyaPak").items()
print(users)

#save user A's follwers as CSV file
HEADER = ['screen_name']


def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(HEADER)
    count = 0
    while True:
        try:
            user = next(users)
            count = count + 1
        except tweepy.TweepError:
            time.sleep(60*20)
            user = next(users)
            print("Error happened in"+count)
        except StopIteration:
            break
        print(count)
        csv_writer.writerow(["@"+user.screen_name])
        csvfile.flush()
        time.sleep(5)

# write to a CSV file
with open('filename.csv', 'w') as csvfile:
    processing_loop(csvfile)

twitter_app_auth = {
    'consumer_key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'consumer_secret': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
    'access_token_secret': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

bom=botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key, **twitter_app_auth)
#check a sequence of accounts and their disagregated bot score
data=[]
temp=pandas.read_csv("filename.csv", header=0)
print(temp)
accounts = list(temp.screen_name)
print(accounts)
for screen_name, result in bom.check_accounts_in(accounts):
	data.append(result)
	with open("filename.json", "w") as write_file:
		json.dump(data, write_file, indent=4)
# to keep only the main score
with open('filename.json') as data_file:
    data = json.load(data_file)
for element in data:
    element.pop('categories', None)
for element in data:
    element.pop('cap', None)
for element in data:
    element.pop('scores', None)
with open('filename.json', 'w') as data_file:
    data = json.dump(data, data_file, indent=4)
