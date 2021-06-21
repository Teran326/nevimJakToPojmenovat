from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('picture/', views.picture, name='picture'),
    path('witcher/create/', views.ProfessionCreate.as_view(), name='profession-create'),
    path('witcher/<int:pk>/update/', views.ProfessionUpdate.as_view(), name='profession-update'),
    path('witcher/<int:pk>/delete/', views.ProfessionDelete.as_view(), name='profession-delete'),
]
