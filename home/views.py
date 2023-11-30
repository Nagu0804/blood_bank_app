from django.shortcuts import render, get_object_or_404
from .models import HomePageSlider, HomePageBody

def homedisplay(request):
    try:
        home_slider = HomePageSlider.objects.last()
    except HomePageSlider.DoesNotExist:
        home_slider = {}
    try:
        our_vision = HomePageBody.objects.last()
    except HomePageBody.DoesNotExist:
        our_vision = {}
        
    context = {
        'home_slider' : home_slider,
        'our_vision' : our_vision
    }

    return render(request, 'donor_home.html', context)
