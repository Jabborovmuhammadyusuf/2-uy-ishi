from django.urls import path
from .views import GenreAPIView, GenreDetailAPIView, BookAPIView, BookDetailAPIView

urlpatterns = [
    path('genres/', GenreAPIView.as_view()),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view()),
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
]
