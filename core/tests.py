from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import Consulta


class ConssultaMedica(APITestCase):
    def test_get_doctors_name(self):
        doctor_names = ['João', 'Pedro', 'Marcos', 'Ademar', 'Pedro']
        for name in doctor_names:
            mommy.make(Consulta, nome_medico=name)

        url = reverse('doctors')
        response = self.client.get(url)

        self.assertEqual(response.data, sorted(list(set(doctor_names))))
