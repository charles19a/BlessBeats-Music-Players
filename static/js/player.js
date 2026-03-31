/* ──────────────────────────────────────────
   BlessBeats Player  — Reliable Build
   Fixes: play/pause icon toggle, audio flow
────────────────────────────────────────── */

// Inline SVGs so we never depend on lucide re-rendering
const SVG = {
    play:  `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="black" stroke="none"><polygon points="5 3 19 12 5 21 5 3"/></svg>`,
    pause: `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="black" stroke="black" stroke-width="2.5" stroke-linecap="round"><line x1="6" y1="4" x2="6" y2="20"/><line x1="18" y1="4" x2="18" y2="20"/></svg>`,
    heart_filled: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="#f43f5e" stroke="#f43f5e" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>`,
    heart_empty:  `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>`,
};

document.addEventListener('DOMContentLoaded', () => {
    /* ── DOM refs ── */
    const audio           = document.getElementById('main-audio');
    const playPauseBtn    = document.getElementById('play-pause-btn');
    const progressBar     = document.getElementById('progress-bar');
    const progressCont    = document.getElementById('progress-container');
    const playerTitle     = document.getElementById('player-title');
    const playerArtist    = document.getElementById('player-artist');
    const playerCover     = document.getElementById('player-cover');
    const currentTimeEl   = document.getElementById('current-time');
    const totalTimeEl     = document.getElementById('total-time');
    const nextBtn         = document.getElementById('next-btn');
    const prevBtn         = document.getElementById('prev-btn');
    const shuffleBtn      = document.getElementById('shuffle-btn');
    const repeatBtn       = document.getElementById('repeat-btn');
    const sleepTimerBtn   = document.getElementById('sleep-timer-btn');
    const shareBtn        = document.getElementById('share-song-btn');
    const volumeSlider    = document.getElementById('volume-slider');
    const volumeFill      = document.getElementById('volume-fill');
    const playerFavBtn    = document.getElementById('player-favorite-toggle');
    const lyricsBtn       = document.getElementById('lyrics-btn');
    const lyricsModal     = document.getElementById('lyrics-modal');
    const closeLyrics     = document.getElementById('close-lyrics');
    const lyricsText      = document.getElementById('lyrics-text');
    const lyricsTamilText = document.getElementById('lyrics-tamil-text');
    const lyricsBg          = document.getElementById('lyrics-bg');
    const lyricsTitle       = document.getElementById('lyrics-title');
    const lyricsArtist      = document.getElementById('lyrics-artist');
    const lyricsCoverSmall  = document.getElementById('lyrics-cover-small');
    
    /* ── Search refs ── */
    const searchInput       = document.getElementById('live-search-input');
    const searchDropdown    = document.getElementById('search-dropdown');
    const searchResultsList = document.getElementById('search-results-list');
    const searchClearBtn    = document.getElementById('search-clear-btn');
    const liveSearchWrap    = document.getElementById('live-search-wrap');

    if (!audio || !playPauseBtn) return;  // Guard

    /* ── State ── */
    let isPlaying       = false;
    let currentIndex    = -1;
    let songCards       = [];
    let shuffleMode     = localStorage.getItem('shuffleMode') === 'true';
    let repeatMode      = localStorage.getItem('repeatMode') || 'all';
    let sleepTimer      = null;
    let currentSongId   = null;

    // Set initial volume
    audio.volume = 0.8;
    if (volumeFill) volumeFill.style.width = '80%';

    /* ── Init shuffle / repeat state ── */
    if (shuffleMode && shuffleBtn) shuffleBtn.classList.add('active');
    applyRepeatIcon();

    /* ────────────────────────────
       Song Cards
    ──────────────────────────── */
    function refreshCards() {
        songCards = Array.from(document.querySelectorAll('.lib-item'));
        songCards.forEach((card, i) => {
            card.addEventListener('click', (e) => {
                if (e.target.closest('.fav-btn')) return;
                loadSong(i);
            });
        });
    }

    /* ────────────────────────────
       Load & Play a Song
    ──────────────────────────── */
    function loadSong(index) {
        if (!songCards.length) return;
        if (index < 0) index = songCards.length - 1;
        if (index >= songCards.length) index = 0;

        currentIndex = index;
        const card = songCards[index];

        const url      = card.getAttribute('data-audio') || '';
        const title    = card.getAttribute('data-title')  || 'Unknown';
        const artist   = card.getAttribute('data-artist') || '';
        const cover    = card.getAttribute('data-cover')  || '';
        const lyrics   = card.getAttribute('data-lyrics') || '';
        const lyricsT  = card.getAttribute('data-lyrics-tamil') || '';
        currentSongId  = card.getAttribute('data-id');

        if (!url) {
            showToast('⚠️ No audio URL for this song');
            return;
        }

        // Update player UI (Dock & Immersive Lyrics)
        if (playerTitle)  playerTitle.textContent  = title;
        if (playerArtist) playerArtist.textContent = artist;
        if (playerCover)  playerCover.src = cover || playerCover.src;

        // Lyrics View Sync
        if (lyricsTitle)      lyricsTitle.textContent = title;
        if (lyricsArtist)     lyricsArtist.textContent = artist;
        if (lyricsCoverSmall) lyricsCoverSmall.src = cover || playerCover.src;
        if (lyricsBg)         lyricsBg.src = cover || playerCover.src;
        
        if (lyricsText)       lyricsText.innerHTML      = lyrics  ? nl2br(lyrics) : '<p style="opacity:0.3; font-style:italic;">Meditation / Instrumental<br>No lyrics found in the archive.</p>';
        if (lyricsTamilText)  lyricsTamilText.innerHTML = lyricsT ? nl2br(lyricsT) : '<p style="opacity:0.3; font-style:italic;">பாடல் வரிகள் இல்லை</p>';

        // Update Lyrics Button Glow
        if (lyricsBtn) {
            if (lyrics || lyricsT) {
                lyricsBtn.classList.add('has-lyrics');
                lyricsBtn.setAttribute('title', 'Lyrics Available');
            } else {
                lyricsBtn.classList.remove('has-lyrics');
                lyricsBtn.setAttribute('title', 'No Lyrics Available');
            }
        }

        // Highlight active card & scroll to it
        songCards.forEach(c => c.classList.remove('playing'));
        card.classList.add('playing');
        card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        // Sync fav icon
        syncFavState(currentSongId);

        // History
        saveHistory({ id: currentSongId, title, artist, cover });

        // Load & play audio
        audio.src = url;
        audio.load();
        playAudio();
    }

    /* ────────────────────────────
       Audio Control
    ──────────────────────────── */
    function playAudio() {
        const promise = audio.play();
        if (promise !== undefined) {
            promise
                .then(() => {
                    isPlaying = true;
                    setPlayIcon('pause');
                    playPauseBtn.classList.add('btn-main-active');
                })
                .catch(err => {
                    console.warn('Playback error:', err);
                    isPlaying = false;
                    setPlayIcon('play');
                    showToast('⚠️ Could not play. Check audio URL.');
                });
        }
    }

    function pauseAudio() {
        audio.pause();
        isPlaying = false;
        setPlayIcon('play');
        playPauseBtn.classList.remove('btn-main-active');
    }

    /* Swap play / pause icon using pre-built SVG strings */
    function setPlayIcon(mode) {
        if (!playPauseBtn) return;
        playPauseBtn.innerHTML = mode === 'pause' ? SVG.pause : SVG.play;
    }

    /* ────────────────────────────
       Controls
    ──────────────────────────── */
    playPauseBtn.addEventListener('click', () => {
        if (isPlaying) {
            pauseAudio();
        } else {
            if (audio.src && audio.src !== window.location.href) {
                playAudio();
            } else if (songCards.length) {
                loadSong(0);
            }
        }
    });

    if (nextBtn) nextBtn.addEventListener('click', () => {
        loadSong(shuffleMode ? randIndex() : currentIndex + 1);
    });

    if (prevBtn) prevBtn.addEventListener('click', () => {
        // If > 3 seconds in, restart; else go to previous
        if (audio.currentTime > 3) {
            audio.currentTime = 0;
        } else {
            loadSong(currentIndex - 1);
        }
    });

    if (shuffleBtn) shuffleBtn.addEventListener('click', () => {
        shuffleMode = !shuffleMode;
        localStorage.setItem('shuffleMode', shuffleMode);
        shuffleBtn.classList.toggle('active', shuffleMode);
        showToast(shuffleMode ? '🔀 Shuffle ON' : '🔀 Shuffle OFF');
    });

    if (repeatBtn) repeatBtn.addEventListener('click', () => {
        const modes = ['all', 'one', 'none'];
        repeatMode = modes[(modes.indexOf(repeatMode) + 1) % modes.length];
        localStorage.setItem('repeatMode', repeatMode);
        applyRepeatIcon();
        const labels = { all: '🔁 Repeat All', one: '🔂 Repeat One', none: '➡️ No Repeat' };
        showToast(labels[repeatMode]);
    });

    // Auto-advance
    audio.addEventListener('ended', () => {
        if (repeatMode === 'one') {
            audio.currentTime = 0;
            playAudio();
        } else if (shuffleMode) {
            loadSong(randIndex());
        } else if (repeatMode === 'all' || currentIndex < songCards.length - 1) {
            loadSong(currentIndex + 1);
        } else {
            pauseAudio();
        }
    });

    /* ────────────────────────────
       Progress bar
    ──────────────────────────── */
    audio.addEventListener('timeupdate', () => {
        const { duration, currentTime } = audio;
        if (!isNaN(duration) && duration > 0) {
            const pct = (currentTime / duration) * 100;
            if (progressBar) progressBar.style.width = pct + '%';
            if (totalTimeEl) totalTimeEl.textContent = fmt(duration);
        }
        if (currentTimeEl) currentTimeEl.textContent = fmt(audio.currentTime);
    });

    if (progressCont) {
        progressCont.addEventListener('click', (e) => {
            const rect = progressCont.getBoundingClientRect();
            const pct  = (e.clientX - rect.left) / rect.width;
            if (!isNaN(audio.duration)) audio.currentTime = pct * audio.duration;
        });
    }

    /* ────────────────────────────
       Volume
    ──────────────────────────── */
    if (volumeSlider) {
        volumeSlider.addEventListener('click', (e) => {
            const rect = volumeSlider.getBoundingClientRect();
            const vol  = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
            audio.volume = vol;
            if (volumeFill) volumeFill.style.width = (vol * 100) + '%';
        });
    }

    /* ────────────────────────────
       Sleep Timer & Share
    ──────────────────────────── */
    if (sleepTimerBtn) {
        sleepTimerBtn.addEventListener('click', () => {
            const min = prompt('Sleep timer — minutes (0 to cancel):', '30');
            if (min === null) return;
            if (sleepTimer) clearTimeout(sleepTimer);
            const ms = parseInt(min) * 60000;
            if (ms > 0) {
                sleepTimer = setTimeout(() => { pauseAudio(); showToast('😴 Sleep timer — stopped'); }, ms);
                sleepTimerBtn.classList.add('active');
                showToast(`⏲️ Stops in ${min} min`);
            } else {
                sleepTimerBtn.classList.remove('active');
                showToast('⏲️ Timer cancelled');
            }
        });
    }

    if (shareBtn) {
        shareBtn.addEventListener('click', () => {
            if (!currentSongId) { showToast('Play a song first'); return; }
            const url = `${location.origin}/?song=${currentSongId}`;
            navigator.clipboard.writeText(url).then(() => showToast('🔗 Link copied!'));
        });
    }

    /* ────────────────────────────
       Favorites
    ──────────────────────────── */
    function syncFavState(songId) {
        if (!playerFavBtn || !songId) return;
        const isFav = Array.isArray(window.favoriteIds) && window.favoriteIds.includes(parseInt(songId));
        playerFavBtn.innerHTML = isFav ? SVG.heart_filled : SVG.heart_empty;
        playerFavBtn.classList.toggle('active', isFav);
    }

    if (playerFavBtn) {
        playerFavBtn.addEventListener('click', () => {
            if (!currentSongId) return;
            const csrf = (document.cookie.match('(^|;) ?csrftoken=([^;]*)(;|$)') || [])[2] || '';
            fetch(`/toggle-favorite/${currentSongId}/`, {
                method: 'POST',
                headers: { 'X-CSRFToken': csrf }
            })
            .then(r => r.json())
            .then(data => {
                if (data.status === 'success') {
                    const id = parseInt(currentSongId);
                    if (data.is_favorite) {
                        if (!window.favoriteIds.includes(id)) window.favoriteIds.push(id);
                    } else {
                        window.favoriteIds = window.favoriteIds.filter(x => x !== id);
                    }
                    syncFavState(currentSongId);
                }
            });
        });
    }

    /* Global toggleFavorite (for song row heart buttons) — defined in base.html too,
       but the player.js version updates the player heart icon consistently */
    window.toggleFavorite = function(songId, btn) {
        const csrf = (document.cookie.match('(^|;) ?csrftoken=([^;]*)(;|$)') || [])[2] || '';
        fetch(`/toggle-favorite/${songId}/`, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrf }
        })
        .then(r => r.json())
        .then(data => {
            if (data.status === 'success') {
                const id = parseInt(songId);
                if (data.is_favorite) {
                    btn.classList.add('active');
                    btn.style.color = '#f43f5e';
                    const icon = btn.querySelector('i');
                    if (icon) icon.setAttribute('fill', 'currentColor');
                    if (!window.favoriteIds.includes(id)) window.favoriteIds.push(id);
                } else {
                    btn.classList.remove('active');
                    btn.style.color = '';
                    const icon = btn.querySelector('i');
                    if (icon) icon.removeAttribute('fill');
                    window.favoriteIds = window.favoriteIds.filter(x => x !== id);
                }
                // Sync player dock heart if current song
                if (currentSongId && parseInt(currentSongId) === id) syncFavState(currentSongId);
            }
        });
    };

    /* ────────────────────────────
       Lyrics Modal
    ──────────────────────────── */
    if (lyricsBtn && lyricsModal) {
        lyricsBtn.addEventListener('click', () => {
            lyricsModal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    }
    if (closeLyrics && lyricsModal) {
        closeLyrics.addEventListener('click', () => {
            lyricsModal.classList.remove('open');
            document.body.style.overflow = '';
        });
    }
    window.addEventListener('click', (e) => {
        if (e.target === lyricsModal) {
            lyricsModal.classList.remove('open');
            document.body.style.overflow = '';
        }
        // Hide search dropdown if clicking outside
        if (searchDropdown && !liveSearchWrap.contains(e.target)) {
            searchDropdown.style.display = 'none';
        }
    });

    /* ── Live Search Dropdown Logic ── */
    let searchDebounce = null;
    let selectedSearchIdx = -1;

    if (searchInput) {
        searchInput.addEventListener('input', () => {
            clearTimeout(searchDebounce);
            const q = searchInput.value.trim();
            
            if (searchClearBtn) searchClearBtn.style.display = q ? 'block' : 'none';
            if (!q) { searchDropdown.style.display = 'none'; selectedSearchIdx = -1; return; }

            searchDebounce = setTimeout(() => {
                fetch(`/api/search/?q=${encodeURIComponent(q)}`)
                    .then(r => r.json())
                    .then(data => {
                        searchResultsList.innerHTML = '';
                        selectedSearchIdx = -1;
                        if (!data.songs || data.songs.length === 0) {
                            searchResultsList.innerHTML = '<div style="padding: 18px; color: var(--text-dim); text-align: center; font-size: 0.9rem;">No tracks found</div>';
                        } else {
                            data.songs.forEach((song, idx) => {
                                const div = document.createElement('div');
                                div.className = 'search-result-item';
                                div.setAttribute('data-index', idx);
                                div.innerHTML = `
                                    <div class="playing-viz" style="display:none; width:12px; margin-right:4px;">
                                        <div class="viz-bar"></div><div class="viz-bar"></div><div class="viz-bar"></div>
                                    </div>
                                    <img src="${song.cover}" style="width:40px; height:40px; border-radius:8px; object-fit:cover; flex-shrink:0;">
                                    <div style="flex:1; min-width:0;">
                                        <div class="truncate" style="font-weight:700; font-size:0.92rem; color:#fff;">${song.title}</div>
                                        <div class="truncate" style="font-size:0.75rem; color:var(--text-muted);">${song.artist}</div>
                                    </div>
                                    <div style="color:var(--text-dim);"><i data-lucide="play" style="width:14px;"></i></div>
                                `;
                                div.onclick = () => selectSearchResult(song);
                                searchResultsList.appendChild(div);
                            });
                            if (window.lucide) lucide.createIcons();
                        }
                        searchDropdown.style.display = 'block';
                    });
            }, 250);
        });

        function selectSearchResult(song) {
            const mockCard = document.createElement('div');
            mockCard.className = 'lib-item';
            mockCard.setAttribute('data-audio', song.audio);
            mockCard.setAttribute('data-title', song.title);
            mockCard.setAttribute('data-artist', song.artist);
            mockCard.setAttribute('data-cover', song.cover);
            mockCard.setAttribute('data-lyrics', song.lyrics);
            mockCard.setAttribute('data-lyrics-tamil', song.lyrics_tamil);
            mockCard.setAttribute('data-id', song.id);
            
            songCards.unshift(mockCard);
            loadSong(0);
            searchDropdown.style.display = 'none';
            searchInput.value = '';
            if (searchClearBtn) searchClearBtn.style.display = 'none';
            selectedSearchIdx = -1;
        }

        function updateSearchSelection() {
            const items = searchResultsList.querySelectorAll('.search-result-item');
            items.forEach((item, idx) => {
                item.classList.toggle('selected', idx === selectedSearchIdx);
                if (idx === selectedSearchIdx) item.scrollIntoView({ block: 'nearest' });
            });
        }

        searchInput.addEventListener('keydown', (e) => {
            const items = searchResultsList.querySelectorAll('.search-result-item');
            if (searchDropdown.style.display === 'block' && items.length > 0) {
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    selectedSearchIdx = (selectedSearchIdx + 1) % items.length;
                    updateSearchSelection();
                } else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    selectedSearchIdx = (selectedSearchIdx - 1 + items.length) % items.length;
                    updateSearchSelection();
                } else if (e.key === 'Enter' && selectedSearchIdx >= 0) {
                    e.preventDefault();
                    items[selectedSearchIdx].click();
                } else if (e.key === 'Escape') {
                    searchDropdown.style.display = 'none';
                }
            } else if (e.key === 'Enter') {
                const q = searchInput.value.trim();
                if (q) window.location.href = `/search/?q=${encodeURIComponent(q)}`;
            }
        });

        // Re-show dropdown on refocus if query exists
        searchInput.addEventListener('focus', () => {
            if (searchInput.value.trim() && searchResultsList.children.length > 0) {
                searchDropdown.style.display = 'block';
            }
        });
    }

    if (searchClearBtn) {
        searchClearBtn.addEventListener('click', () => {
            searchInput.value = '';
            searchClearBtn.style.display = 'none';
            searchDropdown.style.display = 'none';
            searchInput.focus();
        });
    }

    function nl2br(str) {
        if (typeof str !== 'string') return '';
        return str.replace(/\n/g, '<br>');
    }

    /* ────────────────────────────
       Helpers
    ──────────────────────────── */
    function applyRepeatIcon() {
        if (!repeatBtn) return;
        repeatBtn.classList.toggle('active', repeatMode !== 'none');
        // Show repeat-1 vs repeat visually using opacity
        repeatBtn.title = repeatMode === 'one' ? 'Repeat One' : repeatMode === 'all' ? 'Repeat All' : 'No Repeat';
        repeatBtn.style.opacity = repeatMode === 'none' ? '0.4' : '1';
    }

    function randIndex() {
        let i;
        do { i = Math.floor(Math.random() * songCards.length); } while (i === currentIndex && songCards.length > 1);
        return i;
    }

    function fmt(s) {
        if (!s || isNaN(s)) return '0:00';
        const m = Math.floor(s / 60);
        const sec = Math.floor(s % 60);
        return `${m}:${sec < 10 ? '0' + sec : sec}`;
    }

    function saveHistory(song) {
        try {
            let h = JSON.parse(localStorage.getItem('recent_played') || '[]');
            h = h.filter(x => x.id !== song.id);
            h.unshift(song);
            localStorage.setItem('recent_played', JSON.stringify(h.slice(0, 15)));
        } catch(e) {}
    }

    function showToast(msg) {
        const t = document.createElement('div');
        Object.assign(t.style, {
            position: 'fixed', bottom: '130px', left: '50%', transform: 'translateX(-50%)',
            background: 'rgba(8,9,16,0.95)', backdropFilter: 'blur(20px)',
            border: '1px solid rgba(255,255,255,0.1)', color: '#fff',
            padding: '10px 26px', borderRadius: '50px', fontWeight: '600',
            fontSize: '0.88rem', zIndex: '9999', pointerEvents: 'none',
            boxShadow: '0 10px 40px rgba(0,0,0,0.5)',
            fontFamily: "'Outfit', sans-serif",
        });
        t.textContent = msg;
        document.body.appendChild(t);
        setTimeout(() => t.remove(), 3000);
    }

    /* ── Bootstrap ── */
    refreshCards();
    setPlayIcon('play');   // ensure play icon is visible on load
});
