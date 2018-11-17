from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Consulta


def index(request):
    return render(request, 'relatorio.html', {})


@api_view(['GET'])
def report(request):
    return Response({"oi": "oi"})


@api_view(['GET'])
def doctors(request):
    names = Consulta.objects.order_by('nome_medico').values_list('nome_medico', flat=True).distinct()
    return Response(list(names))