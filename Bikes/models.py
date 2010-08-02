from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Bike(models.Model):
  seattube = models.IntegerField(max_length = 3)
  toptube = models.IntegerField(max_length = 3)
  downtube = models.IntegerField(max_length = 3)
  soheight = models.IntegerField(max_length = 3)
  make = models.CharField(max_length = 20)
  model = models.CharField(max_length = 20)
  year = models.DateField()
  type = models.CharField(max_length = 2 , choices = TYPE_CHOICES)
  TYPE_CHOICES = (
    (RD, Road),
    (MT, Mountain),
    (CZ, Cruser),
  )
  #wheels = CharField
  gears = models.IntegerField(max_length = 3)
  bars = models.CharField(max_length = 2)
  BAR_CHOICES = (
  (BH, Bull Horns
  (DD, Drop Bars),
  (ST, Straight Bars),
  (CZ, Cruzer),
  )
  #petals = CharField
  price = models.IntegerField(max_length = 7)
  pictures =
  fixedgear = BoolianFeild(Default = False)
  dateposted = DateTimeField(default = datetime.now)
  user = models.ForignKey(User)
  description = model.TextField(max_length = 500)
  
  
# class Help(models.Model):
#   make = TextField
#   model = TextField
#   type = TextField
#   height = TextField
#   wheels = TextField
#   gears = TextField
#   bars = TextField
#   petals = TextField
#   price = TextField
#   pictures = TextField
#   year = TextField