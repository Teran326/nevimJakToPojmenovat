from django.shortcuts import render
from witcher.models import Profession, Attachment


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


def profession(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_attachments = Attachment.objects.all().count()
    attachments = Attachment.objects.order_by('profession')

    context = {
        'num_attachments': num_attachments,
        'attachments': attachments
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'profession.html', context=context)
