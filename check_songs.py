import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from musicplayer.models import Song

urls = [
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/001.Athumamae_En_Muzhu_ucsbdd.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/006.Antha_Naal_Inba_i6gjad.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/063.Pottuvoma_Pottuvoma_En_Deavanaiya_t4d8xj.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/004.Anandamae_Jeya_nlsvyg.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352319/007.Arul_Eralamay_Peyyum_nguuaw.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352318/015.Ekkala_Satham_Vanil_al690v.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/010.Abraham_Deaven_ufy4hv.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/014.Deva_Prasannam_wkab7g.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/009.Athithiru_Varthai_Thiviya_anzmml.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352316/013.Bavani_Selkirar_Raja_vbrkfz.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352313/025.Ethanai_Thiral_En_Pavam_En_covv4d.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/024.Enthan_Navil_Puthu_x8vqq2.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/019.Engum_Puzhal_issebs.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352303/047.Mangal_Neerodaiyai_btfzf6.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352272/067.Sathai_Niskaliyamai_qe7sof.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352274/040.Keetham_Keetham_Jeya_fcvlkv.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352287/044.Kothukalam_Niraintha_dxsfua.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352277/050.Nadakka_Sollitharum_tin7pv.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352286/060.Pavathin_Barathinaal_pykbrv.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/052.Nambivanthean_sfzl8t.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/033.Iyya_Umathu_Sitham_avw0kr.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352292/056.Pareer_Arunothayam_mvyndp.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352288/039.Kattadam_Kattidum_wctsj7.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352289/065.Santhosam_Ponguthey_frw9xx.mp3",
    "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352293/057.Parisuthar_Kootam_Naduvil_b1b1lg.mp3"
]

found = []
missing = []

for url in urls:
    if Song.objects.filter(audio__contains=os.path.basename(url)).exists():
        found.append(url)
    else:
        missing.append(url)

print(f"Total Songs to Check: {len(urls)}")
print(f"Found on Site: {len(found)}")
print(f"Missing on Site: {len(missing)}")

if missing:
    print("\nMISSING SONGS:")
    for m in missing:
        print(f"- {m}")
else:
    print("\nAll songs are listed on the site!")
