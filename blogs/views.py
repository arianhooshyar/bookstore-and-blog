from django.shortcuts import render
from django.views import generic
from .models import Blog, Comment
from django.urls import reverse_lazy


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 2
    context_object_name = 'blogs'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blogs'


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ['title', 'author', 'text', 'active', ]
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('Blog_List_View')


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ['title', 'author', 'text', 'active', ]
    template_name = 'blog/blog_update.html'


class BlogDeleteView(generic.DeleteView):
    model = Blog
    fields = ['title', 'author', 'text', 'active', ]
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('Blog_List_View')
    context_object_name = 'blogs'


class BlogAddCommentView(generic.CreateView):
    model = Comment
    fields = ['name', 'blog', 'text', ]
    template_name = 'blog/blog.comment.html'
    success_url = reverse_lazy('Blog_List_View')
    context_object_name = 'comments'


class BlogCommentDeleteView(generic.DeleteView):
    model = Comment
    template_name = 'blog/blog_comment_delete.html'
    success_url = reverse_lazy('Blog_detail_View')
    context_object_name = 'blogs'
