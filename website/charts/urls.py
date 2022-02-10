from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chart/<str:chart_name>', views.chart, name='chart'),

]
