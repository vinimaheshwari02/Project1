from django import forms
class CostForm(forms.Form):
	name=forms.CharField()
	address=forms.CharField()
	about=forms.CharField()