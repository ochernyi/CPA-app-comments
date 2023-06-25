from django.urls import reverse_lazy
from django.views import generic

from comments.forms import CommentForm
from comments.models import Comment


class CommentListView(generic.ListView):
    model = Comment
    template_name = "comment_list.html"
    paginate_by = 25


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment_form.html"
    success_url = reverse_lazy("comments:comment-list")


class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = "comment_detail.html"
