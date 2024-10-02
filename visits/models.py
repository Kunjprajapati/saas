from django.db import models

# Create your models here.
class VisitsModel(models.Model):
    # Creating a df with listed number of columns 
    path = models.TextField(null=True, blank=True) # First Column....
    timing = models.DateTimeField(auto_now_add=True) # Second Column

