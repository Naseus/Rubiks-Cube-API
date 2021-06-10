from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins

from .models import Algorithm, SolveTime, Alternative
from .serializers import AlgorithmSerializer, SolveTimeSerializer, AlternativeSerializer


# Create your views here.

class UserSolveTimesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
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
        self.queryset = self.queryset.filter(owner=request.user)
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


class AlgorithmView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    serializer_class = AlgorithmSerializer
    queryset = Algorithm.objects.all()
    _classifications = (
        'PLL',
        'OLL'
    )

    lookup_field = 'slug'

    def get(self, request, slug=None, classification='PLL'):
        if slug:
            return self.retrieve(request)
        elif classification and classification in self._classifications:
            self.queryset = self.queryset.filter(classification=classification)
            return self.list(request)
        return Response(status=status.HTTP_404_NOT_FOUND)


class AlternativeView(generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    serializer_class = AlternativeSerializer
    queryset = Alternative.objects.all()

    lookup_field = 'id'

    def validate_user(self, id, request):
        data = self.queryset.get(id=id)
        if data.owner == request.user:
            return True
        return False

    def get(self, request, slug=None, id=None):
        self.queryset = self.queryset.filter(owner=request.user)
        if id and self.validate_user(id, request):
            return self.retrieve(request)
        if slug:
            self.queryset = self.queryset.filter(owner=request.user, base_alg__slug=slug)
            return self.list(request)
        self.queryset = self.queryset.filter(owner=request.user)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id=None):
        if id and self.validate_user(id, request):
            return self.destroy(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        if id and self.validate_user(id, request):
            return self.update(request)
