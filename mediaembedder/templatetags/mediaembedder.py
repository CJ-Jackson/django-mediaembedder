from django import template

register = template.Library()

@register.simple_tag
def mediaembedder(url, **kwargs):
    attr = {}
    attr['url'] = url
    if 'width' in kwargs:
        attr['width'] = kwargs['width']
    if 'height' in kwargs:
        attr['height'] = kwargs['height']
    from django.utils.safestring import mark_safe
    from ..mediaembedder import parse
    value = parse(attr)
    if not value:
        value = url
    return mark_safe(value)
