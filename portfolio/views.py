from django.shortcuts import render
from .models import Html_CSS, React_JS, Python_DJ, Stack

# Create your views here.
def home_page(request):
    projects_html = Html_CSS.objects.all()
    projects_react = React_JS.objects.all()
    projects_python = Python_DJ.objects.all()
    stacks = Stack.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects_html': projects_html, 
        'projects_react': projects_react,
        'projects_python': projects_python,
        'stacks': stacks,
        })
    


