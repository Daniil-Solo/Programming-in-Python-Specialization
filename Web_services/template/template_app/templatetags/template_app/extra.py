from django import template
register = template.Library()


@register.filter(name='inc')
def inc(value, arg):
    return int(value) + int(arg)


@register.simple_tag(name='division')
def division(a, b, *args, **kwargs):
    to_int = kwargs.get('to_int')
    if to_int:
        return int(a) // int(b)
    else:
        return int(a) / int(b)
