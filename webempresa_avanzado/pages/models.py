from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Ofertas(models.Model):
    title = models.CharField(verbose_name="Título de la oferta", max_length=200)
    price = models.CharField(verbose_name="Precio oferta", max_length=6)

    class Meta:
        verbose_name = "oferta"
        verbose_name_plural = "ofertas"
        ordering = ['title']

    def __str__(self):
        return self.title