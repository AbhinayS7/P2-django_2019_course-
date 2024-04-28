from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=50,default='')
    sub_category = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.product_name