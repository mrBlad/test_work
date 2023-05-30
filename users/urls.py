from django.conf.urls import url
from views import Register, Login, logout_request


urlpatterns = [
    url('register/', Register.as_view(), name='register'),
    url('login/', Login.as_view(), name='login'),
    url('logout/', logout_request, name='logout'),
]