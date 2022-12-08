from django.shortcuts import render
from django.http import HttpResponse
""" Extend the things app with a view that renders a simple HTML page. The HTML must include a title in the document head:

<title>Things</title>

and it must display a title on the page body:

<h1>Things</h1>	

Extend the project with a URL to the root path. This must lead to the view that you just created."""

# Create your views here.
def home(request):
    response = HttpResponse("<h1>Things</h1>")
    #return response
    return render(request, 'home.html')


