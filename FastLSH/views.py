from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'FastLSH/home.html')

def contact(request):
    return render(request, 'FastLSH/basic.html' , {'content': ['if you would','fsdaf']})


