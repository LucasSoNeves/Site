from django.contrib import admin
from .models import Post, category

@admin.register(category)
class postAdmin(admin.ModelAdmin) :
    list_display = ("nome", "criado", "publicado")
    list_filter = ("nome", "criado", "publicado")
    date_hierarchy = "publicado"
    search_fields = ("nome",)

@admin.register(Post)
class postAdmin(admin.ModelAdmin) :
    list_display = ("title", "author", "publicado", "status")
    list_filter = ("status", "author", "content", "publicado")
    readOnly_fields = ("visualizar_imagem",)
    date_hierarchy = "publicado"
    raw_id_fields = ("author",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    
    def visualizar_imagem(self, obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem inserida!"
    
# Register your models here.
