# Generated by Django 2.0.3 on 2018-04-13 18:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('inicio_data', models.DateField(default=None)),
                ('fim_data', models.DateField(default=None)),
                ('ano', models.PositiveIntegerField(default=2018)),
                ('criado_em', models.DateField(default=datetime.datetime(2018, 4, 13, 18, 14, 41, 282123, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'Contratos',
                'ordering': ('numero',),
            },
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('ano', models.PositiveIntegerField(default=2018)),
                ('criado_em', models.DateField(default=datetime.datetime(2018, 4, 13, 18, 14, 41, 282893, tzinfo=utc))),
                ('contrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licitacao.Contrato')),
            ],
            options={
                'verbose_name_plural': 'Modalidades',
                'ordering': ('tipo', 'ano', 'numero'),
            },
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('objeto', models.TextField()),
                ('ano', models.PositiveIntegerField(default=2018)),
                ('criado_em', models.DateField(default=datetime.datetime(2018, 4, 13, 18, 14, 41, 281488, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'Processos',
                'ordering': ('numero',),
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('criado_em', models.DateField(default=datetime.datetime(2018, 4, 13, 18, 14, 41, 280910, tzinfo=utc))),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='processo',
            unique_together={('ano', 'numero')},
        ),
        migrations.AddField(
            model_name='modalidade',
            name='processo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='licitacao.Processo'),
        ),
        migrations.AddField(
            model_name='modalidade',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licitacao.Tipo'),
        ),
        migrations.AlterUniqueTogether(
            name='contrato',
            unique_together={('ano', 'numero')},
        ),
        migrations.AlterUniqueTogether(
            name='modalidade',
            unique_together={('ano', 'tipo', 'numero')},
        ),
    ]
