from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def description_filter(text):
    if text != None:
        return text[:100]
    else:
        return 'нет описания'
