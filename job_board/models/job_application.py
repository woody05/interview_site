#---------------------------------------------------------------
# HEADER
#---------------------------------------------------------------

# Database Class for job listings

#---------------------------------------------------------------
# NOTES
#---------------------------------------------------------------

#---------------------------------------------------------------
# IMPORTS
#---------------------------------------------------------------
from django.db import models

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
class JobApplication(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200) # I would possible break this into another model if this was real. But will keep simple
    email = models.EmailField()
    about_applicant = models.TextField()
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
#---------------------------------------------------------------
# TESTING
#---------------------------------------------------------------