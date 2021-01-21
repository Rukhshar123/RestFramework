from django.urls import path,include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register(r'employees',views.EmployeeViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]
