from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'second_name',
            'tg_user_id', 'tg_username', 'role'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget = forms.RadioSelect(choices=User.ROLE_CHOICES)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Пароль")

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].widget = forms.RadioSelect(choices=User.ROLE_CHOICES)
