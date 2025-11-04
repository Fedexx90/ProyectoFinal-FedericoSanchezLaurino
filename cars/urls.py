from django.urls import path
from .views import (
    AutoListView,
    AutoDetailView,
    AutoCreateView,
    AutoUpdateView,
    AutoDeleteView
)

app_name = 'cars'

urlpatterns = [
    path('', AutoListView.as_view(), name='auto_list'),
    path('<int:pk>/', AutoDetailView.as_view(), name='auto_detail'),
    path('new/', AutoCreateView.as_view(), name='auto_create'),
    path('<int:pk>/edit/', AutoUpdateView.as_view(), name='auto_edit'),
    path('<int:pk>/delete/', AutoDeleteView.as_view(), name='auto_delete'),
]

