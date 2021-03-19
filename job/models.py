from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    STATUSES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, null=True)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.FloatField()
    image = models.FileField()
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title
