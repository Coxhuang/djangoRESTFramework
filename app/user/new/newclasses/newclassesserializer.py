from rest_framework import serializers
from app import models
from drf_dynamic_fields import DynamicFieldsMixin



class newclassesserializer(DynamicFieldsMixin,serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = "__all__"