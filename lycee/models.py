from django.db import models
from django.urls import reverse

class Cursus(models.Model):
  name = models.CharField(
    max_length=50,
    blank=False,
    null=True,
    default='aucun'
    )
  year_from_bac = models.SmallIntegerField(
    help_text ="year since le bac",
    verbose_name="year",
    blank=False,
    null=True,
    default=0
  )
  scholar_year = models.CharField(
    max_length=9,
    blank=False,
    null=True,
    default='0000-00001'
  )

  def __str__(self):
    return'{} {}'.format (self.name,self.scholar_year)


class Student(models.Model):
  first_name = models.CharField(
    max_length=50,
    blank=False,
    null=False
  )
  birth_date = models.DateField(
    verbose_name='date of birth',
    blank=False,
    null=True
  )
  last_name = models.CharField(
    verbose_name="lastname",
    help_text="last name of the student",
    blank=False,
    null=False, 
    default="???",
    max_length=255,
  )
  phone = models.CharField(
    verbose_name="Phone number",
    help_text="phone number of the student",
    blank=False, 
    null=False, 
    default="0999999999",
    max_length=10,
  )
  email = models.EmailField(
    verbose_name="Email",
    help_text="",
    blank=False, 
    null=False,
    default="x@y.z",
    max_length=255,
  )
  comments = models.CharField(
    verbose_name="comments",
    help_text="some comments about the student",
    blank=True,
    null=False, 
    default="",
    max_length=255, 
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE, 
    null=True
  )

  def __str__(self):
    return'{} {} {}'.format (self.first_name,self.last_name,self.email)

class Presence(models.Model):
  date = models.DateField(
    verbose_name="Date of call",
    blank=False,
    null=False,
  )

  isMissing = models.BooleanField(
    verbose_name="Is Missing",
    default = True
  )

  reason = models.CharField(
    verbose_name="Reason",
    help_text="Raison de l'absence",
    blank=False, 
    null=False, 
    default="",
    max_length=255, 
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE, 
    null=True,
  )
  student =  models.ManyToManyField(
    Student,
  )

  def get_absolute_url(self):
        return reverse('index')

  def __str__(self):
    return'{} {} {} {}'.format (self.date,self.isMissing,self.reason, self.cursus)

class ParticularPresence(models.Model):
  date = models.DateField(
    verbose_name="Date of call",
    blank=False, 
    null=False, 
  )

  isMissing = models.BooleanField(
    verbose_name="Is Missing"
  )

  reason = models.CharField(
    verbose_name="Reason",
    help_text="Raison de l'absence",
    blank=False, 
    null=False, 
    default="",
    max_length=255, 
  )
  cursus = models.ForeignKey(
    Cursus,
    on_delete=models.CASCADE, 
    null=True,
  )
  student =  models.ForeignKey(
    Student,
    on_delete=models.CASCADE, 
    null=True,
  )

  def get_absolute_url(self):
        return reverse('index')

  def __str__(self):
    return'{} {} {} {}'.format (self.date,self.isMissing,self.reason, self.cursus)

  