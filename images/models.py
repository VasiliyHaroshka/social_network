from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    """Модель отображения картинки"""
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Картинка", upload_to="images/%Y/%m/%d")
    description = models.TextField("Описание", blank=True)
    slug = models.SlugField("Слаг", max_length=200, blank=True)
    url = models.URLField("URL")
    created = models.DateTimeField("Дата создания", auto_now_add=True, db_index=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="images_created",
        verbose_name="пользователь, добавивший картинку",
    )
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="liked_images",
        verbose_name="лайк",
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Добавление слага по заголовку"""
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
