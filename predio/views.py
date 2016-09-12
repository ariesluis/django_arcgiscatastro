from django.shortcuts import render
from .models import Propietarios
from .models import Fichas
import datetime

#metodos redireccionamientos
def insert_predio(request):
	return render(request, 'predio/insert_predio.html',{})

def index(request):
	return render(request, 'predio/index.html',{})

def insert_propietario(request):
	return render(request, 'predio/insert_propietario.html',{})


#metodos manejo de la DB

#insertar propietario
def insertar_propietario(request):
	#datetime.datetime.today().strftime('%Y-%m-%d') obtener fecha sistema
	#datos propietario
	pr_fec_nac=datetime.datetime.today().strftime('%Y-%m-%d')

	pr_dni=request.POST.get('dni','')
	pr_apellido=request.POST.get('apellidos','')
	pr_nombre=request.POST.get('nombre','')
	pr_fec_nac=request.POST.get('fecha_nac','')
	pr_email=request.POST.get('email','')
	pr_tel=request.POST.get('phone','')
	pr_dir=request.POST.get('res_pro','')
	pr_res=request.POST.get('city','')
	pr_id=1
	# dato propietario anterior
	pr_prop_ant=request.POST.get('nom_ape_ant_pro','')
	#traer el ultimo propietario guardado para obtener su id
	try:
		propietario=Propietarios.objects.latest('pr_id')
		pr_id=propietario.pr_id+1
	except Propietarios.DoesNotExist:
		pass
	#datos representante legal
	re_dni=request.POST.get('dni_rep','')
	re_nom=request.POST.get('nom_ape_rep','')
	re_dir=request.POST.get('address_rep','')

	Propietarios.objects.create(
		pr_id=pr_id,
		pr_dni=pr_dni,
		pr_apellido=pr_apellido,
		pr_nombre=pr_nombre,
		pr_fec_nac=pr_fec_nac,
		pr_prop_ant=pr_prop_ant,
		pr_dir=pr_dir,
		pr_tel=pr_tel,
		pr_email=pr_email,
		pr_residencia_pro=pr_res,
		pr_rep_legal_dir=re_dir,
		pr_rep_legal_dni=re_dni,
		pr_rep_legal_nombre=re_nom
	)
	return render(request, 'predio/index.html',{})

propietario_global=None #variable global que contiene el propietario
#buscar propietario y asignacion a una variable global 
def buscarPropietarioPredio(request):
	cad=request.POST.get('ci_ape','')
	propietario=None
	if cad.isdigit():
		propietario=Propietarios.objects.get(pr_dni=cad)
	else:
		propietario=Propietarios.objects.get(pr_apellido=cad)
	global propietario_global
	propietario_global=propietario
	return render(request, 'predio/insert_predio.html',{'propietario':propietario})

ficha_global=None #variable glogal que contiene el cod predio
def insertar_predio(request):
	fi_id=1
	#ultimo id guardado
	try:
		ficha=Fichas.objects.latest('fi_id')
		fi_id=ficha.fi_id+1
	except Fichas.DoesNotExist:
		pass
	fi_cod_prov=request.POST.get('cod_prov','')
	fi_cod_can=request.POST.get('cod_can','')
	fi_cod_par=request.POST.get('cod_par','')
	fi_cod_zon=request.POST.get('cod_zon','')
	fi_cod_sec=request.POST.get('cod_sec','')
	fi_cod_pol=request.POST.get('cod_man','')
	fi_cod_pre=request.POST.get('cod_pre','')
	fi_cod_div=request.POST.get('cod_div','')
	fi_cod_ant_pre=request.POST.get('cod_ant','')
	pr=prop
	Fichas.objects.create(
		fi_cod_prov=fi_cod_prov,
		fi_cod_can=fi_cod_can,
		fi_cod_par=fi_cod_par,
		fi_cod_zon=fi_cod_zon,
		fi_cod_sec=fi_cod_sec,
		fi_cod_pol=fi_cod_pol,
		fi_cod_pre=fi_cod_pre,
		fi_cod_div=fi_cod_div,
		fi_cod_ant_pre=fi_cod_ant_pre,
		pr=pr
	)
	global ficha_global
	ficha_global=Fichas.objects.latest('fi_id')
	return render(request, 'predio/index.html',{})

