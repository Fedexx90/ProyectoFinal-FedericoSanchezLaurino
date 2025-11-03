from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.auto_list, name='auto_list'),
    path('<int:pk>/', views.auto_detail, name='auto_detail'),
    path('nuevo/', views.auto_create, name='auto_create'),
    path('<int:pk>/editar/', views.auto_update, name='auto_update'),
    path('<int:pk>/eliminar/', views.auto_delete, name='auto_delete'),
]

