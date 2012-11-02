from django.contrib.auth.models import User
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=False,help_text='Enter Product Name')
    description =  models.CharField(max_length=200,blank=True,help_text='Enter short description')
    slug = models.SlugField()
    price = models.IntegerField(max_length=10,help_text='Enter Price in Numbers',blank=True,)
    in_stock = models.BooleanField(default=True,help_text='Is the Product available')
    sku = models.IntegerField(blank=True,max_length=12,help_text='Enter Product Code')
    #user =
    old_price = models.IntegerField(max_length=10,help_text='Enter Price in Numbers',blank=True,)
    new_price = models.IntegerField(max_length=10,help_text='Enter Price in Numbers',blank=True,)
    category = models.CharField(max_length=50,help_text='Product Category eg Software', blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=True,help_text='Is the Product featured')
    supplier = models.CharField(max_length=50,help_text='Enter Manufacturer', blank=False)


    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

# Create your models here.
