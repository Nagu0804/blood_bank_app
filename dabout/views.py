from django.shortcuts import render
from .models import AboutPageBody

def aboutdisplay(request):
    try:
        about = AboutPageBody.objects.last()
    except AboutPageBody.DoesNotExist:
        about = {}

    context = {
        'about': about,
    }

    return render(request, 'about_us.html', context)
