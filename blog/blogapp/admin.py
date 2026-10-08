from django.contrib import admin
from .models import FotoPost, Post


class FotoPostInline(admin.TabularInline):
    model = FotoPost
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cantidad_fotos", "cantidad_likes")
    inlines = [FotoPostInline]

    @admin.display(description="Fotos")
    def cantidad_fotos(self, obj):
        return obj.fotos.count()

    @admin.display(description="Likes")
    def cantidad_likes(self, obj):
        return obj.likes.count()
