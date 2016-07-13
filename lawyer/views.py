from django.shortcuts import render
from lawyer.forms import *
from lawyer.models import Cost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
@csrf_protect
def law_register(request):
	if request.method=="Post":
		form=CostForm(request.Post)
		if form.is_valid():
			name=request.Post.get('name','')
			address=request.Post.get('address','')
			about=request.Post.get('about','')
			cost_obj=Cost(name=name,address=address,about=about)
			cost_obj.save()
			
			return HttpResponseRedirect("/lawyer_register/sucess/")
	else:
		
		form=CostForm()
	
	variables = RequestContext(request, {'form': form})
 
	return render_to_response(
	'lawy.html',
	variables,
	)
def lawyer_sucess(request):
	return render_to_response(
	'sucess.html',
    )
	


# Create your views here.
