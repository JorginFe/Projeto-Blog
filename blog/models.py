from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = RichTextField()
    conteúdo = RichTextUploadingField
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo