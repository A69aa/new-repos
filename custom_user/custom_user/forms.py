from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, "VIP-Client"),
    (CLIENT, 'CLIENT')
)
MALE = 1
FEMALE = 2
OTHER = 3
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, "FEMALE"),
    (OTHER, 'OTHER')
)
KYRGYZSTAN = 1
KAZAKHSTAN = 2
UZBEKISTAN = 3
RUSSIA = 4
USA = 5
CITIZENSHIP_TYPE = (
    (KYRGYZSTAN,'KYRGYZSTAN'),
    (KAZAKHSTAN,'KAZAKHSTAN'),
    (UZBEKISTAN,'UZBEKISTAN'),
    (RUSSIA,'RUSSIA'),
    (USA,'USA')
)
SCHOOLBOY  =1
STUDENT = 2
OFFICE_WORKER = 3
BUSINESSMAN = 4
BUSINESSWOMAN = 5
OTHER = 6
YOU_STATUS = (
    (SCHOOLBOY,'SCHOOLBOY'),
    (STUDENT,'STUDENT'),
    (OFFICE_WORKER,'OFFICE_WORKER'),
    (BUSINESSMAN,'BUSINESSMAN'),
    (BUSINESSWOMAN,'BUSINESSWOMAN'),
    (OTHER,'OTHER')

)



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    telegram_account = forms.CharField(required=True)
    citizenship = forms.ChoiceField(choices=CITIZENSHIP_TYPE,required=True)
    profession = forms.CharField(required=True)
    marital_status = forms.CharField(required=True)
    who_are_you = forms.ChoiceField(choices=YOU_STATUS,required=True)


    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "user_type",
            "gender",
            "telegram_account",
            "citizenship",
            "profession"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'email',
            'id': 'he'}

    ))

    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'username',
            'id': 'hello'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder': 'password',
            'id': 'hi',
        }
    ))