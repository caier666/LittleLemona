from rest_framework.serializers import ModelSerializer
from . import models

class MenuSerializer(ModelSerializer):
    class Meta:
        model=models.Menu
        fields='__all__'
    