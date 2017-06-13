import pickle, os
import settings

def housemateScoreAdjuster(name, sentiment):


    if os.path.isfile('housemateScores.pkl') == False: #check if pickle file exists & create if false
        createScores = open('housemateScores.pkl', 'wb')
        pickle.dump(settings.CONTESTANTS, createScores)
        createScores.close()

        if sentiment == 'neg':

            #retreive current scores
            currentScores = open('housemateScores.pkl', 'rb')
            scores = pickle.load(currentScores)
            currentScores.close()

            #adjust values
            scores[name] += 1

            #save new scores
            newScores = open('housemateScores.pkl', 'wb')
            pickle.dump(scores, newScores)
            newScores.close()
    else:
        if sentiment == 'neg':

            #retreive current scores
            currentScores = open('housemateScores.pkl', 'rb')
            scores = pickle.load(currentScores)
            currentScores.close()

            #adjust values
            scores[name] += 1

            #save new scores
            newScores = open('housemateScores.pkl', 'wb')
            pickle.dump(scores, newScores)
            newScores.close()