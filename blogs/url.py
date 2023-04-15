from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogAddCommentView, \
    BlogCommentDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='Blog_List_View'),
    path('<int:pk>/', BlogDetailView.as_view(), name='Blog_detail_View'),
    path('create/', BlogCreateView.as_view(), name='Blog_create_View'),
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='Blog_update_View'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='Blog_delete_View'),
    path('<int:pk>/comment/', BlogAddCommentView.as_view(), name='Blog_comment_view'),
    path('<int:pk>/comment/delete', BlogCommentDeleteView.as_view(), name='Blog_comment_delete_view'),

]
