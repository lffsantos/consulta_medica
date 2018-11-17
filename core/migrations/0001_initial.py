# Generated by Django 2.1.3 on 2018-11-17 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('numero_guia_consulta', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_medico', models.IntegerField()),
                ('nome_medico', models.CharField(max_length=255, null=True)),
                ('data_consulta', models.DateField(null=True)),
                ('valor_consulta', models.FloatField(null=True)),
            ],
            options={
                'verbose_name_plural': 'oxen',
                'ordering': ['-data_consulta'],
            },
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_exame', models.IntegerField()),
                ('valor_exame', models.FloatField(null=True)),
                ('numero_guia_consulta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Consulta')),
            ],
            options={
                'ordering': ['-numero_guia_consulta'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='exame',
            unique_together={('cod_exame', 'numero_guia_consulta')},
        ),
    ]
