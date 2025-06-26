from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post

# Список статей (только опубликованные)
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

# Детальный просмотр статьи (с увеличением счетчика просмотров)
class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj

# Создание новой статьи
class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview_image", "is_published")
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Пост успешно создан!")
        return response

    def form_invalid(self, form):
        # Вывод ошибок формы для отладки
        print(form.errors)
        return super().form_invalid(form)


# Редактирование статьи с перенаправлением на просмотр после сохранения
class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "content", "preview_image", "is_published")

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

# Удаление статьи
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')