# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# from django import forms
# User = get_user_model()

# class RegisterCustomerForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'password1', 'password2')

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('', 'Select Role'),
        ('Employee', 'Employee'),
        ('Support', 'Support')
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label='Role')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['role'].error_messages = {'required': 'Please select a role.'}

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if not role:
            self.add_error('role', "You must select either Customer or Support.")
        return cleaned_data
    
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
