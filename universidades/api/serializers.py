from rest_framework import serializers
from uni_data.models import * 

class DefaultCampusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Campus
		fields = ['id','campus']

class DefaultUniversidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Universidad
		fields = ['id','nombre','pais','campus']


class CampusSerializer(serializers.ModelSerializer):
	universidades = DefaultUniversidadSerializer(many=True,read_only=True)
	class Meta:
		model = Campus
		fields = ['id','campus','universidades']

class UniversidadSerializer(serializers.ModelSerializer):
	campus = DefaultCampusSerializer(many=False,read_only=True)
	campus_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Campus.objects.all(), source='campus')
	class Meta:
		model = Universidad
		fields = ['id','nombre','pais','campus','campus_id']
