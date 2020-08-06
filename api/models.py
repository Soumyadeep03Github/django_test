from django.db import models

# Create your models here.
class user(models.Model): 
    id = models.CharField(primary_key=True, max_length=25)
    real_name = models.CharField( blank=False, max_length=255)
    tz = models.CharField( blank=False, max_length=255)
   
    def __str__(self):
        return self.real_name

class activity_periods(models.Model):
    user_id = models.ForeignKey(user, on_delete = models.CASCADE) 
    start_time = models.CharField( blank=False, max_length=255)
    end_time = models.CharField( blank=False, max_length=255)
   
    def __str__(self):
        return self.user_id.real_name +"_"+ str(self.id)
