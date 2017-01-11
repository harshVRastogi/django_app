import os

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'about/index.html', {})


def download_resume(request):
    filename = 'D:/mywebsite/blog/about/downloadable/resume.pdf'
    data = open(filename, "rb").read()
    response = HttpResponse(data, content_type='application/vnd')
    response['Content-Disposition'] = 'attachment; filename=resume_harsh.pdf'
    response['Content-Length'] = os.path.getsize(filename)
    return response
