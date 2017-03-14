import subprocess
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import os


# Create your views here.


def index(request):
    return render(request, 'FastLSH/home.html')

def parameterSet(request):
    return render(request, 'FastLSH/parameterSet.html')

def execution(request):
    return render(request, 'FastLSH/execution.html')

def contact(request):
    return render(request, 'FastLSH/basic.html' , {'content': ['if you would','fsdaf']})

def submit(request):
    # info=request.POST['info']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    s = subprocess.check_output(["./FastLSH/cExec/FastLSH"])
    s = s.replace("\n","<br>")
    return render(request, 'FastLSH/execution.html', {'content': s})
#    return HttpResponse(s)
#    return HttpResponse('Hello World!')


def download(request):
    f = open('/home/peter/FYP/SimPointSite/FastLSH/cExec/output/candidate.csv', 'r')
    response = HttpResponse(f, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="candidate.csv"'
    f.close()
    return response

# def hello(request):
#     return HttpResponse('Hello World!')
#
# def home(request):
#     return render_to_response('index.html', {'variable': 'world'})
