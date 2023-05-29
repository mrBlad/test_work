from django.conf.urls import url, include
from views import Register


urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url('register/', Register.as_view(), name='register'),
]