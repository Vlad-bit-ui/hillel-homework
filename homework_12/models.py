from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=150, verbose_name="Назва")
    developer = models.CharField(max_length=100, verbose_name="Розробник")
    genre = models.CharField(max_length=80, verbose_name="Жанр")
    release_year = models.PositiveSmallIntegerField(verbose_name="Рік виходу")
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        verbose_name="Ціна"
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Опис"
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступна"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата додавання"
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Гра"
        verbose_name_plural = "Ігри"