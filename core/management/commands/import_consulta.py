import csv

from django.core.management import BaseCommand

from core.models import Consulta
from datetime import datetime


class Command(BaseCommand):
    help = 'Import Investors from Autonomos Agent spreadsheet'

    def handle(self, *args, **options):
        with open('/home/lucas/Lucas/experimentos/teste_django/consulta.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['numero_guia_consulta', 'cod_medico', 'nome_medico', 'data_consulta', 'valor_consulta'], delimiter=';')
            for row in reader:
                consulta = Consulta()
                consulta.numero_guia_consulta = row['numero_guia_consulta']
                consulta.cod_medico = row['cod_medico']
                consulta.nome_medico = row['nome_medico']
                consulta.data_consulta = datetime.strptime(row['data_consulta'], '%d/%m/%y')
                consulta.valor_consulta = row['valor_consulta']
                consulta.save()
