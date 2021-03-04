from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass