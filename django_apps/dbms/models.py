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
	name = models.CharField(max_length=35, unique=True)
	address = models.CharField(max_length=35)
	# Fields
	# Relation
	pass

class Inventory(models.Model):
	sku = modles.ForeignKey(ItemMaster)
	# Fields
	# Relation
	pass

class SoldInventory(models.Model):
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
