from config import consumer_api_key, consumer_api_secret_key, access_token, access_token_secret

import csv
import tweepy

# twitter authorization stuff
auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# these are our search terms
companiesTracked = ["Tesla", "Google", "Apple", "CVS Health", "Verizon", "Facebook", "Amazon", "General Motors",
                    "Chevron", "J.P. Morgan Chase"]

# csv file will track all our raw data
rawTweetFile = open("rawTweetFile.csv", 'a')
csvWriter = csv.writer(rawTweetFile)

# searches for tweets related to each corporation we're tracking
for company in companiesTracked:

    searchTerm = company

    # records raw tweets and other data in our rawTweetFile
    for tweet in tweepy.Cursor(api.search, q = searchTerm + " -filter:retweets", tweet_mode ='extended', lang = 'en').items(10):
        # makes sure a tweet isn't a reply to some other tweet
        if tweet.in_reply_to_status_id is None:
            csvWriter.writerow([tweet.user.id, tweet.user.screen_name, tweet.user.followers_count,
                                tweet.created_at, tweet.full_text])

rawTweetFile.close()