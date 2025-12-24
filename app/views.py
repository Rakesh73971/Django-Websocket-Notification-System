from django.shortcuts import render

# Create your views here.

def notify(request):
    return render(request,'app/notify.html')