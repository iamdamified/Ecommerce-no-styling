from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('M', 'Men'),
    ('W', 'WOmen'),
    ('G', 'General')
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images", default="product.jpg")

    # class Meta:
    #     verbose_name_plural = 'producties'# USed to control the model display in the admin.

    def __str__(self):
        return self.name