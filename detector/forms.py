from django import forms

class EmailForm(forms.Form):
    message = forms.CharField(
        label="Enter Email Text",
        widget=forms.Textarea(attrs={
            'rows': 8,
            'class': 'form-control custom-textarea',
            'placeholder': 'Type or paste the email message here...'
        })
    )