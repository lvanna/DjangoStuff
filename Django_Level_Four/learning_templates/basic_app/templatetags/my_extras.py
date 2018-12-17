from django import template

register = template.Library()

@register.filter(name='cutt')
def cutt(value,arg):
	return value.replace(arg,'*')

# register.filter('cutt',cutt)