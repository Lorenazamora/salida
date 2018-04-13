from django.shortcuts import render, redirect	
from django.contrib.auth import login, logout, authenticate 
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers

def vista_lista_Producto(request):
	lista= Producto.objects.filter()
	return render(request,'lista_producto.html', locals())

def vista_lista_Marca(request):
	listar= Marca.objects.filter()
	return render(request,'lista_marca.html', locals())

def vista_lista_Categoria(request):
	lista2= Categoria.objects.filter()
	return render(request,'lista_categoria.html', locals())

def vista_agregar_producto(request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)
		if formulario.is_valid():
			prod = formulario.save(commit = False)
			#prod.status = True
			prod.save()
			formulario.save_m2m()
			return redirect ('/lista_producto/')

	else:
		formulario = agregar_producto_form()
	return render(request, 'agregar_Producto.html', locals())

def vista_ver_producto(request, id_prod):
	p=Producto.objects.get(id=id_prod)
	return render(request,'ver_producto.html', locals())

def vista_editar_producto(request, id_prod):
	prod=Producto.objects.get(id=id_prod)
	if request.method =='POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			prod=formulario.save()
			return redirect ('/lista_producto/')
	else:
		formulario = agregar_producto_form(instance= prod)
		return render(request, 'agregar_producto.html', locals())

def vista_eliminar_producto(request, id_prod):
	prod = Producto.objects.get(id=id_prod)
	prod.delete()
	return redirect('/lista_producto/', locals())

def vista_login(request):
	usu= ""
	cla=""
	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario =authenticate(username = usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/admin/')
			else:
				msj = "usuario o clave incorrectos"
	formulario = login_form()
	return render(request, 'login.html', locals())

def vista_logout(request):
	logout(request)
	return redirect('/login/')


def vista_registrar(request):
	formulario = Registrar_form()
	if request.method == "POST":
		formulario = Registrar_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo = formulario.cleaned_data['email']
			password_one= formulario.cleaned_data['password_one']
			password_two= formulario.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario, email=correo, password=password_one)
			u.save()
			return render(request, 'thanks_for_registrar.html', locals())
		
	return  render(request, 'registrar.html', locals())

def ws_productos_vista(request):
	data = serializers.serialize('json', Producto.objects.filter(status=True))
	return HttpResponse(data, content_type='application/json')




