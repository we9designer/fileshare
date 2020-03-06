from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.contrib.auth.models import Permission
from .forms import UserLoginForm,UserRigester,UserProfile
from django.shortcuts import render,redirect
User = get_user_model()
def login_view(request):
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        if next:
            redirect(next)
        return redirect("home")
    return render(request,"login.html",{"form":form,"title":title})

def register(request):
    next = request.GET.get("next")
    title = "register"
    form = UserRigester(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user.set_password(password)
        # User.objects.get_or_create(username=username)
        # u = User.objects.get(username=username)
        # permission = Permission.objects.get(name='can_change')
        # user.user_permissions(permissions)
        user.is_staff=True
        user.save()
        new_user = authenticate(username=user.username,password=password)
        login(request,new_user)
        if next:
            redirect(next)
        return redirect("/share/file/list")
    return render(request,"accounts/register.html",{"title":title,"form":form})


def logout_view(request):
    logout(request)
    return redirect("home")

def edit_all(request):
    title = "custmize Profile"
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfile(request.POST or None, request.FILES or None,instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfile(instance=profile)
    return render(request,'editall.html',{'title':title,"form":form})





"""
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
"""