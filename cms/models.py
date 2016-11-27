from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from cms.stream_blocks import BlockQuoteBlock


class ContentPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('html', blocks.RawHTMLBlock()),
        ('page', blocks.PageChooserBlock()),
        ('blockquote', BlockQuoteBlock()),

    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def __str__(self):
        return "{0} - {1}".format(self.title, self.owner)


class SectionPage(Page):

    intro = models.TextField(blank=True, help_text="Optional section intro")

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

    def __str__(self):
        return self.title
