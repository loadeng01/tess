from django.db import models as m


class Category(m.Model):
    category  = m.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


class Post(m.Model):
    category = m.ForeignKey(Category, on_delete=m.CASCADE,
                blank=True, null=True, related_name='posts')
    title = m.CharField(max_length=200)
    body = m.TextField(blank=True, null=True)
    created_at = m.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


