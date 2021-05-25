from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Algorithm, SolveTime
from .serializers import AlgorithmSerializer, SolveTimeSerializer


# Create your views here.

def algorithm_list(request):
    if request.method == 'GET':
        algorithms = Algorithm.objects.all()
        serializer = AlgorithmSerializer(algorithms, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request == 'POST':
        pass


def user_solve_times(request):
    if request.method == 'GET':
        times = SolveTime.objects.filter(owner=request.user)
        serializer = SolveTimeSerializer(times, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = SolveTimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
