from django.conf.urls import url, include
from django.contrib import admin
from create_order.views import home_page


urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include('users.urls')),
    url('order/', include('create_order.urls')),
    url('', home_page, name='home'),
]
