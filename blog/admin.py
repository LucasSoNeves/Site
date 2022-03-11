from django.contrib import admin
from .models import Post

@admin.register(Post)
class postAdmin(admin.ModelAdmin) :
    list_display = ("title", "author", "publicado", "status")
    list_filter = ("status", "author", "content", "publicado")
    date_hierarchy = "publicado"
    raw_id_fields = ("author",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    
# Register your models here.
"""
title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    content = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
     choices=STATUS,
    default="rascunho")
"""
