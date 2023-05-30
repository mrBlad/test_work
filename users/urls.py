from django.conf.urls import url
from views import Register, Login, logout_request, profile_page


urlpatterns = [
    url('register/', Register.as_view(), name='register'),
    url('login/', Login.as_view(), name='login'),
    url('logout/', logout_request, name='logout'),
    url('profile/', profile_page, name='profile'),
]
