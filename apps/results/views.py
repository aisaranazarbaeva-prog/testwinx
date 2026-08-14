from rest_framework import generics, permissions

from .models import Result
from .serializers import ResultSerializer


class ResultListCreateView(generics.ListCreateAPIView):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(
            user=self.request.user
        ).select_related("fairy")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultDetailView(generics.RetrieveAPIView):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Result.objects.filter(
            user=self.request.user
        ).select_related("fairy")