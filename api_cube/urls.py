from django.urls import path
from .views import user_solve_times, algorithm_list

urlpatterns = [
    path('time/', user_solve_times),
    path('all-algorithms/', algorithm_list),
]
