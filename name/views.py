from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import HttpResponse

from .models import Article, Response
from .filters import ResponseFilter
from .forms import ArticleForm, ResponseForm

from .permissions import AuthorPermissionsMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http.response import HttpResponse
from flask import request


class ArticleList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 8


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'


class ArticleCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleUpdate(AuthorPermissionsMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(self.get_object().author == self.request.user)


class ArticleDelete(AuthorPermissionsMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    pk_url_kwarg = 'id'


class ResponseList(ListView):
    model = Response
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ResponseDetail(DetailView):
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'
    pk_url_kwarg = 'id'


class ResponseCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'


class ResponseUpdate(AuthorPermissionsMixin, UpdateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_edit.html'
    pk_url_kwarg = 'id'


class ResponseDelete(AuthorPermissionsMixin, DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = reverse_lazy('response_list')
    pk_url_kwarg = 'id'


