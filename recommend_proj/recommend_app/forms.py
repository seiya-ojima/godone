from django import forms
from .models import Parameter

class InputForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ('name', 'max_price', 'min_price', 'product_price', 'price_weight', 'max_size', 'min_size', 'product_size', 'size_weight', 'max_memory', 'min_memory', 'product_memory', 'memory_weight')
