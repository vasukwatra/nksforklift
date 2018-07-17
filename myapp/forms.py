from .models import NKS
from django import forms
class NKS_form(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    middle_initial =forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    last_name =forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    address = forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    city = forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    province =forms.CharField(widget=forms.TextInput(),required=True,max_length=20)
    postal_code = forms.IntegerField(widget=forms.TextInput(),required=True)
    residential_phone = forms.IntegerField(widget=forms.TextInput(),required=True)
    cell_phone = forms.IntegerField(widget=forms.TextInput(),required=True)
    operator_number = forms.IntegerField(widget=forms.TextInput(),required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(),required=True)

    class Meta():
        model=NKS
        fields=['first_name','middle_initial','last_name','address','city','province','postal_code','residential_phone','cell_phone','operator_number','date']



