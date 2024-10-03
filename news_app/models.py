from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255, null=True)
    description = models.TextField("Описание", null=True)
    image = models.CharField("URL-фото", max_length=500, null=True)
    created_at = models.DateTimeField("Дата и время публикации", default=datetime.now)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.created_at}"
