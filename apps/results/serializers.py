from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    fairy_name = serializers.CharField(
        source="fairy.name",
        read_only=True
    )

    class Meta:
        model = Result
        fields = [
            "id",
            "user",
            "fairy",
            "fairy_name",
            "score",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "created_at",
        ]