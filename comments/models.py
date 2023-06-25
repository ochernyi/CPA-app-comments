import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


class Comment(models.Model):
    ALLOWED_TAGS_REGEX = r'^<(a|code|i|strong)>(.*?)<\/(a|code|i|strong)>$'

    allowed_tags_validator = RegexValidator(
        regex=ALLOWED_TAGS_REGEX,
        message='Only <a>, <code>, <i>, and <strong> tags are allowed.',
    )

    alphanumeric_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9]+$',
        message='Only Latin letters and digits are allowed.',
    )

    username = models.CharField(
        max_length=255, null=False, blank=False,
        validators=[alphanumeric_validator]
    )
    email = models.EmailField(null=False, blank=False)
    homepage = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(
        null=False, blank=False,
        # validators=[allowed_tags_validator]
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='replies'
    )

    def clean(self):
        super().clean()
        self.validate_html_tags()

    def validate_html_tags(self):
        if "<" not in self.text:
            return
        if not re.match(self.ALLOWED_TAGS_REGEX, self.text):
            raise ValidationError('Only <a>, <code>, <i>, and <strong> tags are allowed.')

    def __str__(self):
        return f"Comment by {self.username}"

    def get_replies(self):
        return self.replies.all()

    class Meta:
        ordering = ["-created_at"]
