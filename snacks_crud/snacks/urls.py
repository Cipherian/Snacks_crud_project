from django.urls import path
from .views import SnackCreateView, SnackListview, SnackDeleteView, SnackDetailView, SnackUpdateView

urlpatterns = [
    path('create/', SnackCreateView.as_view(), name='create'),
    path('', SnackListview.as_view(), name='list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail'),
    path('<int:pk>/update', SnackUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='delete')
]