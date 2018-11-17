import csv
import os

from django.core.management import BaseCommand

from core.models import Exame


class Command(BaseCommand):
    help = 'Import Investors from Autonomos Agent spreadsheet'

    def handle(self, *args, **options):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{path}/exame.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=['cod_exame', 'numero_guia_consulta', 'valor_exame'], delimiter=';')
            for row in reader:
                exame = Exame()
                exame.cod_exame = row['cod_exame']
                exame.valor_exame = row['valor_exame']
                exame.numero_guia_consulta_id = row['numero_guia_consulta']
                exame.save()