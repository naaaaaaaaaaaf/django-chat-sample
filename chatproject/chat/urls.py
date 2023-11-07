from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('room/create/', views.RoomCreateView.as_view(),name='room.create'),
    path('room/list/', views.RoomListView.as_view(),name='room.list')
]
