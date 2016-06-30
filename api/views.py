from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
import urllib2
import json


class HomepageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        text = request.POST.get('text', 'happy')
        context['image'] = settings.AVATAR_URL.format(text)
        context['username'] = text
        return render(request, self.template_name, context)
