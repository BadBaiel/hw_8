from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ClothesListView.as_view(), name='products'),
    path('products/<int:id>/', views.BabyListView.as_view(), name='baby'),
    path('products/<int:id>/', views.SportsWearListView.as_view(), name='baby'),
    path('products/<int:id>/', views.WomenListView.as_view(), name='baby'),
    path('products/<int:id>/', views.ManListView.as_view(), name='baby'),
    path('add-order/', views.OrderClCreateView.as_view(), name='add'),
]