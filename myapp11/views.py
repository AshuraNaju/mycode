from django.shortcuts import render
from myapp11.form import contactform
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method=='POST':
        x=contactform(request.POST)
        if x.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False})



    x=contactform()
    return render(request,'index.html',{'form':x})
