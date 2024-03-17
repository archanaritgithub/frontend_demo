from django.urls import path
from . import views


from store.controller import authview,cart

urlpatterns = [
    path('homee',views.home, name='homee'),
]