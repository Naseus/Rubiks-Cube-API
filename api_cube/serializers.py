from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Alternative, Algorithm, SolveTime


class AlternativeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    base_alg = serializers.PrimaryKeyRelatedField(many=False, queryset=Algorithm.objects.all())

    class Meta:
        model = Alternative
        fields = [
            'alternative',
            'owner',
            'base_alg',
        ]


class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = [
            'slug',
            'classification',
            'alg_name',
            'moves',
        ]


class SolveTimeSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    class Meta:
        model = SolveTime
        fields = [
            'time',
            'created',
            'owner',
        ]

