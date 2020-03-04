import csv
import tweepy
import numpy
import apikeys


def tweetBySearch(api, search_keyword):

    replies = []
    for tweet in tweepy.Cursor(api.search,q=search_keyword, tweet_mode='extended', timeout=1805).items(500):
        if hasattr(tweet, 'full_text'):
            if (search_keyword in tweet.full_text):
                # replies.append(tweet)
                replies += [(tweet.user.name, int(tweet.retweet_count), int(tweet.favorite_count), tweet.full_text)]

    return replies


if __name__ == "__main__":

    # get credentials at developer.twitter.com
    auth = tweepy.OAuthHandler(apikeys.JENNY_CONSUMER_KEY, apikeys.JENNY_CONSUMER_SECRET)
    auth.set_access_token(apikeys.JENNY_ACCESS_TOKEN, apikeys.JENNY_ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # change this value to search for different keyword(s)
    keyword = "Cloud Computing"
    replies = tweetBySearch(api, keyword)

    # sorted_retweets = sorted(replies, key = lambda x: x[1], reverse=True)
    sorted_favorites = sorted(replies, key = lambda x: x[2], reverse=True)

    f = open('tweetsearches/cloud_computing2.csv','w')
    csv_out=csv.writer(f)
    for row in sorted_favorites:
        csv_out.writerow(row)
