from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfilePlus

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='User', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'forms'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'forms'}))
    password1 = forms.CharField(label='Password1',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'forms password', 'autocomplete':"on"}))
    password2 = forms.CharField(label='Password2',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class':'forms', 'autocomplete':"on"}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 

class UserProfilePlusForm(ModelForm):
        avatar = forms.ImageField(label='Avatar', required=False,
                                  widget=forms.FileInput(attrs={'placeholder': 'Avatar', 'id':'id_avatar', 'class':'avatar_form', 'hidden':"True"}))
        first_name = forms.CharField(label='First name', required=False, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class':'forms'}))
        last_name = forms.CharField(label='Last name', required=False, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class':'forms'}))
        phone_number = forms.CharField(label='Phone number', required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'type':'tel', 'class':'forms'}))
        user_cat = forms.ChoiceField(choices=UserProfilePlus.USER_CAT, label='User Type', required=False, widget=forms.Select(attrs={'class': 'form-control'}))

        class Meta:
            model = UserProfilePlus
            fields = ['user', 'avatar', 'first_name', 'last_name','phone_number', 'user_cat']
            exclude = ['user']