from django import forms
from comments.models import Comment
from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ["username", "email", "homepage", "text"]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_homepage(self):
        homepage = self.cleaned_data.get('homepage')
        if homepage and not homepage.startswith(('http://', 'https://')):
            homepage = f'http://{homepage}'
        return homepage
