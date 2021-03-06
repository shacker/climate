from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from beheard.views import lookup, edit_and_send, beheard_thanks, beheard_noop
from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^djadmin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'^beheard/$', lookup, name='beheard_lookup'),
    url(r'^beheard/thanks/$', beheard_thanks, name='beheard_thanks'),
    url(r'^beheard/noop/$', beheard_noop, name='beheard_noop'),
    url(r'^beheard/send/(?P<zip>[\w-]+)/$', edit_and_send, name='edit_and_send'),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
