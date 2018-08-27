from django.db import models
from django.urls import reverse_lazy

class Author(models.Model):
    nome = models.CharField(max_length=300)
    pais =  models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Author'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('author-list')
