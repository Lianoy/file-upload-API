from django.urls import path
from . import views
 
urlpatterns = [
    path('files/', views.FileAPIView.as_view()),
    path('upload/', views.FileAPICreate.as_view()),
]