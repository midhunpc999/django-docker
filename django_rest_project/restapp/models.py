from django.db import models

# Create your models here.

class ClassStudent(models.Model):

   student_name = models.CharField(max_length = 50)
   rollno = models.IntegerField()

   class Meta:
       db_table = "classstudent"

   def __str__(self):
       return self.student_name