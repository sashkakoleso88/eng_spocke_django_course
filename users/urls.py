from django.urls import path
from users.views import login, registration


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registrtion/', registration, name='registration'),
]