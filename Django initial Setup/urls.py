from django.urls import path
from headerfunctions.views import home_view,abt,cnt,hlp

urlpatterns=[
    path('Home/',home_view),
    path('About/',abt),
    path('Contact/',cnt),
    path('Help/',hlp)
]