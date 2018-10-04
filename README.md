# Blog do Lolzinho

O Blog do Lolzinho é uma iniciativa dos alunos Antonio Yves, Maria Francisca e Rafael Almeida do 4º INTIN 2018 do IFPB - Campus Cajazeiras. Que buscam mostrar aos jogadores de League of Legends o que se passa além do jogo. Fique por dentro de tudo que rola no mundo do LoL, e claro, conheça os principais campeões do jogo e suas histórias. 

## Páginas do Site
1. Página Inicial - Essa página mostra as 10 últimas notícias publicadas no site e na lateral mostra a previa da história de 5 Campeões do LoL;
2. Notícias - Mostra todas as notícias publicadas;
3. Campeões - Mostra os Campeões cadastrados e suas histórias;
4. Contato - Página para entrar em contato com os administradores do site (O formulário possuí validação JS);
5. Sobre o Jogo - Página onde são encontrados algumas coisas falando do jogo.

## Sobre o Desenvolvimento
> Projeto desenvolvido em Django e utiliza validação de formulário com JavaScript.

## models.py
O blog possui duas classes responsáveis pela criação do banco de dados, uma responsável pela adição de novas notícias (Model News) e outra para adicionar novos campeões (Model Champions).

```python
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
```

```python
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
```

## Testando
Para testar e conhecer o projeto, você deve realizar o seguinte passo a passo:
1. Clone o projeto para o seu computador:
> git clone https://github.com/antonio-yves/blog-lolzinho.git
2. Instale as dependências do projeto
> pip install -r requeriments.txt
3. Realize a criação do banco de dados, caso você tenha excluído o arquivo "db.sqlite3". Execute os comandos nessa ordem
> python manage.py makemigrations core
>
> python manage.py makemigrations blog
>
> python manage.py migrate core
>
> python manage.py migrate blog
>
> python manage.py migrate
4. Crie um super usuário (Administrador)
> python manage.py createsuperuser
5. Execute o projeto
> python manage.py runserver


