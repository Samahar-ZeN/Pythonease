from django.shortcuts import render

# Create your views here.

def home_view(callme):
    return render(callme,'Home.html')
def abt(callback):
    return render(callback,'About.html')
def cnt(callback):
    return render(callback,'Contact.html')
def hlp(callme):
    return render(callme,'Help.html')