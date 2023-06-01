from django import forms
from models import Order

class NewUserForm(forms.ModelForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Order
		fields = ("username", "email", "password1", "password2")
