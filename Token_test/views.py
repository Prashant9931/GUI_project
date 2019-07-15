from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User,auth
from rest_framework.decorators import api_view
from django.http import HttpResponse
# from Token_test.models  import User
from rest_framework.views import APIView
class Log(APIView):
    def Login_api(request):
        content = {'message': 'Hello, World!'}
        return HttpResponse(content)

def home(request):
    return render(request,'layout.html');
@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        list1=User.objects.filter(username=username)
        if list1[0].username == username and list1[0].password == password:
            return redirect('/')


    return render(request,'login.html')
@csrf_exempt
def register(request):
    if request.method=="POST":
        # name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        # confirm=request.POST['confirm']
        user=User.objects.create_user(username=username,password=password)
        user.save();
        print('created')
        return redirect('/')

        pass
    return render(request,'register.html')
# Create your views here.
