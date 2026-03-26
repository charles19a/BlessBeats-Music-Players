import requests
import os
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from musicplayer.models import Category, Artist, Album, Song

class Command(BaseCommand):
    help = 'Seed initial Tamil Christian songs and data'

    def handle(self, *args, **kwargs):
        # 1. Create Categories
        worship, _ = Category.objects.get_or_create(name='Worship', name_tamil='ஆராதனை')
        praise, _ = Category.objects.get_or_create(name='Praise', name_tamil='துதி')
        
        # 2. Create Artists
        artist1, _ = Artist.objects.get_or_create(name='Sample Artist', name_tamil='மாதிரி கலைஞர்')
        
        # 3. Create Albums
        album1, _ = Album.objects.get_or_create(title='Devotional Journey', title_tamil='பக்திப் பயணம்', artist=artist1)
        
        # 4. Download a Sample Audio File
        audio_url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
        self.stdout.write(f'Downloading sample audio from {audio_url}...')
        
        try:
            response = requests.get(audio_url, stream=True)
            if response.status_code == 200:
                audio_content = response.content
                
                # 5. Create Songs
                song_data = [
                    {'title': 'Glory to God', 'title_tamil': 'தேவனுக்கே மகிமை', 'lyrics': 'Sample lyrics...', 'lyrics_tamil': 'மாதிரி வரிகள்...'},
                    {'title': 'Amazing Grace', 'title_tamil': 'அற்புதமான கிருபை', 'lyrics': 'Another sample...', 'lyrics_tamil': 'மற்றொரு மாதிரி...'},
                ]
                
                for i, s in enumerate(song_data):
                    song, created = Song.objects.get_or_create(
                        title=s['title'],
                        artist=artist1,
                        album=album1,
                        category=worship if i == 0 else praise,
                        defaults={
                            'title_tamil': s['title_tamil'],
                            'lyrics': s['lyrics'],
                            'lyrics_tamil': s['lyrics_tamil']
                        }
                    )
                    
                    if created or not song.audio_file:
                        song.audio_file.save(f'sample_song_{i+1}.mp3', ContentFile(audio_content))
                        self.stdout.write(self.style.SUCCESS(f'Successfully created song: {s["title"]}'))
            else:
                self.stdout.write(self.style.ERROR('Failed to download sample audio.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded sample data!'))
