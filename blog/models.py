from turtle import title
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe

class PublishedManager(models.Manager) :
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='publicado')
            
class category(models.Model):
    nome = models.CharField(max_length = 100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["criado",]

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    STATUS = (
        ("rascunho", "Rascunho"),
        ("publicado", "Publicado"),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    category = models.ManyToManyField(category, related_name="get_posts")
    image = models.ImageField(upload_to="blog", blank=True, null=True)
    content = RichTextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
     choices=STATUS,
    default="rascunho")
    
    objects = models.Manager()
    published = PublishedManager()
    
    def get_absolute_url(self):
        return reverse("post_detail",args={self.slug})
    
    def get_absolute_url_update(self):
        return reverse("post_edit",args={self.pk})
    
    def get_absolute_url_delete(self):
        return reverse("post_delete",args={self.pk})
    
    def view_image(self):
        return mark_safe('<img src="%s"width="400px" />'%self.image.url)
        view_image.short_description = "Imagem Cadastrada com sucesso!"
        view_image.allow_tags = True
    
    class Meta:
        ordering = ('publicado',)
    
    def __str__(self):
        return self.title
    
@receiver(post_save, sender=Post)
def insert_slug(sender, instance,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance, title)
        return instance.save()
    



"""
Post.objects.bulk_create([
    Post(title='testando o shell com bulk,slug='testando-o-shell-com-bulk,content='Testando o shell com bulk,author=user)])

"""