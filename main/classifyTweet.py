import tweetProcessor, pickle
import settings

def classifier(tweet):

    with open('savedNBClassifier.pkl', 'rb') as f:
        NBClassifier = pickle.load(f)

    processedTestLine = tweetProcessor.formatTweet(tweet)
    result = NBClassifier.classify(tweetProcessor.extract_features(tweetProcessor.getFeatureVector(processedTestLine)))
    return result

#check to see if the tweet mentions one of the contestants
def checkForContestant(tweet):
    contestantFound = 0
    formattedTweet = tweetProcessor.formatTweet(tweet)
    tweetWords = formattedTweet.split()

    for name in settings.CONTESTANTS.keys():
        if name in tweetWords:
            contestantFound = 1
            return name
    if contestantFound == 0:
        noName = 'No name'
        return noName