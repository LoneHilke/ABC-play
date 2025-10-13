from django.db import models

class Words(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)
    letter = models.ManyToManyField('letter', related_name='item')


    def __str__(self):
        return self.ord
    
class Letter(models.Model):
    letter = models.CharField(max_length=10)

    def __str__(self):
        return self.letter
