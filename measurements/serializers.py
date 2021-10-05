from django.db.models import fields
from rest_framework import serializers
from measurements.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # latitude = serializers.FloatField()
    # longitude = serializers.FloatField()
    # created_at = serializers.DateTimeField()
    # update_at = serializers.DateTimeField()