# JobListingBoard
Web application for Job Interview

## Features
- Create, Update, Delete Job Listings
- View Job Listings
- Filter Job Listings
- Apply for Job Listings

### Environment:
For smooth developement processes, you must configure your development to match the standard for this project:
1. VS Code
2. Refer to requirements.txt for all required pip packages

## Installation
1. Clone the repository:
git clone https://github.com/your-username/your-repository.git

2. Navigate to the project directory:
cd interview_site

4. Install dependencies:
pip install -r requirements.txt

5. Setup database config:
copy database_config_sample.json
rename database_config_sample.json to database_config.json
modify database_config.json with desired postgresql settings

6. Run migrations:
python manage.py migrate

7. Start the development server:
python manage.py runserver

8. Open your web browser and visit `http://127.0.0.1:8000/` to view the application.

## Usage

### Create Job Listing
1. Click Add Listing
2. Fillout form
3. Click Submit

### Edit Job Listing
1. Find desired job listing
2. Click three dots button
3. Click Edit
4. Modify form
5. Click Submit

### Deletre Job Listing
1. Find desired job listing
2. Click three dots button
3. Click Delete
4. Confirm delte with delete button

### Filter jobs
1. enter keywords into "Job title, keyword and company name" field
2. enter location into the "City, state, zip, or remote" field
3. Click Search button

### View Details
1. Find desired job listing
2. Click on blue job title

### Apply for Job
1. Find desired job listing
2. Click on the blue job title
3. Click the "Apply" button
4. Fillout form
5. Click Submit form

## License

This project is licensed under Kevin Woods.