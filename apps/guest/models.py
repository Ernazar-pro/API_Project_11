from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.id}'
    
