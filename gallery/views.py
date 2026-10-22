from django.shortcuts import get_object_or_404, render
from .models import Category, Photo

def home(request):
    photos = Photo.objects.select_related("category").all()
    categories = Category.objects.all()
    return render(request, "gallery/home.html",{"photos": photos, "categories": categories})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk = pk)
    return render(request, 'gallery/photo_detail.html', {'photo': photo})