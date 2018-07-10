from django.shortcuts import render
from .models import Usuario

def home(request):
    data = {}
    data['usuarios'] = Usuario.objects.all()
    return render(request, 'index.html', data)
