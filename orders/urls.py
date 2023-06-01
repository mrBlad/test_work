from django.conf.urls import url, include
from django.contrib import admin
from create_order.views import home_page, order_page

urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include('users.urls')),
    url('order/', order_page, name='add-order'),
    url('', home_page, name='home'),
]
