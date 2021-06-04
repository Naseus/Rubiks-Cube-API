from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Alternative, Algorithm, SolveTime


class AlternativeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=CurrentUserDefault())
    base_alg = serializers.PrimaryKeyRelatedField(many=False, queryset=Algorithm.objects.all())

    class Meta:
        model = Alternative
        fields = [
            'id',
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
    owner = serializers.HiddenField(default=CurrentUserDefault())
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SolveTime
        fields = [
            'id',
            'time',
            'created',
            'owner',
        ]

