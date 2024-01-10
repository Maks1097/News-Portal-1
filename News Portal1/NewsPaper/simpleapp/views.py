from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import New


class NewsList(ListView):
    model = New
    ordering = '-time_now'
    #queryset = Product.objects.order_by(
    #    'name'
    #)
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = New
    # Используем другой шаблон — product.html
    template_name = 'new.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'new'