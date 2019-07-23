from django.contrib import admin
from .models import Post, Comment, Gallery
from django.urls import path
from users import models as users_models
from django.http import HttpResponseRedirect

admin.site.site_header = 'NDMU Admin Page'
admin.site.site_title = 'NDMU Admin Page'

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_posted')
	list_filter = ('date_posted',)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'image')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('post', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(users_models.Profile, ProfileAdmin)
admin.site.register(Gallery)
