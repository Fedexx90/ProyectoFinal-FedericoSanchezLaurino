from django.views.generic import TemplateView
from django.shortcuts import render

class AboutView(TemplateView):
    template_name = 'about.html'

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')