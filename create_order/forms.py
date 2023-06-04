# coding=utf-8
from django import forms
from models import Order


class DateForm(forms.DateInput):
	input_type = "date"

	def __init__(self, **kwargs):
		kwargs["format"] = "%Y-%m-%d"
		super(DateForm, self).__init__(**kwargs)


class OrderForm(forms.ModelForm):
	full_name = forms.CharField(
		max_length=30,
		label='Имя',
		required=True,
		widget=forms.TextInput(),
	)
	birthday = forms.DateField(
		required=True,
		label='День рождения',
		widget=DateForm(format=["%Y-%m-%d"])
	)
	comment = forms.CharField(
		required=True,
		label='Комментарий',
		max_length=255,
		widget=forms.Textarea()
	)
	confirm_file = forms.CharField(
		required=True,
		label='Файл',
		disabled=True,
		widget=forms.TextInput()
	)

	class Meta:
		model = Order
		fields = ("full_name", "birthday", "comment", "confirm_file")
