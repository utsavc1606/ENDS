import tweepy
import time
auth = tweepy.OAuthHandler("5h0pbcWgzoOldnmKpkunQaOGs","BJsKV7OEmeyr9BNNpPUPprcIWPhZsstFBsuv0MivewTYycQSBX")
auth.set_access_token("1373683584-8IJa9OsNEesDqnW0FzM9bdLU1MqFnoqb9JmWw3S", "Sp6qJVCiNThSPwQejd3dqHTtayG0R4FAt4yhIIt6Bba5m")

api = tweepy.API(auth)

for follower in api.followers_ids('uxchatterjee'):
    print api.get_user(follower).screen_name
