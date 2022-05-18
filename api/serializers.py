from rest_framework.serializers import ModelSerializer
from .models import UserReg

class UserRegSerializer(ModelSerializer):
    class Meta:
        model = UserReg
        fields = ['id', 'phone_number', 'jam','names']

        