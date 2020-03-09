from django.shortcuts import render
from .models import ChatApp
from .forms import MessageApp

def home(request):
	msg = ChatApp.objects.all()
	form = MessageApp(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	context = {
	"form":form,
	'msg':msg
	}
	return render(request,'file/list/',context)

