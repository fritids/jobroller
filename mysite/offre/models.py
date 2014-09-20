# -*- coding: utf-8 -*-                 
from django.db import models
# from car_shop.fields import ThumbnailImageField 
from car_shop.model_choices import *
import datetime
import math
from offre.managers import OfferManager
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

import subprocess
from django.conf import settings
from PyPDF2 import PdfFileReader, PdfFileWriter


class Offer(models.Model):
    """ Modele pour les offres de travail """
    user        = models.ForeignKey(User)
    
    title       = models.CharField(max_length=250)
    offerType   = models.CharField(max_length = 200, choices=OFFER_CHOICES, default='1')
    category    = models.CharField(max_length = 200, choices=CATEGORY_CHOICES, default='1')
    region      = models.CharField(max_length = 200, choices=REGION_CHOICES)
    salary      = models.CharField(max_length = 200, blank=True, choices=SALARY_CHOICES)
    
    views       = models.CharField(_('Views count'),max_length = 200, blank=True, default=0)
    description = models.TextField(_('description'), blank=True, null=True)
    
    created     = models.DateTimeField(_('Created'), null=True)
    modified    = models.DateTimeField(_('Modified'), null=True)
    immediate   = models.CharField(max_length = 20, choices=YESNO, default='1')
    
    activated   = models.BooleanField(_('Activated'), blank=True, default=True)

    class Meta:
        verbose_name        = _('Offre')
        verbose_name_plural = _('Offres')
    
    def __unicode__(self):
        return unicode(OFFER_CHOICES[int(self.offerType)][1])

    def get_absolute_url(self): return '/offre/%s'%(self.id)

    def get_absolute_url(self): return '/offer/%s' %(self.id)

    def get_disable_url(self): return '/offer/%s/disable' %(self.id)

    def get_activation_url(self): return '/offer/%s/activate' %(self.id)

    def get_edition_url(self): return '/offer/%s/edit' %(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id: self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Offer, self).save(*args, **kwargs) 
    
    # this a function for the image list display
    def image_tag(self):

        return u'<img src="%s" width="80" height="80" />' % self.image.url
        image_tag.short_description = 'Image'

    image_tag.allow_tags = True 

    objects = OfferManager() # pour avoir que les objets active: Offer.objects.is_watermaked
    # objects = models.Manager() # On garde le manager par default
