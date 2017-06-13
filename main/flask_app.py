from string import Template
from flask import Flask
import pickle, os, getGraphScript
import settings

MAIN_TEMPLATE = Template("""
    <head>
        <script type="text/javascript" src="/static/d3.min.js"></script>
        <meta charset="utf-8">
    <style>

    body {
        background: #59b8ba;
    }

    #BBpost {
        margin: 0 auto;
    }

    .graph {
        position:relative;
        top: 700px;
        margin: 0 auto;
        width: 1030px;
        height: 550px;
        background: #0080FF;
        border-style: solid;
        border: dotted 5px;
        border-color: black;
        margin-bottom:25px;
    }

    #housemateArea {
        position: relative;
        bottom: 10px;
        height: 20px;
        width: 100%;
    }

    .housemate {
        position: absolute;
        top: 15px;
        color: white;
        font-size: 13px;
    }

    /*Rectangle bar class styling*/

    .bar {
      fill: #f9027d;
      stroke: black;
      stroke-width: 5;
    }

    .bar:hover {
      fill: #a82d42;
    }

    /*Text class styling*/

    .text {
      fill: white;
      font-family: sans-serif;
    }

    </style>

    </head>

    <body>
        <div id='header' style="position:absolute; width:100%; background:#59b8ba;">
            <img src='/static/intro.png' style="position:absolute; width:600px; top:20px; right:60px"/>
            <a href="http://www.lamartalkscode.com/"><img src='/static/visit_blog.png' style="position:relative; width:500px; top:20px; left:20px;"/></a>
            <a href="https://twitter.com/_lamjo"><img src='/static/visit_twitter.png' style="position:absolute; width:500px; top:300px; left:20px"/></a>
        </div>

        <p style="text-align:center; margin: 50px; position:absolute; top:470px;">
            <span style="font-size: 25pt; color:white;">This graph keeps track of how many negative tweets each of the housemates are receiving. Refresh the page to update the graph. I will set the scores back to zero after every live eviction (with a bit of a lag since I live in Canada and can’t watch the live version).</span>
        </p>

        <div class="graph">
            <script>${graph_script}</script>
            <div id='housemateArea'>
                <div class='housemate' id='Arthur' style='left: 30px;'><strong>Arthur</strong></div>
                <div class='housemate' id='Chanelle' style='left: 88px;'><strong>Chanelle</strong></div>
                <div class='housemate' id='Charlotte' style='left: 145px;'><strong>Charlotte</strong></div>
                <div class='housemate' id='Deborah' style='left: 210px;'><strong>Deborah</strong></div>
                <div class='housemate' id='Ellie' style='left: 285px;'><strong>Ellie</strong></div>
                <div class='housemate' id='Hannah' style='left: 335px;'><strong>Hannah</strong></div>
                <div class='housemate' id='Imran' style='left: 405px;'><strong>Imran</strong></div>
                <div class='housemate' id='Joe' style='left: 475px;'><strong>Joe</strong></div>
                <div class='housemate' id='Kayleigh' style='left: 520px;'><strong>Kayleigh</strong></div>
                <div class='housemate' id='Kieran' style='left: 590px;'><strong>Kieran</strong></div>
                <div class='housemate' id='Lotan' style='left: 655px;'><strong>Lotan</strong></div>
                <div class='housemate' id='Mandy' style='left: 715px;'><strong>Mandy</strong></div>
                <div class='housemate' id='Raph' style='left: 780px;'><strong>Raph</strong></div>
                <div class='housemate' id='Rebecca' style='left: 835px;'><strong>Rebecca</strong></div>
                <div class='housemate' id='Sukhvinder' style='left: 890px;'><strong>Sukhvinder</strong></div>
                <div class='housemate' id='Tom' style='left: 970px;'><strong>Tom</strong></div>
            </div>
            <p style="text-align:left; position:relative; bottom:10px; left:5px">
                <span style="font-size:15pt;"><strong>Graph started collecting tweets: </strong>${date}</span>
            </p>
        </div>

        <center><img src="/static/accuracy2.png" style="width:95%; position:relative; top:700px;"></center>
    </body>
""")
app = Flask(__name__)

@app.route('/')
def homepage():
    if os.path.isfile('housemateScores.pkl') == False: #check if pickle file exists & create if false
        createScores = open('housemateScores.pkl', 'wb')
        pickle.dump(settings.CONTESTANTS, createScores)
        createScores.close()
    startDate = '5:55 PM Sunday, June 11, 2017 (EDT)'
    graphScript = getGraphScript.getScript()

    return MAIN_TEMPLATE.substitute(date=startDate, graph_script=graphScript)

if __name__ == '__main__':
    
    app.run(debug=True, use_reloader=True)