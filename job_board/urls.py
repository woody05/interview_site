from django.urls import path

from .views import job_posting_views

urlpatterns = [
    path("", job_posting_views.index, name="index"),
    path("about", job_posting_views.about, name="about"),
    path("jobs-list", job_posting_views.JobListingView.as_view(), name="jobs-list"),
    path("recent-jobs-list", job_posting_views.MostRecentJobListingView.as_view(), name="recent-jobs-list"),
    path("job-listing/create", job_posting_views.create_job_listing, name="create-jobs-list"),
    path("job-listing/<pk>", job_posting_views.job_listing_details, name="jobs-list-details"),
    path("job-listing/<pk>/edit/", job_posting_views.edit_job_listing, name="edit-jobs-list"),
    path("job-listing/<pk>/delete/", job_posting_views.delete_job_listing, name="delete-jobs-list"),
    path("job-listing-apply", job_posting_views.create_job_application, name="apply-job"),
]