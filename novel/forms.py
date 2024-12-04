from django.forms import ModelForm
from novel.models import Novel


class NovelForm(ModelForm):
    class Meta:
        model = Novel
        fields = ['title', 'author', 'description', 'letter_body']