# Generated by Django 3.2.20 on 2023-09-01 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MIReApp', '0010_alter_indicador_frecuencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='indicador',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, verbose_name='Descripción'),
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('ambito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MIReApp.ambito')),
            ],
        ),
        migrations.AlterField(
            model_name='indicador',
            name='ambito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MIReApp.ambito'),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MIReApp.tipo'),
        ),
    ]