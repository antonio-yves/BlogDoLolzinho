from django.db import models
from app.core.models import UUIDUser

class News(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nome')
	image = models.ImageField(upload_to = 'images/', verbose_name = 'Imagem')
	create = models.DateField(auto_now_add = True, verbose_name = 'Criado em')
	user = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'Usuário', related_name = 'users')
	description = models.TextField(verbose_name = 'Descrição')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Notícia'
		verbose_name_plural = 'Notícias'

class Champion(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Nome')
	description = models.TextField(verbose_name = 'Descrição')
	image = models.ImageField(upload_to = 'champions/', verbose_name = 'Imagem')
	slug = models.CharField(max_length = 50, verbose_name = 'Slug', default = 'Slug')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Campeão'
		verbose_name_plural = 'Campeões'
