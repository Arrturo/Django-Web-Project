<<<<<<< HEAD
=======
import datetime
>>>>>>> origin/main
from rest_framework import serializers
from .models import Book, Order, Author, Client, Genre


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
<<<<<<< HEAD
        fields = ['book_id', 'title', 'author', 'price', 'publisher', 'genre_genre', 'number_of_copies', 'year_of_publication']
=======
        fields = ['book_id', 'title', 'author', 'price', 'publisher', 'genre_genre', 'number_of_copies',
                  'year_of_publication']

>>>>>>> origin/main


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'book_book', 'client_client', 'purchase_date']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'name', 'last_name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'name', 'last_name', 'birth_date', 'city', 'address']

<<<<<<< HEAD

=======
>>>>>>> origin/main
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_id', 'genre']
