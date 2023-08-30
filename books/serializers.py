from rest_framework import serializers

from books.models import Author, Books, Readers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=Author.objects.all(), slug_field='last_name')

    class Meta:
        model = Books
        fields = ["id", "title", "description", "number_of_pages", "author", "books"]


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(queryset=Books.objects.all(), slug_field='title')

    class Meta:
        model = Readers
        fields = '__all__'
