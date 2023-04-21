from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="homelink"),
    # path("about", aboutpage),
    path('<int:pk>/', productDetailPage, name='detail-link')
]
