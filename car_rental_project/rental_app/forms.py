from django import forms
from .models import registration,price,car_return

class reg_class(forms.ModelForm):
    class Meta:
        model=registration
        fields='__all__'

class priceform(forms.ModelForm):
    class Meta:
        model=price
        fields='__all__'

class car_return_form(forms.ModelForm):
    class Meta:
        model=car_return
        fields='__all__'
