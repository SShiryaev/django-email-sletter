from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
