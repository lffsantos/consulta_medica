from django.db import models


class Consulta(models.Model):
    numero_guia_consulta = models.IntegerField(primary_key=True)
    cod_medico = models.IntegerField(null=False)
    nome_medico = models.CharField(max_length=255, null=True)
    data_consulta = models.DateField(null=False)
    valor_consulta = models.FloatField(null=True)

    def __str__(self):
        return f'{self.numero_guia_consulta}'

    class Meta:
        ordering = ["-data_consulta"]


class Exame(models.Model):
    cod_exame = models.IntegerField()
    valor_exame = models.FloatField(null=True)
    numero_guia_consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE, related_name='exames')

    def __str__(self):
        return f'{self.cod_exame} - {self.numero_guia_consulta_id}'

    class Meta:
        ordering = ["-cod_exame"]
        unique_together = (("cod_exame", "numero_guia_consulta"),)
