from django.conf.urls import url
from views import Register, Login, logout_request, Profile


urlpatterns = [
    url('register/', Register.as_view(), name='register'),
    url('login/', Login.as_view(), name='login'),
    url('logout/', logout_request, name='logout'),
    url('profile/', Profile.as_view(), name='profile'),
]
