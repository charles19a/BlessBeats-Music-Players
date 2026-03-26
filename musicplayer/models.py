from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    name_tamil = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    name_tamil = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='artists/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    title_tamil = models.CharField(max_length=200, blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover_image = models.ImageField(upload_to='albums/', blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    title_tamil = models.CharField(max_length=200, blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True, related_name='songs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='songs')
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    audio_url = models.URLField(blank=True, null=True, help_text="External URL for the MP3 file")
    cover_image = models.ImageField(upload_to='song_covers/', blank=True, null=True, help_text="Overrides album cover if set")
    lyrics = models.TextField(blank=True, null=True)
    lyrics_tamil = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    @property
    def audio(self):
        if self.audio_url:
            return self.audio_url
        if self.audio_file:
            return self.audio_file.url
        return ""

    @property
    def cover(self):
        if self.cover_image:
            return self.cover_image
        elif self.album and self.album.cover_image:
            return self.album.cover_image
        return None

class FavoriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return f"{self.user.username} - {self.song.title}"
