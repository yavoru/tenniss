from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#import models
from .models import *

# Create your views here.
def members(request):
	#Get all members from the database
	myproducts=Member.objects.all().order_by('name')
	#Create a context dictionary
	template = loader.get_template('all_products.html')
	#Load the template
	context = {
		'myproducts': myproducts,
	}
	return HttpResponse(template.render(context, request))

def testing(request):
	myproducts = Member.objects.all()
	template = loader.get_template('ryudat.html')
	context = {
		'myproducts': myproducts,
	}
	return HttpResponse(template.render(context, request))

#Create a view for a single member
def details(request, id):
	myproduct=Member.objects.get(id=id)
	#Create a context dictionary
	template = loader.get_template('details.html')
	#Load the template
	context = {
	'myproduct': myproduct,
	}
	return HttpResponse(template.render(context, request))

def findNew(request):
    myproducts=Member.objects.filter(create_date__gt = '2023-07-01')
    
    template = loader.get_template('findmem.html')
    
    context={
		'myproducts':myproducts,
	}
    
    return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())