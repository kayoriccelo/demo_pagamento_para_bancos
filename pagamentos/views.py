from rest_framework.views import APIView
from rest_framework.response import Response

from contratos.models import Contrato
from pagamentos.serializers import PagamentoOnlineSerializer


class PagamentoOnlineViewSet(APIView):
    # neste momento você pode colocar a modelagem de contratos que você usa exemplo: Contrato.objects.all()
    queryset = [Contrato()]
    serializer_class = PagamentoOnlineSerializer

    def post(self, request):
        serializer = self.serializer_class(data={}, context={'request': request, 'contratos': self.get_queryset()})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
