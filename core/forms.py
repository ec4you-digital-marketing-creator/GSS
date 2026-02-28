from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'category', 'service', 'booking_date', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-input'}),
            'category': forms.HiddenInput(),
            'service': forms.HiddenInput(),
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message (Optional)', 'class': 'form-textarea', 'rows': 3}),
        }
