import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MusicConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
        # Extended Cloudinary Songs Library
        songs = [
            {
                "title": "Athumamae",
                "artist": "Worship Leader",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/001.Athumamae_En_Muzhu_ucsbdd.mp3",
                "cover": "/static/img/default_cover.png",
                "lyrics": "Athumamae En Muzhu...",
                "lyrics_tamil": "ஆத்துமாவே என் முழு உள்ளமே..."
            },
            {
                "title": "Antha Naal Inba",
                "artist": "Christian Chorus",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352321/006.Antha_Naal_Inba_i6gjad.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Pottuvoma En Deavanaiya",
                "artist": "Praise Team",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/063.Pottuvoma_Pottuvoma_En_Deavanaiya_t4d8xj.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Anandamae Jeya",
                "artist": "Traditional",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352320/004.Anandamae_Jeya_nlsvyg.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Arul Eralamay Peyyum",
                "artist": "Hymn Choir",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352319/007.Arul_Eralamay_Peyyum_nguuaw.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Ekkala Satham Vanil",
                "artist": "Spiritual Singers",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352318/015.Ekkala_Satham_Vanil_al690v.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Abraham Deaven",
                "artist": "Gospel Group",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/010.Abraham_Deaven_ufy4hv.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Deva Prasannam",
                "artist": "Presence Worship",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/014.Deva_Prasannam_wkab7g.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Athithiru Varthai Thiviya",
                "artist": "Sacred Music",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352317/009.Athithiru_Varthai_Thiviya_anzmml.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Bavani Selkirar Raja",
                "artist": "Kings Choir",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352316/013.Bavani_Selkirar_Raja_vbrkfz.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Ethanai Thiral En Pavam",
                "artist": "Faith Journey",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352313/025.Ethanai_Thiral_En_Pavam_En_covv4d.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Enthan Navil Puthu",
                "artist": "New Life Band",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/024.Enthan_Navil_Puthu_x8vqq2.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Engum Puzhal",
                "artist": "Global Praise",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352310/019.Engum_Puzhal_issebs.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Mangal Neerodaiyai",
                "artist": "Grace Flow",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352303/047.Mangal_Neerodaiyai_btfzf6.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Sathai Niskaliyamai",
                "artist": "Truth Seekers",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352272/067.Sathai_Niskaliyamai_qe7sof.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Keetham Keetham Jeya",
                "artist": "Victory Singers",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352274/040.Keetham_Keetham_Jeya_fcvlkv.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Kothukalam Niraintha",
                "artist": "Joyful Noise",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352287/044.Kothukalam_Niraintha_dxsfua.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Nadakka Sollitharum",
                "artist": "Pathfinder Worship",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352277/050.Nadakka_Sollitharum_tin7pv.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Pavathin Barathinaal",
                "artist": "Soul Rest",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352286/060.Pavathin_Barathinaal_pykbrv.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Nambivanthean",
                "artist": "Faith Trust",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/052.Nambivanthean_sfzl8t.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Iyya Umathu Sitham",
                "artist": "Thy Will Leaders",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352302/033.Iyya_Umathu_Sitham_avw0kr.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Pareer Arunothayam",
                "artist": "Morning Star",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352292/056.Pareer_Arunothayam_mvyndp.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Kattadam Kattidum",
                "artist": "Builders Praise",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352288/039.Kattadam_Kattidum_wctsj7.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Santhosam Ponguthey",
                "artist": "Happiness Group",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352289/065.Santhosam_Ponguthey_frw9xx.mp3",
                "cover": "/static/img/default_cover.png"
            },
            {
                "title": "Parisuthar Kootam Naduvil",
                "artist": "Holiness Choir",
                "audio": "https://res.cloudinary.com/dlt2wry8q/video/upload/v1774352293/057.Parisuthar_Kootam_Naduvil_b1b1lg.mp3",
                "cover": "/static/img/default_cover.png"
            }
        ]
        
        await self.send(text_data=json.dumps({
            'type': 'song_list',
            'songs': songs
        }))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
