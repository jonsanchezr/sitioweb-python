from django.db import models

# Create your models here.

class Comeisu(models.Model):
	"""docstring for Comeisu"""
	cla_isu = models.CharField(max_length = 30)
	des_isu = models.CharField(max_length = 70)
	key_pri = models.IntegerField(primary_key=True)

	class Meta:
		db_table = 'comeisu'
		unique_together = (('key_pri'),)
