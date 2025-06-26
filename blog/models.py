from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое",
        blank=True,
        null=True,
    )
    preview_image = models.ImageField(
        upload_to="post/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания",
        help_text="Введите дату создания"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публикации"
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']


    def __str__(self):
        return self.title
