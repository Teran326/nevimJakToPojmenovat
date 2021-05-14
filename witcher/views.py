from django.shortcuts import render
from witcher.models import Profession


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
