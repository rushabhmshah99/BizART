import csv
import datetime
from themeSetup.bayesian import *
from themeSetup.apriori import *

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

def calculateRevenue():
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

	return data2, data

def populateFlights():
	
	data2, data = calculateRevenue()
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
	#regression(answer_set)
	print answer_set

def bayesian(input_para):
	revenue_data, flight_data = calculateRevenue()

	max_rev = max(revenue_data)
	min_rev = min(revenue_data)
	rev_range = (max_rev - min_rev)/3

	training_data = []	
	for el in xrange(1, len(flight_data)-1):
		source = flight_data[el][2]+"-"+flight_data[el][3]
		destination = flight_data[el][4]+"-"+flight_data[el][5]
		
		if revenue_data[el] > min_rev and revenue_data[el] < min_rev+rev_range:
			rev = "Low"
		elif revenue_data[el] > min_rev+rev_range and revenue_data[el] < min_rev+2*rev_range:
			rev = "Medium"
		else:
			rev = "High"

		capacity = flight_data[el][6]

		training_data.append([source, destination, rev])

	#print training_data	
	uniqueElements = countUnique(training_data)
	attribute_list = []
	for element in uniqueElements:
		ele = calcOutputProbability(element, uniqueElements.index(element), training_data)
		attribute_list+= [ele]
	mainTable = createList(attribute_list, training_data)
	#print mainTable
	data = input_para
	rev_prob = calcOutput(mainTable, data, attribute_list)
	content = '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title">Revenue Probability is '+rev_prob+'</h6></div></div>'
	return content
 

#pass attribute as flights or passenger - query 'show all flights, show all passengers, show competitor flights'  	
def showAttributeDetails(attribute):
	
	if attribute == "passengers" :
		data = readFlightData("data/passengers.csv")
	elif attribute == "competitor":
		data = readFlightData("data/otherFlightData.csv")
	elif attribute == "flights":
		data = readFlightData("data/flightData.csv")


	content = '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title"><i class="icon-table"></i> Flight Information</h6></div><div class="datatable"><table class="table" id="dataTable"><thead><tr>'
	for el in data[0]:
		content+= '<th>'+el+'</th>'
	content += '</tr></thead><tbody>'
	data  = data[1:len(data)-1]
	for row in data:
		content += '<tr>'
		for el in row:
			content += '<td>'+el+'</td>'
	content = content + '</tbody></table></div></div>'
   	
   	return content
   		


def clustering():
	data = readFlightData("data/flightData.csv")
	numberofdays = []
	passenger_data = []
	with open("data/passengers_plane.csv", 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        if row[0]!="Passenger_ID":
	        	plane_id = int(row[1])
	        	flight_date = data[plane_id][1].split(' ')[0]
	        	year, month, day = (int(x) for x in flight_date.split('-'))
	        	ans = datetime.date(year,month,day)
	        	ans = ans.strftime("%s")
	        	numberofdays.append(int(ans))
	        
	# perform clustering by K-means
	no_of_clusters = 6
	cluster_center = [numberofdays[0],numberofdays[1],numberofdays[2],numberofdays[3],numberofdays[4],numberofdays[5]]
	clusters = [[],[],[],[],[],[]]
	previous_clusters = [[]]
	for count in range(0,10):
		for i in numberofdays:
			min = float('inf')
			cluster_no = -1
			for j in cluster_center:
				if abs(i-j) < min:
					min = abs(i-j)
					cluster_no = cluster_center.index(j)
			clusters[cluster_no].append(i)
		for i in range(0,6):
			cluster_center[i] = sum(clusters[i])/len(clusters[i])
		previous_clusters = clusters
		clusters = [[],[],[],[],[],[]]

	
	month_density_center = [0]*12  # number of passengers in that month cluster
	for milisec in cluster_center:
		date = datetime.datetime.fromtimestamp(milisec)
		flight_date = str(date).split(' ')[0]
		year, month, day = (int(x) for x in flight_date.split('-'))
		month_density_center[month-1] += len(previous_clusters[cluster_center.index(milisec)])
	
	frequent_month =  months[month_density_center.index(max(month_density_center))+1]
	content = ""
	content += '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title">Customer Desnity is concentrated around the month of '+frequent_month+'. Increasing flights around that time will be profitable. </h6></div></div>'
	return content
 



def aprioriFrequentCustomers():
	itemSet = []
	with open("data/passengers.csv", 'rb') as f:
	    reader = csv.reader(f)
	    for row in reader:
	        if row[0]!="Passenger_ID":
	        	age_group = int(row[2])/10
	        	itemSet.append([row[1], age_group, row[3]])
	frequent_sets = applyAlgo(itemSet)
	content = ""
	for sets in frequent_sets:
		gender = "Male"	
		if sets[1]=='M':
			gender = "Male"
		else:
			gender = "Female"
		content += '<div class="panel panel-default"><div class="panel-heading"><h6 class="panel-title">Most Frequent Customers are in the age group '+str(int(sets[0])*10)+' to '+str(int(sets[0])*10+10)+', are '+ gender + ' working as  '+ sets[2] +'</h6></div></div>'
	return content
 