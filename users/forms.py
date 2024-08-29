# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    field_of_work = forms.ChoiceField(choices=CustomUser.FIELD_CHOICES, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth', 'field_of_work')

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get('date_of_birth')
        field_of_work = cleaned_data.get('field_of_work')

        if date_of_birth and field_of_work:
            raise forms.ValidationError("A user can't be both a customer and a company.")
        elif not date_of_birth and not field_of_work:
            raise forms.ValidationError("Please provide either a date of birth (for customers) or a field of work (for companies).")

        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'field_of_work')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.is_company():
            del self.fields['date_of_birth']
        else:
            del self.fields['field_of_work']