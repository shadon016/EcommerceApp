from django.db import models


size_choices=(
    ('M','M'),
    ('L','L'),
    ('XL','XL'),

)
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Products(models.Model):
    product_name=models.CharField(max_length=50)
    product_details=models.TextField(max_length=250)
    photo=models.ImageField(upload_to='products')
    price=models.IntegerField(default=0)
    size=models.CharField(choices=size_choices,max_length=50,null=True,blank=True)
    stock=models.IntegerField(default=0)
    uploaded_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.product_name


