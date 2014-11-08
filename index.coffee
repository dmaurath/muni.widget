command: "python ./muni.widget/app.py"

refreshFrequency: 20000

style: """
  top: 6%
  left: 10%
  padding: 10
  margin: 0 0 0 -100px
  font-family: Helvetica Neue
  color: #fff

  #route
    border-bottom: 1px solid white
    margin: 0
    font-weight: 200

  #direction
    margin: 0
    text-transform: uppercase
    font-size: 80%
    font-weight: 200
  
  #times
    margin: 0
    border-bottom: 0px

  #route2
    border-bottom: 1px solid white
    margin: 0
    font-weight: 200

  #direction2
    margin: 0
    font-size: 80%
    text-transform: uppercase
    font-weight: 200
  
  #times2
    margin: 0
    border-bottom: 0px
"""
render: (output) -> """
    <h2 id = "route"></h1>
    <br>
    <h2 id = "direction"></h2>
    <br>
    <h1 id = "times"></h3>
    <br>
    <h2 id = "route2"></h1>
    <br>
    <h2 id = "direction2"></h2>
    <br>
    <h1 id = "times2"></h3>
"""

update: (output, domEl) ->

  $dom = $(domEl)

  $abfahrt = JSON.parse(output)

  $dom.find('#route').html  $abfahrt.route[0]
  $dom.find('#direction').html  $abfahrt.direction[0]
  $dom.find('#times').html  $abfahrt.times

  $dom.find('#route2').html  $abfahrt.route2[0]
  $dom.find('#direction2').html  $abfahrt.direction2[0]
  $dom.find('#times2').html  $abfahrt.times2






