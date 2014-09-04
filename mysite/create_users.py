from django.core.management import setup_environ
from example_bootstrap import settings
setup_environ(settings)

import datetime
from django.contrib.auth.models import User
from car_shop.models import UserInfo

import random

li =  ['John Reese', 'Harold Finch', 'Airi Satou', 'Angelica Ramos', 'Ashton Cox', 'Bradley Greer', 'Brenden Wagner', 'Brielle Williamson','Bruno Nash', 
	'Charde Marshall', 'Colleen Hurst', 'Dai Rios', 'Donna Snider', 'Doris Wilder', 'Finn Camacho', 'Fiona Green'
	,'Garrett Winters', 'Caesar Vance', 'Cara Stevens', 'Cedric Kelly']

lfirst = [ i.split()[0] for i in li ]
llast = [ i.split()[1] for i in li ]

rand_list = range(1,6)

for i in range(len(li)):
	lst = lfirst[i]
	name = llast[i]
	email='user%d@free.com' % i
	user = User.objects.create_user(name, email, 'redareda')

	user.last_name = lst
	user.first_name = name
	user.save()

	atuser = UserInfo(user = user) 
	atuser.adress        = '%d rue kleber' %i 
	atuser.telephone     = i,i,i,i,'-',i,i,i,i 
	atuser.sector1       = str(random.choice( rand_list ) )
	atuser.sector2       = str(random.choice( rand_list ) )
	atuser.sector3       = str(random.choice( rand_list ) )
	atuser.mobility1     = str(random.choice( rand_list ) )
	atuser.mobility2     = str(random.choice( rand_list ) )
	atuser.mobility3     = str(random.choice( rand_list ) )
	atuser.disponibility = str(random.choice( rand_list ) )
	atuser.status        = str(random.choice( range(2) ) )
	atuser.salary        = str(random.choice( rand_list ) )
	atuser.study_level   = str(random.choice( rand_list ) )
	atuser.experience    = str(random.choice( rand_list ) )
	atuser.contract      = str(random.choice( range(2) ) )
	atuser.period        = str(random.choice( range(2) ) )
	atuser.languages     = 'English'

	atuser.save()
	
	