from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import *
from datetime import date
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone



def add_file():
    File.objects.create(expiration_date=timezone.now() + datetime.timedelta(minutes=10080))

class FileList(ListView):
    paginate_by = 50

    model = File
    template_name = 'file/list.html'

    def get_queryset(self):
        self.queryset = super(FileList, self).get_queryset().filter(user=self.request.user)
        if self.request.GET.get('search_box', False):
            self.queryset=self.queryset.filter(description__icontains = self.request.GET['search_box'])
        return self.queryset

class FileDetail(DetailView):
    model = File
    template_name = 'file/details.html'

class FileCreate(CreateView):
    model = File
    template_name = 'file/add.html'
    form_class = FileForm
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FileUpdate(UpdateView):
    model = File
    template_name = 'file/update.html'
    form_class = FileForm
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FileDelete(DeleteView):
    model = File
    success_url = reverse_lazy('file_list')
