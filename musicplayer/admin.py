from django.contrib import admin
from .models import Category, Artist, Album, Song

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_tamil')
    search_fields = ('name', 'name_tamil')

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_tamil')
    search_fields = ('name', 'name_tamil')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tamil', 'artist', 'release_year')
    search_fields = ('title', 'title_tamil', 'artist__name')
    inlines = [SongInline]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tamil', 'artist', 'album', 'category', 'created_at')
    list_filter = ('artist', 'album', 'category')
    search_fields = ('title', 'title_tamil', 'artist__name', 'lyrics', 'lyrics_tamil')
