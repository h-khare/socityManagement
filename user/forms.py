from django import forms

class UserLogin(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

class UserRegistration(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))