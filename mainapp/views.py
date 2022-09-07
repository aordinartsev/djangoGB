from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hellp world")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
