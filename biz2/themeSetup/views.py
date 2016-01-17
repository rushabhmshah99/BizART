from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

# Create your views here.
username = ''
def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
def aboutus(request):
	return render_to_response('aboutus.html', {}, context_instance=RequestContext(request))
def login_simple(request):
	if request.POST:
		username = request.POST['username']
		return redirect('/login_advanced/'+username)
	else:
		return render_to_response('login_simple.html', {}, context_instance=RequestContext(request))
def login_advanced(request, username):
	if request.POST:
		username = request.POST['username']
		if len(username) == 0:
			return redirect('/login_simple/');	
	
		password = request.POST['password']
		return redirect('/search', username = username)
	else:
		if len(username) == 0:
			return redirect('/login_simple/');	
	
		return render_to_response('login_advanced.html', {'username':username}, context_instance=RequestContext(request))

def search(request):
	if request.POST:
		query = request.POST['query']
		return render_to_response('search.html', {'query': query}, context_instance=RequestContext(request))
	else:	
		return render_to_response('search.html', {}, context_instance=RequestContext(request))
