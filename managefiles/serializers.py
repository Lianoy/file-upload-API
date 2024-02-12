from rest_framework import serializers
from .models import File
from .tasks import processing_file
 
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

    def create(self, validated_data):
        new = File.objects.create(**validated_data)
        processing_file.delay(new.id) 
        return new