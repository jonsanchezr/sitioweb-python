from django.db import models

# Create your models here.

class Comeisu(models.Model):
	"""docstring for Persona"""
	cla_isu = models.CharField(max_length = 30)
	des_isu = models.CharField(max_length = 70)
	dpa_isu = models.IntegerField()
	dea_isu = models.CharField(max_length = 2048)
	un1_isu = models.CharField(max_length = 3)
	un2_isu = models.CharField(max_length = 3)
	un3_isu = models.CharField(max_length = 3)
	fa2_isu = models.DecimalField(max_digits = 9, decimal_places = 4)
	fa3_isu = models.DecimalField(max_digits = 9, decimal_places = 4)
	pv1_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	pv2_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	pv3_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	pv4_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	pv5_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	im1_isu = models.IntegerField()
	im2_isu = models.IntegerField()
	im3_isu = models.IntegerField()
	im4_isu = models.IntegerField()
	im5_isu = models.IntegerField()
	ta1_isu = models.CharField(max_length = 2)
	ta2_isu = models.CharField(max_length = 2)
	ta3_isu = models.CharField(max_length = 2)
	ta4_isu = models.CharField(max_length = 2)
	ta5_isu = models.CharField(max_length = 2)
	mon_isu = models.CharField(max_length = 2)
	cst_isu = models.DecimalField(max_digits = 12, decimal_places = 4)
	sku_isu = models.CharField(max_length = 19)
	est_isu = models.CharField(max_length = 1)
	pvp_isu = models.DecimalField(max_digits = 15, decimal_places = 5)
	dst_isu = models.CharField(max_length = 60)
	tci_isu = models.CharField(max_length = 2)
	usu_usu = models.IntegerField()
	tie_uac = models.DateTimeField()
	key_pri = models.AutoField(primary_key = True)
	ta0_isu = models.CharField(max_length = 2)
	im0_isu = models.IntegerField()
	uni_sat = models.CharField(max_length = 3)
	ubf_sat = models.CharField(max_length = 1)
	cls_sat = models.CharField(max_length = 8)
	fum_sat = models.DecimalField(max_digits = 16, decimal_places = 5)
	du1_isu = models.CharField(max_length = 14)
	du2_isu = models.CharField(max_length = 14)
	du3_isu = models.CharField(max_length = 14)
	fra_isu = models.CharField(max_length = 1)


	def __str__(self):
		return self.cla_isu