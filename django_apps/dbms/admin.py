from django.contrib import admin

# Register your models here.
from django_apps.dbms.models import ItemMaster

class ItemMasterAdmin(admin.ModelAdmin):
	class Meta:
		model = ItemMaster

admin.site.register(ItemMaster, ItemMasterAdmin)

