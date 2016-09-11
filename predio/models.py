from django.db import models

class Propietarios(models.Model):
	pr_id=models.AutoField(primary_key=True)
	pr_dni=models.CharField(max_length=10, null=True, unique=True)
	pr_apellido=models.CharField(max_length=45)
	pr_nombre=models.CharField(max_length=45, null=True)
	pr_fec_nac=models.DateField(null=True)
	pr_prop_ant=models.CharField(max_length=50, null=True)
	pr_dir=models.CharField(max_length=50, null=True)
	pr_tel=models.CharField(max_length=10, null=True)
	pr_email=models.CharField(max_length=40, null=True)
	pr_residencia_pro=models.CharField(max_length=20, null=True)
	pr_rep_legal_dni=models.CharField(max_length=10, default='', null=True)
	pr_rep_legal_nombre=models.CharField(max_length=50, default='', null=True)
	pr_rep_legal_dir=models.CharField(max_length=50, default='', null=True)

class Fichas(models.Model):
	fi_id=models.AutoField(primary_key=True)
	pr=models.ForeignKey('Propietarios', null=True)
	fi_cod_prov=models.CharField(max_length=3)
	fi_cod_can=models.CharField(max_length=3)
	fi_cod_par=models.CharField(max_length=3)
	fi_cod_zon=models.CharField(max_length=3)
	fi_cod_sec=models.CharField(max_length=3)
	fi_cod_pol=models.CharField(max_length=3)
	fi_cod_pre=models.CharField(max_length=3)
	fi_cod_div=models.CharField(max_length=3)
	fi_cod_ant_pre=models.CharField(max_length=20, null=True)

class Ubicaciones(models.Model):
	ub_id = models.AutoField(primary_key=True)
	fi = models.ForeignKey('Fichas', null=True)
	ub_cod_sector = models.CharField(max_length=45, blank=True, null=True)
	ub_nombre_sector = models.CharField(max_length=45, blank=True, null=True)
	ub_cod_via = models.CharField(max_length=45, blank=True, null=True)
	ub_nombre_via = models.CharField(max_length=45, blank=True, null=True)
	ub_nombre_predio = models.CharField(max_length=45, blank=True, null=True)
	ub_coordenadas_x = models.FloatField(blank=True, null=True)
	ub_coordenadas_y = models.FloatField(blank=True, null=True)

class Ref_Cartog(models.Model):
    rc_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    rc_descripcion = models.CharField(max_length=45, blank=True, null=True)
    rc_cod = models.CharField(max_length=45, blank=True, null=True)

class Linderos(models.Model):
    li_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    li_punto_card = models.CharField(max_length=45, blank=True, null=True)
    li_nom_propietario = models.CharField(max_length=60, blank=True, null=True)

class Situ_Legal(models.Model):
    sl_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    sl_dominio = models.CharField(max_length=45, blank=True, null=True)
    sl_desc_tenencia = models.CharField(max_length=45, blank=True, null=True)
    sl_trans_dominio = models.CharField(max_length=45, blank=True, null=True)
    sl_tipo_tenencia = models.CharField(max_length=45, blank=True, null=True)

class Escrituras(models.Model):
    es_id = models.AutoField(primary_key=True)
    sl = models.ForeignKey('Situ_Legal', blank=True, null=True)
    es_nro_notaria = models.CharField(max_length=45, blank=True, null=True)
    es_canton = models.CharField(max_length=45, blank=True, null=True)
    es_nro_reg_prop = models.CharField(max_length=45, blank=True, null=True)
    es_fecha = models.CharField(max_length=45, blank=True, null=True)

class Ident_Divisiones(models.Model):
    id_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    id_aprobacion = models.CharField(max_length=45, blank=True, null=True)
    id_responsable_aprob = models.CharField(max_length=45, blank=True, null=True)
    id_fecha_aprobacion = models.CharField(max_length=45, blank=True, null=True)
    id_nombre_lotizacion = models.CharField(max_length=45, blank=True, null=True)
    id_nro_lote = models.CharField(max_length=45, blank=True, null=True)
    id_cod_jace = models.CharField(max_length=45, blank=True, null=True)

