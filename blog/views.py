from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


# def home(request):
# 	context ={
# 	'posts':Post.objects.all()
# 	}

# 	return render(request, 'blog/home.html',context )

def about(request):
 	return render(request, 'blog/about.html')

def mypost(request):
	return render(request, 'blog/myposts.html')

class MyPostView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/myposts.html'

class PostListView(LoginRequiredMixin,ListView):
	model = Post
	template_name='blog/home.html'
	context_object_name = 'posts'
	ordering = ["-date_posted"]

class PostDetailView(LoginRequiredMixin,DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	# def test_func(self):
	# 	post = self.get_object()
	# 	if self.request.user == post.author:
	# 		return True

	# 	return False

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True

		return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url="/"

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True

		return False

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})