from base.builders import PagamentoOnlineBuilder
from febraban import adapters


class PagamentoOnlineFBBBradescoBuilder(PagamentoOnlineBuilder):
    adapter_class = adapters.PagamentoOnlineFBBBradescoAdapter


class PagamentoOnlineFBBCEFBuilder(PagamentoOnlineBuilder):
    adapter_class = adapters.PagamentoOnlineFBBCEFAdapter


class PagamentoOnlineFBBBancoBrasilBuilder(PagamentoOnlineBuilder):
    adapter_class = adapters.PagamentoOnlineFBBBancoBrasilAdapter
