import pickle, os

def getScript():
    currentScores = open('./bbuk/housemateScores.pkl', 'rb')
    latestScores = pickle.load(currentScores)
    currentScores.close()

    formattedScores = [latestScores['arthur'], latestScores['chanelle'], latestScores['charlotte'], latestScores['deborah'], latestScores['ellie'], latestScores['hannah'], latestScores['imran'], latestScores['joe'], latestScores['kayleigh'], latestScores['kieran'], latestScores['lotan'], latestScores['mandy'], latestScores['raph'], latestScores['rebecca'], latestScores['sukhvinder'], latestScores['tom']]


    def roundup (n) :
        return 10*((n+9)//10)

    highestValue = max(formattedScores)
    graphHeight = roundup(highestValue)

    startScript = "var dataArray = " + str(formattedScores) + "; var graphHeight = " + str(graphHeight) + "; "
    endScript = """
        var svg = d3.select(".graph").append("svg")
                  .attr("height","500px")
                  .attr("width","100%")
                  .attr("position", "fixed")
                  .attr("top", "0")
                  .attr("left", "0");

        svg.selectAll("rect")
            .data(dataArray)
            .enter().append("rect")
                  .attr("class", "bar")
                  .attr("height", function(d, i) {return (500*d/graphHeight)})
                  .attr("width","52")
                  .attr("x", function(d, i) {return (i * 62) + 25})
                  .attr("y", function(d, i) {return 500 - (500*d/graphHeight)});

        svg.selectAll("text")
            .data(dataArray)
            .enter().append("text")
            .text(function(d) {return d})
                   .attr("class", "text")
                   .attr("x", function(d, i) {return (i * 62) + 41})
                   .attr("y", function(d, i) {return 520 - (500*d/graphHeight)});
        """

    return startScript + endScript
