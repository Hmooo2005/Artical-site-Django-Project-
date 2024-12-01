from django.shortcuts import render
from .models import Artical, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
	DetailView,
	CreateView,
	DeleteView,
)

# Create your views here.


class ArticalListView(LoginRequiredMixin, ListView):
    model = Artical
    context_object_name = 'artical'
    ordering = ['-artical_date']

class ArticalDetailView(LoginRequiredMixin, DetailView):
	model = Artical


class ArticalCreateView(LoginRequiredMixin, CreateView):
	model = Artical
	fields = ['title', 'content','img', 'category' ]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ArticalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Artical
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def comment(request, pk):
	if request.method == 'POST':
		form = Comment(request.POST)
		form.save()

	return render(request, 'home/comment_form.html', {'comment':Comment})


# class CommentCreateView(LoginRequiredMixin, CreateView):
# 	model = Comment
# 	fields = ['content']
	# if request.method == 'POST':
	# 	form = Comment(request.POST)
 #        if form.is_valid:
 #            form.save()

# 	def form_valid(self, form):
# 		form.instance.author = self.request.user
# 		return super().form_valid(form)