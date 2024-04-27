

from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html" )

def about_view(request):
    return render(request, "about.html" )

def blog_view(request):
    return render(request, "blog.html" )

def contact_view(request):
    return render(request, "contact.html" )

def detail_view(request):
    return render(request, "detail.html" )

def price_view(request):
    return render(request, "price.html" )

def service_view(request):
    return render(request, "service.html" )

def team_view(request):
    return render(request, "team.html" )

def testimonial_view(request):
    return render(request, "testimonial.html" )
