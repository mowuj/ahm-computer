from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ManyToManyField(Category)
    Brand = models.ManyToManyField(Brand)
    image = models.ImageField(
        default='default.jpg', upload_to='media/images')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
