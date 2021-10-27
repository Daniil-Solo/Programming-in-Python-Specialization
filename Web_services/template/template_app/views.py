from django.shortcuts import render


def echo(request):
    answer = dict()
    if request.GET:
        answer['response'] = request.GET
        answer['method'] = 'get'
    elif request.POST:
        answer['response'] = request.POST
        answer['method'] = 'get'
    else:
        answer['response'] = dict()
    answer['header'] = request.META.get('HTTP_USER_AGENT')
    return render(request, 'template_app/echo.html', answer)


def filter(request):
    return render(request, 'template_app/filters.html', {"a": 2, "b": 3})


def extend(request):
    return render(request, 'template_app/extend.html', {"a": 1, "b": 3})
