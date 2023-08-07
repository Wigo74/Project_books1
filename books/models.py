from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания", null=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class Author(DatesModelMixin):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.TextField(max_length=50, verbose_name='Имя')
    last_name = models.TextField(max_length=50, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.name


class Books(DatesModelMixin):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    number_of_pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')
    books = models.PositiveIntegerField(verbose_name='Кол-во книг в библиотеке')

    def __str__(self):
        return self.title


class Readers(DatesModelMixin):
    username = models.CharField(max_length=64, verbose_name="Имя")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    phone = PhoneNumberField(verbose_name="номер телефона")
    is_active = models.BooleanField(default=True, verbose_name="Статус читателя")

    books = models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name="Книги")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return self.username
