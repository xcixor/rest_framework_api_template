from django.conf.urls import url
from django.urls import path
from toys import views

app_name = 'toys'

urlpatterns = [
    path('', views.toy_list, name='toys'),
    path('<int:pk>', views.toy_detail, name='toy'),
]
