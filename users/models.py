from django.db import models

# Create your models here.
class Passwords(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  website = models.CharField(max_length=100)
  login = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
      return self.name
    
  def getNameWebsiteLogin(self):
    return {'name': self.name, 'website': self.website, 'login': self.login}