from django import template

register = template.Library()


@register.filter
def ru_plural(value):
    variants = ('','а','ов')
    abs_value = abs(int(value))

    if abs_value % 10 == 1 and abs_value % 100 != 11:
        variant = 0
    elif abs_value % 10 >= 2 and abs_value % 10 <= 4 and \
            (abs_value % 100 < 10 or abs_value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]