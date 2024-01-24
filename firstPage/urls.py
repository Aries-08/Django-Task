from django.urls import path
from firstPage import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('graph1api/', views.graph_view_api, name='stacked_bar_chart_api'),
    path('graph1/', views.graph_view, name='stacked_bar_chart'),
]
