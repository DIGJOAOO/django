from django.db import models

class Post(models.Model):
    titulo = models.CharField("Título", max_length=200)
    descripcion = models.TextField("Descripción")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.titulo
