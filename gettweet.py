import csv
import tweepy
import numpy



if __name__ == "__main__":

    # get credentials at developer.twitter.com
    auth = tweepy.OAuthHandler('SyABIQE3iEugeygKIGuLWWmSD', 'ozotNuRfw6EfMzxq50ntIE3vK7mi2qUZwB08gOXUotMCgWfg60')
    auth.set_access_token('1136359757198110727-TkXiorAxiVezilL7gfrKloMFuffwAP', 'Rsl201YVdK1dKcyh2PR75kV1hWa2GAgM6Go5aKHtGXiVJ')

    api = tweepy.API(auth, wait_on_rate_limit=True)

    # update these for whatever tweet you want to process replies to
    name = 'elonmusk'
    tweet_id = '1234791532391260160'

    replies=[]
    for tweet in tweepy.Cursor(api.search,q='to:'+name, since_id=tweet_id, tweet_mode='extended', timeout=1805).items(100):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if (tweet.in_reply_to_status_id_str==tweet_id):
                # replies.append(tweet)
                replies += [(tweet.user.name, int(tweet.retweet_count), int(tweet.favorite_count), tweet.full_text)]

    # sorted_retweets = sorted(replies, key = lambda x: x[1], reverse=True)
    sorted_favorites = sorted(replies, key = lambda x: x[2], reverse=True)

    # dt=numpy.dtype('str,int,int,str')
    # print(numpy.array(sorted_favorites,dtype=dt))

    f = open('replies.csv','w')
    csv_out=csv.writer(f)
    for row in sorted_favorites:
        csv_out.writerow(row)
