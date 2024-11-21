from django.urls import path
from .views import UserRegistrationViewDRF, register_view, close_session

urlpatterns = [
    path('register/', register_view, name='register'),  # This will render the registration form
    path('api/register/', UserRegistrationViewDRF.as_view(), name='user-register'),  # API for registration
    path('close_session/', close_session, name='close_session')
]
