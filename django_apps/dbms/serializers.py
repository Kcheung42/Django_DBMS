from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from django_apps.dbms.models import ItemMaster

class ItemMasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemMaster
		fields = '__all__'
