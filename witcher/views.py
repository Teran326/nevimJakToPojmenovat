from django.shortcuts import render
from witcher.models import Profession, Attachment
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache



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


class ProfessionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Profession
    fields = ['profession', 'description', 'race', 'name', 'poster']
    template_name = 'witcher/profession_bootstrap_form.html'
    success_url = reverse_lazy('index')
    login_url = '/accounts/login/'
    permission_required = 'witcher.add_profession'


class ProfessionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Profession
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    template_name = 'witcher/profession_bootstrap_form.html'
    success_url = reverse_lazy('index')
    login_url = '/accounts/login/'
    permission_required = 'witcher.change_profession'


class ProfessionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Profession
    success_url = reverse_lazy('index')
    login_url = '/accounts/login/'
    permission_required = 'witcher.delete_profession'


def error_404(request, exception=None):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')


def error_400(request, exception=None):
    return render(request, 'errors/400.html')


@never_cache
def clear_cache(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    cache.clear()
    return HttpResponse('Cache has been cleared')