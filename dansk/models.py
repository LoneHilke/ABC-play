from django.db import models

# Create your models here.
class Alfabet(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)
    bogstav = models.ManyToManyField('bogstav', related_name='item')


    def __str__(self):
        return self.ord
    
class Bogstav(models.Model):
    bogstav = models.CharField(max_length=10)

    def __str__(self):
        return self.bogstav
    