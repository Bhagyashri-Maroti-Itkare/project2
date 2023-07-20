from django.urls import path
from . import views

urlpatterns = [
    path('get12/',views.sign_up1),
    path('get13/',views.user_login),
    path('get14/',views.user_profile),
    path('get15/',views.user_logout),
    path('get16/',views.setcookies),
    path('get17/',views.getcookies),
    path('get18/',views.deletecookies),
    path('get19/',views.setsession),
    path('get20/',views.get_key),
    path('get21/',views.getsession),
    path('get22/',views.delsession),
    path('get23/',views.setsession1),
    path('get24/',views.getsession1),
    path('get25/',views.delsession1),
    
]