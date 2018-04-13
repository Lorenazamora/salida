from django import forms
from .models import *
from django.contrib.auth.models import User


#//____________segir con el formulario..... no se olvide bitch :P jajajaj______

class contacto_form(forms.Form):
	correo = forms.EmailField(widget=forms.TextInput())
	tema = forms.CharField(widget=forms.TextInput())
	texto = forms.EmailField(widget=forms.Textarea())


class formulario_form(forms.Form):
	nombres = forms.CharField(widget=forms.TextInput())
	edad= forms.IntegerField(min_value=0, max_value =100, widget=forms.NumberInput())
	Fecha_Nacimiento = forms.SplitDateTimeField(widget=forms.SelectDateWidget())
	celular = forms.IntegerField(max_value =99999999999999, widget=forms.TextInput())
	#sexo=forms.extend([('a',1),('b',2),('c',3)])
	Forever_Alone = forms.BooleanField()
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput())
	correo = forms.EmailField(widget=forms.TextInput())


class agregar_producto_form(forms.ModelForm):
	#status= forms.BooleanField()
	class Meta:
		model = Producto
		exclude =["status"]
		fields = '__all__'





class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave = forms.CharField(widget=forms.PasswordInput(render_value=False))


class Registrar_form(forms.Form):
	username= forms.CharField(widget=forms.TextInput())
	email = forms.EmailField(widget=forms.TextInput())
	password_one = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=False))
	password_two= forms.CharField(label="Confirmar Password", widget=forms.PasswordInput(render_value=False))


	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u=User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de Usuario ya Registrado')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u=User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya Existe')

	def clean_password_two(self):
		password_one=self.cleaned_data['password_one']
		password_two=self.cleaned_data['password_two']

		if password_one==password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

	
