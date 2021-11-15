import json
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.

def landingPage(request):
    Name = request.POST.get("name")
    Email = request.POST.get("email")
    Number = request.POST.get("number")
    
    content=GetInTouch(Title=Name, Email=Email, Number=Number)
    content.save()

    All_blogs = Blogs.objects.all()
    All_menus = Menu.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {
        'All_blogs': All_blogs,
        'All_menus': All_menus,
        'items': items,
        'order': order,
        'cartItems': cartItems
    }

    return render(request, 'index.html', context)

def Blog_Detail(request, pk):
    each_blogs = Blogs.objects.filter(id=pk)

    context = {
        'each_blogs': each_blogs
    }

    return render(request, 'blog-detail.html', context)


def payment(request):

    return render(request, 'Payment.html')


def login(request):


    return render(request, 'login.html')

def Signup(request):


    return render(request, 'signup.html')



@csrf_exempt
def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['username'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("signup")
            except User.DoesNotExist:
                if len(username) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("signup")
                if not username.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("signup")
        # create the user
        user = User.objects.create_user(username, email, password1)
        user.username = username
        user.save()
        messages.success(
            request, " Your account has been successfully created. Please navigate to Login to access your account")
        return redirect("login")
    else:
        return HttpResponse('404 - NOT FOUND ')
# view for rendering data from login page

def handlelogin(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        # cheching for valid login
         # cheching for valid login
        if user is not None:
            auth_login(request, user)
            print("user logged in")
            messages.success(request, " Successfully logged in")
            return redirect('landingPage')
        else:
            messages.error(request, " Invalid Credentials, Please try again....")
            return redirect("login")
    else:
        return render(request, 'signup')

@login_required
def handlelogout(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    print("we are logged out")
    return redirect('/')


def updateItem(request):
    data = json.loads(request.body)
    menuId = data['menuId']
    Action = data['action']

    print('menuId:', menuId)
    print('action:', Action)

    customer = request.user.customer
    MenuId = Menu.objects.get(id=menuId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)


    orderItem, created = OrderItem.objects.get_or_create(order=order, product=MenuId)

    if Action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)

    elif Action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added..', safe=False)
