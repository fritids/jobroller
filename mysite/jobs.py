# -*- coding: utf-8 -*-			
from django.core.management import setup_environ
from example_bootstrap import settings
setup_environ(settings)
from car_shop.models import Offer
from django.contrib.auth.models import User
import random

sett = {
	"Asssistante SAP", "Logisticien/Supply Chain", "Shef de rayon", "Chef de projet informatique", "Asssistante commerciale", "conseiller clientele", "Property manager"
	"chef de secteur", "Approvisionneur", "Cadre en ressource humaine", "Chef de produits", "Controleur de gestion", "Electricien fibre optique", "Formateur", "conducteur de traveaux"
	"Technicien", "magasinier", "Asssistante de direction" }

di ={
	"Formateur"                   : 'Education' ,
	"Asssistante de direction"    : 'Education' ,
	"Chef de projet informatique" : 'Informatique' , 
	"Technicien en réseaux"       : 'Informatique' , 
	"conseiller clientele"        : 'Telecom' , 
	"Property manager"            : 'Juridique' , 
	"Cadre en ressource humaine"  : 'Ressources Humaines' , 
	'Asssistante SAP'             : 'Distribution' ,
	"chef de secteur"             : 'Distribution' ,
	"Shef de rayon"               : 'Distribution' ,
	"Asssistante commerciale"     : 'Marketing' ,
	"Electricien fibre optique"   : 'Batiment et Travaux publics' , 
	"conducteur de traveaux"      : 'Batiment et Travaux publics' , 
	"Logisticien/Supply Chain"    : 'Logistique' , 
	"Approvisionneur"             : 'Industrie' , 
	"magasinier"                  : 'Industrie' , 
	"Chef de produits"            : 'Agriculture' ,
	"Controleur de gestion"       : 'Agroalimentaire' 
} 

REGIONCHOICES = [ 
	('all', ('Tous.....')),
	('1', ('Nord Pas de Calais')), 
	('2', ('Picardie')), 
	('3', ('Haute Normandie')), 
	('4', ('Basse Normandie')), 
	('5', ('Ile de France')), 
	('6', ('Bretagne')), 
	('7', ('Champagne Ardenne')), 
	('8', ('Alsace')), 
	('9', ('Pays de la Loire')), 
	('10', ('Centre')), 
	('11', ('Bourgogne')), 
	('12', ('Rhone Alpes')), 
	('13', ('Aquitaine')), 
	('14', ('PACA')), 
	('15', ('Corse')), 
	('16', ('Midi Pyrenees')), 
	('17', ('Languedoc Roussillon')), 
	('18', ('Lorraine')),
	('19', ('Poitou Charentes')),
	('20', ('Limousin')),
	('21', ('Auvergne')),
	('22', ('Franche Comte'))
]

OFFERCHOICES = [
	('all', ('Tous.....')),
	('1', ('Freelance')),
	('2', ('CDD')),
	('3', ('CDI')),
	('4', ('Stage')),
	('5', ('Interim'))
]


CATEGORY_CHOICES = [('all', 'Tous....'),
	('1', 'Assurance'),
	('2', 'Banque'),
	('3', 'Comptabilite'), 
	('4', 'Finance'), 
	('5', 'Informatique'), 
	('6', 'Telecom'), 
	('7', 'Juridique'), 
	('8', 'Ressources Humaines'), 
	('9', 'Communication'),
	('10', 'Distribution'),
	('11', 'Marketing'),
	('12', 'Batiment et Travaux publics'), 
	('13', 'Immobilier'), 
	('14', 'Logistique'), 
	('15', 'Securite'), 
	('16', 'Transport'),
	('17', 'Energie et nucleaire'), 
	('18', 'Industrie'), 
	('19', 'Agriculture'),
	('20', 'Agroalimentaire'), 
	('21', 'Artisanat'),
	('22', 'Energies renouvelables'),
	('23', 'Environnement'),
	('24', 'Recherche et Developpement'),
	('25', 'Luxe'), 
	('26', 'Mode'), 
	('27', 'Production'),
	('28', 'Audiovisuel'),
	('29', 'Culture'), 
	('30', 'Tourisme'), 
	('31', 'Biotechnologies'), 
	('32', 'Sante'),
	('33', 'Social'), 
	('34', 'Animation'), 
	('35', 'Education'),
	('36', 'Humanitaire'), 
	('37', 'Hotellerie'),
	('38', 'Nettoyage'), 
	('39', 'Restauration'), 
	('40', 'International'),
	('41', 'Travailleur Handicape'),
	('42', 'Stage (- de 2 mois)'), 
	('43', 'Stage (2 mois et +)')
]

u = User.objects.get(username='logika')

for x in range(1,len(di)):
	
	title = di.items()[x][0]
	region = REGIONCHOICES[random.randrange(1,len(REGIONCHOICES))][0] 
	offer = OFFERCHOICES[random.randrange(1, len(OFFERCHOICES))][0] 
	salaire = random.randrange(1, 17)
	immediat = random.choice( ["Used", 'New'] )
	description = "lorem sipsum dolore sit amet lorem ipsum dolore sit amet lorem ipsum dolore sit amet lorem ipsum dolore sit amet"

	print region, "----", title, '------' , offer, '------', salaire, '--------', immediat, '--------',region

	o = Offer(user = u, title=title, offerType=offer, region=region, salary=salaire, immediate = immediat,  description = description )
	o.save()

