from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:program_id>/', views.detail, name='detail'),
    path('grid/<int:grid_id>/', views.grid, name='grid'),
]