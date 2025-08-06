from django import forms
from .models import Car, Contract, Driver, User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'number_plate', 'color']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['user', 'driver', 'from_address', 'to_address', 'distance_km']

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'phone', 'car']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone', 'address']
