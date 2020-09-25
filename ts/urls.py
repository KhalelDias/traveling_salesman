from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='dep'),
    path('url/', url, name='url'),
    path('url/<str:token>', get_url, name='get_url')
]
