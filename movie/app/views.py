from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import RegisterForm
from .models import CustomerUser


# Create your views here.
def home(request):
    return render(request, 'main.html')

def movie_detail(request):
    return render(request, 'movie-detail.html')

def signup_view(request):

    # POST 방식으로 요청이 들어올 경우.
    if request.method == "POST":

        # 패스워드가 같은지 체크
        if request.POST['password1'] == request.POST['password2']:
            custom_user = CustomerUser()
            custom_user.username = request.POST['username']
            custom_user.password = request.POST['password1']
            custom_user.phone_number = request.POST['phone_number']
            custom_user.rank = '1'
            print(request.POST['username'])
            custom_user.save()

            user = authenticate(request=request, username=custom_user.username, password=custom_user.password)
            login(request, user)
            return redirect("main")
        
        # 패스워드가 다른 경우
        else:
            return HttpResponse("패스워드가 일치하지 않습니다.")
        
    # GET 방식으로 요청이 들어올 경우.
    else:
        context = {

        }
        return render(request, 'signup.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            print("유저의 형식이 옳지 않습니다.")
        return redirect("main")
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("main")
    

def events(request):
    return render(request, 'events.html')