class Ir_Internas(models.Model):
    iri_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    iri_cod = models.CharField(max_length=45, blank=True, null=True)
    iri_desc = models.CharField(max_length=45, blank=True, null=True)
    iri_tipo_mat = models.CharField(max_length=45, blank=True, null=True)
    iri_cant = models.FloatField(blank=True, null=True)
    iri_unidad = models.FloatField(blank=True, null=True)
    iri_estado = models.CharField(max_length=45, blank=True, null=True)

class Carac_Fisi_Predios(models.Model):
    cfi_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', null=True)
    cfi_form_predio = models.CharField(max_length=45, blank=True, null=True)
    cfi_topografia = models.CharField(max_length=45, blank=True, null=True)
    cfi_tipo_riesgo = models.CharField(max_length=45, blank=True, null=True)
    cfi_erosion = models.CharField(max_length=45, blank=True, null=True)

class Desc_Predios(models.Model):
    dp_id = models.AutoField(primary_key=True)
    cfi = models.ForeignKey('Carac_Fisi_Predios', null=True)
    dp_sect_homo = models.CharField(max_length=45, blank=True, null=True)
    dp_cal_suelo = models.CharField(max_length=45, blank=True, null=True)
    dp_superficie = models.FloatField(blank=True, null=True)

class Ir_Otras(models.Model):
    iro_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', null=True)
    iro_cod = models.CharField(max_length=45, blank=True, null=True)
    iro_desc = models.CharField(max_length=45, blank=True, null=True)
    iro_superficie = models.CharField(max_length=45, blank=True, null=True)
    iro_unid = models.CharField(max_length=45, blank=True, null=True)
    iro_cant = models.CharField(max_length=45, blank=True, null=True)

class Serv_Instal_Predios(models.Model):
    sp_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    sp_abast_agua = models.CharField(max_length=45, blank=True, null=True)
    sp_num_medidores_agua=models.IntegerField(blank=True, null=True)
    sp_num_med_prin_agua=models.CharField(max_length=45, blank=True, null=True)
    sp_evac_agua_servida = models.CharField(max_length=45, blank=True, null=True)
    sp_energia_elect = models.CharField(max_length=45, blank=True, null=True)
    sp_num_medidores_elec=models.IntegerField(blank=True, null=True)
    sp_num_med_prin_elec=models.CharField(max_length=45, blank=True, null=True)
    sp_num_lineas_tel=models.IntegerField(blank=True, null=True)
    sp_num_telf_prin=models.CharField(max_length=15, blank=True, null=True)
    sp_riego = models.CharField(max_length=45, blank=True, null=True)

class Infra_Serv_Vias(models.Model):
    iv_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    iv_tipo_vial = models.CharField(max_length=45, blank=True, null=True)
    iv_mat_calzada = models.CharField(max_length=45, blank=True, null=True)
    iv_agua_consumo_hum = models.CharField(max_length=45, blank=True, null=True)
    iv_energia_electrica = models.CharField(max_length=45, blank=True, null=True)
    iv_alumbrado_public = models.CharField(max_length=45, blank=True, null=True)
    iv_estado_via = models.CharField(max_length=45, blank=True, null=True)
    iv_pobla_cerca_predio = models.CharField(max_length=45, blank=True, null=True)
    iv_alcantarillado = models.CharField(max_length=45, blank=True, null=True)
    iv_telefonia = models.CharField(max_length=45, blank=True, null=True)
    iv_mat_poste_predio = models.CharField(max_length=45, blank=True, null=True)
    iv_nro_poste_predio = models.CharField(max_length=45, blank=True, null=True)
    iv_transporte_public = models.CharField(max_length=45, blank=True, null=True)

