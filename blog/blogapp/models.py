from django.db import models


class Post(models.Model):
    titulo = models.CharField("Título", max_length=200)
    descripcion = models.TextField("Descripción")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.titulo


class FotoPost(models.Model):
    post = models.ForeignKey(Post, related_name="fotos", on_delete=models.CASCADE)
    imagen = models.ImageField("Foto", upload_to="posts/%Y/%m/")

    class Meta:
        ordering = ["id"]
        verbose_name = "foto"
        verbose_name_plural = "fotos"

    def __str__(self):
        return f"Foto de {self.post}"


class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["post", "session_key"], name="like_unico_por_sesion"
            ),
        ]

    def __str__(self):
        return f"Like en {self.post}"
