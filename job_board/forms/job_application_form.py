#---------------------------------------------------------------
# HEADER
#---------------------------------------------------------------

# Form object for creating, and updating job listings

#---------------------------------------------------------------
# NOTES
#---------------------------------------------------------------

#---------------------------------------------------------------
# IMPORTS
#---------------------------------------------------------------
from django import forms

from job_board.models.job_application import JobApplication

#---------------------------------------------------------------
# CONSTANTS
#---------------------------------------------------------------

#---------------------------------------------------------------
# FUNCTIONS
#---------------------------------------------------------------

#---------------------------------------------------------------
# CLASSES
#---------------------------------------------------------------

class JobApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_listing'].widget.attrs['hidden'] = True
        self.fields['job_listing'].widget.attrs['type'] = 'hidden'
        self.fields['job_listing'].label = ''
    
    first_name = forms.CharField(
        label='First Name', 
        max_length=200, 
        help_text='Enter your first name', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        label='Last name', 
        max_length=200, 
        help_text='Enter your last name.', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-control'}), 
        help_text='Enter your email address.', 
        required=True,
    )

    about_applicant = forms.CharField(
        label='About', 
        max_length=100, 
        help_text='Enter about yourself.', 
        required=True,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
    )
    
    # job_listing = forms.DateField(
    #     required=True,
    #     widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'hidden': 'true'})
    # )

    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email', 'about_applicant', 'job_listing']

#---------------------------------------------------------------
# TESTING
#---------------------------------------------------------------