from rest_framework import serializers
from .models import Genre, Book

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, valid_data):
        return Genre.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.name = valid_data.get('name', instance.name)
        instance.save()
        return instance

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    genre_id = serializers.IntegerField()

    def create(self, valid_data):
        return Book.objects.create(**valid_data)

    def update(self, instance, valid_data):
        instance.title = valid_data.get('title', instance.title)
        instance.price = valid_data.get('price', instance.price)
        instance.genre_id = valid_data.get('genre_id', instance.genre_id)
        instance.save()
        return instance
