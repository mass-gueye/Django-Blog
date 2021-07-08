from django.contrib import admin
from .models import Post,Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','author',)
    list_filter = ('title', 'pub_date',)
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)