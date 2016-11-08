from rest_framework import serializers
from song.models import *



class GenreSerializer(serializers.Serializer):
	genre=serializers.CharField(max_length=100)
class AlbumSerializer(serializers.Serializer):
	album=serializers.CharField(max_length=100)

class ArtistSerializer(serializers.Serializer):
	artist=serializers.CharField(max_length=100)
class playlistSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=100)
class CommentAddSerializer(serializers.Serializer):
	comment=serializers.CharField(max_length=999999)
	song=serializers.CharField(max_length=1000)
class CommentshowSerializer(serializers.Serializer):
	song = serializers.CharField(max_length=1000)
class FeedbackSerializer(serializers.Serializer):
	feedback=serializers.CharField(max_length=999999)
	song=serializers.CharField(max_length=1000)



