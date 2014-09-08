from django.contrib import admin
from car_shop.models import Offer, Setting, Article , UserInfo, EmployerInfo
from car_shop.forms import ArticleAdminForm
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

# add image display to car administration
class AdminImageWidget(AdminFileWidget):
	def render(self, name, value, attrs=None):
		output = []
		if value and getattr(value, "url", None):
			image_url = value.url
			file_name=str(value)
			output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="80" height="80" /></a> <br/> %s ' % \
				(image_url, image_url, file_name, _('Change:')))
		output.append(super(AdminFileWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))

class OfferAdmin(admin.ModelAdmin):
	list_display 	= ('title','offerType', 'region', 'offerType', 'salary', 'user')
	# delete selected car and it's  file
	
class ArticleAdmin(admin.ModelAdmin):
	list_display 	= ('title', 'created')
	search_fields 	= ('title', 'content')
	list_filter 	= ('created',)
	form 			= ArticleAdminForm

class UserInfoAdmin(admin.ModelAdmin):
    list_display 	= ['user', 'created_at']
    search_fields 	= ['user']
    date_hierarchy 	= 'created_at'
    
class EmployerInfoAdmin(admin.ModelAdmin):
    list_display 	= ['user', 'created_at']
    search_fields 	= ['user']
    date_hierarchy 	= 'created_at'

# admin.site.register(UserUploadedCars, UserUploadedCarsAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(EmployerInfo, EmployerInfoAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Setting)

