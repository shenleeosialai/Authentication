from django.urls import include, path
from .import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('dahboard/',views.dashboard, name='dashboard'),
]