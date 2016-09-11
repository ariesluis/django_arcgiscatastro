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
def insertar_propietario(request):
	#datetime.datetime.today().strftime('%Y-%m-%d') obtener fecha sistema
	#datos propietario
	pr_dni=request.POST.get('dni','')
	pr_apellido=request.POST.get('apellidos','')
	pr_nombre=request.POST.get('nombre','')
	pr_fec_nac=request.POST.get('fecha_nac','')
	pr_email=request.POST.get('email','')
	pr_tel=request.POST.get('phone','')
	pr_dir=request.POST.get('address','')
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

def insertar_predio(request):
	fi_id=1
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
	pr=Propietarios.objects.latest('pr_id')
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