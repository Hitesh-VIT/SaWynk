from django.contrib import admin
from song.models import *
from django.contrib.auth.models import User


class SongsAdmin(admin.ModelAdmin):
	pass
admin.site.register(Songs,SongsAdmin)
class playlistAdmin(admin.ModelAdmin):
	pass
admin.site.register(playlist,playlistAdmin)
class CommentsAdmin(admin.ModelAdmin):
	pass
admin.site.register(Comments,CommentsAdmin)


# Register your models here.
