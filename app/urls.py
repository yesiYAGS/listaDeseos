from django.urls import path
from app import views

urlpatterns = [
	path('', views.main),
    path('logout', views.logout),
    path('register',views.register),
    path('dashboard', views.dashboard),
    path('wish_items', views.wish_items),
    path('wish_items_create', views.wish_items_create),
    
]