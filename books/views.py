import requests
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from books.models import Author, Books, Readers
from books.serializers import AuthorSerializer, BooksSerializer, ReaderSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BooksViewSet(ModelViewSet):

    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class ReaderViewSet(ModelViewSet):

    queryset = Readers.objects.all()
    serializer_class = ReaderSerializer

