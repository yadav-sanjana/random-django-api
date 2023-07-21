from django.db import models

SIZES = (
    ('S', 'XS'),
    ('M', 'L'),
    ('XL', 'LL'),
)

class Item(models.Model):
    item_id = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    fitting_type = models.CharField(max_length=50)
    is_imported = models.BooleanField(default=False)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    colors = models.CharField(max_length=200)
    

    def __str__(self):
        return self.item_id

class Category(models.Model):
    name = models.CharField(max_length=100)
    sizes = models.CharField(max_length=10, choices=SIZES, default='S')

    def __str__(self):
        return self.name
