from django.shortcuts import render
from .models import ContactPageBody

def contactdisplay(request):
    try:
        contact = ContactPageBody.objects.get(id_contact=1)
    except ContactPageBody.DoesNotExist:
        contact = {}
    context = {
        'contact' : contact
    }
    return render(request, 'contact_us.html', context)
