from django.contrib import admin
from .models import Post

@admin.register(Post) # a decorator to register the Post model with the admin site.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date') # fields to display in the admin site for Post model. 
    list_filter = ('publication_date', 'author') # filters used for Post model filtering. 
    search_fields = ('title', 'content')
