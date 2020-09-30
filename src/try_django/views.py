from django.http import HttpResponse



def home_page(request):
    return HttpResponse("<h1> hello world <h1>")


def about_page(request):
    return HttpResponse("<h1> about us <h1>")


def contact_page(request):
    return HttpResponse("<h1> contach us <h1>")