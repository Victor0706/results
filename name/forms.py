from django import forms
from django.core.exceptions import ValidationError
from .models import Article, Response


class ArticleForm(forms.ModelForm):
    text = forms.CharField(min_length=5)

    class Meta:
        model = Article
        fields = ['title', 'text', 'author', 'category', 'upload']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class ResponseForm(forms.ModelForm):
    text = forms.CharField(min_length=5)

    class Meta:
        model = Response
        fields = ['author', 'text', 'article', 'category_type']
