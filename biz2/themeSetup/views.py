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
	print str(action)
	print str(action) == "show"
	if str(action) == "compare":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateGraph"})
	elif str(action) == "show":
		return render(request,'graph.html',{'query':json.dumps(dates), 'page': "generateTable"})

def generateGraph(request):
	if request.POST:
		dates = request.POST['dates']
	data = generateResult(dates)
	return HttpResponse(json.dumps(data), content_type="application/json")

def generateTable(request):
	if request.POST:
		dates = request.POST['dates']
	data = generateProfitLossTable(dates)
	return HttpResponse(json.dumps(data), content_type="application/json")