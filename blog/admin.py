from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    list_display = ['title', 'slug', 'status', 'created_on' ]
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    
    

# Register your models here.
# admin.site.register(Post)