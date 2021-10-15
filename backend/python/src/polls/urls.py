from django.urls import path, re_path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    path('list/',views.questions, name='list'),
    path('', views.index, name='index'),
    re_path(r'^index/$', views.index, name='index'),
]
