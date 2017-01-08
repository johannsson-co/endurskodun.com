from django.shortcuts import render

from .models import HomePage




def home(request):
    
    home = HomePage.objects.first()
    
    
    return render(request, 'index.html', {
        'title': 'endurskodun.com',
        'home': home
    })




