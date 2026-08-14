from rest_framework import serializers
from .models import Fairy, Question, Answer


class FairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fairy
        fields = (
            "id",
            "name",
            "description",
            "image",
        )


class AnswerSerializer(serializers.ModelSerializer):
    fairy = serializers.IntegerField(
        source="fairy.id",
        read_only=True
    )

    class Meta:
        model = Answer
        fields = (
            "id",
            "text",
            "fairy",
        )


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Question
        fields = (
            "id",
            "text",
            "answers",
        )