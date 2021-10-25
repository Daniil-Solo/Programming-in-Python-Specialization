from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import render


def simple_route(request):
    if request.GET:
        return HttpResponse("GET")
    elif request.POST:
        return HttpResponseNotAllowed()
    else:
        return HttpResponse("No GET, no POST")


def slug_route(request, slug_content):
    if len(slug_content) > 16:
        return HttpResponseNotFound()
    else:
        return HttpResponse(slug_content)


def sum_route(request, num1, num2):
    num_sum = int(num1) + int(num2)
    return HttpResponse(str(num_sum))


def sum_get_method(request):
    if request.GET:
        try:
            num1 = request.GET.get('a')
            num2 = request.GET.get('b')
            num_sum = int(num1) + int(num2)
            return HttpResponse(str(num_sum))
        except TypeError:
            return HttpResponseBadRequest()
        except ValueError:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()


def sum_post_method(request):
    if request.POST:
        try:
            num1 = request.POST.get('a')
            num2 = request.POST.get('b')
            num_sum = int(num1) + int(num2)
            return HttpResponse(str(num_sum))
        except TypeError:
            return HttpResponseBadRequest()
        except ValueError:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
