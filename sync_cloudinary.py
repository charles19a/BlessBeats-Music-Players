import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from musicplayer.models import Song, Artist, Album, Category

def sync_cloudinary():
    print("Clearing database...")
    Song.objects.all().delete()
    Artist.objects.all().delete()
    Album.objects.all().delete()
    Category.objects.all().delete()

    default_cat, _ = Category.objects.get_or_create(name="Worship")
    default_artist, _ = Artist.objects.get_or_create(name="Various Artists")
    default_album, _ = Album.objects.get_or_create(title="Cloud Archive", artist=default_artist)

    # Full Library (25 Songs)
    cloudinary_songs = [
        {"title": "Athumamae", "artist": "Worship Leader", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/001.Athumamae_En_Muzhu_ucsbdd.mp3", 
         "lyrics": "Athumamae en muzhu ullamae\nKartharai sthothari\nEnthavar seitha sagala upagarangalai\nOru podhum maravadhey", 
         "lyrics_tamil": "ஆத்துமாவே என் முழு உள்ளமே\nகர்த்தரை ஸ்தோத்தரி\nஎந்தவர் செய்த சகல உபகாரங்களை\nஒரு போதும் மறவாதே"},
        
        {"title": "Antha Naal Inba", "artist": "Christian Chorus", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/006.Antha_Naal_Inba_i6gjad.mp3",
         "lyrics": "Antha naal inba naal\nEn paavam neengi pona naal\nYesu ennai meettukonda naal\nPuthu vazhvu thandha naal",
         "lyrics_tamil": "அந்த நாள் இன்ப நாள்\nஎன் பாவம் நீங்கி போன நாள்\nஇயேசு என்னை மீட்டுக்கொண்ட நாள்\nபுது வாழ்வு தந்த நாள்"},

        {"title": "Pottuvoma En Deavanaiya", "artist": "Praise Team", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/063.Pottuvoma_Pottuvoma_En_Deavanaiya_t4d8xj.mp3",
         "lyrics": "Pottuvoma pottuvoma en devanaiya\nPottuvoma pottuvoma nam iratchaganaiya\nAvar periya kariyagalai seidhaar\nNamakkaga yaavaiyum seidhu mudithar",
         "lyrics_tamil": "போற்றுவோமே போற்றுவோமே என் தேவனையே\nபோற்றுவோமே போற்றுவோமே நம் இரட்சகனையே\nஅவர் பெரிய காரியங்களைச் செய்தார்\nநமக்காக யாவையும் செய்து முடித்தார்"},

        {"title": "Anandamae Jeya", "artist": "Traditional", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/004.Anandamae_Jeya_nlsvyg.mp3",
         "lyrics": "Anandamae jeya anandamae\nArputhar yesuvai padiduvom\nInbamai avar thirunamathai\nEndrumae pottrip padiduvom",
         "lyrics_tamil": "ஆனந்தமே ஜெய ஆனந்தமே\nஅற்புதர் இயேசுவைப் பாடிடுவோம்\nஇன்பமாய் அவர் திருநாமத்தை\nஎன்றுமே போற்றிப் பாடிடுவோம்"},
        
        {"title": "Arul Eralamay Peyyum", "artist": "Hymn Choir", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352319/007.Arul_Eralamay_Peyyum_nguuaw.mp3"},
        {"title": "Ekkala Satham Vanil", "artist": "Spiritual Singers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352318/015.Ekkala_Satham_Vanil_al690v.mp3"},
        {"title": "Abraham Deaven", "artist": "Gospel Group", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/010.Abraham_Deaven_ufy4hv.mp3"},
        {"title": "Deva Prasannam", "artist": "Presence Worship", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/014.Deva_Prasannam_wkab7g.mp3"},
        
        {"title": "Merry Christmas", "artist": "Joy Choir", "cat": "Christmas", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/009.Athithiru Varthai Thiviya_anzmml.mp3", "lyrics": "Glory to God in the highest...", "lyrics_tamil": "உன்னதத்தில் தேவனுக்கு மகிமை..."},
        {"title": "Silent Night", "artist": "Peace Worship", "cat": "Christmas", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352316/013.Bavani_Selkirar_Raja_vbrkfz.mp3"},
        
        {"title": "Calvary Love", "artist": "Cross Singers", "cat": "Lent", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352313/025.Ethanai_Thiral_En_Pavam_En_covv4d.mp3", "lyrics": "Broken for us on the tree...", "lyrics_tamil": "கல்வாரி சிலுவையிலே..."},
        {"title": "Via Dolorosa", "artist": "Meditation Band", "cat": "Lent", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/024.Enthan Navil Puthu_x8vqq2.mp3"},
        
        {"title": "Engum Puzhal", "artist": "Global Praise", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/019.Engum_Puzhal_issebs.mp3"},
        {"title": "Mangal Neerodaiyai", "artist": "Grace Flow", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352303/047.Mangal_Neerodaiyai_btfzf6.mp3"},
        {"title": "Sathai Niskaliyamai", "artist": "Truth Seekers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352272/067.Sathai_Niskaliyamai_qe7sof.mp3"},
        {"title": "Keetham Keetham Jeya", "artist": "Victory Singers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352274/040.Keetham_Keetham_Jeya_fcvlkv.mp3"},
        {"title": "Kothukalam Niraintha", "artist": "Joyful Noise", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352287/044.Kothukalam_Niraintha_dxsfua.mp3"},
        {"title": "Nadakka Sollitharum", "artist": "Pathfinder Worship", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352277/050.Nadakka_Sollitharum_tin7pv.mp3"},
        {"title": "Pavathin Barathinaal", "artist": "Soul Rest", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352286/060.Pavathin_Barathinaal_pykbrv.mp3"},
        {"title": "Nambivanthean", "artist": "Faith Trust", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/052.Nambivanthean_sfzl8t.mp3"},
        {"title": "Iyya Umathu Sitham", "artist": "Thy Will Leaders", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/033.Iyya_Umathu_Sitham_avw0kr.mp3"},
        {"title": "Pareer Arunothayam", "artist": "Morning Star", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352292/056.Pareer_Arunothayam_mvyndp.mp3"},
        {"title": "Kattadam Kattidum", "artist": "Builders Praise", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352288/039.Kattadam_Kattidum_wctsj7.mp3"},
        {"title": "Santhosam Ponguthey", "artist": "Happiness Group", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352289/065.Santhosam_Ponguthey_frw9xx.mp3"},
        {"title": "Parisuthar Kootam Naduvil", "artist": "Holiness Choir", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352293/057.Parisuthar_Kootam_Naduvil_b1b1lg.mp3"},
        
        # New Additions
        {"title": "Yesu Rajanin Malaradikku", "artist": "Worship Leader", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514587/102.Yesu_Rajanin_Malaradikku_e9f9jm.mp3"},
        {"title": "Yeasuvai Pole", "artist": "Christian Chorus", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514585/099.Yeasuvai_Pole_l5fwq4.mp3"},
        {"title": "Ysuvin Namam Inithana", "artist": "Praise Team", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514580/100.Ysuvin_Namam_Inithana_bjwxad.mp3"},
        {"title": "Yesu Neasikiraar", "artist": "Traditional", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514590/101.Yesu_Neasikiraar_gy6zoc.mp3"},
        {"title": "Vara Veandum Enatharasa", "artist": "Hymn Choir", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514559/091.Vara_Veandum_Enatharasa_usbhq3.mp3"},
        {"title": "Varuvai Tharunamithuva", "artist": "Spiritual Singers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514554/094.Varuvai_Tharunamithuva_kpb0dn.mp3"},
        {"title": "Yeasu Enta Thiru Namathirku", "artist": "Gospel Group", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514556/098.Yeasu_Enta_Thiru_Namathirku_fjvrae.mp3"},
        {"title": "Thuthithu Padida Pathirana", "artist": "Presence Worship", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514535/085.Thuthithu_Padida_Pathirana_d5bwqe.mp3"},
        {"title": "Unnathamanavarin", "artist": "Joy Choir", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514535/088.Unnathamanavarin_mcsqya.mp3"},
        {"title": "Theanilum Magilum", "artist": "Peace Worship", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514541/077.Theanilum_Magilum_uwujv9.mp3"},
        {"title": "Thothirem Seivanae", "artist": "Cross Singers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514534/082.Thothirem_Seivanae_pvhxur.mp3"},
        {"title": "Thuthithu Padida Pathirana (V2)", "artist": "Meditation Band", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514534/085.Thuthithu_Padida_Pathirana_1_byltxf.mp3"},
        {"title": "Thasara Itharaniyai", "artist": "Global Praise", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514532/076.Thasara_Itharaniyai_q6eb2q.mp3"},
        {"title": "Thuthiganam Magimai", "artist": "Grace Flow", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514533/083.Thuthiganam_Magimai_pfa23a.mp3"},
        {"title": "Nadakka Sollitharum (V2)", "artist": "Truth Seekers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514531/050.Nadakka_Sollitharum_1_ucspty.mp3"},
        {"title": "Sthothiripane Sthothiripane", "artist": "Victory Singers", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514531/072.Sthothiripane_Sthothiripane_1_zosqzo.mp3"},
        {"title": "Inba Yasu Rajavai Naan", "artist": "Joyful Noise", "cat": "Worship", "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774514532/074.Inba_Yasu_Rajavai_Naan_tsyeha.mp3"}
    ]

    for s in cloudinary_songs:
        artist, _ = Artist.objects.get_or_create(name=s["artist"])
        Song.objects.get_or_create(
            title=s["title"],
            artist=artist,
            album=default_album,
            category=default_cat,
            audio_url=s["audio"],
            lyrics=s.get("lyrics", "Spiritual lyrics following soon..."),
            lyrics_tamil=s.get("lyrics_tamil", "பாடல் வரிகள் விரைவில்...")
        )
    
    print(f"Sync complete. {len(cloudinary_songs)} songs seeded with lyrics.")

if __name__ == "__main__":
    sync_cloudinary()
