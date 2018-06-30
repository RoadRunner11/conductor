from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from support.forms import SupportTicketForm


def contact(request):
    """Show a contact form."""
    if request.method == 'POST':
        form = SupportTicketForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thanks! We’ll get back to you soon.')
            return HttpResponseRedirect(reverse('contact'))
    else:
        form = SupportTicketForm()
    context = {'form': form}
    return render(request, 'support/contact.html', context)


def handle_500(request):
    """Display a customer 500 error page."""
    return render(request, 'support/500.html', {})
