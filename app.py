#!/usr/bin/python

import xml.etree.cElementTree as ET
import requests
import json
import xml.dom.minidom

token = "PASTE TOKEN HERE"
stopid = "PASTE STOP ID HERE"

url = "http://services.my511.org/Transit2.0/GetNextDeparturesByStopCode.aspx?token="+token+"&Muni&stopCode="+stopid

response = requests.get(url)

root = ET.fromstring(response.content)

items = {}

route=""
route2=""
route3=""
route4=""
route5=""
route6=""

direction=""
direction2=""
direction3=""
direction4=""
direction5=""
direction6=""

times = []
times2 = []
times3 = []
times4 = []
times5 = []
times6 = []

route_track = 0

for child in root: 
	for child2 in child: 
		for child3 in child2: 
			for child4 in child3:
				route_track += 1
				if route_track == 1:
					route = child4.attrib['Name']
				elif route_track == 2:
					route2 = child4.attrib['Name']
				elif route_track == 3:
					route3 = child4.attrib['Name']
				elif route_track == 4:
					route4 = child4.attrib['Name']
				elif route_track == 5:
					route5 = child4.attrib['Name']
				elif route_track == 6:
					route6 = child4.attrib['Name']
				for child5 in child4:
					for child6 in child5:
						if route_track == 1:
							direction = child6.attrib['Name']
						elif route_track == 2:
							direction2 = child6.attrib['Name']
						elif route_track == 3:
							direction3 = child6.attrib['Name']
						elif route_track == 4:
							direction4 = child6.attrib['Name']
						elif route_track == 5:
							direction5 = child6.attrib['Name']
						elif route_track == 6:
							direction6 = child6.attrib['Name']
						for child7 in child6:
							for child8 in child7:
								for child9 in child8:
									for child10 in child9:
										if route_track == 1:
											times.append(child10.text)
										elif route_track == 2:
											times2.append(child10.text)
										elif route_track == 3:
											times3.append(child10.text)
										elif route_track == 4:
											times4.append(child10.text)
										elif route_track == 5:
											times5.append(child10.text)
										elif route_track == 6:
											times6.append(child10.text)

									if route_track == 1:
										items["route"] = route,
										items["direction"] = direction,
										items["times"] = ', '.join(times)

									elif route_track == 2:
										items["route2"] = route2,
										items["direction2"] = direction2,
										items["times2"] = ', '.join(times2)
										if len(items["times2"]) <1:
											items["times2"] = "No Times :("

									elif route_track == 3:
										items["route3"] = route3,
										items["direction3"] = direction3,
										items["times3"] = ', '.join(times3)
										if len(items["times3"]) <1:
											items["times24"] = "No Times :("

									elif route_track == 4:
										items["route4"] = route4,
										items["direction4"] = direction4,
										items["times4"] = ', '.join(times4)
										if len(items["times4"]) <1:
											items["times4"] = "No Times :("

									elif route_track == 5:
										items["route5"] = route5,
										items["direction5"] = direction5,
										items["times5"] = ', '.join(times5)
										if len(items["times5"]) <1:
											items["times5"] = "No Times :("

									elif route_track == 6:
										items["route6"] = route6,
										items["direction6"] = direction6,
										items["times6"] = ', '.join(times6)
										if len(items["times6"]) <1:
											items["times6"] = "No Times :("

print json.dumps(items)







