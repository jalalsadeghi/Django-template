from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    """Simple model form for contact data."""
    class Meta:
        model = ContactRequest
        fields = ["email", "name", "content"]