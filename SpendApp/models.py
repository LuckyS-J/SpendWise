from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    COLOR_CHOICES = [
        ('#FF6384', 'Red'),
        ('#36A2EB', 'Blue'),
        ('#FFCE56', 'Yellow'),
        ('#4BC0C0', 'Teal'),
        ('#9966FF', 'Purple'),
        ('#FF9F40', 'Orange'),
        ('#C0C0C0', 'Gray'),
    ]

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#C0C0C0')

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.amount} zł"