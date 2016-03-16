import csv
import datetime

months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def readFlightData(fileName):	
	data = []
	with open(fileName, 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        data.append(row)

	#print len(data)
	return data

def calcRevenueWithinTime(year, month=-1):

	data = readFlightData("data/flightData.csv")
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
	data  = readFlightData("data/flightData.csv")
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
	content = '<div id="barchart_values" style="width: 900px; height: 500px; margin:0 auto" align="center"></div>'
	
	#content += '<script type="text/javascript">google.charts.load("current", {"packages":["bar"]}); google.charts.setOnLoadCallback(drawChart);function drawChart() {    	var query = '+str(data)+';    var data = new google.visualization.DataTable();  		data.addColumn("string", "Years");  		data.addColumn("number", "Revenue");  	   	for(i = 0; i < query.length; i++)   	{	 data.addRow([query[i][0], query[i][1]]);     } var options = {            animation:{          startup: true,        duration: 1000,        easing: "out",      },     chart: {            title: "Company Performance",                      },             };        var chart = new google.charts.Bar(document.getElementById("barchart_material"));        chart.draw(data, options);     }    </script> '
	content += '<script type="text/javascript">    google.charts.load("43", {packages:["corechart"]});    google.charts.setOnLoadCallback(drawChart);    function drawChart() {  var query = '+str(data)+'; var data = new google.visualization.DataTable();      data.addColumn("string", "Years");      data.addColumn("number", "Revenue");        for(i = 0; i < query.length; i++)     {  data.addRow([query[i][0], query[i][1]]);     }     var view = new google.visualization.DataView(data);      view.setColumns([0, 1]);      var options = {        title: "Company Performance",        width: 600,        height: 400,        animation: {  startup:true,          duration: 1000,          easing: "out"        }      };      var chart = new google.visualization.ColumnChart(document.getElementById("barchart_values"));      chart.draw(view, options);  }  </script>'
	return content

def generateProfitLossTable(data):
	loss_flight,profit_flight = populateFlights()
	a=[]
	data = data[1:len(data)-1]
	if data == "loss":
		a = loss_flight
	elif data == "profit":
		a = profit_flight
	content = '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title"><i class="icon-table"></i> Flight Information</h6></div><div class="datatable"><table class="table" id="dataTable"><thead><tr><th>Plane Id</th><th>Source Country</th><th>Source State</th><th>Destination Country</th><th>Destination State</th><th>Halt</th></tr></thead><tbody>'
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
   	content+= '<script>$("#dataTable").DataTable();</script>'
   	return content

def findFlights(source, destination):
	flight_data = readFlightData("data/otherFlightData.csv")
	print "Finding Flights"
	answer_set = []
	for row in flight_data:
		source_country = source.split("-")[0]
		source_state = source.split("-")[1]

		dest_country = destination.split("-")[0]
		dest_state = destination.split("-")[1]

		if((source_country == row[2] and source_state == row[3] and dest_country == row[4] and dest_state == row[5] ) or (source_country == row[4] and source_state == row[5] and dest_country == row[2] and dest_state == row[3])):
			passenger_count = eval(row[14])
			capacity = eval(row[6]) 
			percentage = passenger_count*1.0/capacity
			flight_date = row[1].split(" ")[0]
			year, month, day = (int(x) for x in flight_date.split('-'))    
			ans = datetime.date(year, month, day)

			#print ans.strftime("%A")
			answer_set.append([ans.strftime("%w"), percentage])
	regression(answer_set)
	print answer_set

def regression(data):

	x = []
	y = []
	n = len(data)
	for row in data:
		x.append(row[0])
		y.append(row[1])
	xmean,ymean,xy,sum1,sum2,sum3 = sum(x)/n,sum(y)/n,0,0,0,0
	for i in range(n):
		xy += x[i]*y[i]
		sum1 += (x[i]-xmean)*(y[i]-ymean)
		sum2 += (x[i]-xmean)**2
		sum3 += x[i]**2
	b1 = xy/sum3
	b0 = ymean - b1*xmean

	xin = int(raw_input("Enter x value\n"))
	print "The y value is",(b0+b1*xin)

