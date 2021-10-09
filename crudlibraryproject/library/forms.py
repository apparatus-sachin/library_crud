from django import forms
from .models import libraryinfo

class libraryinfoForm(forms.ModelForm):
	class Meta:
		model=libraryinfo
		fields="__all__"

		widgets={
		'book_name':forms.TextInput(attrs={'class':'form-control'}),
		'author_name':forms.TextInput(attrs={'class':'form-control'}),
		'student_name':forms.TextInput(attrs={'class':'form-control'}),
		'borrow_date':forms.DateTimeInput(attrs={'class':'form-control','id':'datetimepicker'})
		}