from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def welcome1(request):
    res =HttpResponse('welcome to Django Frame work')
    return res

def welcome2(request):
    return render(request,'welcome.html')

class Home(View):
    def get(self,request):
        return render(request,'input.html')

class Add(View):
    def get(self,request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        op=request.GET["operation"]
        if op=="click to Add":
            i =int(x)
            j =int(y)
            k = i+j
            res = HttpResponse('The sum is : {}'.format(k))
            return res

        elif op=="click to Sub":
            i =int(x)
            j =int(y)
            k = i-j
            res = HttpResponse('The sum is : {}'.format(k))
            return res

        elif op=="click to Mul":
            i =int(x)
            j =int(y)
            k = i*j
            res = HttpResponse('The sum is : {}'.format(k))
            return res

        else:
            i =int(x)
            j =int(y)
            k = i/j
            res = HttpResponse('The sum is : {}'.format(k))
            return res


