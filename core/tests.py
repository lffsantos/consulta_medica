from parameterized import parameterized
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import Consulta, Exame


class ConsultaMedica(APITestCase):
    def setUp(self):
        self.consulta1 = mommy.make(
            Consulta, numero_guia_consulta=1, data_consulta='2018-01-01', nome_medico='Pedro',
            valor_consulta=10)
        self.consulta2 = mommy.make(
            Consulta, numero_guia_consulta=2, data_consulta='2018-04-22', nome_medico='João',
            valor_consulta=22)
        self.consulta3 = mommy.make(
            Consulta, numero_guia_consulta=3, data_consulta='2018-03-12', nome_medico='João',
            valor_consulta=90)
        self.consulta4 = mommy.make(
            Consulta, numero_guia_consulta=4, data_consulta='2017-11-04', nome_medico='João',
            valor_consulta=5)
        self.consulta5 = mommy.make(
            Consulta, numero_guia_consulta=5, nome_medico='Ademar',
            valor_consulta=5)
        self.consulta6 = mommy.make(
            Consulta, numero_guia_consulta=6, nome_medico='Marcos',
            valor_consulta=5)
        self.exame1 = mommy.make(
            Exame, valor_exame=100, numero_guia_consulta=self.consulta1)
        self.exame2 = mommy.make(
            Exame, valor_exame=39, numero_guia_consulta=self.consulta3)
        self.exame2 = mommy.make(
            Exame, valor_exame=45, numero_guia_consulta=self.consulta4)

    def test_get_doctors_name(self):
        doctor_names = ['João', 'Pedro', 'Marcos', 'Ademar', 'Pedro']
        url = reverse('doctors')
        response = self.client.get(url)

        self.assertEqual(response.data, sorted(list(set(doctor_names))))

    def test_get_report_without_filters(self):
        expected = [
            {'qt_exames': 1, 'nome_medico': 'Pedro', 'numero_guia': 1, 'dt_consulta': '01/01/2018', 'valor_consulta': 10.0, 'gasto_consulta': 100.0},
            {'qt_exames': 1, 'nome_medico': 'João', 'numero_guia': 4, 'dt_consulta': '04/11/2017', 'valor_consulta': 5.0, 'gasto_consulta': 45.0},
            {'qt_exames': 1, 'nome_medico': 'João', 'numero_guia': 3, 'dt_consulta': '12/03/2018', 'valor_consulta': 90.0, 'gasto_consulta': 39.0},
            {'qt_exames': 0, 'nome_medico': 'Ademar', 'numero_guia': 5, 'dt_consulta': '17/11/2018', 'valor_consulta': 5.0, 'gasto_consulta': 0},
            {'qt_exames': 0, 'nome_medico': 'Marcos', 'numero_guia': 6, 'dt_consulta': '17/11/2018', 'valor_consulta': 5.0, 'gasto_consulta': 0},
            {'qt_exames': 0, 'nome_medico': 'João', 'numero_guia': 2, 'dt_consulta': '22/04/2018', 'valor_consulta': 22.0, 'gasto_consulta': 0}
        ]
        url = reverse('report')
        response = self.client.get(url)
        self.assertEqual(response.data, expected)

    @parameterized.expand([
        ("João", '01/11/2017 - 04/01/2018', "", "",
         [{'qt_exames': 1, 'nome_medico': 'João', 'numero_guia': 4,
           'dt_consulta': '04/11/2017', 'valor_consulta': 5.0,
           'gasto_consulta': 45.0}]
         ),
        ("Marcos", "", "", "",
         [{'qt_exames': 0, 'nome_medico': 'Marcos', 'numero_guia': 6,
           'dt_consulta': '17/11/2018', 'valor_consulta': 5.0,
           'gasto_consulta': 0}]
         ),
        ("João", "", "", "0",
         [{'qt_exames': 0, 'nome_medico': 'João', 'numero_guia': 2,
           'dt_consulta': '22/04/2018', 'valor_consulta': 22.0,
           'gasto_consulta': 0}]
         ),
    ])
    def test_get_report_without_filters(self, nome_medico, intervalo_consulta,
                                        valor_consulta, qt_exames, expected):
        paylolad = {
            'nome_medico': nome_medico,
            'intervalo_consulta': intervalo_consulta,
            'qtd_exames_ate': qt_exames,
            'valor_consulta_ate': valor_consulta
        }
        url = reverse('report')
        response = self.client.get(url, paylolad)
        self.assertEqual(response.data, expected)
