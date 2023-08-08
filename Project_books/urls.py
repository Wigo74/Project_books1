from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from books.views import AuthorViewSet, BooksViewSet, ReaderViewSet

router = routers.SimpleRouter()
router.register('author', AuthorViewSet)
router.register('books', BooksViewSet)
router.register('readers', ReaderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
