from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreAPIView(APIView):
    def get(self, request):
        janrlar = Genre.objects.all()
        seralizer = GenreSerializer(janrlar, many=True)
        return Response(seralizer.data)

    def post(self, request):
        seralizer = GenreSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

class GenreDetailAPIView(APIView):
    def get(self, request, pk):
        janr = Genre.objects.get(pk=pk)
        seralizer = GenreSerializer(janr)
        return Response(seralizer.data)

    def put(self, request, pk):
        janr = Genre.objects.get(pk=pk)
        seralizer = GenreSerializer(janr, data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

    def delete(self, request, pk):
        janr = Genre.objects.get(pk=pk)
        janr.delete()
        return Response(status=204)

class BookAPIView(APIView):
    def get(self, request):
        kitoblar = Book.objects.all()
        seralizer = BookSerializer(kitoblar, many=True)
        return Response(seralizer.data)

    def post(self, request):
        seralizer = BookSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        kitob = Book.objects.get(pk=pk)
        seralizer = BookSerializer(kitob)
        return Response(seralizer.data)

    def put(self, request, pk):
        kitob = Book.objects.get(pk=pk)
        seralizer = BookSerializer(kitob, data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

    def delete(self, request, pk):
        kitob = Book.objects.get(pk=pk)
        kitob.delete()
        return Response(status=204)
