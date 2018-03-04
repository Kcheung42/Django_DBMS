from django.db import models

# Create your models here.

class ItemMaster(models.Model):
	# Fields
	sku = models.CharField(max_length=32, unique=True)
	price = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	# Relation
	pass

class StoreMaster(models.Model):
	# Fields
	# Relation
	pass

class Warehouse(models.Model):
	# Fields
	# Relation
	pass

class TransactionMaster(models.Model):
	# Fields
	# Relation
	pass

class TransactionDetail(models.Model):
	# Fields
	# Relation
	pass
