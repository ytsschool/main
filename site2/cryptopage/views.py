from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from cryptopage.models import Cryptotext, ContactForm

normal_text = Cryptotext.random_text()
new_text = Cryptotext.encrypt(normal_text)

def index(request):
	template = loader.get_template('cryptopage/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def main(request):
	template = loader.get_template('cryptopage/main.html')
	form = ContactForm()
	context = RequestContext(request, {"new_text": new_text, "form": form})
	return HttpResponse(template.render(context))

def check(request):
	template = loader.get_template('cryptopage/check.html')
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			text = form.cleaned_data['decrypted']
			if text == normal_text:
				return_text = "Valid decryption!"
			else:
				return_text = "Not valid decryption!"
		else:
			return_text = "Not valid input."
		context = RequestContext(request, {"form": return_text})
	return HttpResponse(template.render(context))