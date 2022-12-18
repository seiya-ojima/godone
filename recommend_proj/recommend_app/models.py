from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Parameter(models.Model):
    name = models.CharField('製品名', max_length=30)
    max_price = models.IntegerField('最高価格')
    min_price = models.IntegerField('最低価格')
    product_price = models.IntegerField('値段')
    price_weight = models.IntegerField('価格の重み(%)', validators=[MinValueValidator(0), MaxValueValidator(100)])
    price_score = models.IntegerField('価格評価', null=True, blank=True)
    max_size = models.IntegerField('最高サイズ')
    min_size = models.IntegerField('最低サイズ')
    product_size = models.IntegerField('サイズ')
    size_weight = models.IntegerField('サイズの重み(%)', validators=[MinValueValidator(0), MaxValueValidator(100)])
    size_score = models.IntegerField('サイズ評価', null=True, blank=True)
    max_memory = models.IntegerField('最高メモリ')
    min_memory = models.IntegerField('最低メモリ')
    product_memory = models.IntegerField('メモリ')
    memory_weight = models.IntegerField('メモリの重み(%)', validators=[MinValueValidator(0), MaxValueValidator(100)])
    memory_score = models.IntegerField('メモリ評価', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.price_score = 100 - round(self.product_price/(self.max_price - self.min_price)*100)
        self.size_score = round(self.product_size/(self.max_size - self.min_size)*100)
        self.memory_score = round(self.product_memory/(self.max_memory - self.min_memory)*100)
        super().save(*args, **kwargs)