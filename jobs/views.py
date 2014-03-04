from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from linkedin import linkedin
from oauthlib import *
from jobs.models import Employer

CONSUMER_KEY = '77cfcdlhhozb9o'
CONSUMER_SECRET = 'Wtr666Df8DDg1GMV'
USER_TOKEN = '65e9b8d1-23f7-4f6d-bd21-564b283f6b1d'
USER_SECRET = 'f0342bfa-ed92-4828-904b-f32c2dacd8b8'
RETURN_URL = 'http://localhost:8000/'

authentication = linkedin.LinkedInDeveloperAuthentication(
                    CONSUMER_KEY, CONSUMER_SECRET, 
                    USER_TOKEN, USER_SECRET, 
                    RETURN_URL, linkedin.PERMISSIONS.enums.values())

application = linkedin.LinkedInApplication(authentication)

def index(request):
    latest_employer_list = Employer.objects.all()

    for job in latest_employer_list:
        id=job.linkedin_id
        company_info = application.get_companies(company_ids=[id], selectors=['description'])
        job.description = company_info["values"][0]["description"]
    
    template = loader.get_template('jobs/index.html')
    context = RequestContext(request, {
        'latest_employer_list': latest_employer_list,
    })
    return HttpResponse(template.render(context))

def detail(request, id):
    employer = Employer.objects.get(id=id)
    jobs = application.get_company_updates(employer.linkedin_id, params={'count': 15})

    latest_jobs_list = []

    for i in range(0, 14):
	try:
		latest_jobs_list.append((jobs['values'][i]['updateContent']['companyJobUpdate']['job']).items)
		continue
	except KeyError:
		print i
		
    template = loader.get_template('jobs/jobs.html')
    context = RequestContext(request, {
        'latest_jobs_list': latest_jobs_list,
    })
    return HttpResponse(template.render(context))