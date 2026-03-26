"""
Django seed script for Tamil Christian Songs database.

Usage:
    python manage.py shell < seed_tamil_songs.py
"""

from musicplayer.models import Category, Artist, Album, Song

print("Clearing existing data...")
Song.objects.all().delete()
Album.objects.all().delete()
Artist.objects.all().delete()
Category.objects.all().delete()

print("Seeding Categories...")
categories = {
    "praise":    Category.objects.create(name="Praise & Worship",  name_tamil="துதி மற்றும் வழிபாடு"),
    "hymn":      Category.objects.create(name="Hymn",              name_tamil="கீர்த்தனை"),
    "gospel":    Category.objects.create(name="Gospel",            name_tamil="நற்செய்தி பாடல்"),
    "christmas": Category.objects.create(name="Christmas",         name_tamil="கிறிஸ்துமஸ்"),
    "lent":      Category.objects.create(name="Lent & Passion",   name_tamil="தவக்காலம்"),
    "easter":    Category.objects.create(name="Easter",            name_tamil="உயிர்த்தெழுதல்"),
    "children":  Category.objects.create(name="Children",          name_tamil="குழந்தைகள் பாடல்"),
}

print("Seeding Artists...")
artists = {
    "berchmans": Artist.objects.create(name="Fr. S.J. Berchmans",    name_tamil="பாடகர் பெர்க்மன்ஸ்",    image="artists/berchmans.jpg"),
    "dgs":       Artist.objects.create(name="D.G.S. Dhinakaran",     name_tamil="டி.ஜி.எஸ். தினகரன்",    image="artists/dgs_dhinakaran.jpg"),
    "jikki":     Artist.objects.create(name="Jikki",                  name_tamil="ஜிக்கி",                image="artists/jikki.jpg"),
    "chithra":   Artist.objects.create(name="K.S. Chithra",           name_tamil="கே.எஸ். சித்ரா",       image="artists/ks_chithra.jpg"),
    "jollee":    Artist.objects.create(name="Jollee Abraham",          name_tamil="ஜோலி ஆபிரகாம்",        image="artists/jollee_abraham.jpg"),
    "nataraja":  Artist.objects.create(name="V. Nataraja Mudaliar",   name_tamil="வி. நடராஜ முதலியார்"),
    "mkpaul":    Artist.objects.create(name="M.K. Paul",              name_tamil="எம்.கே. பால்"),
    "darwin":    Artist.objects.create(name="Darwin Ebenezer",        name_tamil="டார்வின் எபனேசர்",     image="artists/darwin_ebenezer.jpg"),
    "paul_c":    Artist.objects.create(name="Paul Charles",           name_tamil="பால் சார்லஸ்"),
    "jebaraj":   Artist.objects.create(name="Pr. John Jebaraj",       name_tamil="பாஸ்டர் ஜான் ஜெபராஜ்", image="artists/john_jebaraj.jpg"),
    "sharon":    Artist.objects.create(name="Arpana Sharon",          name_tamil="அர்பனா ஷாரோன்"),
    "prabhu":    Artist.objects.create(name="Prabhu Isaac",           name_tamil="பிரபு ஐசக்"),
    "various":   Artist.objects.create(name="Various Artists",        name_tamil="பல கலைஞர்கள்"),
}

