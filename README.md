#Muni Widget for Übersicht

This is my first attempt at writing coffescript and in creating a widget for SF Muni arrival times. At the moment, the script only allows you to enter 1 stop ID. More stop IDs will be allowed in later updates. 

##Requirements

You will need to have python installed with the [Requests Package](http://docs.python-requests.org/en/latest/).

##Instructions 

1. Register an API token here: [http://511.org/developer-resources_api-security-token_dt.asp](http://511.org/developer-resources_api-security-token_dt.asp)
2. Open *app.py*
3. Paste your token between the "" next to *token=*
4. Find the stop id for your stop: [http://transit.511.org/schedules/realtimedepartures.aspx](http://transit.511.org/schedules/realtimedepartures.aspx)
5. Paste the stop id between the "" next to *stopid=*
6. Save File

##Stops with many routes
Your stop may have more than two bus routes assigned to it. Its difficult to know the order routes will appear in so you will need to edit the index.coffee script to find your desired route. The script can parse out up to 6 routes per stop, which I have found to be the maximum number of routes per stop so far. 

If you do not see your stop appearing, you will need to edit the coffescript, index.coffee. This is easy to do. Open the script in a text editor (recommend Sublime Text 2) and find the code that looks like this: 

    $dom.find('#route').html  $abfahrt.route[0]
  	$dom.find('#direction').html  $abfahrt.direction[0]
  	$dom.find('#times').html  $abfahrt.times

Try adding a 3, 4, 5, or 6 after $abfahrt.route, $abfahrt.direction and $abfahrt.times. For example, route 4 would look like this:

	$dom.find('#route').html  $abfahrt.route4[0]
  	$dom.find('#direction').html  $abfahrt.direction4[0]
  	$dom.find('#times').html  $abfahrt.times4

The first output set of times on your desktop should change as the number changes. If you wish to change both the first and second outputs, then you will need to edit the dom.find code. For example, here is the script in the case were my desired routes are 4 and 6:

	$dom.find('#route').html  $abfahrt.route4[0]
  	$dom.find('#direction').html  $abfahrt.direction4[0]
  	$dom.find('#times').html  $abfahrt.times4

  	$dom.find('#route2').html  $abfahrt.route6[0]
  	$dom.find('#direction2').html  $abfahrt.direction6[0]
  	$dom.find('#times2').html  $abfahrt.times6







