from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.constants import GENDER_TYPE
from account.models import ProfileModel


class UserSignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    city = forms.CharField(max_length=350)
    street = forms.CharField(max_length=750)
    country = forms.CharField(max_length=800)
    post_code = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "gender",
            "birth_date",
            "city",
            "street",
            "country",
            "post_code",
        ]

    def save(self, commit=True):
        requested_user = super().save(commit=False)
        if commit:
            requested_user.save()
            gender = self.cleaned_data.get("gender")
            birth_date = self.cleaned_data.get("birth_date")
            city = self.cleaned_data.get("city")
            street = self.cleaned_data.get("street")
            country = self.cleaned_data.get("country")
            post_code = self.cleaned_data.get("post_code")

            ProfileModel.objects.create(
                user=requested_user,
                gender=gender,
                birth_date=birth_date,
                city=city,
                street=street,
                country=country,
                post_code=post_code,
            )
        return requested_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-md bg-transparent outline-none focus:ring-2 focus:ring-blue-500"
                }
            )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-md bg-transparent outline-none focus:ring-2 focus:ring-blue-500"
                }
            )
