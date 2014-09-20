# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from registration.signals import user_registered

from car_shop.model_choices import *
from django.db.models.signals import post_save
from django.dispatch import receiver

import subprocess
from django.conf import settings
from PyPDF2 import PdfFileReader, PdfFileWriter

profile_type = ((True, 'Candidat'), (False, 'Recruteur') )

class ExUserProfile(models.Model):
    user        = models.ForeignKey(User, unique=True)
    is_candid   = models.CharField(max_length=230)
 
    def __unicode__(self):
        return unicode(self.user)

class Profile_emp(models.Model):
    user        = models.ForeignKey(User, unique=True)
    is_candid   = models.CharField(max_length=230)

    class Meta:
        verbose_name        = "Employeur"
        verbose_name_plural = 'Emplyeurs'

    def __unicode__(self):
        return unicode(self.user)

    created_at   = models.DateTimeField(auto_now_add = True)
    society      = models.CharField(max_length=200, null=True, blank=True)
    phone        = models.CharField(max_length=200, null=True, blank=True)
    postal_code  = models.CharField(max_length=200, null=True, blank=True)
    town         = models.CharField(max_length=200, null=True, blank=True)
    website      = models.CharField(max_length=200, null=True, blank=True)
    presentation = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user)    

    def get_offers(self):
        offers = self.user.offer_set.all()
        return offers

    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr( self, get_choice): value = getattr( self, get_choice)()
            else:
                try : value = getattr(self, fname)
                except User.DoesNotExist: value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'user', 'is_candid', 'created_at', 'presentation') :
                fields.append( f.name )

        keys = ['society', 'phone', 'postal_code', 'town', 'website']

        msg = None
        print fields
        for i in keys:
            if not i in fields:
                msg = 'Veuillez completez votre profile s\'il vous plait ' 
                break
            else:
                continue 
        return msg    



