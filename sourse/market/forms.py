from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Наименование товара')
    balance = forms.IntegerField(min_value=0, required=True, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Цена товара')
