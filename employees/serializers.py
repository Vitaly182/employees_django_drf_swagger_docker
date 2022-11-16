from rest_framework import serializers
from .models import Employee



class EmployeesSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='position.name')

    class Meta:
        model = Employee
        fields = ('__all__')