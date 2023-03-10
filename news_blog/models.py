from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True, 'is_superuser': True})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='articles', verbose_name='Новость')
    content = models.TextField('Контент')
    image = models.ImageField('Изображение', upload_to='images/news_article/', blank=True, null=True)
    caption = models.CharField('Описание изображения', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Абзац'
        verbose_name_plural = 'Абзацы'
        ordering = ['id']

    def __str__(self):
        return self.caption or self.image.name or str(self.id)
