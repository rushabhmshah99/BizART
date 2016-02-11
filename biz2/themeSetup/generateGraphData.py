import csv


months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def readFlightData():	
	data = []
	with open('data/flightData.csv', 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        data.append(row)

	#print len(data)
	return data

def calcRevenueWithinTime(year, month=-1):

	data = readFlightData()
	data2 = [0]*(len(data)+1)
	rownum = 0
	with open('data/passengers_plane.csv', 'rb') as f:
	    reader = csv.reader(f) 
	    for row in reader:

	    	if rownum != 0:
	    		#print eval(row[1])+1
		    	if row[2] == 'Economy':
		    		rev = data[eval(row[1])][7]
		    	if row[2] == 'Business':
		    		rev = data[eval(row[1])][8]
		    	if row[2] == 'First Class':
		    		rev = data[eval(row[1])][9]
		    	data2[eval(row[1])] += eval(rev)
	    	rownum +=1

	
	for x in xrange(1, len(data2)-1):
		data2[x] = data2[x] - eval(data[x][10]) - eval(data[x][11]) - eval(data[x][12])
	#print data2
	#print len(data2)
	rev2 = 0
	for el in xrange(1, len(data)-1):
		str1 = data[el][1].split(" ")
		date = str1[0].split("-")
		if (int(date[0]) == year and month == 0) or (int(date[0]) == year and int(date[1]) == month):
			rev2 += data2[el]
	if month == -1:
		print "Revenue for "+str(year)+ " is "+str(rev2)
	else:
		print "Revenue for "+months[month]+", "+str(year)+ " is "+str(rev2)
	return rev2      
#calcRevenueWithinTime(2014)

def populateFlights():
	data  = readFlightData()
	data2 = [0]*(len(data)+1)
	rownum = 0
	with open('data/passengers_plane.csv', 'rb') as f:
	    reader = csv.reader(f) 
	    for row in reader:

	    	if rownum != 0:
	    		#print eval(row[1])+1
		    	if row[2] == 'Economy':
		    		rev = data[eval(row[1])][7]
		    	if row[2] == 'Business':
		    		rev = data[eval(row[1])][8]
		    	if row[2] == 'First Class':
		    		rev = data[eval(row[1])][9]
		    	data2[eval(row[1])] += eval(rev)
	    	rownum +=1

	for x in xrange(1, len(data2)-1):
		data2[x] = data2[x] - eval(data[x][10]) - eval(data[x][11]) - eval(data[x][12])
	loss_flight,profit_flight = [],[]

	for i in xrange(1, len(data2)-1):
		if data2[i] < 0:
			loss_flight.append(data[i])
		else:
			profit_flight.append(data[i])

	return loss_flight, profit_flight


def generateResult(dates):
	months = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
	months2 = ['', 'jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']
	print dates
	dates = dates[1:len(dates)-1]
	dates = dates.split(",")
	print dates
	month1 , month2 = 0,0
	if dates[0] in months:
		month1 = months.index(dates[0])
	elif dates[0] in months2:
		month1 = months2.index(dates[0])
	if dates[2] in months:
		month2 = months.index(dates[2])
	elif dates[2] in months2:
		month2 = months2.index(dates[2])

	rev1 = calcRevenueWithinTime(int(dates[1]), month1)
	rev2 = calcRevenueWithinTime(int(dates[3]), month2)
	data = [ [months[month1]+" "+str(dates[1]), rev1], [months[month2]+" "+str(dates[3]), rev2]]
	print data
	#content = '<script>alert("Hi");</script>'
	content = '<div id="barchart_material" style="width: 900px; height: 500px; margin:0 auto" align="center"></div>'
	
	content += '<script type="text/javascript">google.charts.load("current", {"packages":["bar"]}); google.charts.setOnLoadCallback(drawChart);function drawChart() {    	var query = '+str(data)+';    var data = new google.visualization.DataTable();  		data.addColumn("string", "Years");  		data.addColumn("number", "Revenue");  		for(i = 0; i < query.length; i++)   	{	 data.addRow([query[i][0], query[i][1]]);     }   var options = {          chart: {            title: "Company Performance",                      },             };        var chart = new google.charts.Bar(document.getElementById("barchart_material"));        chart.draw(data, options);      }    </script> '
	
	return content

def generateProfitLossTable(data):
	loss_flight,profit_flight = populateFlights()
	a=[]
	data = data[1:len(data)-1]
	if data == "loss":
		a = loss_flight
	elif data == "profit":
		a = profit_flight
	content = '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title"><i class="icon-table"></i> Default datatable inside panel</h6></div><div class="datatable"><table class="table"><thead><tr><th>Plane Id</th><th>Source Country</th><th>Source State</th><th>Destination Country</th><th>Destination State</th><th>Halt</th></tr></thead><tbody>'
   	for l in a:
	   	plane_id = l[0]
	   	source_country = l[2]
	   	source_state = l[3]
	   	dest_country = l[4]
	   	dest_state = l[5]
	   	halt = l[13]
	   	temp = '<tr><td>'+plane_id+'</td><td>'+source_country+'</td><td>'+source_state+'</td><td>'+dest_country+'</td><td>'+dest_state+'</td><td>'+halt+'</td></tr>'
	   	content = content + temp
   	content = content + '</tbody></table></div></div>'
   	return content