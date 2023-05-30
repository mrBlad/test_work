from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(),
	)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(),
	)
	middle_name = forms.CharField(
		max_length=30,
		widget=forms.TextInput(),
	)
	birthday = forms.DateField(
		required=True,
		widget=forms.DateInput()
	)
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput()
	)
	confirm_file = forms.FileField(
		required=True,
		widget=forms.FileInput()
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'email', 'confirm_file']
