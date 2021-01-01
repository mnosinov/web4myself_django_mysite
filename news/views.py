from django.http import HttpResponse


def index(request):
    print(request)
    print(dir(request))
    return HttpResponse('Hello world!')
