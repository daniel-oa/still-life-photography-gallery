from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'photos/')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'photos')
    photographer = models.CharField(max_length = 150, blank = True)
    source_url = models.URLField(blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
