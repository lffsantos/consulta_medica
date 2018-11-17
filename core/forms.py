from datetime import datetime
from operator import itemgetter

from django import forms
from django.db.models import Sum

from core.models import Consulta


class ReportForm(forms.Form):
    intervalo_consulta = forms.CharField(label="intervalo_consulta", required=False)
    valor_consulta_ate = forms.CharField(label="valor_consulta_ate", required=False)
    qtd_exames_ate = forms.CharField(label="qtd_exames", required=False)
    nome_medico = forms.CharField(label="nome_medico", required=False)

    def filter_consulta(self):
        data = self.cleaned_data
        intervalo_consulta = data.get('intervalo_consulta')
        valor_consulta_ate = data.get('valor_consulta')
        qtd_exames_ate = data.get('qtd_exames_ate')
        nome_medico = data.get('nome_medico')
        query_params = {}
        if nome_medico:
            query_params.update({'nome_medico': nome_medico})
        if valor_consulta_ate:
            query_params.update({'valor_consulta__lte': valor_consulta_ate})

        if intervalo_consulta:
            inicio_consulta = intervalo_consulta.split('-')[0].strip()
            fim_consulta = intervalo_consulta.split('-')[1].strip()
            query_params.update({
                'data_consulta__gte': datetime.strptime(inicio_consulta, '%d/%m/%Y'),
                'data_consulta__lte': datetime.strptime(fim_consulta, '%d/%m/%Y')
            })

        consultas_realizadas = Consulta.objects.filter(**query_params)
        result = []
        for consulta in consultas_realizadas:
            exames = consulta.exames.all()
            content = {
                "qt_exames": len(exames) if exames else 0
            }
            if not qtd_exames_ate or content['qt_exames'] <= int(qtd_exames_ate):
                content.update({
                    'nome_medico': consulta.nome_medico,
                    'numero_guia': consulta.numero_guia_consulta,
                    'dt_consulta': consulta.data_consulta.strftime('%d/%m/%Y'),
                    'valor_consulta': consulta.valor_consulta,
                    'gasto_consulta': consulta.exames.all().aggregate(Sum('valor_exame'))['valor_exame__sum'] or 0,
                })
                result.append(content)
        ordered_result = sorted(result, key=itemgetter('gasto_consulta'), reverse=True)

        return ordered_result
