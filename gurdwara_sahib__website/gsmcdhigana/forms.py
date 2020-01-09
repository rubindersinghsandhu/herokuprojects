from django import forms
from .models import post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class userloginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

    def clean(self,*args,**kwargs):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        if username and password:
            user =authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Login Failed! Enter login Credentials carefully')
        return super(userloginform, self).clean(*args,**kwargs)


class postForm(forms.ModelForm):
    class Meta:
        model=post
        fields='__all__'





