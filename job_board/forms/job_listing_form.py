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

from job_board.models.job_listing import JobListing

#---------------------------------------------------------------
# CONSTANTS
#---------------------------------------------------------------

#---------------------------------------------------------------
# FUNCTIONS
#---------------------------------------------------------------

#---------------------------------------------------------------
# CLASSES
#---------------------------------------------------------------

class JobListingForm(forms.ModelForm):
    
    job_title = forms.CharField(
        label='Job Title', 
        max_length=200, 
        help_text='Enter the title of the job.', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    company_name = forms.CharField(
        label='Company Name', 
        max_length=200, 
        help_text='Enter the name of the company.', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    job_description = forms.CharField(
        label='Job Description', 
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}), 
        help_text='Enter the job description.', 
        required=True,
    )

    location = forms.CharField(
        label='Location', 
        max_length=100, 
        help_text='Enter the location of the job.', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    application_deadline = forms.DateField(
        label='Application Deadline', 
        help_text='Enter the deadline for application.', 
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = JobListing
        fields = ['job_title', 'company_name', 'job_description', 'location', 'application_deadline']

#---------------------------------------------------------------
# TESTING
#---------------------------------------------------------------