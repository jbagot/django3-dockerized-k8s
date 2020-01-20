from django.urls import path

from api import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('animals', views.AnimalsViewset, basename='animal')
router.register('animal-types', views.AnimalTypesViewset, basename='animal-types')

urlpatterns = [
    path('ping', views.PingView.as_view(), name="ping"),
]

urlpatterns += router.urls
