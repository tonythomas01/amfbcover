from django.shortcuts import render
from django.shortcuts import redirect
from amfbcover import settings
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView ):
    template_name = "index.html"
