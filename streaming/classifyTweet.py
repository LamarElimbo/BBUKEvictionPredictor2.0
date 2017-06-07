import re, nltk, csv, codecs, tweetProcessor, pickle, os
import sys
sys.path.append("../")
import settings

def classifier(tweet):
    os.chdir('../sentimentClassifier')
    with open('savedNBClassifier.pkl', 'rb') as f:
        NBClassifier = pickle.load(f)
        
    processedTestLine = tweetProcessor.formatTweet(tweet)
    result = NBClassifier.classify(tweetProcessor.extract_features(tweetProcessor.getFeatureVector(processedTestLine)))
    print('Tweet: ', tweet)
    print('Classifier: ', result)
    return result
    
#check to see if the tweet mentions one of the contestants
def checkForContestant(tweet):
    contestantFound = 0
    
    tweetWords = tweet.split()
    
    for name in settings.CONTESTANTS.keys():
        if name in tweetWords:
            contestantFound = 1
            print('Housemate: ', name)
            return name
    if contestantFound == 0:
        noName = 'No name'
        return noName