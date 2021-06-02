from django.urls import path, re_path
import re
from .views import UserSolveTimes, AlgorithmList, AlgorithmDetails, AlternativeList

urlpatterns = [
    re_path(r'^time/(?P<id>\d+)?$', UserSolveTimes.as_view()),
    re_path('^alternative/(?P<slug>\[a-z, A-Z]+)?$', AlternativeList.as_view()),
    path('algorithms/<classification>', AlgorithmList.as_view()),
    path('algorithm/<slug>', AlgorithmDetails.as_view()),
]
