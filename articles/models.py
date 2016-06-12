from django.db import models
from django.utils import timezone

# Create your models here.
class Articles (models.Model):
	title= models.CharField(max_length=250)
	add_date= models.DateField()
	content= models.TextField(blank=True,null=True)
	
def __str__(self):
	return self.title
	
class Coment (models.Model):
	name =models.CharField(max_length=100)
	add_date= models.DateTimeField(timezone.now)
	content = models.TextField()
	article = models.ForeignKey(Articles)

def __str__(self):
	return self.name
