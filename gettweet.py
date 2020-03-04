import csv
import tweepy
import numpy
import apikeys


def buildTestSet(api, data, new):
    if (new ==1):
        search_keyword = data
        try:
            tweets_fetched = api.GetSearch(search_keyword, count=1000)
            print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
            return [{"text":status.text, "label":None} for status in tweets_fetched]
        except:
            print("Unfortunately, something went wrong..")
            return None


if __name__ == "__main__":

    # get credentials at developer.twitter.com
    auth = tweepy.OAuthHandler(apikeys.CONSUMER_KEY, apikeys.CONSUMER_SECRET)
    auth.set_access_token(apikeys.ACCESS_TOKEN, apikeys.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # update these for whatever tweet you want to process replies to
    name = 'elonmusk'
    tweet_id = '1231330415639552001'

    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+name, since_id=tweet_id, tweet_mode='extended', timeout=1805).items(10000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                # replies.append(tweet)
                replies += [(tweet.user.name, int(tweet.retweet_count), int(tweet.favorite_count), tweet.full_text)]

    # sorted_retweets = sorted(replies, key = lambda x: x[1], reverse=True)
    sorted_favorites = sorted(replies, key = lambda x: x[2], reverse=True)

    f = open('replies_elon_musk2.csv','w')
    csv_out=csv.writer(f)
    for row in sorted_favorites:
        csv_out.writerow(row)

