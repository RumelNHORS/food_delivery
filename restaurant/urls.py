from django.urls import path
from restaurant import views as res_views

urlpatterns = [
    path('register/', res_views.RegisterUserView.as_view(), name='register'),
    path('login/', res_views.CustomAuthToken.as_view(), name='login'),
    # Create Restaurant
    path('restaurants/', res_views.RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    # Update/Delete Restaurant
    path('restaurants/<int:pk>/', res_views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    # List of all Restaurant
    path('restaurants_list/', res_views.RestaurantListView.as_view(), name='restaurant-list'),
    # Create Restaurant Category
    path('categories/', res_views.CategoryListCreateView.as_view(), name='category-list-create'),
    # Update/Delete Restaurant Category
    path('categories/<int:pk>/', res_views.CategoryDetailView.as_view(), name='category-detail'),
    # List of all Restaurant's Category
    path('categories_list/', res_views.CategoryListView.as_view(), name='category-list'),
    # Create Menu Item
    path('menu_items/', res_views.MenuItemListCreateView.as_view(), name='menuitem-list-create'),
    # Update the Menu Item
    path('menu_items/<int:pk>/', res_views.MenuItemDetailView.as_view(), name='menuitem-detail'),
    # List of all Menu Item
    path('menuLitems_list/', res_views.MenuItemListView.as_view(), name='menuitem-list'),
    path('modifiers/', res_views.ModifierListCreateView.as_view(), name='modifier-list-create'),
    path('modifiers/<int:pk>/', res_views.ModifierDetailView.as_view(), name='modifier-detail'),
    # Order Create 
    path('orders/', res_views.OrderCreateView.as_view(), name='order-create'),

]
