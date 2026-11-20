from django.contrib import admin
from .models import Movie,Review


@admin.register(Movie)
class Movieadmin(admin.ModelAdmin):
    list_display = ('title','release_date','genre')
    search_fields = ('title',)
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie','user','rating','created_at')
    list_filter = ('rating',)
# Register your models here.
