from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post,Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib import messages
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



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    comments =Comment.objects.filter(post=post)    
    context = {
      	'post': post,
    }

    return render(request, 'post_detail.html', context)

def add_comment(request,pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get("content")
        author = request.user
        comment = Comment(content=content, author=author, post=post)
        comment.save()
        messages.success(request, "The comment is Posted")
       

        return redirect('post_detail',pk=pk)
    else:
        # Retrieve the post using the provided pk parameter
        post = get_object_or_404(Post, pk=pk)
        context = {'post': post}
        return render(request, 'post_detail.html', context)




    # post = get_object_or_404(Post, id=pk)
    # form = CommentForm()

    # context = {
    #     'form': form
    # }
    # return render(request, 'post_detail.html', context)

   
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment_text = request.POST.get('comment_text')
    #         comment.post = post
    #         comment.author = request.user
    #         comment.content = comment_text
    #         comment.save()
    #         return redirect('post_detail', post_id=post_id)      
    # else:
    #     comment_form = CommentForm()


    # return render(request, 'post_detail.html', {'comment_form': comment_form})
