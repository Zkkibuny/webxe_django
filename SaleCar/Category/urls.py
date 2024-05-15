from django.urls import path
from . import views
from .views import CarDetailView, HolderDetailView

urlpatterns = [
    path('Holder', views.HolderListView.as_view(),name='holder_info'),
    path('Holder/<int:pk>/', HolderDetailView.as_view(), name='holder_detail'),
    path('Car',views.CarListView.as_view(),name='car_info'),
    # path('Car/new',views.CarInfo,name='car_new'),
    path('Car/<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    # path('Car/<int:pk>/edit/',views.CarInfo,name='car_edit'),
    # path('Car/<int:pk>/delete/',views.CarInfo,name='car_delete'),
    path('',views.Home,name='home')
]