print("Seeding Albums...")
albums = {
    "jjg11":   Album.objects.create(title="Jebathotta Jeyageethangal Vol 11", title_tamil="ஜெபத்தொட்டி ஜெயகீதங்கள் தொகுதி 11", artist=artists["berchmans"], release_year=1990),
    "jjg16":   Album.objects.create(title="Jebathotta Jeyageethangal Vol 16", title_tamil="ஜெபத்தொட்டி ஜெயகீதங்கள் தொகுதி 16", artist=artists["berchmans"], release_year=1993),
    "jjg28":   Album.objects.create(title="Jebathotta Jeyageethangal Vol 28", title_tamil="ஜெபத்தொட்டி ஜெயகீதங்கள் தொகுதி 28", artist=artists["berchmans"], release_year=2007),
    "jjg36":   Album.objects.create(title="Jebathotta Jeyageethangal Vol 36", title_tamil="ஜெபத்தொட்டி ஜெயகீதங்கள் தொகுதி 36", artist=artists["berchmans"], release_year=2015),
    "jjg40":   Album.objects.create(title="Jebathotta Jeyageethangal Vol 40", title_tamil="ஜெபத்தொட்டி ஜெயகீதங்கள் தொகுதி 40", artist=artists["berchmans"], release_year=2019),
    "dgs_dev": Album.objects.create(title="DGS Dhinakaran Devotional Vol 1",  title_tamil="தினகரன் பக்தி பாடல்கள்",              artist=artists["dgs"],       release_year=1985),
    "divine":  Album.objects.create(title="Divine Collections",                title_tamil="தெய்வீக தொகுப்பு",                   artist=artists["dgs"],       release_year=1988),
    "alleluya":Album.objects.create(title="Alleluya Aanandame",                title_tamil="அல்லேலூயா ஆனந்தமே",                  artist=artists["dgs"],       release_year=1990),
    "jikki_c": Album.objects.create(title="Tamil Christian Hymns Classic",     title_tamil="தமிழ் கிறிஸ்தவ பழைய கீர்த்தனைகள்",  artist=artists["jikki"],     release_year=1968),
    "thuthip": Album.objects.create(title="Thuthipookal",                      title_tamil="துதிப்பூக்கள்",                       artist=artists["chithra"],   release_year=1995),
    "masilla": Album.objects.create(title="Masilla Yesu Vol 1",                title_tamil="மாசில்லா இயேசு",                     artist=artists["nataraja"],  release_year=1980),
    "ulagin":  Album.objects.create(title="Ulagin Oliye",                      title_tamil="உலகின் ஒளியே",                       artist=artists["nataraja"],  release_year=1982),
    "mkp":     Album.objects.create(title="Hits of M.K. Paul",                 title_tamil="எம்.கே. பால் சிறந்த பாடல்கள்",       artist=artists["mkpaul"],    release_year=1995),
    "darwin_p":Album.objects.create(title="Darwin Ebenezer Praise",            title_tamil="டார்வின் எபனேசர் துதி பாடல்கள்",    artist=artists["darwin"],    release_year=2016),
    "paul_c_a":Album.objects.create(title="Tamil Christian Songs by Paul Charles", title_tamil="பால் சார்லஸ் பாடல்கள்",         artist=artists["paul_c"],    release_year=2010),
    "thazhvil":Album.objects.create(title="Thazhvil Ninaithavare",             title_tamil="தாழ்வில் நினைத்தவரே",                artist=artists["jebaraj"],   release_year=2010),
    "adonai":  Album.objects.create(title="Adonai Vol 1",                      title_tamil="அடோனாய்",                            artist=artists["sharon"],    release_year=2005),
    "xmas":    Album.objects.create(title="Christmas Tamil Special",           title_tamil="கிறிஸ்துமஸ் சிறப்பு பாடல்கள்",      artist=artists["various"],   release_year=2001),
    "prabhu_a":Album.objects.create(title="Prabhu Isaac Gospel Collection",    title_tamil="பிரபு ஐசக் நற்செய்தி தொகுப்பு",    artist=artists["prabhu"],    release_year=2013),
}

