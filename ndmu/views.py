#####################################################################
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment, Gallery
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django_filters import rest_framework as filters
from django.db.models import Q
from django.shortcuts import redirect
from .forms import PostForm, CommentForm, GalleryForm
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
import json
from django.conf import settings
from django.core.paginator import Paginator
#####################################################################

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'ndmu/add_comment_to_post.html', {'form': form})

#####################################################################
#announcements
class GalleryListView(ListView):
	model = Gallery
	template_name = 'ndmu/gallery.html'
	context_object_name = 'galleries'
	paginate_by = 6

class GalleryCreateView(LoginRequiredMixin, CreateView):
	model = Gallery
	fields = ['title', 'info', 'image']
	success_url = reverse_lazy('ndmu-gallery')
	fields = ['title', 'image']

class GalleryHomeListView(ListView):
	model = Gallery
	context_object_name = 'homegallery'
	paginate_by = 4
	template_name = 'ndmu/home.html'


class PostListView(ListView):
	model = Post
	template_name = 'ndmu/announcements.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class UserPostListView(ListView):
	model = Post
	template_name = 'ndmu/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'ndmu/edit_post.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('ndmu-announcements')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


####################################################################
#about
def about(request):
	return render(request, 'ndmu/about.html')

def history(request):
	return render(request, 'ndmu/about/history.html', {'title': 'History'})

def contact(request):
	return render(request, 'ndmu/about/contact.html')

def developers(request):
	return render(request, 'ndmu/about/developers.html')

def trustees(request):
	return render(request, 'ndmu/about/trustees.html', {'title': 'Board of Trustees'})

def administration(request):
	return render(request, 'ndmu/about/administration.html', {'title': 'Administration'})

def teachers(request):
	return render(request, 'ndmu/about/teachers.html', {'title': 'SHS teachers'})

def vision(request):
	return render(request, 'ndmu/about/vision_mission.html', {'title': 'Vision & Mission'})

def objectives(request):
	return render(request, 'ndmu/about/objectives.html', {'title': 'Objectives'})

def corevalues(request):
	return render(request, 'ndmu/about/corevalues.html', {'title': 'Core Values'})

def citationsandawards(request):
	return render(request, 'ndmu/about/citationsandawards.html', {'title': 'Citations & Awards'})

def universitycolors(request):
	return render(request, 'ndmu/about/universitycolors.html', {'title': 'University Colors'})

def hymn(request):
	return render(request, 'ndmu/about/hymn.html', {'title': 'University Hymn'})

def seal(request):
	return render(request, 'ndmu/about/seal.html', {'title': 'University Seal'})

def maristbrothers(request):
	return render(request, 'ndmu/about/maristbrothers.html', {'title': 'The Marist Brothers'})

def strands(request):
	return render(request, 'ndmu/about/strands.html', {'title': 'Senior High School Strands'})

def schoolfacilities(request):
	return render(request, 'ndmu/about/schoolfacilities.html', {'title': 'School Facilities'})

####################################################################
#home
def home(request):
	return render(request, 'ndmu/home.html')

def superhome(request):
	return render(request, 'ndmu/superhomepage.html')
####################################################################\
def whatsnew(request):
	return render(request, 'ndmu/whats_new.html')

def error_404(request):
	return render(request, 'ndmu/error_404.html', {'title': 'Page Not Found'})

def error_404_demo(request):
	return render(request, 'ndmu/error_404.html', {'title': 'Page Not Found'})
def game(request):
	return render(request, 'ndmu/game.html')