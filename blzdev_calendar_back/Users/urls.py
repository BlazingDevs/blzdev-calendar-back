from django.urls import path,include
from . import views
from knox import views as knox_views

urlpatterns = [
    path('login/', views.LoginAccount.as_view()),
    path('register/', views.CreateAcoount.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]