from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def addition(request):
	if request.POST:
		num1 = request.POST['num1']
		num2 = request.POST['num2']
		ress = eval(num1) + eval(num2)

		return render_to_response('result.php', {'result': ress}, context_instance=RequestContext(request))
	else:
		return render_to_response('result.php', {}, context_instance=RequestContext(request))
