from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from app.forms import JobPostForm
from app.models import JobPost

# Create your views here.

def job_list(request):
    jobs= JobPost.objects.all()
    context = {'job': jobs}
    return render(request, 'app/index.html', context)

def job_detail(request, slug):
    try:
        jobs= JobPost.objects.get(slug=slug)
        context = {'job': jobs}
        return render(request, 'app/job_detail.html', context)
    except:
        return HttpResponseNotFound('Not Found')

def job_create(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        form.save()
        return redirect('jobs_list')
    form = JobPostForm()
    return render(request, 'app/job_create.html', {'form': form})