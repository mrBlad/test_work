# coding=utf-8
from django import forms
from models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy


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


class DateForm(forms.DateInput):
	input_type = "date"

	def __init__(self, **kwargs):
		kwargs["format"] = "%Y-%m-%d"
		super(DateForm, self).__init__(**kwargs)


class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(
		max_length=30,
		label='Имя',
		required=True,
		widget=forms.TextInput(),
	)
	last_name = forms.CharField(
		max_length=30,
		label='Фамилия',
		required=True,
		widget=forms.TextInput(),
	)
	middle_name = forms.CharField(
		max_length=30,
		label='Отчество',
		required=False,
		widget=forms.TextInput(),
	)
	birthday = forms.DateField(
		required=True,
		label='День рождения',
		widget=DateForm(format=["%Y-%m-%d"])
	)
	email = forms.EmailField(
		required=True,
		label='Почта',
		widget=forms.TextInput()
	)
	path_to_file = forms.CharField(
		label='Путь до файла',
		disabled=True,
		widget=forms.TextInput(
			attrs={
				'id': 'filename',
				'class': 'filename form-control',
			}
		)
	)
	confirm_file = forms.FileField(
		required=True,
		label='Выбор файла',
		widget=forms.FileInput(
			attrs={
				'class': 'custom-file-input'
			}
		)
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'email', 'path_to_file', 'confirm_file']
