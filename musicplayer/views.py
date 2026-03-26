from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Song, Category, Artist, Album, FavoriteSong
from django.utils import timezone

def get_base_context(request):
    """Utility to provide sidebar and common data."""
    context = {
        'categories': Category.objects.all(),
        'artists': Artist.objects.all()[:10],
        'favorite_ids': [],
        'common_timezones': [
            'Asia/Kolkata', 'Asia/Singapore', 'Asia/Dubai', 
            'Europe/London', 'America/New_York', 'UTC'
        ],
        'current_timezone': timezone.get_current_timezone_name(),
    }
    if request.user.is_authenticated:
        context['favorite_count'] = FavoriteSong.objects.filter(user=request.user).count()
        context['favorite_ids'] = list(FavoriteSong.objects.filter(user=request.user).values_list('song_id', flat=True))
    return context

@login_required
def player_view(request):
    category_id = request.GET.get('category')
    artist_id = request.GET.get('artist')
    album_id = request.GET.get('album')
    
    songs = Song.objects.all().order_by('-created_at')
    active_category = None
    active_artist = None
    active_album = None
    
    if category_id:
        if category_id.isdigit():
            active_category = Category.objects.filter(id=category_id).first()
        else:
            active_category = Category.objects.filter(name__iexact=category_id).first()
        if active_category:
            songs = songs.filter(category=active_category)
    if artist_id:
        active_artist = Artist.objects.filter(id=artist_id).first()
        if active_artist:
            songs = songs.filter(artist=active_artist)
    if album_id:
        active_album = Album.objects.filter(id=album_id).first()
        if active_album:
            songs = songs.filter(album=active_album)
        
    context = get_base_context(request)
    hour = timezone.localtime(timezone.now()).hour

    # Build seasonal shelves
    christmas_cat = Category.objects.filter(name__icontains='christmas').first()
    lent_cat      = Category.objects.filter(name__icontains='lent').first()

    all_songs = Song.objects.all().order_by('-created_at')
    worship_songs  = all_songs.exclude(category=christmas_cat).exclude(category=lent_cat)[:20] if (christmas_cat or lent_cat) else all_songs[:20]
    christmas_songs = all_songs.filter(category=christmas_cat)[:20] if christmas_cat else Song.objects.none()
    lent_songs     = all_songs.filter(category=lent_cat)[:20] if lent_cat else Song.objects.none()

    now = timezone.localtime(timezone.now())
    # Robust lookup for Keerthanai Padal
    keerthanai_album = Album.objects.filter(title__icontains='Keerthanai').first()
    if not keerthanai_album:
        # Emergency fallback: create it if it's missing (shouldn't happen but safe)
        worship_art = Artist.objects.first()
        keerthanai_album, _ = Album.objects.get_or_create(title='Keerthanai Padal', defaults={'artist': worship_art})
    
    keerthanai_songs = Song.objects.filter(album=keerthanai_album)
    if not keerthanai_songs.exists():
        # Second fallback: grab all 'Worship' category songs if album mapping is lost
        worship_cat = Category.objects.filter(name__icontains='worship').first()
        keerthanai_songs = Song.objects.filter(category=worship_cat)

    context.update({
        'songs': songs,
        'worship_songs': worship_songs,
        'christmas_songs': christmas_songs,
        'lent_songs': lent_songs,
        'keerthanai_songs': keerthanai_songs,
        'keerthanai_album': keerthanai_album,
        'active_category': active_category,
        'artist': active_artist,
        'active_album': active_album,
        'hour': hour,
        'time_24': now.strftime('%H:%M'),
        'time_12': now.strftime('%I:%M %p'),
    })
    return render(request, 'musicplayer/index.html', context)

@login_required
def search_view(request):
    query = request.GET.get('q', '')
    songs = Song.objects.none()
    
    if query:
        songs = Song.objects.filter(
            Q(title__icontains=query) | 
            Q(title_tamil__icontains=query) | 
            Q(artist__name__icontains=query) |
            Q(artist__name_tamil__icontains=query) |
            Q(album__title__icontains=query) |
            Q(lyrics__icontains=query)
        ).distinct()
    
    context = get_base_context(request)
    context.update({
        'songs': songs,
        'query': query,
    })
    return render(request, 'musicplayer/search.html', context)

@login_required
def library_view(request):
    # If filtered to favorites
    show_favorites = request.GET.get('view') == 'favorites'
    category_id = request.GET.get('category')
    artist_id = request.GET.get('artist')
    
    songs = Song.objects.all().order_by('title')
    title = "Spiritual Archive"

    if show_favorites and request.user.is_authenticated:
        songs = songs.filter(favorited_by__user=request.user)
        title = "Your Favorites"
    
    if category_id:
        songs = songs.filter(category_id=category_id)
    if artist_id:
        songs = songs.filter(artist_id=artist_id)
        
    albums = Album.objects.all()
    artists = Artist.objects.all()
    
    context = get_base_context(request)
    
    context.update({
        'songs': songs,
        'albums': albums,
        'all_artists': artists,
        'page_title': title,
        'is_favorites_view': show_favorites
    })
    return render(request, 'musicplayer/library.html', context)

@login_required
def toggle_favorite(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    favorite, created = FavoriteSong.objects.get_or_create(user=request.user, song=song)
    
    if not created:
        favorite.delete()
        is_favorite = False
    else:
        is_favorite = True
        
    return JsonResponse({
        'status': 'success',
        'is_favorite': is_favorite,
        'song_id': song_id
    })
@login_required
def live_search_api(request):
    """
    Returns JSON song results for live search dropdown.
    Called via AJAX as the user types.
    """
    query = request.GET.get('q', '').strip()
    if not query:
        return JsonResponse({'songs': []})

    songs = Song.objects.filter(
        Q(title__icontains=query) |
        Q(title_tamil__icontains=query) |
        Q(artist__name__icontains=query) |
        Q(album__title__icontains=query) |
        Q(lyrics__icontains=query)
    ).distinct().select_related('artist', 'album')[:10]

    results = []
    for song in songs:
        cover_url = song.cover.url if song.cover else '/static/img/default_cover.png'
        results.append({
            'id': song.id,
            'title': song.title,
            'artist': song.artist.name if song.artist else 'Unknown',
            'audio': song.audio,
            'cover': cover_url,
            'lyrics': song.lyrics or '',
            'lyrics_tamil': song.lyrics_tamil or '',
        })

    return JsonResponse({'songs': results})
@login_required
def set_timezone(request):
    if request.method == 'POST':
        tzname = request.POST.get('timezone')
        if tzname:
            request.session['django_timezone'] = tzname
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
