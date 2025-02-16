from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage")
    context={
        'variable':"this is sent",
        'variable2':"this is sent"
    }
    return render(request,'index.html',context)
def about(request):
    # return HttpResponse("this is about page")
    return render(request,"about.html")
def services(request): 
    # return HttpResponse("this is services page")
    return render(request,"services.html")
def contact(request):
    # return HttpResponse("this is contact page")
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone)
        contact.save()
        messages.success(request, "your Message is send")

    
    return render(request,"contact.html")
                                                                                                                                                                                                                               