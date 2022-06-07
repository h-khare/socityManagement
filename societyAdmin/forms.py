from django import forms

class AdminLogin(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    
class Carpenters(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    
class Plumbers(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    
class Electricians(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))

class Painters(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    
class Roofers(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control"}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}),max_length=10)
    address=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    
    