# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
# models and forms
from car_shop.models import Offer, Setting, Article, UserInfo, EmployerInfo
from car_shop.forms import Search_Form, OfferForm, EditOfferForm, Text_Search_Form, CustomRegistrationForm, UserInfoForm, CustomRegistrationFormEmp, LoginForm, EmployerInfoForm
from django.http import HttpResponse
from django.db.models import F
# pagination
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from model_choices import REGION_CHOICES, SALARY_CHOICES, CATEGORY_CHOICES, OFFER_CHOICES, YESNO

# login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
# from decorators.auth import group_required

from django.core.mail import send_mail
from django.contrib import messages
from django.contrib import auth

from django.core.context_processors import csrf
from django.utils import translation

def home(request):

    msg         = _('target message') 
    cars        = Offer.objects.all()
    form        = Search_Form()
    text_form   = Text_Search_Form()
    articles    = Article.objects.all()[:4]

    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def car_edit(request, num):
    car = Offer.objects.get(id = num) 
    if request.method == 'POST':
        form = EditOfferForm(request.POST, request.FILES)

        if form.is_valid():
            print '---------the editing form is valid'
            changed_fields = form.changed_data
            print '----------------changed fields'
            print changed_fields

            if 'title' in changed_fields:           title = form.cleaned_data['title']
            if 'category' in changed_fields:        category = form.cleaned_data['category']
            if 'offer' in changed_fields:           offer = form.cleaned_data['offer']
            if 'region' in changed_fields:          region = form.cleaned_data['region']
            if 'salary' in changed_fields:          salary = int(form.cleaned_data['salary'])
            if 'immediate' in changed_fields:       immediate = form.cleaned_data['immediate']
            if 'description' in changed_fields:     description = form.cleaned_data['description']
            if 'image' in changed_fields:           image = form.cleaned_data['image']
                
            else:
                image = car.image       
            
            car.title       = title 
            car.offerType   = offer
            car.salary      = salary
            car.region      = region
            car.category    = category 
            car.immediate   = immediate
            car.description = description
            car.image       = image

            car.save()  
            return HttpResponseRedirect(car.get_absolute_url())
            
        else:
            print '--------- There is error in the form '
            print form.errors   

    else:
        form = EditOfferForm(initial={  'title':        car.title,
                                        'category':     car.category,
                                        'salary':       car.salary,
                                        'offer':        car.offerType,
                                        'immediate':    car.immediate,
                                        'description':  car.description,
                                        'image':        car.image
                                        })


    return render_to_response('car_edit.html', locals(), context_instance = RequestContext(request))

@login_required
def free_add(request):
    cars = Offer.objects.watermarked

    if request.method == 'POST':

        form = OfferForm(request.POST, request.FILES)

        print request.FILES
        print request.POST
        print form.errors

        if form.is_valid():
            print 'the form is valid'
            title           = form.cleaned_data['title']
            offer           = form.cleaned_data['offer']
            category        = form.cleaned_data['category']
            region          = form.cleaned_data['region']
            salary          = form.cleaned_data['salary']
            
            immediate       = form.cleaned_data['immediate']    
            description     = form.cleaned_data['description']  
            image           = request.FILES['image']

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
            return HttpResponseRedirect('/free_add')
        else:
            messages.add_message(request, messages.ERROR, ' SVP complétez ou bien corrigez votre formulaire .')

    else:
        form = OfferForm()
    return render_to_response('free_add.html', locals(), context_instance = RequestContext(request))

def after_upload(request):
    return render_to_response('after_upload.html', locals(), context_instance = RequestContext(request))

def search(request):
    # preparing forms
    text_form   = Text_Search_Form()
    form        = Search_Form()

    # preparing search words if we came from the index page
    offer       = request.GET.get('offer')
    category    = request.GET.get('category')
    region      = request.GET.get('region')
    low_salary  = request.GET.get('low_salary')
    high_salary = request.GET.get('high_salary')
    page        = request.GET.get('page')

    # in the normal display of the view
    if region == None : region = 'all'
    if category == None : category = 'all'
    if offer == None : offer = 'all'
    if low_salary == None : low_salary = 'all'
    if high_salary == None : high_salary = 'all'

    offers          = Offer.objects.all()
    if region       != "all":   offers = offers.filter(region   = region)
    if category     != 'all':   offers = offers.filter(category = category)
    if offer        != 'all':   offers = offers.filter(offerType    = offer)
    if low_salary   != 'all':   offers = offers.filter(salary__gte=int( low_salary ))
    if high_salary  != 'all':   offers = offers.filter(salary__lte= int( high_salary ))

    articles    = offers
    paginator   = Paginator(articles, 6) 
    page        = request.GET.get('page')
    query        = request.GET.get('region')

    try: contacts = paginator.page(page)
    except PageNotAnInteger: contacts = paginator.page(1)
    except EmptyPage: contacts = paginator.page(paginator.num_pages)

    return render_to_response('search.html' , locals(), context_instance = RequestContext(request))

