# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

# models and forms
from offre.models import Offer
from offre.forms import OfferForm, EditOfferForm
from profile.models import Profile_candid, Profile_emp
from profile.forms import UserInfoForm, EmployerInfoForm
# pagination and search
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from car_shop.model_choices import REGION_CHOICES, SALARY_CHOICES, CATEGORY_CHOICES, OFFER_CHOICES, YESNO
from django.db.models import F

# login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

from django.core.mail import send_mail
from django.contrib import messages
from django.core.context_processors import csrf
from django.utils import translation

def offer(request, num):
    car = Offer.objects.get(id=num)

    car.views = int(car.views)+1
    car.save()

    can_edit = False
    if request.user.username == car.user.username: can_edit = True

    return render_to_response('offer.html', locals(), context_instance = RequestContext(request))


def offer_edit(request, num):
    car = Offer.objects.get(id = num)

    # if request.user.username == car.user.user.username:
    if request.user.username == car.user.username:
        can_edit = True


    if request.method == 'POST':
        form = EditOfferForm(request.POST, request.FILES)

        if form.is_valid():
            changed_fields = form.changed_data

            if 'title' in changed_fields:           title = form.cleaned_data['title']
            if 'category' in changed_fields:        category = form.cleaned_data['category']
            if 'offer' in changed_fields:           offer = form.cleaned_data['offer']
            if 'region' in changed_fields:          region = form.cleaned_data['region']
            if 'salary' in changed_fields:          salary = int(form.cleaned_data['salary'])
            if 'immediate' in changed_fields:       immediate = form.cleaned_data['immediate']
            if 'description' in changed_fields:     description = form.cleaned_data['description']

                
            else:
                image = car.image       
            
            car.title       = title 
            car.offerType   = offer
            car.salary      = salary
            car.region      = region
            car.category    = category 
            car.immediate   = immediate
            car.description = description


            car.save()  
            return HttpResponseRedirect(car.get_absolute_url())
            
        else:
            print form.errors   

    else:
        form = EditOfferForm(initial={  'title':        car.title,
                                        'category':     car.category,
                                        'salary':       car.salary,
                                        'region':       car.region,
                                        'offer':        car.offerType,
                                        'immediate':    car.immediate,
                                        'description':  car.description
                                        
                                        })


    return render_to_response('offer_edit.html', locals(), context_instance = RequestContext(request))


# make the call by ajax
@login_required
def offer_disable(request, num):
    offer = get_object_or_404(Offer, id=num)
    offer.activated = False
    offer.save()
    return HttpResponseRedirect('/emp_profile_offres/')

# make the call by ajax
@login_required
def offer_activate(request, num):
    offer = get_object_or_404(Offer, id=num)
    offer.activated = True
    offer.save()
    return HttpResponseRedirect("/emp_profile_offres/")

@login_required
def deposer_offre(request):
    # cars = Offer.objects.watermarked

    if request.method == 'POST':

        form = OfferForm(request.POST, request.FILES)

        if form.is_valid():
            title           = form.cleaned_data['title']
            offer           = form.cleaned_data['offer']
            category        = form.cleaned_data['category']
            region          = form.cleaned_data['region']
            salary          = form.cleaned_data['salary']
            
            immediate       = form.cleaned_data['immediate']    
            description     = form.cleaned_data['description']  
            # image           = request.FILES['image']

            newcar = Offer( title           = title, 
                            offerType       = offer,
                            salary          = salary, 
                            category        = category, 
                            region          = region, 
                            immediate       = immediate, 
                            description     = description, 
                            user            = request.user )
            newcar.save()

            messages.add_message(request, messages.INFO, ' Ajoutée avec succée .')
            return HttpResponseRedirect('/deposer_offre')
        else:
            messages.add_message(request, messages.ERROR, ' SVP complétez ou bien corrigez votre formulaire .')

    else:
        form = OfferForm()
    return render_to_response('deposer_offre.html', locals(), context_instance = RequestContext(request))

def after_upload(request):
    return render_to_response('after_upload.html', locals(), context_instance = RequestContext(request))

