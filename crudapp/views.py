from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Msg

# Create your views here.
def create(request):
    print("request =",request.method)
    if request.method=="GET":
        print("we are inside get method")
        return render(request,"create.html")
    else:
        print("we are inside POSTmethod")
        nm=request.POST["uname"]
        print(nm)
        em=request.POST["Email"]
        print(em)
        mb=request.POST["umobile"]
        print(mb)
        ms=request.POST["Message"]
        print(ms)
       
        m = Msg.objects.create(name = nm, email = em, mobile = mb, message = ms)
        print(m)
        return HttpResponse("data stored succefully")
    


def show(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context["data"]=m
    return render(request, "dashboard.html", context)

def update(request):
    return render(request,"update.html")
       
def delete(request,rid):
    print("delete id",rid)
    
    m=Msg.objects.filter(id=rid)
    m.delete()
    return HttpResponse("id to be deleted "+rid)

def edit(request,rid):
    #return HttpResponse(rid)
    if request.method == "GET":
        
        m=Msg.objects.filter(id=rid)
        context={}
        context["data"]=m
        return render(request,"edit.html",context)
    
    else:
        
        nm=request.POST["uname"]
        em=request.POST["Email"]
        mb=request.POST["umobile"]
        ms=request.POST["Message"]
        
        
        
        m=Msg.objects.filter(id=rid).update(name=nm, email=em, mobile=mb, message=ms)
        #m = Msg.objects.update(id=rid)
       # m=Msg.objects.update(id=rid, name=nm, email=em, mobile=mb, message=ms)
       
       
        #m.save()
        print(m)
        
        return redirect("/show")