from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    image=models.ImageField(upload_to="emp_img")
    phone=models.IntegerField()
    stime=models.TimeField(default='10:00:59')
    etime=models.TimeField(default='16:00:59')
    options=[
        ('feild work','Feild Work'),
        ('tree work','Tree Work'),
        ('plantation work','Plantation Work'),
        ('ferilizer','Ferilizer'),
        ('farmer tech','Farmer Tech'),
        ('cunstruction','Cunstruction')
    ]
    category=models.CharField(choices=options,max_length=100)
    def __str__(self):
        return self.name
    