class Profile_candid(models.Model):
    user        = models.ForeignKey(User, unique=True)
    is_candid   = models.CharField(max_length=230)


    created_at    = models.DateTimeField(auto_now_add=True)
    last_name     = models.CharField(verbose_name = u'Nom de famille', max_length=200, null=True, blank=True)
    adress        = models.CharField(verbose_name = u'Adresse', max_length=200, null=True, blank=True)
    telephone     = models.CharField(verbose_name = u'Telephone', max_length=200, null=True, blank=True)
    # recently added fields
    sector1       = models.CharField(verbose_name = u'Secteur 1', max_length = 200,choices=CATEGORY_CHOICES, null=True, blank=True, default='0')
    sector2       = models.CharField(verbose_name = u'Secteur 2', max_length = 200,choices=CATEGORY_CHOICES, null=True, blank=True,default='0')
    sector3       = models.CharField(verbose_name = u'Secteur 3', max_length = 200,choices=CATEGORY_CHOICES, null=True, blank=True, default='0')
    # mobility
    mobility1     = models.CharField(verbose_name = u'Mobilité 1', max_length = 200,choices=DEPARTEMENT_CHOICES, null=True, blank=True, default='0')
    mobility2     = models.CharField(verbose_name = u'Mobilité 2', max_length = 200,choices=DEPARTEMENT_CHOICES, null=True, blank=True, default='0')
    mobility3     = models.CharField(verbose_name = u'Mobilité 3', max_length = 200,choices=DEPARTEMENT_CHOICES, null=True, blank=True, default='0')
    
    disponibility = models.CharField(verbose_name = u'Disponibilité', max_length = 200,choices=DISPONIBILITY_CHOICES, null=True, blank=True, default='0')
    
    status        = models.CharField(verbose_name = u'Status', max_length = 200, choices=STATUS_CHOICES, null=True, blank=True ,default='0') 
    salary        = models.CharField(verbose_name = u'Salaire', max_length = 200, choices=SALARY_CHOICES, null=True, blank=True ,default='0') 
    
    study_level   = models.CharField(verbose_name = u'Niveau d\'etudes', max_length = 200, choices=STUDY_LEVEL_CHOICES, null=True, blank=True ,default='0') 
    experience    = models.CharField(verbose_name = u'Experience', max_length = 200, choices=EXPERIENCE_CHOICES,  null=True, blank=True ,default='0') 
    contract      = models.CharField(verbose_name = u'Contrat', max_length = 200, choices=OFFER_CHOICES, null=True,  blank=True,default='0') 
    period        = models.CharField(verbose_name = u'periode', max_length = 200, choices=PERIOD_CHOICES, null=True, blank=True,default='0') 
    
    languages     = models.CharField(verbose_name = u'langues', max_length=200, null=True, blank=True, default='')
    document      = models.FileField(verbose_name = u'CV', upload_to = 'uploads/pdfs/', null=True, blank=True)

    class Meta:
        verbose_name        = "Candidat"
        verbose_name_plural = 'Candidats'
 
    def __unicode__(self):
        return unicode(self.user)

    def get_pdf_image(self):
        the_file = self.document.file.name.split('/')[-1].split('.')[0]
        return '%s/pdfs_images/img-%s.jpg' %( "/".join(self.document.file.name.split('/')[:-2] ), the_file)

    def get_absolute_url(self):
        return '/candidate/%s'%(self.id)

    def get_all_fields(self):
        """Returns a list of all field names on the instance."""
        fields = []
        for f in self._meta.fields:

            fname = f.name        
            # resolve picklists/choices, with get_xyz_display() function
            get_choice = 'get_'+fname+'_display'
            if hasattr( self, get_choice): value = getattr( self, get_choice)()
            else:
                try : value = getattr(self, fname)
                except User.DoesNotExist: value = None

            # only display fields with values and skip some fields entirely
            if f.editable and value and f.name not in ('id', 'workshop', 'user', 'complete', 'is_candid') :
                fields.append( f.name )

        keys = ['last_name', 'adress', 'telephone', 'sector1', 'sector2', 'sector3', 'mobility1', 'mobility2', 'mobility3', 'disponibility', 'status', 'salary', 'study_level', 'experience', 'contract', 'period', 'languages']    

        msg = None
        for i in keys:
            if not i in fields:
                msg = 'Veuillez completez votre profile s\'il vous plait ' 
                break
            else:
                continue 
        return msg
    
def pdf_post_save(sender, instance=False, **kwargs):

    pdf = Profile_candid.objects.get(pk=instance.pk)
    if pdf.document:
        new_name =  pdf.document.file.name.split('/')[-1].split('.')[0]

        output = PdfFileWriter()
        pdfOne = PdfFileReader(file( '%s/%s' % (settings.MEDIA_ROOT, pdf.document), "rb"))
        output.addPage(pdfOne.getPage(0))

        outputStream = file(r'%s/uploads/first/%s-first.pdf'  % (settings.MEDIA_ROOT, new_name), "wb")
        output.write(outputStream)
        outputStream.close()

        params = ['convert', 
                    '-blur' ,'4x6',
                    (r'%s/uploads/first/%s-first.pdf')  % (settings.MEDIA_ROOT, new_name),
                     '%s/uploads/pdfs_images/img-%s.jpg' % (settings.MEDIA_ROOT, new_name )
                     ]
        subprocess.check_call(params)

post_save.connect(pdf_post_save, sender=Profile_candid)       


# this called after creation of temporary user
def user_registered_callback(sender, user, request, **kwargs):
    profile = ExUserProfile(user = user)
    profile.is_candid = request.POST["is_candid"]

    if profile.is_candid == '1':
        c = Profile_candid(user = user, is_candid ='cand remotly set')
        #add user to candidate group
        gr = Group.objects.get(name='candidate')
        gr.user_set.add(user)
        c.save()
    elif profile.is_candid == '0': 
        c = Profile_emp(user = user, is_candid ='Emp remotly set', society = user.username)
        # add user to employer group
        gr = Group.objects.get(name='employer')
        gr.user_set.add(user)    
        c.save()

user_registered.connect(user_registered_callback)


