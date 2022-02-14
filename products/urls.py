from django.urls import path
from .views      import ProductView

# http://localhost:8000/products Get

urlpatterns = [
    path('', ProductView.as_view())
]