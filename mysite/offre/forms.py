# -*- coding: utf-8 -*-
from django import forms
from car_shop.model_choices import *

from django.utils.translation import ugettext_lazy as _
import datetime



class OfferForm(forms.Form):
	title 			= forms.CharField(label=_("titre"), required=True, widget=forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Titre précis de l\'offre'}))
	offer 			= forms.ChoiceField(label=_("Offre"), choices=OFFER_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	category	 	= forms.ChoiceField(label=_("Categorie"), choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	region 			= forms.ChoiceField(label="Region", choices=REGION_CHOICES, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	salary 			= forms.ChoiceField(label=_("Salaire"), choices=SALARY_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
	description 	= forms.CharField(label=_("description"), required=False, widget=forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Decrivez votre annonce '}))
	immediate 		= forms.ChoiceField(label= _("immédiat"), required=False ,choices=YESNO, widget=forms.Select(attrs={'class':'form-control input-sm'}))
	
class EditOfferForm(OfferForm):
	image = forms.FileField(label='Choisissez votre image', required=False, help_text='upload your photo')
	
	def __init__(self, *args, **kwargs):
		super(EditOfferForm, self).__init__(*args, **kwargs)
		self.fields["image"].widget.attrs.update({"class":"input-sm"})

