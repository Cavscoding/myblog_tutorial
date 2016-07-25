from django import forms


class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)