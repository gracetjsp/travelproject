from django.shortcuts import render
from django.http import HttpResponse
from .models import Places,Peoples

# Create your views here.
def demo(request):
    obj = Places.objects.all()
    people_obj = Peoples.objects.all()
    return render(request,"index.html",{'result':obj,'people': people_obj})
    # return HttpResponse("<h1>hello world</h1>")
    
# def add(request):
#     x = int(request.GET["num1"])
#     y = int(request.GET["num2"])
#     res = x+ y
#     return render(request,"result.html",{'result':res})