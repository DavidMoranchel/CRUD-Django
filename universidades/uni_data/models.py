from __future__ import unicode_literals
from django.db import models



# Create your models here.
class Campus(models.Model):
	class Meta:
		verbose_name='Campus'
		verbose_name_plural='Campus'

	campus = models.CharField(max_length=30)

	def __str__(self):
		return self.campus

class Universidad(models.Model):
	class Meta:
		verbose_name='Universidad'
		verbose_name_plural='Universidades'
		
	nombre = models.CharField(max_length=30, blank= False)
	pais = models.CharField(max_length=30, blank=False)
	campus = models.ForeignKey(Campus, blank=True)

	def __str__(self):
		return self.nombre + ' campus ' + self.campus.campus



			