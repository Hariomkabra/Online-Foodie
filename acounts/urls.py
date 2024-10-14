from django.urls import path, include, re_path
from .import urls_reset
from .views import index, register, profile, logout, login, contact_view, contact_success_view

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('password-reset/', include(urls_reset)),
    path('contact/', contact_view, name='contact'),  # Correct path for contact form
    path('contact/success/', contact_success_view, name='contact_success'),  # Success page
]
