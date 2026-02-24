from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Multiplica dos números en plantillas Django."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def subtract(value, arg):
    """Resta dos números en plantillas Django."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def get_item(dictionary, key):
    """Obtiene un elemento del diccionario por clave."""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return ''
