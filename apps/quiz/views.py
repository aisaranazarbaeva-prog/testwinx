from collections import Counter

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Question, Answer, Fairy
from .serializers import QuestionSerializer, FairySerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.prefetch_related(
        "answers__fairy"
    ).all()

    serializer_class = QuestionSerializer


class QuizResultAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        answer_ids = request.data.get("answers", [])

        # Проверяем, что ответы вообще пришли
        if not answer_ids:
            return Response(
                {"error": "Нет ответов."},
                status=400
            )

        # Получаем ответы
        answers = Answer.objects.select_related("fairy").filter(
            id__in=answer_ids
        )

        # Проверяем, что ответы существуют
        if not answers.exists():
            return Response(
                {"error": "Ответы не найдены."},
                status=400
            )

        # Считаем количество ответов каждой феи
        counter = Counter()

        for answer in answers:
            counter[answer.fairy_id] += 1

        # Находим фею с самым большим количеством ответов
        fairy_id, score = counter.most_common(1)[0]

        # Получаем эту фею
        fairy = Fairy.objects.get(id=fairy_id)

        return Response(
            {
                "fairy": FairySerializer(fairy).data,
                "score": score,
                "scores": dict(counter),
            }
        )