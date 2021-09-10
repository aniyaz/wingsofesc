from django import forms
from datetime import datetime


year_limit = datetime.today().year - 99 ###   validation of 99 years as upper limit

GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
STREAM_CHOICES = [
    ('1', 'Arts'),
    ('2', 'Commerce'),
    ('3', 'Science')
]

class RegisterForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=50)
    email = forms.EmailField(label="E-mail Address", required=False)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    father_name = forms.CharField(label="Father's Name", max_length=50, required=False)
    birth_year = forms.IntegerField(min_value=year_limit)
    primary_phone = forms.CharField(max_length=13, initial='+91')
    is_whatsapp = forms.BooleanField(required=True)
    whatsapp_number = forms.CharField(max_length=13, initial='+91')
    hs_year = forms.IntegerField(label='HS Year', min_value=2008, max_value=datetime.today().year)
    enroll_year = forms.IntegerField(min_value=2008, max_value=datetime.today().year, required=False)
    stream = forms.CharField(label='Stream', widget=forms.Select(choices=STREAM_CHOICES))
    current_profession = forms.CharField(label='Current Profession', max_length=50, required=False)