# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import User
from django.utils.translation import ugettext_lazy
from django.contrib.admin.widgets import AdminDateWidget


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


FILE_INPUT_CONTRADICTION = object()


class FileForm(forms.ClearableFileInput):
	template_name = 'widget/FileForm.html'
	initial_text = ugettext_lazy('Upload file:')

	def get_context(self, name, value, attrs):
		context = super(FileForm, self).get_context(name, value, attrs)
		context['widget'].update({
			'get_value': str(value).split('/')[-1],
			'is_initial': self.is_initial(value),
			'initial_text': self.initial_text,
		})
		return context


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
	confirm_file = forms.FileField(
		required=True,
		label='Файл подтверждения',
		widget=FileForm()
	)
	remove_file = forms.BooleanField(
		required=False,
		label='Удалить',
		widget=forms.CheckboxInput()
	)

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'email', 'confirm_file', 'remove_file']
