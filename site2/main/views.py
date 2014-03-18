# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from main.models import *
from django.http import HttpResponseRedirect
from django.http import Http404


def home(request):
    l=App.objects.all()
    return render_to_response('home.html',{'app':l})