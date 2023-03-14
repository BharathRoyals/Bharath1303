from django.shortcuts import render

# Create your views here.
def jinjafirst(request):
    d={'name':'Bharath','age':23}
    return render(request,'jinjafirst.html',context=d)