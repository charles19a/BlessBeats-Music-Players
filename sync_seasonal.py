import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from musicplayer.models import Song, Artist, Album, Category

def sync_seasonal():
    print("Categorizing songs for Christmas and Lent...")
    
    # Categories
    worship_cat, _ = Category.objects.get_or_create(name="Worship")
    christmas_cat, _ = Category.objects.get_or_create(name="Christmas")
    lent_cat, _ = Category.objects.get_or_create(name="Lent")

    # Move some songs to Christmas
    christmas_titles = ["Mangal Neerodaiyai", "Pareer Arunothayam", "Keetham Keetham Jeya", "Bavani Selkirar Raja"]
    Song.objects.filter(title__in=christmas_titles).update(category=christmas_cat)

    # Move some songs to Lent
    lent_titles = ["Ethanai Thiral En Pavam", "Pavathin Barathinaal", "Iyya Umathu Sitham", "Abraham Deaven"]
    Song.objects.filter(title__in=lent_titles).update(category=lent_cat)

    print(f"Categories updated: Worship ({Song.objects.filter(category=worship_cat).count()}), Christmas ({Song.objects.filter(category=christmas_cat).count()}), Lent ({Song.objects.filter(category=lent_cat).count()})")

if __name__ == "__main__":
    sync_seasonal()
