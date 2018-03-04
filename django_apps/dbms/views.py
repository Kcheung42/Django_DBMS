from django_apps.dbms.models import ItemMaster
from django_apps.dbms.serializers import ItemMasterSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class ItemMasterList(mixins.ListModelMixin,
					 mixins.CreateModelMixin,
					 generics.GenericAPIView):
	queryset = ItemMaster.objects.all()
	serializer_class = ItemMasterSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ItemMasterDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ItemMaster.objects.all()
	serializer_class = ItemMasterSerializer
