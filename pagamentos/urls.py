from django.conf.urls import url

from .views import PagamentoOnlineViewSet

urlpatterns = [
    url(r'^online/$', PagamentoOnlineViewSet.as_view(), name = 'pagamentoonline'),
]
