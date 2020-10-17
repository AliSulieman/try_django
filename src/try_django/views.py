from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "hello there...."
    return render(request, "hello_world.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "about us"})


def contact_page(request):
    return render(request, "form.html", {"title": "contact"})


def example_page(request):
    context = {"title": "example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
