from wagtail.wagtailcore.blocks import FieldBlock
from django import forms
from django.utils.encoding import force_text
from django.utils.html import format_html


class BlockQuoteBlock(FieldBlock):

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, **kwargs):
        self.field = forms.CharField(
            required=required,
            help_text=help_text,
            max_length=max_length,
            min_length=min_length
        )
        super(BlockQuoteBlock, self).__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_text(value)]

    def render_basic(self, value, context=None):
        if value:
            return format_html('<blockquote>{0}</blockquote>', value)
        else:
            return ''

    class Meta:
        icon = "openquote"
