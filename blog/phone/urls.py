from django.urls import path 
from .views import PhoneDetail , PhoneList

urlpatterns = [
    path('',PhoneList.as_view(),name='phone_list'),
    path('<int:pk>', PhoneDetail.as_view(),name='phone_detail')
]