def map_search(request):
    # preparing forms
    text_form   = Text_Search_Form()
    form        = Search_Form()

    # preparing search words if we came from the index page
    offer       = request.GET.get('offer')
    category    = request.GET.get('category')
    region      = request.GET.get('region')
    low_salary  = request.GET.get('low_salary')
    high_salary = request.GET.get('high_salary')
    page        = request.GET.get('page')

    # in the normal display of the view
    if region == None : region = 'all'
    if category == None : category = 'all'
    if offer == None : offer = 'all'
    if low_salary == None : low_salary = 'all'
    if high_salary == None : high_salary = 'all'

    offers          = Offer.objects.all()
    if region       != "all":   offers = offers.filter(region   = region)
    if category     != 'all':   offers = offers.filter(category = category)
    if offer        != 'all':   offers = offers.filter(offerType    = offer)
    if low_salary   != 'all':   offers = offers.filter(salary__gte=int( low_salary ))
    if high_salary  != 'all':   offers = offers.filter(salary__lte= int( high_salary ))

    articles  = offers
    paginator = Paginator(articles, 6) 
    page      = request.GET.get('page')
    query     = request.GET.get('region')

    try: contacts = paginator.page(page)
    except PageNotAnInteger:    contacts = paginator.page(1)
    except EmptyPage:           contacts = paginator.page(paginator.num_pages)

    return render_to_response('map_search.html', locals(), context_instance = RequestContext(request))

def search_candidates(request):
    # preparing forms
    text_form   = Text_Search_Form()
    form        = Search_Form()
    
    users = UserInfo.objects.all()

    articles  = users
    paginator = Paginator(articles, 15) 
    page      = request.GET.get('page')
    #paginating found users
    try: contacts = paginator.page(page)
    except PageNotAnInteger:    contacts = paginator.page(1)
    except EmptyPage:           contacts = paginator.page(paginator.num_pages)
    return render_to_response('search_candidates.html', locals(), context_instance = RequestContext(request) )

def news(request):
    articles    = Article.objects.all()
    paginator   = Paginator(articles, 3) # Show 25 contacts per page
    page        = request.GET.get('page')

    try: contacts = paginator.page(page)
    except PageNotAnInteger:    contacts = paginator.page(1)
    except EmptyPage:           contacts = paginator.page(paginator.num_pages)

    return render_to_response('news.html', locals(), context_instance = RequestContext(request))

def news_item(request, num):
    article = Article.objects.get(id = num)
    return render_to_response('news_item.html', locals(), context_instance = RequestContext(request))

def car(request, num):
    car = Offer.objects.get(id=num)

    # car.update(views=F('views')+1)
    Offer.objects.filter(id=num).update(views=F('views')+1)
    can_edit = False
    # if request.user.username == car.user.user.username:
    if request.user.username == car.user.username: can_edit = True

    return render_to_response('car.html', locals(), context_instance = RequestContext(request))


def get_pagination_page(page=1, items=None):

    items = Offer.objects.all()
    print '----------------------in get pagination page'
    paginator = Paginator(items, 4)
    try: page = int(page)
    except ValueError: page = 1

    try:    items = paginator.page(page)
    except  (EmptyPage, InvalidPage): items = paginator.page(paginator.num_pages)

    return items

def land_page_pagination(page=1, items=None):
    # items = range(0, 100)
    items = items
    paginator = Paginator(items, 6)
    
    try:    page = int(page)
    except  ValueError: page = 1

    try:    items = paginator.page(page)
    except  (EmptyPage, InvalidPage): items = paginator.page(paginator.num_pages)

    return items


def contact(request):
    errors = []
    if request.method == 'POST':
        print 'in POST'

        if not request.POST.get('name', ''): errors.append('Enter a name')
        if not request.POST.get('subject', ''): errors.append('Enter a subject.')
        if not request.POST.get('message', ''): errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']: errors.append('Enter a valid e-mail address.')
        # create a model to just save contact messages tickets  
        if not errors:
            print 'sending message'
            try:
                send_mail(
                    #subject
                    request.POST['subject'],
                    #message
                    request.POST['message'],
                    # from
                    request.POST.get('email'),
                    # To [recipient list]
                    ['redatest7@gmail.com'],
                )
                messages.add_message(request, messages.INFO, 'message sent successflully.')
                # return render_to_response('contact.html', locals(), context_instance = RequestContext(request))
                return HttpResponseRedirect('/contact')
            except Exception, err:
                messages.add_message(request, messages.INFO, 'there was an error when processing your request.')
                return render_to_response('contact.html', locals(), context_instance = RequestContext(request))
            
    return render_to_response('contact.html', locals(), context_instance = RequestContext(request))


