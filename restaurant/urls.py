from django.urls import path
from restaurant import views as res_views

urlpatterns = [
    path('register/', res_views.RegisterUserView.as_view(), name='register'),
    path('login/', res_views.CustomAuthToken.as_view(), name='login'),
    path('restaurants/', res_views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', res_views.RestaurantDetailView.as_view(), name='restaurant-detail'),
]
