#---------------------------------------------------------------
# HEADER
#---------------------------------------------------------------

# View function to handle passing all data for Job Listings

#---------------------------------------------------------------
# NOTES
#---------------------------------------------------------------

#---------------------------------------------------------------
# IMPORTS
#---------------------------------------------------------------
from datetime import datetime
import json
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.core.serializers import serialize
from django.db.models import Q

from job_board.forms.job_application_form import JobApplicationForm
from job_board.forms.job_listing_form import JobListingForm
from job_board.models.job_listing import JobListing


#---------------------------------------------------------------
# CONSTANTS
#---------------------------------------------------------------

MOST_RECENT_LISTINGS_COUNT = 10

#---------------------------------------------------------------
# FUNCTIONS
#---------------------------------------------------------------

def index(request):
    context = {
        'title': 'Job Board',
        'JobListingForm': JobListingForm,
        'JobApplicationForm': JobApplicationForm
    }
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

@require_GET
def job_listing_details(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk)

    data = serialize('json', [job_listing])

    return JsonResponse(data, safe=False)

@require_POST
def create_job_listing(request):
    
    if request.method == 'POST':
        # Assuming the data is sent in JSON format from AJAX
        try:
            data = json.loads(request.body)
            form = JobListingForm(data)
            if form.is_valid():
                job_listing = form.save()
            else:
                return JsonResponse({'error': form.errors}, status=400)
            
            return JsonResponse({'success': 'Job Listing Created!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Sorry Failed to add Job Posting'}, status=405)
    
def edit_job_listing(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk)

    if request.method == 'GET':
        # Populate form with data from job_listing instance
        form = JobListingForm(instance=job_listing)
        # Serialize form data
        form_data = model_to_dict(form.instance)
        return JsonResponse(form_data)
    elif request.method == 'POST':
        # Assuming the data is sent in JSON format from AJAX
        try:
            data = json.loads(request.body)
        
            # Update the fields with new data
            form = JobListingForm(data, instance=job_listing)
            if form.is_valid():
                job_listing = form.save()
                return JsonResponse({'success': 'Job Listing Updated!'}, status=200)
            else:
                return JsonResponse({'error': form.errors}, status=400)
            
        except JobListing.DoesNotExist:
            return JsonResponse({'error': 'Job Listing not found.'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def delete_job_listing(request, pk):
    if request.method == 'DELETE':
        try:
            # Retrieve the job listing object
            job_listing = JobListing.objects.get(pk=pk)
            title = job_listing.job_title
            job_listing.delete()
            return JsonResponse({'success': 'Job Listing Deleted!', 'title': title}, status=200)
        
        except JobListing.DoesNotExist:
            return JsonResponse({'error': 'Job Listing not found.'}, status=404)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def create_job_application(request):
    
    if request.method == 'POST':
        # Assuming the data is sent in JSON format from AJAX
        try:
            data = json.loads(request.body)
            form = JobApplicationForm(data)
            if form.is_valid():
                job_listing = form.save()
            else:
                return JsonResponse({'error': form.errors}, status=400)
            
            return JsonResponse({'success': 'Job Application Submitted!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Sorry Failed to add Job Posting'}, status=405)

#---------------------------------------------------------------
# CLASSES
#---------------------------------------------------------------

class JobListingView(View):
    model = JobListing

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = 'Showing all Job Listings'

    def get_query(self, object_id=None):
        return self.model.objects

    def _get_args(self, key=None):
        return self.request.GET.get(key, None) if key else self.request.GET
    
    def apply_filters(self, query_set):
        if filters := self._get_args().get('filters', {}):
            filters = json.loads(filters)
            return query_set.filter(**filters)
        return query_set
    
    def apply_limit(self, query_set):
        if limit := self._get_args().get('limit', None):
            return query_set[:int(limit)]
        return query_set
    
    def apply_search_fields(self, query_set):
        q = self._get_args('q')
        location = self._get_args('location')

        params = []
       
        if q:
            query_set = query_set.filter(
                Q(job_title__icontains=q) |
                Q(company_name__icontains=q) |
                Q(job_description__icontains=q)
            )

            params.append(q)
            
        if location:
            query_set = query_set.filter(location__icontains=location)

            params.append(location)

        if params:
            self.description = f'Showing results for: {", in ".join(params)}'
        
        return query_set
    
    def get(self, request, *args, **kwargs):
        query_set = self.get_query()
        query_set = self.apply_filters(query_set)
        query_set = self.apply_search_fields(query_set)
        query_set = query_set.all()
        query_set = self.apply_limit(query_set)

        data = {
            'description': self.description,
            'data': list(query_set.values())
        }

        return JsonResponse(data, safe=False)
    
class MostRecentJobListingView(JobListingView):
    # get the last 10 most recent job postings
    model = JobListing

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = "Showing most recent job listings."

    def get_query(self, object_id=None):
        return self.model.objects.order_by('-id')[:MOST_RECENT_LISTINGS_COUNT]

#---------------------------------------------------------------
# TESTING
#---------------------------------------------------------------