from django.shortcuts import render
from witcher.models import Profession, Attachment
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_professions = Profession.objects.all().count()
    professions = Profession.objects.order_by('name')

    context = {
        'num_professions': num_professions,
        'professions': professions
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def picture(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_attachments = Attachment.objects.all().count()
    attachments = Attachment.objects.order_by('profession')

    context = {
        'num_attachments': num_attachments,
        'attachments': attachments
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'picture.html', context=context)


class ProfessionCreate(CreateView):
    model = Profession
    fields = ['profession', 'description', 'race', 'name', 'poster']
    success_url = reverse_lazy('index')


class ProfessionUpdate(UpdateView):
    model = Profession
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    success_url = reverse_lazy('index')


class ProfessionDelete(DeleteView):
    model = Profession
    success_url = reverse_lazy('index')