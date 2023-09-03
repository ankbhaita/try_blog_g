from django.db import models
from authuser.models import User
from datetime import datetime


STATUS_CHOICES=(
	('pen','pending'),
	('Re','Reject'),
	('App','Apporved'),
	
	)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc=models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0])
    

    def __str__(self):
        return self.title

    




