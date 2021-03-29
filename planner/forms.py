from django import forms
from .models import TodoModel
class TodoForm(forms.ModelForm):
	class Meta:
		model=TodoModel
		fields='__all__'
		widgets={'user': forms.HiddenInput(), 'uid': forms.HiddenInput()}
		