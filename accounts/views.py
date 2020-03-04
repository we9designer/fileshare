from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from share.models import File
from django.shortcuts import redirect


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/share/file/list')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
