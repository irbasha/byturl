from django.db import models


class TeenyURLs(models.Model):
	teeny_url = models.CharField(max_length=10)
	origin_url = models.CharField(max_length=9999)

	def __str__(self):
		return self.teeny_url
