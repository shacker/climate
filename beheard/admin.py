from django.contrib import admin
from beheard.models import BeheardLog


class LogAdmin(admin.ModelAdmin):

    list_display = ['timestamp', 'sender_name', 'recip_name', ]
    search_fields = ['sender_name', 'sender_email', 'recip_name', 'recip_email', 'cust_msg', ]

admin.site.register(BeheardLog, LogAdmin)
