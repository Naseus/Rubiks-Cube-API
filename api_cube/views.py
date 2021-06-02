from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Algorithm, SolveTime, Alternative
from .serializers import AlgorithmSerializer, SolveTimeSerializer, AlternativeSerializer


# Create your views here.

class AlgorithmList(APIView):
    def get(self, request, classification):
        algorithms = Algorithm.objects.filter(classification=classification)
        serializer = AlgorithmSerializer(algorithms, many=True)
        return Response(serializer.data)


class AlgorithmDetails(APIView):
    def get_object(self, slug):
        try:
            return Algorithm.objects.get(slug=slug)
        except Algorithm.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        algorithm = self.get_object(slug)
        if type(algorithm) == HttpResponse:
            return algorithm
        serializer = AlgorithmSerializer(algorithm)
        return Response(serializer.data)


class AlternativeList(APIView):
    def get(self, request, slug):
        algorithms = Alternative.objects.filter(base_alg__slug=slug, owner=request.user)
        serializer = AlternativeSerializer(algorithms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlternativeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug):
        alternative = Alternative.objects.get(id)
        serializer = AlternativeSerializer(alternative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, id):
        alternative = Alternative.objects.get(id=id)
        if alternative.owner != request.user and alternative.base_alg.slug == slug:
            return Response(status=status.HTTP_403_FORBIDDEN)
        alternative.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSolveTimes(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = SolveTimeSerializer
    queryset = SolveTime.objects.all()

    lookup_field = 'id'

    def validate_user(self, id, request):
        data = self.queryset.get(id=id)
        if data.owner == request.user:
            return True
        return False

    def get(self, request, id=None):
        if id and self.validate_user(id, request):
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def delete(self, request, id=None):
        if id and self.validate_user(id, request):
            return self.destroy(request)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        if id and self.validate_user(id, request):
            return self.update(request)
        return Response(status=status.HTTP_400_BAD_REQUEST)
