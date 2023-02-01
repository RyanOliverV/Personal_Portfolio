from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentView, LikeView
from . import views as contact_views

#These url patterns setup the mapping, and sends the users to the correct locations
urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment', CommentView.as_view(), name='add-comment'),
    path("contact/", contact_views.contact_view, name="contact"),
    path("like/<int:pk>", LikeView, name="like-post")
]