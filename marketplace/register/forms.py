from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'email')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError(r'Passwords don\'t match.')
    #     return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Additional custom logic here (e.g., creating a related record)
        if commit:

            user.save()

            # Create a related record in your own database
        return user
