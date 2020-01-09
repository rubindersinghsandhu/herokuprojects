from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.WeightsView)
urlpatterns = [
    path('', views.weightreq, name='weightform'),
    path('api/', include(router.urls)),
    path('result/', views.predictweight),
]