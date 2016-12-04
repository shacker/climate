from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

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

    if request.method == "POST":

        form = BeHeardForm(request.POST)
        if form.is_valid():
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
