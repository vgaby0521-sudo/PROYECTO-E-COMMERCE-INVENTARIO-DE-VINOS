from django.urls import path
from . import views

urlpatterns = [
    # ... otras URLs existentes ...
    path('generar-reporte-excel/', views.generar_reporte_excel, name='generar_reporte_excel'),
]