print("Seeding Songs...")
songs_data = [
    ("Dhaagamullavanmel",        "தாகமுள்ளவன்மேல்",           "berchmans", "jjg11",    "praise"),
    ("Yosanaiyil Periyavare",    "யோசனையில் பெரியவரே",        "berchmans", "jjg11",    "hymn"),
    ("Nam Yesu Nallavar",        "நம் இயேசு நல்லவர்",         "berchmans", "jjg11",    "gospel"),
    ("Kalangaathe Maname",       "கலங்காதே மனமே",             "berchmans", "jjg11",    "hymn"),
    ("Paava Mannippin Daagam",   "பாவ மன்னிப்பின் தாகம்",     "berchmans", "jjg11",    "hymn"),
    ("Enadhu Thalaivan Yesu",    "எனது தலைவன் இயேசு",         "berchmans", "jjg11",    "gospel"),
    ("Naan Padumbothu En Udhadu","நான் படும்போது என் உதடு",   "berchmans", "jjg16",    "hymn"),
    ("Yesu Neenga Irukkaiyile",  "இயேசு நீங்க இருக்கையிலே",  "berchmans", "jjg11",    "hymn"),
    ("Yesu Nee Mahaneeya",       "இயேசு நீ மகாநீயா",          "berchmans", "jjg36",    "gospel"),
    ("Vetri Yesu Vaazhga",       "வெற்றி இயேசு வாழ்க",        "berchmans", "jjg40",    "gospel"),
    ("Ullam Urugi Kaniyadha",    "உள்ளம் உருகி கனியாதா",      "dgs",       "dgs_dev",  "hymn"),
    ("Enna En Aanandam",         "என்ன என் ஆனந்தம்",           "dgs",       "dgs_dev",  "gospel"),
    ("Kappaar Unnai",            "காப்பார் உன்னை",             "dgs",       "dgs_dev",  "praise"),
    ("Yesu Azhaikiraar",         "இயேசு அழைக்கிறார்",         "dgs",       "divine",   "gospel"),
    ("Neer Illatha Naalellam",   "நீர் இல்லாத நாளெல்லாம்",   "dgs",       "dgs_dev",  "hymn"),
    ("Alleluya Aanandame",       "அல்லேலூயா ஆனந்தமே",         "dgs",       "alleluya", "praise"),
    ("Anbin Deva Markarunaiyile","அன்பின் தேவா மகாகருணையிலே", "jikki",     "jikki_c",  "hymn"),
    ("Narkarunai Nadhane",       "நற்கருணை நாதனே",             "jikki",     "jikki_c",  "hymn"),
    ("Siluvai Sumantha Nadhane", "சிலுவை சுமந்த நாதனே",       "jikki",     "jikki_c",  "lent"),
    ("Pareer Gethsamaney",       "பாரீர் கெத்சமனே",            "jikki",     "jikki_c",  "lent"),
    ("Thuthipookal",             "துதிப்பூக்கள்",               "chithra",   "thuthip",  "praise"),
    ("Yesu En Rajanae",          "இயேசு என் ராஜனே",            "chithra",   "thuthip",  "gospel"),
    ("Aaraathipen Unnai",        "ஆராதிப்பேன் உன்னை",          "chithra",   "thuthip",  "praise"),
    ("Masilla Yesu",             "மாசில்லா இயேசு",             "nataraja",  "masilla",  "hymn"),
    ("Ulagin Oliye",             "உலகின் ஒளியே",               "nataraja",  "ulagin",   "gospel"),
    ("Deiveega Raagam",          "தெய்வீக ராகம்",              "mkpaul",    "mkp",      "hymn"),
    ("Ennodu Pesuvaya",          "என்னோடு பேசுவாயா",           "darwin",    "darwin_p", "gospel"),
    ("Ellam Yesuve En Aayanai",  "எல்லாம் இயேசுவே என் ஆயனை", "paul_c",    "paul_c_a", "hymn"),
    ("Kirubaiyile Ennai Meetavare","கிருபையிலே என்னை மீட்டவரே","paul_c",   "paul_c_a", "gospel"),
    ("Thazhvil Ninaithavare",    "தாழ்வில் நினைத்தவரே",        "jebaraj",   "thazhvil", "gospel"),
    ("Adonai",                   "அடோனாய்",                    "sharon",    "adonai",   "praise"),
    ("En Nambikkai Yesu",        "என் நம்பிக்கை இயேசு",        "prabhu",    "prabhu_a", "gospel"),
    ("Yesu Kristhu Piranthaar",  "இயேசு கிறிஸ்து பிறந்தார்",  "various",   "xmas",     "christmas"),
    ("Bethlehem Ooril Piranthan","பெத்லகேம் ஊரில் பிறந்தான்", "various",   "xmas",     "christmas"),
    ("Nalla Naadhan Yesu",       "நல்ல நாதன் இயேசு",           "berchmans", "jjg28",    "gospel"),
]

for title_en, title_ta, artist_key, album_key, cat_key in songs_data:
    slug = title_en.lower().replace(" ", "_").replace("'", "")
    Song.objects.create(
        title=title_en,
        title_tamil=title_ta,
        artist=artists[artist_key],
        album=albums[album_key],
        category=categories[cat_key],
        audio_file=f"songs/{slug}.mp3",
    )

print(f"Done! Seeded: {Category.objects.count()} categories, "
      f"{Artist.objects.count()} artists, "
      f"{Album.objects.count()} albums, "
      f"{Song.objects.count()} songs.")