def insertar_ubicacion(request):
	ub_id=1
	try:
		ubicacion=Ubicaciones.objects.latest('ub_id')
		ub_id=ubicacion.ub_id+1
	except Ubicaciones.DoesNotExist:
		pass
	cod_sitio=request.POST.get('cod_sitio','')
	nom_sitio=request.POST.get('nom_sitio','')
	cod_via=request.POST.get('cod_via','')
	nom_via=request.POST.get('nom_via','')
	nom_predio=request.POST.get('nom_predio','')
	x=request.POST.get('coor_x','')
	y=request.POST.get('coor_y','')
	Ubicaciones.objects.create(
		ub_id=ub_id,
		ub_cod_sector=cod_sec,
		ub_nombre=nom_sitio,
		ub_cod_via=cod_via,
		ub_nombre_via=nom_via,
		ub_nombre_predio=nom_predio,
		ub_coordenadas_x=x,
		ub_coordenadas_y=y,
		fi=ficha_global
	)

def insertar_lindero(request):
	nom_norte=request.POST.get('lin_norte','')
	nom_sur=request.POST.get('lin_sur','')
	nom_este=request.POST.get('lin_este','')
	nom_oeste=request.POST.get('lin_oeste','')
	if len(nom_norte)!=0:
		li_id=1;
		try:
			lindero=Linderos.objects.latest('li_id')
			li_id=lindero.li_id+1
		except Linderos.DoesNotExist:
			pass
		Linderos.objects.create(
			li_id=li_id,
			li_punto_card="norte",
			li_nom_propietario=nom_norte,
			fi=ficha_global
		)
	if len(nom_sur)!=0:
		li_id=1;
		try:
			lindero=Linderos.objects.latest('li_id')
			li_id=lindero.li_id+1
		except Linderos.DoesNotExist:
			pass
		Linderos.objects.create(
			li_id=li_id,
			li_punto_card="sur",
			li_nom_propietario=nom_sur,
			fi=ficha_global
		)
	if len(nom_este)!=0:
		li_id=1;
		try:
			lindero=Linderos.objects.latest('li_id')
			li_id=lindero.li_id+1
		except Linderos.DoesNotExist:
			pass
		Linderos.objects.create(
			li_id=li_id,
			li_punto_card="este",
			li_nom_propietario=nom_este,
			fi=ficha_global
		)
	if len(nom_oeste)!=0:
		li_id=1;
		try:
			lindero=Linderos.objects.latest('li_id')
			li_id=lindero.li_id+1
		except Linderos.DoesNotExist:
			pass
		Linderos.objects.create(
			li_id=li_id,
			li_punto_card="oeste",
			li_nom_propietario=nom_oeste,
			fi=ficha_global
		)

def insertar_referencia_cartografica(request):
	c_topo=request.POST.get('c_top','')
	img_sat=request.POST.get('img_sat','')
	fot_area=request.POST.get('fot_area','')
	otro=request.POST.get('otro_ref_car','')
	if len(c_topo)!=0:
		rc_id=1;
		try:
			referencia=Ref_Cartog.objects.latest('rc_id')
			rc_id=referencia.rc_id+1
		except Ref_Cartog.DoesNotExist:
			pass
		Ref_Cartog.objects.create(
			rc_id=rc_id,
			rc_descripcion="Carta Topografica",
			rc_cod=c_topo,
			fi=ficha_global
		)
	if len(img_sat)!=0:
		rc_id=1;
		try:
			referencia=Ref_Cartog.objects.latest('rc_id')
			rc_id=referencia.rc_id+1
		except Ref_Cartog.DoesNotExist:
			pass
		Ref_Cartog.objects.create(
			rc_id=rc_id,
			rc_descripcion="Imagen Satelital",
			rc_cod=img_sat,
			fi=ficha_global
		)
	if len(fot_area)!=0:
		rc_id=1;
		try:
			referencia=Ref_Cartog.objects.latest('rc_id')
			rc_id=referencia.rc_id+1
		except Ref_Cartog.DoesNotExist:
			pass
		Ref_Cartog.objects.create(
			rc_id=rc_id,
			rc_descripcion="Foto area",
			rc_cod=fot_area,
			fi=ficha_global
		)
	if len(otro)!=0:
		rc_id=1;
		try:
			referencia=Ref_Cartog.objects.latest('rc_id')
			rc_id=referencia.rc_id+1
		except Ref_Cartog.DoesNotExist:
			pass
		Ref_Cartog.objects.create(
			rc_id=li_id,
			rc_descripcion="otro",
			rc_cod=otro,
			fi=ficha_global
		)

def insertar_situacion_legal(request):
	sl_id=1;
	try:
		legal=Situ_Legal.objects.latest('sl_id')
		sl_id=legal.sl_id+1
	except Situ_Legal.DoesNotExist:
		pass
	sl_dominio = request.POST.get('dominio','')
	sl_desc_tenencia = request.POST.get('desc_tenencia','')
	sl_trans_dominio = request.POST.get('trans_dom','')
	sl_tipo_tenencia = request.POST.get('tip_tenencia','')
	Situ_Legal.objects.create(
		sl_id=sl_id,
		sl_dominio=sl_dominio,
		sl_desc_tenencia=sl_desc_tenencia,
		sl_trans_dominio=sl_trans_dominio,
		sl_tipo_tenencia=sl_tipo_tenencia,
		fi=ficha_global
	)

