#####################################################################
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView
from .models import Whatsnew
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#####################################################################

#####################################################################
class WNewListView(ListView):
	model = Whatsnew
	template_name = 'ndmu/whatsnew/whats_new.html'
	context_object_name = 'whatsnews'
	ordering = ['-date_updated']

class WNewCreateView(LoginRequiredMixin, CreateView):
	model = Whatsnew
	fields = ['whatsnew_title', 'whatsnew']
	template_name = 'ndmu/whatsnew/whatsnew_form.html'
	success_url = reverse_lazy('new-view')

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

