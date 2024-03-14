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

#---------------------------------------------------------------
# CONSTANTS
#---------------------------------------------------------------

#---------------------------------------------------------------
# FUNCTIONS
#---------------------------------------------------------------

#---------------------------------------------------------------
# CLASSES
#---------------------------------------------------------------
class JobListing(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200) # I would possible break this into another model if this was real. But will keep simple
    job_description = models.TextField()
    location = models.CharField(max_length=100) # would expand into separate fields for city, state and zip. But keeping simple for now
    application_deadline = models.DateField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
#---------------------------------------------------------------
# TESTING
#---------------------------------------------------------------