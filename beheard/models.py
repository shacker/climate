from django.utils import timezone
from django.db import models


class BeheardLog(models.Model):
    '''
    Logs all rep messages sent.
    '''

    timestamp = models.DateTimeField(default=timezone.now)
    sender_name = models.CharField(max_length=128, blank=True)
    sender_email = models.EmailField(max_length=64, default='')
    sender_location = models.CharField(max_length=128, blank=True)
    recip_name = models.CharField(max_length=128, blank=True)
    recip_email = models.EmailField(max_length=64, default='')
    recip_bioguide_id = models.CharField(max_length=12, blank=True)
    cust_msg = models.TextField(blank=True, help_text="Custom message entered by user")

    def __str__(self):
        return "{t}: {sn} - {rn}".format(t=self.timestamp, sn=self.sender_name, rn=self.recip_name)
