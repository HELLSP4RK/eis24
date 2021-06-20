from django.urls import path

from first.views import *

urlpatterns = [
    path('', show_actions_group_by_user),
]