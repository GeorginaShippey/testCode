from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        
class Group(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey('Client')
    subgroups = models.ManyToManyField('Group', blank=True, symmetrical=False)
    
    def __str__(self):
        return self.name
        
class Site(models.Model):
    name = models.CharField(max_length=200)
    client = models.ForeignKey('Client')
    groups = models.ManyToManyField(Group, blank=True)
    
    def __str__(self):
        return self.name
        
#from reports.model import *
#Site.objects.filter(groups__id=1)
#Site.objects.filter(groups__name='')

#Site.objects.filter(client__name__contains='A')
#Returns a list of all sites that belong to a client whose names contains an A

#Site.objects.filter(client__name__contains='A', group__name='')
#Returns a list of sites that ARE in a group and belong to a client whose name contains an A
