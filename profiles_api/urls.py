from django.urls import path

from profiles_api import views


urlpatterns = [
    path('', views.HelloApiView.as_view()),
    path('hello-view/', views.HelloApiView.as_view()),
]

'''
from django.urls import path, include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
'''