from django import forms
from .models import *
from datetime import date

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		exclude = ['created_at', 'update_at', 'user', 'expiration_date']