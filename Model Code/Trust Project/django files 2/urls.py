from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('score/', views.main, name="score"),
    path('',views.sign, name="test"),
    path('details/',views.det, name="details")
]