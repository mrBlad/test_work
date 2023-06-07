from django.conf.urls import url
from views import CreateOrderView, list_orders_page, UserOrderPage, download, stats_page


urlpatterns = [
    url(r'history/(?P<pk>[0-9]+)/', UserOrderPage.as_view(), name='user-order'),
    url('history/', list_orders_page, name='user-orders'),
    url('create/', CreateOrderView.as_view(), name='add-order'),
    url(r'^download/(?P<path_to_file>.*)$', download, name='download'),
    url('stats/', stats_page, name='stats'),
]
