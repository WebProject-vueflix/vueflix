from django.contrib import admin
from .models import PopularMovie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ( 'genres', 'actors', 'director')
    exclude = ('like_users',)
admin.site.register(PopularMovie,MovieAdmin)
