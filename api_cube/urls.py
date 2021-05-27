from django.urls import path
from .views import UserSolveTimes, AlgorithmList, AlgorithmDetails

urlpatterns = [
    path('time/', UserSolveTimes.as_view()),
    path('algorithms/<classification>', AlgorithmList.as_view()),
    path('algorithm/<slug>', AlgorithmDetails.as_view()),
]
