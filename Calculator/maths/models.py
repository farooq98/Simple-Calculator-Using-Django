from django.db import models

# Create your models here.
class math(models.Model):
    operands = (('+', '+'), ('-', '-'), ('x', 'x'), ('/', '/'))
    num1 = models.CharField(max_length=10)
    num2 = models.CharField(max_length=10)
    operation = models.CharField(max_length=1, choices=operands)
