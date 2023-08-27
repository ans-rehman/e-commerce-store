from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.PositiveIntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField(null=True)
    image = models.ImageField(upload_to='products/images', default="")
    status= models.BooleanField(default=True)

    def __str__(self):
        return self.product_name