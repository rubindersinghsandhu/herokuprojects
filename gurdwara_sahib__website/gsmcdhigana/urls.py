from django.urls import path
from .views import postdata,homepage,userlogin,userlogout,imageview

urlpatterns = [
    path('',homepage,name='home'),
    path('createpost/',postdata,name='postdata' ),
    path('login/',userlogin,name='login'),
    path('logout/',userlogout,name='logout'),
    path('homepage/billdetails/<int:id>/',imageview,name='bigimg'),
]
