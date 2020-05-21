from django.db import models

# Create your models here.
class Users(models.Model):
    employee_id = models.CharField(max_length=20,null=True, blank=True,unique=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def upload_photo(self, filename):
        path = 'applicationHR/documents/photo/{}'.format(filename)
        return path
    photo = models.ImageField(upload_to=upload_photo, null=True,blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"


#http POST "http://localhost:8000/api/v1/employees/" name='xgfhcg' positionId='xcfvgh' age=23 salary=7 workedFor='dfgh' scoreBefore=4.5 scoreAfter=6.7 starred=False
#http GET "http://localhost:8000/api/v1/employees/"