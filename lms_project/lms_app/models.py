from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=15, unique=True)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    college_name = models.CharField(max_length=255, blank=True)
    course_name = models.CharField(max_length=255, blank=True)
    branch_name = models.CharField(max_length=255, blank=True)
    college_address = models.TextField(blank=True)
    student_address = models.TextField(blank=True)
    pin_code = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
