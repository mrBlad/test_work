from django.conf.urls import url
from views import CreateOrderView, orders_page, order_page


urlpatterns = [
    url(r'history/(?P<pk>[0-9]+)/', order_page, name='user-order'),
    url('history/', orders_page, name='user-orders'),
    url('create/', CreateOrderView.as_view(), name='add-order'),
]
