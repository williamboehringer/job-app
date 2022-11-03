from django import forms
from django.utils.translation import gettext_lazy as _
from accounts.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _('Enter First Name'),
            'last_name': _('Enter Last Name'),
            'email': _('Enter email')
        }
    