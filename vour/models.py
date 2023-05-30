from django.db import models

# Create your models here.
class Career(models.Model):
    career= models.CharField(max_length=50)
    def __str__(self):
        return self.career
    
    
GENDER= (
    (_)
)