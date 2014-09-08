# -*- coding: utf-8 -*-
from django import forms
from model_choices import *
from car_shop.widgets import TinyMCEWidget
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _
from models import Offer
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from car_shop.models import UserInfo, EmployerInfo
import datetime
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
	username        = forms.CharField(label=(u'User Name'))
	password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

	def __init__(self,*args, **kwargs):
		super(LoginForm,self).__init__(*args, **kwargs)	
		for k, field in self.fields.items():
			if 'required' in field.error_messages:
				field.error_messages['required'] = 'Ce champs est obligatoire'

	def clean(self):

		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)

		if not user or not user.is_active:
		    raise forms.ValidationError("Erreur d'authentification.")
		return self.cleaned_data

	def login(self, request):

		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user				


class Text_Search_Form(forms.Form):
	target_text     = forms.CharField(label= _("target text"), required=True, widget=forms.TextInput(attrs={'class':'form-control input-sm', 'name':'s'}))

class Search_Form(forms.Form):
	offer 			= forms.ChoiceField(label= _("Offre"), choices=OFFER_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	category 		= forms.ChoiceField(label= _("Categorie"), choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	region 			= forms.ChoiceField(label= _("Region"), choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	low_salary 		= forms.ChoiceField(label= _("salaire bas"), choices=SALARY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	high_salary		= forms.ChoiceField(label= _("salaire haut"), choices=SALARY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))

class ArticleAdminForm(forms.ModelForm):
	body=forms.CharField(widget=TinyMCEWidget())

	class Meta:
		model = get_model('car_shop', 'article')

class OfferForm(forms.Form):
	title 			= forms.CharField(label=_("titre"), required=True, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Titre précis de l\'offre'}))
	offer 			= forms.ChoiceField(label=_("Offre"), choices=OFFER_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	category	 	= forms.ChoiceField(label=_("Categorie"), choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	region 			= forms.ChoiceField(label="Region", choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	salary 			= forms.ChoiceField(label=_("Salaire"), choices=SALARY_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
	description 	= forms.CharField(label=_("description"), required=False, widget=forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Decrivez votre annonce '}))
	immediate 		= forms.ChoiceField(label= _("immédiat"), required=False ,choices=YESNO, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	# image 			= forms.FileField(label='Choisissez votre fichier', help_text='uploadze une image ')
	
	# def __init__(self, *args, **kwargs):
	# 	super(OfferForm, self).__init__(*args, **kwargs)
	# 	self.fields["image"].widget.attrs.update({"class":"input-sm"})
	

class EditOfferForm(OfferForm):
	image = forms.FileField(label='Choisissez votre image', required=False, help_text='upload your photo')
	
	def __init__(self, *args, **kwargs):
		super(EditOfferForm, self).__init__(*args, **kwargs)
		self.fields["image"].widget.attrs.update({"class":"input-sm"})

form_error_dict = {
	'invalid': "blah blah",
	'required' : "blah",
	'invalid_choice' : "blah",
	'unique' : "blah"
}

# you must define unique error for username

class CustomRegistrationForm(UserCreationForm):
	username			= forms.CharField(max_length=200,required=True, error_messages={'invalid': "Ce champ doit contenir des lettres ou des chiffres ou @/./+/-/_ , et pas d'espace"})
	email 				= forms.EmailField(required=True, error_messages={'invalid': 'Vous de vez entrez une adresse valide'})
	last_name 			= forms.CharField(max_length=200)
	telephone 			= forms.CharField(max_length=200)
	adress  			= forms.CharField(max_length=200)

	sector1 			= forms.ChoiceField(label="sector1", 		choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	sector2 			= forms.ChoiceField(label="sector2", 		choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}), required=False)
	sector3				= forms.ChoiceField(label="sector3", 		choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}), required=False)

	mobility1 			= forms.ChoiceField(label="mobilite1", 		choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	mobility2 			= forms.ChoiceField(label="mobilite2", 		choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}), required=False)
	mobility3			= forms.ChoiceField(label="mobilite3", 		choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}), required=False)

	disponibility		= forms.ChoiceField(label="disponibilite", 	choices=DISPONIBILITY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}),required=False)
	status				= forms.ChoiceField(label="status", 		choices=STATUS_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	salary				= forms.ChoiceField(label="salary", 		choices=SALARY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}), required=False)

	study_level			= forms.ChoiceField(label="study_level", 	choices=STUDY_LEVEL_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}),required=False)
	experience			= forms.ChoiceField(label="experience", 	choices=EXPERIENCE_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	contract			= forms.ChoiceField(label="contract", 		choices=OFFER_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	period				= forms.ChoiceField(label="period", 		choices=PERIOD_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))

	class Meta:
		model 			= User
		fields 			= ('username', 'last_name',  'email', 'password1', 'password2' )

	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
			raise forms.ValidationError(u'le nom "%s" est deja pris.' % username)
		return username	

	def clean_password1(self):
		password = self.cleaned_data['password1']
		length = len(password)
		if length < 8: raise forms.ValidationError("Il faut taper au moin 8 lettres.")
		return password	

	def clean_sector1(self):
		data = self.cleaned_data.get('sector1')
		if data == self.fields['sector1'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data

	def clean_sector2(self):
		data = self.cleaned_data.get('sector2')
		if data == self.fields['sector2'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data

	def clean_sector3(self):
		data = self.cleaned_data.get('sector3')
		if data == self.fields['sector3'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data

	def clean_mobility1(self):
		data = self.cleaned_data.get('mobility1')
		if data == self.fields['mobility1'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data

	def clean_mobility2(self):
		data = self.cleaned_data.get('mobility2')
		if data == self.fields['mobility2'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data	

	def clean_mobility3(self):
		data = self.cleaned_data.get('mobility3')
		if data == self.fields['mobility3'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data		

	def clean_disponibility(self):
		data = self.cleaned_data.get('disponibility')
		if data == self.fields['disponibility'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data		

	def clean_status(self):
		data = self.cleaned_data.get('status')
		if data == self.fields['status'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data		
	
	def clean_salary(self):
		data = self.cleaned_data.get('salary')
		if data == self.fields['salary'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data		
	
	def clean_study_level(self):
		data = self.cleaned_data.get('study_level')
		if data == self.fields['study_level'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data

	def clean_experience(self):
		data = self.cleaned_data.get('experience')
		if data == self.fields['experience'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data	

	def clean_contract(self):
		data = self.cleaned_data.get('contract')
		if data == self.fields['contract'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
		return data					

	def clean_period(self):
			data = self.cleaned_data.get('period')
			if data == self.fields['period'].choices[0][0]: raise forms.ValidationError('Il faut choisir une valeur')
			return data

	def save(self, commit=True):	
		user 			= super(UserCreationForm, self).save(commit=False) # do not save it at the moment because we did not add the email field
		user.email 		= self.cleaned_data['email']
		user.first_name = "candidate"
		user.last_name 	= self.cleaned_data['last_name']

		user.set_password(self.cleaned_data["password1"])
		if commit: user.save()
		return user

	def __init__(self,*args, **kwargs):
		super(CustomRegistrationForm,self).__init__(*args, **kwargs)	

		for k, field in self.fields.items():
			if 'required' in field.error_messages: field.error_messages['required'] 	= 'Ce champs est obligatoire'
			# if 'invalid' in field.error_messages: field.error_messages['invalid'] 		= 'Entrez une adresse email valide'
			if 'invalid_choice' in field.error_messages: field.error_messages['invalid'] = 'Choisir une valeur valide'


	
class CustomRegistrationFormEmp(UserCreationForm):
	first_name			= forms.CharField(max_length=200)
	email 				= forms.EmailField(required=True)

	username			= forms.CharField(max_length=200, required=True)
	phone				= forms.CharField(max_length=200, required=False)
	postal_code			= forms.CharField(max_length=200, required=False)
	town				= forms.CharField(max_length=200, required=False)
	website				= forms.URLField( max_length=200, required=False)
	presentation		= forms.CharField ( widget=forms.widgets.Textarea(attrs={'rows':7, 'cols':110}), required=False )


	class Meta:
		model 			= User
		fields 			= ('username', 'first_name','email', 'password1', 'password2' )

	def clean_username(self):	
		username = self.cleaned_data['username']
		if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
			raise forms.ValidationError(u'le nom "%s" est deja pris.' % username)	
		return username		

	def __init__(self,*args, **kwargs):
		super(CustomRegistrationFormEmp,self).__init__(*args, **kwargs)	

		for k, field in self.fields.items():
			if 'required' in field.error_messages: field.error_messages['required'] 	 = 'Ce champs est obligatoire'
			if 'invalid' in field.error_messages: field.error_messages['invalid'] 		 = 'Entrez une adresse email valide'
			if 'invalid_choice' in field.error_messages: field.error_messages['invalid'] = 'Choisir une valeur valide'

	def save(self, commit=True):	
		user 			= super(UserCreationForm, self).save(commit=False) # do not save it at the moment because we did not add the email field
		user.email 		= self.cleaned_data['email']
		self.society	= self.cleaned_data['username']
		user.first_name = "employer"

		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
			gr = Group.objects.get(name='employer')
			gr.user_set.add(user)
		return user	

	


class UserInfoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(UserInfoForm, self).__init__(*args, **kwargs)
		for x in self.fields: self.fields[x].widget.attrs['class'] = 'form-control'

	def save(self, *args, **kwargs):

		instance = super(UserInfoForm, self).save(commit=False)
		print '#### instace user #####'
		return instance.save()	

	class Meta:
		model 		= UserInfo
		exclude 	= ['user'] # to add it later

class EmployerInfoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(EmployerInfoForm, self).__init__(*args, **kwargs)
		for x in self.fields: self.fields[x].widget.attrs['class'] = 'form-control'

	def save(self, *args, **kwargs):

		instance = super(EmployerInfoForm, self).save(commit=False)
		print '#### instace user #####'
		return instance.save()	

	class Meta:
		model 		= EmployerInfo
		exclude 	= ['user'] # to add it later

