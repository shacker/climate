import json
import requests

from django.core.mail import EmailMessage
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.template.loader import render_to_string

from beheard.forms import LookupForm, BeHeardForm


def lookup(request):
    """
    Start by letting user look up reps by zip code
    """

    if request.method == "POST":

        form = LookupForm(request.POST)
        if form.is_valid():
            return redirect(reverse('edit_and_send', args=[form.cleaned_data['zip']]))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        form = LookupForm()

    return render(
        request,
        'beheard/lookup.html',
        locals(),
        )


def edit_and_send(request, zip):
    """
    Look up senators and rep by zip, provide form to send email to them.
    """

    cache_name = "zipresults_{z}".format(z=zip)
    results = cache.get(cache_name)
    if not results:
        url = 'https://congress.api.sunlightfoundation.com/legislators/locate?zip={zip}'.format(zip=zip)
        req = requests.request('GET', url)
        results = json.loads(req.text)['results']
        cache.set(cache_name, results, 60 * 10)

    if request.method == "POST":

        form = BeHeardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            personal_message = data['msg']

            ids = request.POST.getlist('rep_ids')
            if ids:
                for i in ids:
                    # Get email for rep with matching ID key
                    for rep in results:
                        if rep.get('govtrack_id') == i:
                            subject = 'I support pro-climate policies like the Paris Agreement and the CPP'
                            ctx = {'rep': rep, 'personal_message': personal_message, 'data': data}
                            message = render_to_string(
                                "beheard/email/beheard.txt",
                                ctx)
                            msg = EmailMessage(
                                subject,
                                message,
                                from_email='Cross the Aisle for Climate <crossforclimate@gmail.com>',
                                # to=[rep.get('oc_email'), ],
                                to=['shacker@birdhouse.org', 'rsalvadorreyes@mac.com', ])
                            msg.send(fail_silently=False)

            return redirect(reverse('beheard_thanks'))
        else:
            messages.error(request, "There were errors in the form.")

    else:
        form = BeHeardForm()

    return render(
        request,
        'beheard/beheard.html',
        locals(),
        )


def beheard_thanks(request):

    return render(
        request,
        'beheard/beheard_thanks.html',
        locals(),
        )
