from django import forms
class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    patronymic = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=13)
    client_account = forms.DecimalField(max_digits=13, decimal_places=2)