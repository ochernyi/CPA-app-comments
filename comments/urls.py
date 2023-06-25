from django.urls import path

from comments.views import CommentCreateView, CommentListView, CommentDetailView

urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="comment-create"),
    path("", CommentListView.as_view(), name="comment-list"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]

app_name = "comments"
