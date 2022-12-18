from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Parameter(models.Model):
    name = models.CharField('製品名', max_length=30)
    max_price = models.IntegerField('最高価格')
    min_price = models.IntegerField('最低価格')
    product_price = models.IntegerField('値段')
    price_weight = models.IntegerField('値段の重み', validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_size = models.IntegerField('最高サイズ')
    min_size = models.IntegerField('最低サイズ')
    product_size = models.IntegerField('サイズ')
    size_weight = models.IntegerField('サイズの重み', validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_memory = models.IntegerField('最高メモリ')
    min_memory = models.IntegerField('最低メモリ')
    product_memory = models.IntegerField('メモリ')
    memory_weight = models.IntegerField('メモリの重み', validators=[MinValueValidator(0), MaxValueValidator(100)])
    created = models.DateTimeField(auto_now=True)