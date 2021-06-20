from django.urls import path

from .views import *

urlpatterns = [
    path('', UnresolvedPaymentsView.as_view()),
]