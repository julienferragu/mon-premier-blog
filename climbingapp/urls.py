from django.urls import path
from . import views
from .views import change_mountaineer_activity


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('change_activity/<str:mountaineer_id>/', change_mountaineer_activity, name='change_mountaineer_activity'),
]