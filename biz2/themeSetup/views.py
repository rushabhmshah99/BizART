from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import render
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
	months = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
	months2 = ['', 'Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

	query = request.POST['query']
	dates = queryProcessing(query)
	# Do your shit Rushabh
	month1 = months.index(dates[0]) if months.index(dates[0]) !=-1 else months2.index(dates[0])
	month2 = months.index(dates[2]) if months.index(dates[0]) !=-1 else months2.index(dates[2])
	
	print month1, month2
	

	rev1 = calcRevenueWithinTime(dates[1], month1)
	rev2 = calcRevenueWithinTime(dates[3], month2)
	data = [ [dates[0]+" "+str(dates[1]), rev1], [dates[2]+" "+str(dates[3]), rev2]]
	return render(request,'graph.html',{'query':json.dumps(data)})
