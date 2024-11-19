from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'membership_type']
        labels = {
            'name': 'Full Name',  
            'email': 'Email Address', 
            'phone':'Phone number,' 
        }

