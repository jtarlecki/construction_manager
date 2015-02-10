from django.db import models
from django.core.validators import RegexValidator
import datetime

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=500)
    owner = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    state = models.CharField(max_length=500, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)    
    email = models.EmailField()
    website = models.URLField(max_length=2000)
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  

    def __unicode__(self):
        return self.name
    
class Employees(models.Model):
    name = models.CharField(max_length=500)
    initials = models.CharField(max_length=5)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    company = models.ForeignKey(Company)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # '(\d{3})\D*(\d{3})\D*(\d{4})
    phone_regex = RegexValidator(regex=r'(\d{3})\D*(\d{3})\D*(\d{4})$', message="Phone number must be entered in the format: '800-555-1212'")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    state = models.CharField(max_length=500, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    email = models.EmailField()
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']    
    

class JobPhases(models.Model):
    jobphase = models.CharField(max_length=1000)
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  
    
    def __unicode__(self):
        return self.jobphase    

class Jobs(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True)
    est_start_date = models.DateField(auto_now_add=True, blank=True)
    start_date = models.DateField(blank=True)
    est_end_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    active = models.BooleanField(default=True)
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['createddate']    
    
class Vendors(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length = 1000, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list
    address1 = models.CharField(max_length=500, blank=True)
    address2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=500, blank=True)
    state = models.CharField(max_length=500, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)    
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=2000, blank=True)
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  

    def __unicode__(self):
        if self.location == '':
            return self.name
        else:
            return '%s (%s)' % (self.name, self.location)
    
    class Meta:
        ordering = ['name']

class Materials(models.Model):
    job = models.ForeignKey(Jobs)
    vendor = models.ForeignKey(Vendors)    
    phase = models.ForeignKey(JobPhases)    
    price = models.DecimalField(decimal_places=2, max_digits=15)
    comments = models.TextField(max_length=5000)
    date = models.DateField(default=datetime.date.today)
    receipt_number = models.CharField(max_length=250, blank=True)
    createduser = models.CharField(max_length=50, default='admin')
    createddate = models.DateField(auto_now_add=True)
    modifieduser = models.CharField(max_length=50, default='admin')
    modifieddate = models.DateField(auto_now=True)
  
    def amount(self):
        return '$%.2f' % (self.price)
    
    def __unicode__(self):            
        return '%s - %s $%d' % (self.job, self.vendor, self.price)
        # return '%s - %s %s' % (self.job, self.vendor, self.amount)
    
    class Meta:
        ordering = ['date']    
