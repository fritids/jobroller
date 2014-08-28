from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


from django.conf import settings
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()

urlpatterns = patterns('',
	# main application
    url('^$', "car_shop.views.home", name='home'),

    url('^free_add$', "car_shop.views.free_add", name='free_add'),

    url('^search$', "car_shop.views.search", name='search'),
    
    url('^news$', "car_shop.views.news", name='news'),

	url('^after_upload$', "car_shop.views.after_upload", name='after_upload'),

    url('^news_item/(?P<num>\d+)/$', "car_shop.views.news_item", name='news_item'),

    url('^offer/(?P<num>\d+)/$', "car_shop.views.car", name='car'),

    url('^offer/(?P<num>\d+)/edit$', "car_shop.views.car_edit", name='car_edit'),

    url('^contact$', "car_shop.views.contact", name='contact'),

    url('^set_ar$', "car_shop.views.set_ar", name='set_ar'),
    
    url('^set_en$', "car_shop.views.set_en", name='set_en'),

    url('^search', "car_shop.views.search", name='search'),

    url('^search_results', "car_shop.views.search_results", name='search_results'),
     
	# administration
    url(r'^admin/', include(admin.site.urls)),

    # forum applicatino
    
    # Profile
    url('^profile', "car_shop.views.profile", name='profile'),    
    url('^profile_emp', "car_shop.views.profile_emp", name='profile_emp'),    

    # daxice 
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # authentication
    url(r'^accounts/login/$', "car_shop.views.login", name="login" ),
    url(r'^accounts/invalid/$', "car_shop.views.invalid_login", name="invalid_login" ),
    url(r'^accounts/auth/$', "car_shop.views.auth_view", name="auth_view" ),
    url(r'^accounts/logout/$', "car_shop.views.logout", name="logout" ),
    url(r'^accounts/register/$', "car_shop.views.register_user", name="register_user" ),
    url(r'^accounts/register_emp/$', "car_shop.views.register_emp", name="register_emp" ),
    url(r'^accounts/register_success/$', "car_shop.views.register_success", name="register_success" ),

)


urlpatterns += patterns('',
        url(r'media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

