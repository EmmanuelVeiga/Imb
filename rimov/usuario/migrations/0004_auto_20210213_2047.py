# Generated by Django 3.1.6 on 2021-02-13 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20210206_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='tipo',
            field=models.CharField(choices=[('ADM', 'Administrador'), ('COR', 'Corretor')], default='CORRETOR', help_text='Campos obrigatórios', max_length=15, verbose_name='tipo de funcionário'),
        ),
    ]
