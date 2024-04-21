from django.contrib import admin
from django.urls import path

from core import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.subservice, name='subservice'),
    # collections/<str:collection>/<str:category>/<int:category_id>
]
