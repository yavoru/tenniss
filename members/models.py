from django.db import models

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=255,null=True)
	quantity = models.IntegerField(null=True)
	age = models.IntegerField(null=True)
	create_date = models.DateField(null=True)
	image = models.ImageField(upload_to='image/',null=True,blank=True)
	def __str__(self):
		return self.name
