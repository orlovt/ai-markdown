from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.editor, name='editor'),
    path('write/', views.write, name='write'),
]