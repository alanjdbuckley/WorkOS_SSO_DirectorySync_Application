from django.urls import path
from . import views
from .views import directory_sync_data

urlpatterns = [
    path("", views.login, name="login"),
    path("auth", views.auth, name="auth"),
    path("auth/callback", views.auth_callback, name="auth_callback"),
    path("logout", views.logout, name="logout"),
    path('directory_sync_data/', directory_sync_data, name='directory_sync_data'),

]
