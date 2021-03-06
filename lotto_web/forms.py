from django.forms import ModelForm
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.utils.translation import ugettext_lazy as _
from .models import LotteryTicket
import datetime


class SigninForm(forms.Form):
	email = forms.EmailField(required = True)
	password = forms.CharField(required = True,
	widget=forms.PasswordInput(render_value=False))

	def addError(self, message):
		self._errors[NON_FIELD_ERRORS] = self.error_class([message])

class UploadFileForm(forms.Form):
    game = forms.CharField(max_length=50)
    image  = forms.FileField(label='Select a file')
    lottery_date = forms.DateField(initial=datetime.date.today)

class EditUploadFileForm(forms.Form):
	image  = forms.FileField
	numbers = forms.CharField(max_length=5000)
	ticketId = forms.CharField(max_length=16)

class UserForm(forms.Form):
	name = forms.CharField(required = True)
	telephone = forms.IntegerField(required = True)
	email = forms.EmailField(required = True)
	password = forms.CharField(required = True,	label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	ver_password = forms.CharField(required = True, label=(u' Verify Password'), widget=forms.PasswordInput(render_value=False))

	def addError(self, message):
		self._errors[NON_FIELD_ERRORS] = self.error_class([message])

	def clean(self):
		cleaned_data = self.cleaned_data
		password = cleaned_data.get('password')
		ver_password = cleaned_data.get('ver_password')
		if password != ver_password:
			raise forms.ValidationError('Passwords do not match')
		telephone = cleaned_data.get('telephone')

		return cleaned_data
