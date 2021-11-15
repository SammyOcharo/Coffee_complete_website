from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('payment/', views.payment, name='payment'),
    path('blog/<int:pk>/', views.Blog_Detail, name='blog'),
    path('handlesignup/', views.handlesignup, name="handlesignup") ,
    path('handlelogin/', views.handlelogin, name="handlelogin") ,
    path('signup/', views.Signup, name="signup") ,
    path('login/', views.login, name="login") ,
    path('handlelogout/', views.handlelogout, name="handlelogout"),
    path('update_item/', views.updateItem, name="update_item"),

]
