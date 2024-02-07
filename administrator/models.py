from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['-name']),
        ]

    def __str__(self):
        return self.name


class Member(models.Model):
    sex =(('Male', 'Male'),('Female', 'Female'),)
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=200, null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=200, blank=True,null=True,choices=sex,default='Male')
    assembly= models.CharField(max_length=200, blank=True,null=True)
    district = models.CharField(max_length=200,null=True,blank=True)
    denomination = models.CharField(max_length=200, blank=True,null=True)
    country = models.CharField(max_length=200, blank=True,null=True, default='Nigeria')
    state= models.CharField(max_length=200, blank=True,null=True)
    department= models.ForeignKey(Department,blank=True, null=True, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
        ]
    def __str__(self):
        return self.name
    
    
    

class Question(models.Model):
    name = models.CharField(max_length=200, blank=True,null=True)
    email = models.EmailField(max_length=200, null=True)
    subject= models.CharField(max_length=200, blank=True,null=True)
    question = models.CharField(max_length=200,null=True)
    date= models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
        ]

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    
class Attendance(models.Model):
    day =(('Day 1', 'Day 1'),('Day 2', 'Day 2'),('Day 3', 'Day 3'))
    member = models.ForeignKey(Member,blank=True, null=True, on_delete=models.CASCADE)
    day = models.CharField(max_length=200, blank=True,null=True,choices=day)
    date= models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
        ]
        
    def __str__(self):
        return str(self.member)
    