from django import forms
from .models import User #==from appTwo.models import User

class NewUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'
