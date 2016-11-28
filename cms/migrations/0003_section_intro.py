# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 19:20
from __future__ import unicode_literals

import cms.stream_blocks
from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_sectionpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionpage',
            name='intro',
            field=models.TextField(blank=True, help_text='Optional section intro'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('html', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('blockquote', cms.stream_blocks.BlockQuoteBlock())), blank=True, null=True),
        ),
    ]