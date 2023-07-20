from django.db import models

class Inscritos(models.Model):     
    id = models.AutoField(primary_key=True)     
    name = models.CharField(max_length=50)          
    phone = models.IntegerField()     
    regis_date = models.DateField()     
    institution = models.CharField(max_length=15)     
    regis_time = models.TimeField()     
    state = models.CharField(max_length=15)     
    observation = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)+ ""+ self.name + "(Observación: "+ str(self.observation) + ")"
    
