from django.shortcuts import render,redirect,render_to_response
from song.models import *
from song.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .forms import LogForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

@csrf_exempt
@api_view(["GET"])	
def index(request):
	obj=Songs.objects.all()
	l=[]
	for i in obj:
		dic={}
		dic={"link":i.link,"artist":i.Artist,"name":i.name,"genre":i.genre,"album":i.album}
		l.append(dic)
	return Response(l)
	
@api_view(['POST'])
def filterq(request):
	user=request.user
	filter_data=GenreSerializer(data=request.data)
	if filter_data.is_valid():
		genre=filter_data.validated_data['genre']
		
	obj=Songs.objects.filter(genre=genre)
	l=[]
	for i in obj:
		dic={}
		dic={"link":i.link,"artist":i.Artist,"name":i.name,"genre":i.genre,"album":i.album}
		l.append(dic)
	return Response(l)
@api_view(['POST'])
def filterartist(request):
	user=request.user
	filter_data=ArtistSerializer(data=request.data)
	if filter_data.is_valid():
		artist=filter_data.validated_data['artist']
		
	obj=Songs.objects.filter(Artist=artist)
	l=[]
	for i in obj:
		dic={}
		dic={"link":i.link,"artist":i.Artist,"name":i.name,"genre":i.genre,"album":i.album}
		l.append(dic)
	return Response(l)
@api_view(['POST'])
def filteralbum(request):
	user=request.user
	filter_data=AlbumSerializer(data=request.data)
	if filter_data.is_valid():
		album=filter_data.validated_data['album']
		
	obj=Songs.objects.filter(album=album)
	l=[]
	for i in obj:
		dic={}
		dic={"link":i.link,"artist":i.Artist,"name":i.name,"genre":i.genre,"album":i.album}
		l.append(dic)
	return Response(l)


@api_view(['POST'])
def playlist_v(request):
	user=request.user
	songs_data=playlistSerializer(data=request.data)
	if songs_data.is_valid():
		name=songs_data.validated_data['name']
	obj=Songs.objects.get(name__contains=name)
	play=playlist.objects.create(song=obj,user=user)
	

@api_view(['GET'])
def playlist_d(request):
	user=request.user
	obj=playlist.objects.filter(user=user)
	l=[]
	for i in obj:
		dic={}
		dic={"link":i.song.link,"artist":i.song.Artist,"name":i.song.name,"genre":i.song.genre,"album":i.song.album}
		l.append(dic)
	return Response(l)

def main_site(request):
	if request.method== 'POST':
		login_form=LogForm(request.POST)
		
		lo=LoginForm(request.POST)
		
		if login_form.is_valid():
			username=login_form.cleaned_data['username']
			password=login_form.cleaned_data['password']
			user= authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('song')
		if lo.is_valid():

			user=lo.save()
			
			
			user= authenticate(username=lo.cleaned_data.get('username'),password=lo.cleaned_data.get('password1'))
			
			
			if user is not None:
				
				if user.is_active:
					login(request,user)
					return redirect('song')
			
			
			else:
				messages.error(request,('Please correct the error below.'))
	else:
		lo = LoginForm(request.POST)
		login_form=LogForm(request.POST)
	return render(request,'song/Login.html',{'login_form':login_form,'lo':lo})
def main_page(request):
	return render_to_response('song/details.html')
	
	
@api_view(["POST"])
def comment_add(request):
	user=request.user
	serializer=CommentAddSerializer(data=request.data)
	if serializer.is_valid():
		comment=serializer.validated_data["comment"]
		song=serializer.validated_data["song"]
		obj=Comments.objects.create(user=user,comment=comment,song=song)
		obj.save()
@api_view(["POST"])
def comment_list(request):
	serializers=CommentshowSerializer(data=request.data)
	if serializers.is_valid():
		song=serializers.validated_data["song"]
		song_obj=Songs.objects.get(name__contains=song)
		obj=Comments.objects.filter(song=song_obj)
		l=[]
		for i in obj:
			d={}
			d={i.user.username:i.comment}
			l.append(d)
	return Response({"l":l})

@api_view(["POST"])
def report_abuse(request):
	serializers=CommentshowSerializer(data=request.data)
	if serializers.is_valid():
		song=serializers.validated_data["song"]
		song_obj=Songs.objects.get(name__contains=song)
		song_obj.abuse=song_obj.abuse+1
		song_obj.save()

@api_view(["POST"])
def feedback(request):
	serializers=FeedbackSerializer(data=request.data)
	user=request.user
	if serializers.is_valid():
		feedback=serializers.validated_data(["feedback"])
		song = serializers.validated_data["song"]
		song_obj = Songs.objects.get(name__contains=song)
		feedback_obj=feedback.objects.create(user=user,feedback=feedback,song=song_obj)
		feedback_obj.save()







