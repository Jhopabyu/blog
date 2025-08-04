from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from decouple import config
from django.core.mail import send_mail
from cloudinary.models import CloudinaryField   

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    photo= models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Bienvenido a Servicios Mineria',
            str('Hola ' + instance.full_name + ', usted se ha registrado satisfactoriamente en esta pagina. ' 
                                               '¡Es un placer que seas parte de nuestra familia!'),
            config('EMAIL_HOST_USER'),
            [instance.email]
    )    
        