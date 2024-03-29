from django.db import models
from django.urls import reverse

# Create your models here.

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    #Fields
    my_field_name = models.CharField(max_length = 20, help_text = 'Enter field documentation')
    #...

    #Metadata
    class Meta:
        ordering = ['-my_field_name']
        
    # Methods
    def get_absolute_url(self):
        """Return the URL to access a particule instance of MyModelName"""
        return reverse('model-detail-view', args = [str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)"""
        return self.my_field_name
    

