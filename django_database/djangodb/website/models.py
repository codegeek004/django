from django.db import models

class Members(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length=150)
	password = models.CharField(max_length=200)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	
	#what we display on admin as members
	def __str__(self):
		return self.fname + ' ' + self.lname
