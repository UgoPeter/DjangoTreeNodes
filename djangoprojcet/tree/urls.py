from django.urls import path
from . import views
urlpatterns = [
    path('', views.TreeView.as_view(), name='index'),
    path('test/', views.TestView.as_view())
]
