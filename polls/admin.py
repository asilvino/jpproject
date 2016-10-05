from django.contrib import admin

# Register your models here.


from django.contrib import admin
from polls.models import Post



class PostAdmin(admin.ModelAdmin):

    search_fields = ['author', 'title', 'text']
    list_filter = ('created_date','published_date')


admin.site.register(Post, PostAdmin)