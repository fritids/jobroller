# -*- coding: utf-8 -*-
from django import forms
from model_choices import REGION_CHOICES, SALARY_CHOICES, CATEGORY_CHOICES, OFFER_CHOICES, YESNO
from car_shop.widgets import TinyMCEWidget
from django.db.models import get_model
from django.utils.translation import ugettext_lazy as _
from models import Offer
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from car_shop.models import UserInfo
import datetime

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
	image 			= forms.FileField(label='Choisissez votre fichier', help_text='uploadze une image ')
	
	def __init__(self, *args, **kwargs):
		super(OfferForm, self).__init__(*args, **kwargs)
		self.fields["image"].widget.attrs.update({"class":"input-sm"})
	

class EditOfferForm(OfferForm):
	image = forms.FileField(label='Choisissez votre image', required=False, help_text='upload your photo')
	
	def __init__(self, *args, **kwargs):
		super(EditOfferForm, self).__init__(*args, **kwargs)
		self.fields["image"].widget.attrs.update({"class":"input-sm"})


class CustomRegistrationForm(UserCreationForm):
	email 				= forms.EmailField(required=True)
	last_name 			= forms.CharField(max_length=200)

	class Meta:
		model 			= User
		fields 			= ('username', 'last_name',  'email', 'password1', 'password2' )

	def save(self, commit=True):	
		user 			= super(UserCreationForm, self).save(commit=False) # do not save it at the moment because we did not add the email field
		user.email 		= self.cleaned_data['email']
		user.first_name = "candidate"
		user.last_name 	= self.cleaned_data['last_name']

		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user	

class CustomRegistrationFormEmp(UserCreationForm):
	first_name			= forms.CharField(max_length=200)
	email 				= forms.EmailField(required=True)

	class Meta:
		model 			= User
		fields 			= ('username', 'first_name','email', 'password1', 'password2' )

	def save(self, commit=True):	
		user 			= super(UserCreationForm, self).save(commit=False) # do not save it at the moment because we did not add the email field
		user.email 		= self.cleaned_data['email']
		user.first_name = "employer"

		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
			# temporarly add user to the group
			gr = Group.objects.get(name='employer')
			gr.user_set.add(user)
		return user	


class UserInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
    	self.user = kwargs.pop('user', None)
    	super(UserInfoForm, self).__init__(*args, **kwargs)
    	for x in self.fields:
    		self.fields[x].widget.attrs['class'] = 'form-control'

    def save(self, *args, **kwargs):

    	instance = super(UserInfoForm, self).save(commit=False)
    	print '#### instace user #####'
    	return instance.save()	

    class Meta:
        model 		= UserInfo
        exclude 	= ['user'] # to add it later
