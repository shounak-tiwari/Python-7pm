from django.db import models

# Create enquiry model.

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    course = models.CharField(max_length=10)