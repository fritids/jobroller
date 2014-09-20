from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from profile.forms import ExRegistrationForm
from registration.backends.default.views import RegistrationView

from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
	# main application
    url('^$', "car_shop.views.home", name='home'),

    # offres
    url('^deposer_offre$', "offre.views.deposer_offre", name='deposer_offre'),

    url('^after_upload$', "offre.views.after_upload", name='after_upload'),

    url('^offer/(?P<num>\d+)/$', "offre.views.offer", name='offer'),

    url('^offer/(?P<num>\d+)/edit/$', "offre.views.offer_edit", name='offer_edit'),

    url('^offer/(?P<num>\d+)/disable/$', "offre.views.offer_disable", name='offer_disable'),    

    url('^offer/(?P<num>\d+)/activate/$', "offre.views.offer_activate", name='offer_activate'),    

    # article
    url('^news$', "article.views.news", name='news'),

    url('^news_item/(?P<num>\d+)/$', "article.views.news_item", name='news_item'),

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
    
    url(r'^candidate/(?P<num>\d+)/$', "profile.views.candidate", name='candidate'),    

    # daxice 
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    
    # custom registration
    url(r'accounts/register/$', RegistrationView.as_view(form_class = ExRegistrationForm), name = 'registration_register'),
    url(r'accounts/login/$', 'registration.views.login', name = 'authentication_login'),
    (r'^accounts/', include('registration.backends.default.urls')),

    
)


urlpatterns += patterns('',
        url(r'media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

