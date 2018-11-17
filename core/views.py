from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.forms import ReportForm
from core.models import Consulta


def index(request):
    return render(request, 'relatorio.html', {})


@api_view(['GET'])
def report(request):
    report = ReportForm(request.GET)
    if report.is_valid():
        result = report.filter_consulta()
        return Response(result)

    return Response({"error": "error"}, status=400)


@api_view(['GET'])
def doctors(request):
    names = Consulta.objects.order_by('nome_medico').values_list('nome_medico', flat=True).distinct()
    return Response(list(names))