from django import template
register = template.Library()

@register.filter
def remove_html(text):
    html_tags = ['span','div']
    for tag in html_tags:
        text = text.replace('<%s>' % tag, '').replace('</%s>' % tag, '')
    return text