from django.db import models
from datetime import timedelta,datetime
# Create your models here.

class libraryinfo(models.Model):
	book_id=models.IntegerField()
	book_name=models.CharField(max_length=100)
	author_name=models.CharField(max_length=100)
	student_name=models.CharField(max_length=100)
	student_roll_no=models.IntegerField()
	borrow_date=models.DateTimeField(auto_now_add=False,auto_now=False)
	due_date=models.DateTimeField(auto_now_add=True,auto_now=False)


	
