from django import template
register = template.Library()

@register.inclusion_tag('userbox.html', takes_context=True)
def authuserbox(context):
    return context
