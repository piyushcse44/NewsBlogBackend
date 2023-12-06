from rest_framework import serializers
from .models import Business, Gallary, Politics, Economics, Entertainment, Lifestyle, Technoloy

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class GallarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallary
        fields = '__all__'

class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politics
        fields = '__all__'

class EconomicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Economics
        fields = '__all__'

class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'

class LifestyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lifestyle
        fields = '__all__'

class TechnoloySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technoloy
        fields = '__all__'
