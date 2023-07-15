from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('non IT', 'non IT')))
    created_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=True)