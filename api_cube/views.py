from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Algorithm, SolveTime
from .serializers import AlgorithmSerializer, SolveTimeSerializer


# Create your views here.

@api_view(['GET'])
def algorithm_list(request):
    if request.method == 'GET':
        algorithms = Algorithm.objects.all()
        serializer = AlgorithmSerializer(algorithms, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def user_solve_times(request):
    if request.method == 'GET':
        times = SolveTime.objects.filter(owner=request.user)
        serializer = SolveTimeSerializer(times, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SolveTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSolveTimes(APIView):
    def get(self, request):
        times = SolveTime.objects.filter(owner=request.user)
        serializer = SolveTimeSerializer(times, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SolveTimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        solve_time = SolveTime.get(id)
        if solve_time.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        solve_time.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlgorithmList(APIView):
    def get(self, request, classification):
        algorithms = Algorithm.objects.filter(classification=classification)
        serializer = AlgorithmSerializer(algorithms, many=True)
        return Response(serializer.data)


class AlgorithmDetails(APIView):
    def get_object(self, id):
        try:
            return Algorithm.objects.get(slug=id)
        except Algorithm.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        algorithm = self.get_object(slug)
        if type(algorithm) == HttpResponse:
            return algorithm
        serializer = AlgorithmSerializer(algorithm)
        return Response(serializer.data)
