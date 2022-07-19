from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def it_head(request):
    return render(request,'it_head.html')

def profile(request):
    return render(request,'profile.html')

def leads_option(request):
    return render(request,'leads_option.html')

def add_leads(request):
    return render(request,'add_leads.html')


