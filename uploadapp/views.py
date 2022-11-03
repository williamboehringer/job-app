from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFileForm
from django.shortcuts import render, redirect

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
        return render(request,  'uploadapp/add_image.html', context={'saved_object': saved_object})
    else:
        return render(request, 'uploadapp/add_image.html', context={'form': UploadForm()})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
        return render(request,  'uploadapp/add_file.html', context={'saved_object': saved_object})
    else:
        return render(request, 'uploadapp/add_file.html', context={'form': UploadFileForm()})