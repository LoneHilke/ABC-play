from django.db import models

class Alfabeth(models.Model):
    image = models.ImageField(upload_to='images/')
    ord = models.CharField(max_length=50)
    beskrivelse = models.TextField(blank=True)
    bugstab = models.ManyToManyField('bugstab', related_name='item')


    def __str__(self):
        return self.ord
    
class Bugstab(models.Model):
    bugstab = models.CharField(max_length=10)

    def __str__(self):
        return self.bugstab