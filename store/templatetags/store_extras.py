from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Look up `key` (int or str) in a dict whose keys are strings —
    used to read cart quantities in templates: {{ cart|get_item:product.id }}"""
    if dictionary is None:
        return None
    return dictionary.get(str(key))
