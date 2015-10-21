from django.shortcuts import render

from home.models import HomePage

# Create your views here.

def index(request):

    homepage = HomePage.objects.all()[0]
    
    template_args = {
        'homepage': homepage,
    }
    
    return render(request, 'index.html', template_args)
