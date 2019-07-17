from django.db import models

# Create your models here.
class produto(models.Model):
	nome = models.CharField(max_length=150)
	tipo_item = models.CharField(max_length=150)
	descricao = models.CharField(max_length=3000, default='')
	referencia = models.CharField(max_length=150)
	preco = models.FloatField()
	image = models.ImageField(upload_to='static/blogue/img')
	timestamp = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nome