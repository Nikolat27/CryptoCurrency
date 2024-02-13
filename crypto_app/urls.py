from . import views
from django.urls import path

app_name = "price_page"
urlpatterns = [
    path("prices", views.price_page, name='price')
]