# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-06 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0014_auto_20160906_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichas',
            name='pr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Propietarios'),
        ),
        migrations.AlterField(
            model_name='propietarios',
            name='pr_dni',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
