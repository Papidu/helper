from rest_framework import serializers
from helper.applicationHR.models import Users

class UsersSerializer(serializers.ModelSerializer):
    empl_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(required=False)

    class Meta:
        model = Users
        #fields = ('name', 'employee_id')
        fields = '__all__'

