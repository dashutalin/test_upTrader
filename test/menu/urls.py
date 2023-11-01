from django.urls import path
from .views import main, page

app_name = 'menu'

urlpatterns = [
    path('', main),
    path('<slug:name>/', page, name='page')
]
