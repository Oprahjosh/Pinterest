from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms




class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    Age = forms.CharField()

    class Meta:
        model = User
        fields = ['email','password1','Age','password2']

    def save(self , commit=True):
        user = super ( RegisterForm , self ).save ( commit=False )
        user.email = self.cleaned_data["email"]
        user.Age = self.cleaned_data['Age']
        if commit:
            user.save ()
        return user

    def __init__(self , *args , **kwargs):
        super ( RegisterForm , self ).__init__ ( *args , **kwargs )
        self.fields.pop ( 'password2' )

'''class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']'''