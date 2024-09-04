from django.urls import path
from restaurant import views as res_views

urlpatterns = [
    path('register/', res_views.RegisterUserView.as_view(), name='register'),
    path('login/', res_views.CustomAuthToken.as_view(), name='login'),
    path('restaurants/', res_views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', res_views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('categories/', res_views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', res_views.CategoryDetailView.as_view(), name='category-detail'),
    path('menu_items/', res_views.MenuItemListCreateView.as_view(), name='menuitem-list-create'),
    path('menu_items/<int:pk>/', res_views.MenuItemDetailView.as_view(), name='menuitem-detail'),
    path('modifiers/', res_views.ModifierListCreateView.as_view(), name='modifier-list-create'),
    path('modifiers/<int:pk>/', res_views.ModifierDetailView.as_view(), name='modifier-detail'),
    path('orders/', res_views.OrderCreateView.as_view(), name='order-create'),

]
