from django import forms
from . models import WorkerProfile
from django.contrib.auth.hashers import make_password
from captcha.fields import CaptchaField


class WorkerProfileForm(forms.ModelForm):
    email = forms.EmailField(label="Введите вашу электронную почту")  
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Пароль"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Подвертите пароль"
    )





    class Meta:
        model = WorkerProfile
        fields = (
            'username',
            'phone_number',
            'email',
            'password',
            'work',
            'skill',
            'experience_work',
            'url_github',
            'image',
            'birthday',
            'address',
        )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        
        return cleaned_data
    

    def save(self, commit=True):
        worker = super().save(commit=False)
        worker.password = make_password(self.cleaned_data["password"])
        if commit:
            worker.save()
        return worker
    


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    captcha = CaptchaField(label="Введите символы с картинки")

