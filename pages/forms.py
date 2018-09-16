from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Email Address", widget=forms.EmailInput(
    attrs={'placeholder': 'guest@example.com', 'class': 'form-control', 'id':'email'}))
    subject = forms.CharField(label='Name', max_length=100, required=True, widget=forms.TextInput(
    attrs={'placeholder': 'Please enter your name.', 'class': 'form-control', 'id':'name'}))
    message = forms.CharField(widget= forms.Textarea(
    attrs={'placeholder': 'Send me a message.', 'class': 'form-control', 'id':'message'}),required=True, label="Message")
