from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('data.html/',views.data,name='data'),
]