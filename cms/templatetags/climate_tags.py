from django import template
from cms.models import SectionPage

register = template.Library()


@register.inclusion_tag('cms/tags/top_menu.html', takes_context=True)
def top_menu(context):
    menuitems = SectionPage.objects.filter().live().in_menu()

    return {
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# See: http://www.tivix.com/blog/working-with-wagtail-menus/
