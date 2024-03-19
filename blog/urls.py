from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,MyPostView,add_comment

urlpatterns = [
	# path('', views.home, name="blog-home"),
	path('about/', views.about, name="blog-about"),
	path('myposts/', MyPostView.as_view(), name="blog-mypost"),
	path('',PostListView.as_view(), name="blog-home"),
	path('post/new',PostCreateView.as_view(), name="blog-new"),
	path('post/<int:pk>/',PostDetailView.as_view(), name="blog-detail"),
	path('post/<int:pk>/update',PostUpdateView.as_view(), name="blog-update"),
	path('post/<int:pk>/delete',PostDeleteView.as_view(), name="blog-delete"),

	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/add_comment/', views.add_comment, name="add_comment"),
	
]

