from config import consumer_api_key, consumer_api_secret_key, access_token, access_token_secret

import csv
# largely copied from tweepy's docs
import tweepy

auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

companiesTracked = ["Tesla", "Google", "Apple", "CVS Health", "Verizon", "Facebook", "Amazon", "General Motors",
                    "Chevron", "J.P. Morgan Chase"]

rawTweetFile = open("rawTweetFile.csv", 'a')
csvWriter = csv.writer(rawTweetFile)

for company in companiesTracked:

    searchTerm = company

    for tweet in tweepy.Cursor(api.search, q = searchTerm + " -filter:retweets", tweet_mode ='extended', lang = 'en').items(10):

        if tweet.in_reply_to_status_id is None:
            csvWriter.writerow([tweet.user.id, tweet.user.screen_name, tweet.user.followers_count,
                                tweet.created_at, tweet.full_text])

rawTweetFile.close()