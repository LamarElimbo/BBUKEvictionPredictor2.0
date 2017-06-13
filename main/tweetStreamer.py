import tweepy, dataset, twitter_creds, classifyTweet, scoreAdjuster
import settings

db = dataset.connect(settings.CONNECTION_STRING)

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):

        text = status.text
        housemate = classifyTweet.checkForContestant(text)
        if housemate == 'No name':
            sentiment = 'NA'
        else:
            sentiment = classifyTweet.classifier(text)
            scoreAdjuster.housemateScoreAdjuster(housemate, sentiment)


        table = db[settings.TABLE_NAME]
        infoDict = dict(
                text=text,
                housemate=housemate,
                sentiment=sentiment,
            )

        table.insert(infoDict)


    def on_error(self, status_code):
        if status_code == 420:
            return False

auth = tweepy.OAuthHandler(twitter_creds.TWITTER_APP_KEY, twitter_creds.TWITTER_APP_SECRET)
auth.set_access_token(twitter_creds.TWITTER_KEY, twitter_creds.TWITTER_SECRET)
api = tweepy.API(auth)

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=settings.TRACK_TERMS)