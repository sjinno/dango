from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, reverse
from django.views import generic

from .forms import ContactForm
from cart.models import Order


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            'orders': Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        received_notice_message = 'Thanks for getting in touch! We have received your message.'
        messages.info(
            self.request, received_notice_message)

        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message_received = f'''
            Received message below from {name}, {email}
            -------------------------------------------


            {message}
        '''

        send_mail(
            subject='Received contact form submission',
            message=full_message_received,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )

        return super(ContactView, self).form_valid(form)
