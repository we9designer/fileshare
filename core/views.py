from django.shortcuts import render
from share.models import File
# Create your views here.

def index(request):
	list_f = File.objects.all().order_by('-created_at')
	return render(request, 'index.html', {'list_files': list_f})

def login(request):
	return render(request, 'login.html')