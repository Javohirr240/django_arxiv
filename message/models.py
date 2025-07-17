from django.db import models

class Contact(models.Model):
  firstname = models.CharField(max_length=100)
  lastname =models.CharField(max_length=100)
  phone_number = models.CharField(max_length=13)
  email = models.EmailField()
  message = models.TextField()

  def __str__(self):
    return self.firstname
