from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from .models import Bookmark


# Create your views here.


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3


# 북마크 추가 기능
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


# 북마크 상세페이지 기능
class BookmarkDetailView(DetailView):
    model = Bookmark


# 북마크 수정 기능
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


# 북마크 삭제 기능
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')