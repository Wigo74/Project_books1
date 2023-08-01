from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.TextField(max_length=50, verbose_name='Имя')
    last_name = models.TextField(max_length=50, verbose_name='Фамилия')
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_editing = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    def __str__(self):
        return self.name


class Books(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    number_of_pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')
    books = models.PositiveIntegerField(verbose_name='Кол-во книг в библиотеке')
    is_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_editing = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    def __str__(self):
        return self.title


class Readers(models.Model):
    username = models.CharField(max_length=64, verbose_name="Имя")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    phone = PhoneNumberField(verbose_name="номер телефона")
    is_active = models.BooleanField(default=True, verbose_name="Статус читателя")

    books = models.ForeignKey(Books,on_delete=models.PROTECT, verbose_name="Книги")
    is_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_editing = models.DateField(auto_now_add=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return self.username
