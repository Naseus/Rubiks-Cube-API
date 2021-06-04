from django.urls import path, re_path
from .views import UserSolveTimesView, AlternativeView, AlgorithmView

urlpatterns = [
    re_path(r'^time/(?P<id>\d+)?$', UserSolveTimesView.as_view()),
    re_path('^alternitive-by-algorithm/(?P<slug>[a-z,A-Z\\-\\d]+)?$', AlternativeView.as_view()),
    re_path('^alternitive/(?P<id>\d+)?$', AlternativeView.as_view()),
    path('<classification>', AlgorithmView.as_view()),
    path('algorithm/<slug>', AlgorithmView.as_view()),
]
