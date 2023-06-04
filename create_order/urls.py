from django.conf.urls import url
from views import home_page, CreateOrderView, orders_page


urlpatterns = [

    url('create/', CreateOrderView.as_view(), name='add-order'),
    url('history/', orders_page, name='user-orders'),
    url('', home_page, name='home'),
]
