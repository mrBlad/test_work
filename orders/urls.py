from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include('users.urls')),
    url('order/', include('create_order.urls')),
]
