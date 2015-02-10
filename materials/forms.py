from django import forms
from models import Materials, Jobs

class MaterialsForm(forms.ModelForm):
    
    class Meta:
        model = Materials
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
        }
        fields = ['job', 'vendor', 'phase', 'price', 'comments', 'date', 'receipt_number']

class JobsForm(forms.ModelForm):
    
    class Meta:
        model = Jobs
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
        }        
        fields = ['name', 'description', 'start_date', 'est_end_date', 'end_date', 'active']
