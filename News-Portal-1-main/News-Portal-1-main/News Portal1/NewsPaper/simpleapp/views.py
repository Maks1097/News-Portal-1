from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import New
from .filters import NewFilter
from .forms import NewForm, ArticleForm


class NewsList(ListView):
    model = New
    ordering = '-time_now'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'


class NewSearch(ListView):
    model = New
    ordering = '-time_now'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class NewCreate(CreateView):
    form_class = NewForm
    model = New
    template_name = 'news_edit.html'


class NewUpdate(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'news_edit.html'


class NewDelete(DeleteView):
    model = New
    template_name = 'news_delete.html'
    success_url = reverse_lazy('new_list')


class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = New
    template_name = 'news_edit.html'