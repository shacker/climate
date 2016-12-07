from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)
from beheard.models import BeheardLog


class ShopBuildingAdmin(ModelAdmin):
    model = BeheardLog
    add_to_settings_menu = True
    menu_label = 'Logs'
    list_display = ['timestamp', 'sender_name', 'recip_name', ]

modeladmin_register(ShopBuildingAdmin)
