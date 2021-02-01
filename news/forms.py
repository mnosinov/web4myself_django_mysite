from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginform(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-select"}),

        }

    def clean_title(self):
        """
        this method is call after django validation process, during call of
        form.is_valid().
        After django
        validation process dictionary cleaned_data is prepared and we can
        do our ownd custom validation. Name of the method is conventional:
            clean_<field name>
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):     # check if first letter in title is digit
            raise ValidationError('Название не должно начинаться с цифры')
        return title.upper()    # just for fun - we convert title to upper case
