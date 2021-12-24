from django import forms
from .models import EmailLists


class CreateEmailList(forms.ModelForm):

	class Meta:
		model = EmailLists
		fields = ['email']

