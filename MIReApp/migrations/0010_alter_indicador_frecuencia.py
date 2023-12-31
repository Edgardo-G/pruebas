# Generated by Django 4.2.4 on 2023-08-30 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MIReApp', '0009_indicador_frecuencia_alter_indicador_ambito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='frecuencia',
            field=models.CharField(choices=[('Bianual', 'Bianual'), ('Anual', 'Anual'), ('Semestral', 'Semestral'), ('Mensual', 'Mensual')], default='Anual', max_length=10, verbose_name='Frecuencia de medición'),
        ),
    ]
