from advert.models import board
from django.views.generic import ListView, DetailView, FormView
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404,render_to_response
from advert.forms import addi
from django.template import RequestContext, loader

# Create your views here.

class BoardDetailView(DetailView): 
    model = board

class BoardListView(ListView): 
    model = board

def addit(request):
    template = loader.get_template('advert/add.html')
    if request.method == 'POST': 
        form = addi(request.POST)
        if form.is_valid():
            #board_id = boa
	    title = form.cleaned_data['title']
    	    description = form.cleaned_data['description']
            contact = form.cleaned_data['contact']
            money = form.cleaned_data['money']
	    
            return HttpResponseRedirect('/board/') # Redirect after POST
    else:
        form = addi() # An unbound form

    return render_to_response('add.html', {
        'form': form,
    })