def insertar_escritura(request):
	nro_notaria=request.POST.get('num_not','')
	nro_reg_propiedad=request.POST.get('num_re_pro','')
	if len(nro_notaria)!=0 and len(nro_reg_propiedad)!=0:
		es_id=1
		try:
			escritura=Escrituras.objects.latest('es_id')
			es_id=escritura.es_id+1
		except Escrituras.DoesNotExist:
			pass
		es_canton=request.POST.get('not_canton','')
		es_fecha=request.POST.get('fecha_notaria','')
		Escrituras.objects.create(
			es_id=es_id,
			es_nro_notaria=nro_notaria,
			es_canton=es_canton,
			es_nro_reg_prop=nro_reg_propiedad,
			sl=Situ_Legal.objects.latest('sl_id')
		)

def insertar_divisiones(request):
	id_id=1
	try:
		divisiones=Ident_Divisiones.objects.latest('id_id')
		id_id=divisiones.id_id+1
	except Ident_Divisiones.DoesNotExist:
		pass
	responsable=request.POST.get('res_aprob','')
	nom_lot=request.POST.get('nom_lot','')
	if len(responsable)!=0 and len(nom_lot)!=0:
		fecha_apro=request.POST.get('fec_aprob','')
		nro_lote=request.POST.get('nro_lote','')
		Ident_Divisiones.objects.create(
			id_id=id_id,
			id_responsable_aprob=responsable,
			id_fecha_aprobacion=fecha_apro,
			id_nombre_lotizacion=nom_lot,
			id_nro_lote=nro_lote,
			fi=ficha_global
		)

def insertar_uso_predio(request):
	up_id=1
	try:
		uso_predio=Uso_Ocup_Predios.objects.latest('up_id')
		up_id=uso_predio.up_id+1
	except Uso_Ocup_Predios.DoesNotExist:
		pass
	cod_eco=request.POST.get('cod_det_eco','')
	desc_eco=request.POST.get('desc_det_eco','')
	tip_usu=request.POST.get('tip_usuario','')
	nro_term=request.POST.get('nro_bloq_term','')
	nro_cons=request.POST.get('num_bloq_cons','')
	Uso_Ocup_Predios.objects.create(
		up_id=up_id,
		up_cod_economico=cod_eco,
		up_desc_economico=desc_eco,
		up_tipo_usuario=tip_usu,
		up_nro_bloq_terminado=nro_term,
		up_nro_bloq_construccion=nro_cons,
		fi=ficha_global
	)

def insertar_caracteristicas_predio(request):
	cfi_id=1
	try:
		carac_predio=Carac_Fisi_Predios.objects.latest('cfi_id')
		cfi_id=carac_predio.cfi_id+1
	except Carac_Fisi_Predios.DoesNotExist:
		pass
	cfi_form_predio = request.POST.get('forma_predio','')
	cfi_topografia = request.POST.get('topog_predio','')
	cfi_tipo_riesgo = request.POST.get('tip_riesgo','')
	cfi_erosion = request.POST.get('erosion_predio','')
	Carac_Fisi_Predios.objects.create(
    	cfi_id=cfi_id,
    	cfi_form_predio=cfi_form_predio,
    	cfi_topografia=cfi_topografia,
    	cfi_tipo_riesgo=cfi_tipo_riesgo,
    	cfi_erosion=cfi_erosion,
    	fi=ficha_global
    )

def insertar_infraestructura_via(request):
	iv_id = 1
	try:
		infra_via=Infra_Serv_Vias.objects.latest('iv_id')
		iv_id=infra_via.iv_id+1
	except Infra_Serv_Vias.DoesNotExist:
		pass
    fi = models.ForeignKey('Fichas', blank=True, null=True)
    iv_tipo_vial = request.POST.get('tip_riesgo','')
    iv_mat_calzada = request.POST.get('tip_riesgo','')
    iv_agua_consumo_hum = request.POST.get('tip_riesgo','')
    iv_energia_electrica = request.POST.get('tip_riesgo','')
    iv_alumbrado_public = request.POST.get('tip_riesgo','')
    iv_estado_via = request.POST.get('tip_riesgo','')
    iv_pobla_cerca_predio = request.POST.get('tip_riesgo','')
    iv_alcantarillado = request.POST.get('tip_riesgo','')
    iv_telefonia = request.POST.get('tip_riesgo','')
    iv_mat_poste_predio = request.POST.get('tip_riesgo','')
    iv_nro_poste_predio = request.POST.get('tip_riesgo','')
    iv_transporte_public = request.POST.get('tip_riesgo','')