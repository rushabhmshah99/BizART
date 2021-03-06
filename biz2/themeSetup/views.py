from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import render, HttpResponse
from themeSetup.validate import *
import json 
from themeSetup.queryProcessing import *
from themeSetup.generateGraphData import *
# Create your views here.

def speech(request):
	return render(request,'speech.html',{})

def login_simple(request):
	if 'loggedin' in request.session:
		del request.session['loggedin']
	if 'username' in request.session:
		del request.session['username']
	return render(request,'login_simple.html',{})

def login_advanced(request):
	if request.POST:
		username = request.POST['username']

		# validate username here
		flag = validateUser(username)
		if(flag is None): 
			return redirect('/login_simple/')
		else:
			return render(request,'login_advanced.html',{'username' : username})
	else:
		return redirect('/error/')

def search(request):
	if request.POST:
		password = request.POST['password']
		username = request.POST['username']
		#validate password here
		flag = validatePassword(username , password)
		if(flag is None):
			return render(request,'login_advanced.html',{'username' : username})
		else:
			request.session['loggedin'] = 1
			request.session['username'] = username
			return render(request,'search.html',{'username' : username})
	elif 'username' in request.session:
		return render(request,'search.html',{'username' : request.session['username']})
	else:
		return redirect('/error/')
def aboutus(request):
	if 'loggedin' in request.session:
		return render(request,'aboutus.html',{'username' : request.session['username']})
	else:
		return redirect('/error/')
def error(request):
	return render(request,'404.html',{})

def graph(request):
	query = request.POST['query']
	dates, action = queryProcessing(query)
	#findFlights("US-UT", "IN-AS")
	#aprioriFrequentCustomers()
	if str(action) == "compare":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateGraph", 'username': request.session['username'] })
	elif str(action) == "show":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateTable", 'username': request.session['username'] })
	elif str(action) == "suggest":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateBayesian", 'username': request.session['username'] })
	elif str(action) == "profit":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateProfit", 'username': request.session['username'] })
	

def generateGraph(request):
	if request.POST:
		dates = request.POST['dates']
	data = generateResult(dates)
	return HttpResponse(json.dumps(data), content_type="application/json")

def generateProfit(request):
	if request.POST:
		dates = request.POST['dates']
	data = aprioriFrequentCustomers()
	data += clustering()
	return HttpResponse(json.dumps(data), content_type="application/json")

def generateTable(request):
	# dates is either profit or loss or passengers or flights
	if request.POST:
		dates = request.POST['dates']
	dates = ''.join(list(str(dates))[1:len(str(dates))-1])
	if dates == "profit" or dates == "loss":
		data = generateProfitLossTable(dates)
	else:
		data = showAttributeDetails(dates)
	return HttpResponse(json.dumps(data), content_type="application/json")

def generateBayesian(request):
	if request.POST:
		inpu = request.POST['dates']
	#inp = ["US-NY", "US-VA"]
	print inpu
	data = bayesian([inpu])
	return HttpResponse(json.dumps(data), content_type="application/json")

def callClustering(request):
	if request.POST:
		inpu = request.POST['dates']
	data = clustering()
	return HttpResponse(json.dumps(data), content_type="application/json")
