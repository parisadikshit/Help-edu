from django.db import models

# Create your models here.
class School(models.Model):
    School_id = models.AutoField
    School_name = models.CharField(max_length=200)
    School_city = models.CharField(max_length=100)
    School_loc = models.CharField(max_length=500,default=" ")
    School_desc = models.TextField(default="")

    def __str__(self):
        return self.School_name

class Document(models.Model):
    name = models.CharField(max_length=30,default="")
    description = models.CharField(max_length=200,default="")
    document = models.FileField(upload_to="document/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)