@login_required
# @user_passes_test(lambda u: u.groups.filter(name='candidate').count() == 0, login_url='/')
def profile(request):
    print 'in simple profile view'
    usname = request.user.username
    uslname = request.user.last_name
    userinfo = UserInfo.objects.get( user = request.user )

    if request.method == 'POST':
        print (request.POST)
        form = UserInfoForm(data=request.POST, instance=userinfo, user=request.user)
        if form.is_valid():
            print '#### the form is good #####'
            form.save()
            message = messages.add_message(request, messages.INFO, 'données enregistrées avec succée')
            return HttpResponseRedirect('/profile/')
        else:
            print form.errors
            message = messages.add_message(request, messages.INFO, 'erreur durant la savegarde  ')
            return render_to_response('profile.html', locals(), context_instance=RequestContext(request))

    else: 
        # use form initial
        print dir(userinfo)
        form = UserInfoForm(instance=userinfo, user=request.user)
        userinfo = UserInfo.objects.get( user = request.user )
        return render_to_response('./registration/profile.html', locals(), context_instance=RequestContext(request))


@login_required
# @user_passes_test(lambda u: u.groups.filter(name='employer').count() == 0, login_url='/')
def profileEmp(request):
    usname = request.user.username
    uslname = request.user.last_name
    userinfo = EmployerInfo.objects.get( user = request.user )

    if request.method == 'POST':
        print (request.POST)
        form = EmployerInfoForm(data=request.POST, instance=userinfo, user=request.user)
        if form.is_valid():
            print '#### the form is good #####'
            form.save()
            message = messages.add_message(request, messages.INFO, 'données enregistrées avec succée')
            return HttpResponseRedirect('/profile/')
        else:
            print form.errors
            message = messages.add_message(request, messages.INFO, 'erreur durant la savegarde  ')
            return render_to_response('./registration/profile.html', locals(), context_instance=RequestContext(request))

    else: 
        # use form initial
        form = EmployerInfoForm(instance=userinfo, user=request.user)
        userinfo = EmployerInfo.objects.get( user = request.user )

        return render_to_response('./registration/profile_emp.html', locals(), context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated(): return HttpResponseRedirect('/profile/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usr = auth.authenticate(username=username, password=password)
            if usr is not None:
                    auth.login(request, usr)
                    return HttpResponseRedirect('/')
            else:
                return render_to_response('./registration/login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('./registration/login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('./registration/login.html', context, context_instance=RequestContext(request))

    return render_to_response('./registration/login.html', c, context_instance=RequestContext(request))



def invalid_login(request):
    return render_to_response('./registration/invalid_login.html', locals(), context_instance = RequestContext(request))


def auth_view(request):
    username    = request.POST.get('username', '') 
    password    = request.POST.get('password', '')
    user        = auth.authenticate( username = username, password = password ) 

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        print "locals"
        print locals()
        return HttpResponseRedirect('/accounts/login')  

def logout(request):
    auth.logout(request)
    message = messages.add_message(request, messages.INFO, 'A bientôt')
    return HttpResponseRedirect('/')


def register_user(request):

    if request.user.is_authenticated(): return HttpResponseRedirect('/profile/')

    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #assign data to the custom user
            u = form.instance
            u = UserInfo.objects.get(user = u)
            userFields = 'adress,telephone,sector1,sector2,sector3,mobility1,mobility2,mobility3,disponibility,status,salary,study_level,experience,contract,period,languages'  
            for key in userFields.split(','):
                setattr(u, key, request.POST.get(key, ''))

            # set the user in candidate user group    
            gr = Group.objects.get(name='candidate')
            # usr = User.objects.get(username=u.username)
            gr.user_set.add(u.user)
            u.save()
            return HttpResponseRedirect('/')
        else:
            return render_to_response('./registration/register.html', locals(), context_instance=RequestContext(request))   

    form = CustomRegistrationForm()        
    return render_to_response('./registration/register.html', locals(), context_instance=RequestContext(request))      

def register_emp(request):
    if request.method == 'POST':
        form = CustomRegistrationFormEmp(request.POST)
        if form.is_valid():
            form.save()
            #assign data to the custom user
            u = form.instance
            u = EmployerInfo.objects.get(user = u)

            # society, phone, postal_code, town, website, presentation
            userFields = 'phone,postal_code,town,website,presentation' # always trim spaces
            for key in userFields.split(','): 
                setattr(u, key, request.POST.get(key, ''))

            # set the user in employer user group    
            gr = Group.objects.get(name='employer')
            # usr = User.objects.get(username=u.username)
            gr.user_set.add(u.user)
            u.save()
                
            return HttpResponseRedirect('/')
        else:
            return render_to_response('./registration/register_emp.html', locals(), context_instance=RequestContext(request)) 

    form = CustomRegistrationFormEmp()        
    return render_to_response('./registration/register_emp.html', locals(), context_instance=RequestContext(request))      

def register_success(request):
    return render_to_response('./registration/register_success.html', locals(), context_instance=RequestContext(request))



def set_ar(request):
    request.session['django_language'] = 'ar'
    translation.activate('ar')
    request.LANGUAGE_CODE = 'ar'
    return HttpResponseRedirect('/')

def set_en(request):
    request.session['django_language'] = 'en'
    translation.activate('en')
    request.LANGUAGE_CODE = 'en'
    return HttpResponseRedirect('/')
