from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from profile.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView

from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

import main
from main import views
from main.views import payment

from django.contrib.auth.decorators import login_required


dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
	# main application
    url('^$', "car_shop.views.home", name='home'),

    # offres
    url('^deposer_offre$', "offre.views.deposer_offre", name='deposer_offre'),

    url('^after_upload$', "offre.views.after_upload", name='after_upload'),

    url('^offer/(?P<num>\w+)/$', "offre.views.offer", name='offer'),

    url('^offer/(?P<num>\w+)/edit/$', "offre.views.offer_edit", name='offer_edit'),

    url('^offer/(?P<num>\w+)/disable/$', "offre.views.offer_disable", name='offer_disable'),    

    url('^offer/(?P<num>\w+)/activate/$', "offre.views.offer_activate", name='offer_activate'),

    url('^offer/(?P<num>\w+)/postulate/$', "offre.views.offer_postulate", name='offer_postulate'),    

    # article
    url('^news$', "article.views.news", name='news'),

    url('^news_item/(?P<num>\w+)/$', "article.views.news_item", name='news_item'),

    url('^contact$', "car_shop.views.contact", name='contact'),

    # searching
    url('^search$', "car_shop.views.search", name='search'),

    url(r'^search/$', "car_shop.views.search", name='search'),
    
    url(r'^map_search/$', "car_shop.views.map_search", name='map_search'),

    url(r'^search_candidates/$', "profile.views.search_candidates", name='search_candidates'),
     
	# administration
    url(r'^admin/', include(admin.site.urls)),

    # Profile
    url(r'^candid_profile/$', "profile.views.candid_profile", name='candid_profile'),    
    url(r'^candid_profile_edit/(?P<id>\w+)/$', "profile.views.candid_profile_edit", name='candid_profile_edit'),    

    url(r'^emp_profile/$', "profile.views.emp_profile", name='emp_profile'),    
    url(r'^emp_profile_offres/$', "profile.views.emp_profile_offres", name='emp_profile_offres'),    
    url(r'^emp_profile_edit/(?P<id>\w+)/$', "profile.views.emp_profile_edit", name='emp_profile_edit'),    
    url(r'^emp_profile_offer_applyers/(?P<id>\w+)/$', "profile.views.emp_profile_offer_applyers", name='emp_profile_offer_applyers'),    
    
    url(r'^candidate/(?P<num>\w+)/$', "profile.views.candidate", name='candidate'),    

    # daxice 
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    
    # custom registration
    url(r'accounts/register/$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),
    url(r'accounts/login/$', 'registration.views.login', name = 'authentication_login'),
    (r'^accounts/', include('registration.backends.default.urls')),


    # potato stripe payments
    url(r'^subscribe-vanilla$', login_required(main.views.payment.subscribe_vanilla), name="subscribe_vanilla"),
    url(r'^subscribe-modal$', login_required(main.views.payment.subscribe_modal), name="subscribe_modal"),
    url(r'^change/plan/$', login_required(main.views.payment.change), name="change_subscription"),
    url(r'^change/card/$', login_required(main.views.payment.change_card), name="change_card"),
    url(r'^cancel$', login_required(main.views.payment.cancel), name="cancel_subscription"),

    url(r'^subscribe_ajax$', login_required(main.views.payment.subscribe_ajax), name="subscribe_ajax"),
    url(r'^cancel_ajax$', login_required(main.views.payment.cancel_ajax), name="cancel_ajax"),
    url(r'^change_plan_ajax$', login_required(main.views.payment.change_plan_ajax), name="change_plan_ajax"),
    url(r'^change_card_ajax$', login_required(main.views.payment.change_card_ajax), name="change_card_ajax"),

    # payments
    url(r"^payments/", include("payments.urls")),
    
)


urlpatterns += patterns('',
        url(r'media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

