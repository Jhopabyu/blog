from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from ckeditor.fields import RichTextField   
from cloudinary.models import CloudinaryField

# Create your models here.
#categoria
class Category (models.Model):
    name = models.CharField(max_length=20)
    image = CloudinaryField('image')
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

#Articulo      
class Article (models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = CloudinaryField('image')
    body = RichTextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'        

#Calificacion
class Rating (models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user_id.username
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'