from django.urls import path
from loginpage import views
urlpatterns=[
    path('',views.loginView,name="loginpage"),
    path('home',views.homeView,name="homepage"),
    path('about',views.aboutView,name="aboutpage"),
    path('contact',views.contactView,name="contactpage"),
    path('post',views.postView,name="postpage"),
    path('form',views.func1,name="formpage")
]