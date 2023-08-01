# Generated by Django 4.1.7 on 2023-08-01 20:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="books.author",
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="books",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.CreateModel(
            name="Readers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=64, verbose_name="Фамилия")),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128,
                        region=None,
                        unique=True,
                        verbose_name="номер телефона",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Статус читателя"),
                ),
                (
                    "is_creation",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "is_editing",
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата редактирования"
                    ),
                ),
                (
                    "books",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="books.books",
                        verbose_name="Книги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Читатель",
                "verbose_name_plural": "Читатели",
            },
        ),
    ]