#observar esta tabla
class Carac_Princ_Edific(models.Model):
    cr_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    cr_nro_bloque = models.CharField(max_length=45, blank=True, null=True)
    cr_nro_piso = models.CharField(max_length=45, blank=True, null=True)
    cr_cod_uso = models.CharField(max_length=45, blank=True, null=True)
    cr_uso = models.CharField(max_length=45, blank=True, null=True)
    cr_area_piso = models.FloatField(blank=True, null=True)
    cr_area_bloque = models.FloatField(blank=True, null=True)
    cr_mat_estruc_viga = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_estruc_columna = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_estruc_pared = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_estruc_entrepiso = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_acab_piso = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_acab_puerta = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_acab_ventana = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_acab_enlucido = models.CharField(max_length=45, blank=True, null=True)
    cr_mat_acab_cielorraso = models.CharField(max_length=45, blank=True, null=True)
    cr_instal_electrica = models.CharField(max_length=45, blank=True, null=True)
    cr_instal_sanitaria = models.CharField(max_length=45, blank=True, null=True)
    cr_instal_banio = models.CharField(max_length=45, blank=True, null=True)
    cr_estado = models.CharField(max_length=45, blank=True, null=True)
    cr_anio_constr = models.CharField(max_length=45, blank=True, null=True)

class Observaciones(models.Model):
    ob_id = models.AutoField(primary_key=True)
    ob_desc = models.CharField(max_length=45, blank=True, null=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)

class Responsables(models.Model):
    re_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    re_empadronado = models.CharField(max_length=45, blank=True, null=True)
    re_fecha_emp = models.DateField(blank=True, null=True)
    re_revisado = models.CharField(max_length=45, blank=True, null=True)
    re_fecha_rev = models.DateField(blank=True, null=True)
    re_digitado = models.CharField(max_length=45, blank=True, null=True)
    re_fecha_dig = models.DateField(blank=True, null=True)
    re_jefe_avaluo_catas = models.CharField(max_length=45, blank=True, null=True)
    re_fecha_jefe_aval_catas = models.DateField(blank=True, null=True)

class Semovientes(models.Model):
    se_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    se_especie = models.CharField(max_length=45, blank=True, null=True)
    se_raza = models.CharField(max_length=45, blank=True, null=True)
    se_edad = models.IntegerField(blank=True, null=True)
    se_sangre = models.CharField(max_length=45, blank=True, null=True)
    se_numero = models.CharField(max_length=45, blank=True, null=True)

class Maq_Equipos(models.Model):
    mq_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    mq_denomicacion = models.CharField(max_length=45, blank=True, null=True)
    mq_marca = models.CharField(max_length=45, blank=True, null=True)
    mq_anio = models.CharField(max_length=45, blank=True, null=True)
    mq_estado = models.CharField(max_length=45, blank=True, null=True)
    mq_numero = models.CharField(max_length=45, blank=True, null=True)

class Uso_Ocup_Predios(models.Model):
    up_id = models.AutoField(primary_key=True)
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    up_cod_economico = models.CharField(max_length=45, blank=True, null=True)
    up_desc_economico = models.CharField(max_length=45, blank=True, null=True)
    up_tipo_usuario = models.CharField(max_length=45, blank=True, null=True)
    up_nro_bloq_terminado = models.CharField(max_length=45, blank=True, null=True)
    up_nro_bloq_construccion = models.CharField(max_length=45, blank=True, null=True)

class Uso_Actual_Predios(models.Model):
    uap_id = models.AutoField(primary_key=True)
    up = models.ForeignKey('Uso_Ocup_Predios', blank=True, null=True)
    uap_uso_general = models.CharField(max_length=45, blank=True, null=True)
    uap_detalle_uso = models.CharField(max_length=45, blank=True, null=True)
    uap_edad = models.CharField(max_length=45, blank=True, null=True)
    uap_conservacion = models.CharField(max_length=45, blank=True, null=True)
    uap_extencion = models.FloatField(blank=True, null=True)
    uap_porcentaje = models.FloatField(blank=True, null=True)