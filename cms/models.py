from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from cms.stream_blocks import BlockQuoteBlock


streamfield_blocks = [
    ('heading', blocks.CharBlock(classname="full title")),
    ('paragraph', blocks.RichTextBlock()),
    ('image', ImageChooserBlock()),
    ('html', blocks.RawHTMLBlock()),
    ('page', blocks.PageChooserBlock()),
    ('blockquote', BlockQuoteBlock()),

]


class ContentPage(Page):
    body = StreamField(streamfield_blocks, blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def __str__(self):
        return "{0} - {1}".format(self.title, self.owner)


class SectionPage(Page):
    intro = StreamField(streamfield_blocks, blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('intro'),
    ]

    def __str__(self):
        return self.title
