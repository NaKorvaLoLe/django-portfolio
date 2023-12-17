from django.shortcuts import render
from .models import Html_CSS, React_JS, Stack

# Create your views here.
def home_page(request):
    projects_html = Html_CSS.objects.all()
    projects_react = React_JS.objects.all()
    stacks = Stack.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects_html': projects_html, 
        'projects_react': projects_react,
        'stacks': stacks,
        })
    


