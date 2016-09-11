# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-11 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predio', '0020_auto_20160910_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uso_ocup_predios',
            name='up_edificacion',
        ),
        migrations.AddField(
            model_name='serv_instal_predios',
            name='sp_num_med_prin_agua',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='serv_instal_predios',
            name='sp_num_med_prin_elec',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='serv_instal_predios',
            name='sp_num_medidores_agua',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='serv_instal_predios',
            name='sp_num_medidores_elec',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carac_fisi_predios',
            name='fi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='carac_princ_edific',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='fichas',
            name='pr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Propietarios'),
        ),
        migrations.AlterField(
            model_name='ident_divisiones',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='infra_serv_vias',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='ir_internas',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='ir_otras',
            name='fi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='linderos',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='maq_equipos',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='observaciones',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='ref_cartog',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='responsables',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='semovientes',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='serv_instal_predios',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='situ_legal',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='ubicaciones',
            name='fi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
        migrations.AlterField(
            model_name='uso_ocup_predios',
            name='fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='predio.Fichas'),
        ),
    ]