from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)
    link = models.CharField(max_length=1000,default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movieapp:movie_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):

    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True)
    release_date = models.DateField()
    actors = models.CharField(max_length=250)
    ytlink = models.CharField(max_length=1000)
    username = models.CharField(max_length=250,default=False)

    def get_url(self):
        return reverse('movieapp:movieCatDetail',args=[self.category.slug,self.slug])
    def get_url_p(self):
        return reverse('movieapp:movie_by_category',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)