from bokeh.plotting import curdoc, figure
from bokeh.client import push_session
from bokeh.embed import autoload_server
import pandas as pd
import sys
sys.path.append("../")
import settings
import pickle, os

# ---------- Setup & design bokeh plot ----------

housemates = ['arthur', 'chanelle', 'charlotte', 'deborah', 'ellie', 'hannah', 'imran', 'joe', 'kayleigh', 'kieran', 'lotan', 'mandy', 'raph', 'rebecca', 'sukhvinder', 'tom']

p = figure(title="Number of Negative Tweets Per Housemate", x_range=housemates, y_range=(0, 50), toolbar_location=None, plot_width=900, plot_height=500)
p.border_fill_color = 'white'
p.background_fill_color = '#0099ff'
p.outline_line_color = 'black'
p.outline_line_width = 7
p.grid.grid_line_color = None
p.yaxis.axis_label = 'Number of Negative Tweets'
p.xaxis.axis_label = 'BB Housemates'

r = p.quad(left=[], right=[], top=[], bottom=[], color="#f9027d", line_width=6, line_color='black')

ds = r.data_source    

session = push_session(curdoc())
script = autoload_server(p, session_id=session.id) # This produces the script that can be embeded into html
print(script)

def update(): # Stuff to update in the plot
    new_data = dict()
    
    lefts = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] # Points on the x-axis of the plot where a new bar starts
    new_data['left'] = [start-0.25 for start in lefts] 
    new_data['right'] = [start+0.5 for start in new_data['left']]
    os.chdir('../sentimentClassifier')
    if os.path.isfile('./housemateScores.pkl') == False: # Check if pickle file exists & create if false
        createScores = open('housemateScores.pkl', 'wb')
        pickle.dump(settings.CONTESTANTS, createScores)
        createScores.close()
    
    currentScores = open('housemateScores.pkl', 'rb')
    scores = pickle.load(currentScores)
    currentScores.close()
    
    arthur = scores['arthur']
    chanelle = scores['chanelle']
    charlotte = scores['charlotte']
    deborah = scores['deborah']
    ellie = scores['ellie']
    hannah = scores['hannah']
    imran = scores['imran']
    joe = scores['joe']
    kayleigh = scores['kayleigh']
    kieran = scores['kieran']
    lotan = scores['lotan']
    mandy = scores['mandy']
    raph = scores['raph']
    rebecca = scores['rebecca']
    sukhvinder = scores['sukhvinder']
    tom = scores['tom']
    
    new_data['top'] = [0, arthur, chanelle, charlotte, deborah, ellie, hannah, imran, joe, kayleigh, kieran, lotan, mandy, raph, rebecca, sukhvinder, tom] # The extra zero, for some reason, shifts the bars to where they are supposed to be
    new_data['bottom'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print('new data: ', new_data)
    ds.data = new_data
    
curdoc().add_periodic_callback(update, 5000) # Update the graph every 5000ms ... aka every 5 seconds
session.show(p)
session.loop_until_closed()