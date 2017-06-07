# BBUKEvictionPredictor 2.0
A program that uses twitter sentiment analysis to predict the next contestant to be evicted on Celebrity Big Brother UK.

Program Rundown
- The program collects recent past tweets based on a tag (e.g., BBUK (Big Brother UK), CBB (Celebrity Big Brother))
- It then uses lists of positive and negative words to model a sentiment analyzer
- The sentiment analyzer keeps a tally of the negative tweets directed at each individual housemate
- The housemate with the highest number of negative tweets is supposed to be the next houseguest to get evicted

Sentiment Analyzer Versions
- I first tried using the nltk sentiment analyzer to categorize the tweets however this led to a lot of false negatives
- I then used a rule-based sentiment analyzer, which draws upon precategorized lists of positive and negative words.  This turned out to be a lot more reliable.

# ---------- Commands to run simultaneously in the terminal ----------

    #bokeh serve --allow-websocket-origin=www.lamartalkscode.com
    #python vizzer.py
    #python tweetStreamer.py