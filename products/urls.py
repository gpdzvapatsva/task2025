from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name='index'),
    path('create/', views.add_product, name='add_product'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path("metrics/", views.metrics, name="metrics"),
    path('', views.index, name='index'),  # optional list view
]